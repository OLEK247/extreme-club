import os
import sys
from collections import deque

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(ROOT, "images")

GRAY_BG_THRESHOLD = 196
BLOB_MIN_PIXELS = 200


BG_FLOOD_MIN = 140
BG_FLOOD_MAX_CHROMA = 22


def whiten_gray_background(px, w, h):
    """Flood the neutral backdrop inward from the frame edges.

    Only pixels reachable from the border stay eligible, so light-gray parts
    enclosed by the vehicle's own outline (silver panels, wheels) are never hit.
    """
    seen = bytearray(w * h)
    q = deque()

    def eligible(x, y):
        r, g, b = px[x, y][:3]
        if min(r, g, b) < BG_FLOOD_MIN:
            return False
        return (max(r, g, b) - min(r, g, b)) <= BG_FLOOD_MAX_CHROMA

    for x in range(w):
        for y in (0, h - 1):
            i = y * w + x
            if not seen[i] and eligible(x, y):
                seen[i] = 1
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            i = y * w + x
            if not seen[i] and eligible(x, y):
                seen[i] = 1
                q.append((x, y))

    changed = 0
    while q:
        cx, cy = q.popleft()
        if px[cx, cy][:3] != (255, 255, 255):
            px[cx, cy] = (255, 255, 255)
            changed += 1
        for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
            if 0 <= nx < w and 0 <= ny < h:
                ni = ny * w + nx
                if not seen[ni] and eligible(nx, ny):
                    seen[ni] = 1
                    q.append((nx, ny))
    return changed


def remove_pure_black_blobs(px, w, h):
    seen = bytearray(w * h)
    removed = 0
    blobs = 0
    for sy in range(h):
        for sx in range(w):
            idx = sy * w + sx
            if seen[idx]:
                continue
            if px[sx, sy][:3] != (0, 0, 0):
                seen[idx] = 1
                continue
            members = []
            q = deque([(sx, sy)])
            seen[idx] = 1
            while q:
                cx, cy = q.popleft()
                members.append((cx, cy))
                for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        nidx = ny * w + nx
                        if not seen[nidx] and px[nx, ny][:3] == (0, 0, 0):
                            seen[nidx] = 1
                            q.append((nx, ny))
            if len(members) >= BLOB_MIN_PIXELS:
                blobs += 1
                for mx, my in members:
                    px[mx, my] = (255, 255, 255)
                    removed += 1
    return blobs, removed


def is_studio_shot(px, w, h):
    """White-cyclorama product shot: the border ring is uniformly bright and unsaturated."""
    inset_x = max(1, int(w * 0.02))
    inset_y = max(1, int(h * 0.02))
    pts = []
    for i in range(24):
        x = int(inset_x + (w - 2 * inset_x) * (i / 23.0))
        pts.append((x, inset_y))
        pts.append((x, h - inset_y - 1))
    for i in range(16):
        y = int(inset_y + (h - 2 * inset_y) * (i / 15.0))
        pts.append((inset_x, y))
        pts.append((w - inset_x - 1, y))
    for x, y in pts:
        r, g, b = px[x, y][:3]
        if min(r, g, b) < 205:
            return False
        if max(r, g, b) - min(r, g, b) > 14:
            return False
    return True


INK_MAX = 244
ISLAND_MAX_RATIO = 0.01


def remove_orphan_islands(px, w, h):
    """Whiten leftover specks: the subject is one large mass, artifacts are tiny islands."""
    seen = bytearray(w * h)
    comps = []
    for sy in range(h):
        for sx in range(w):
            i = sy * w + sx
            if seen[i]:
                continue
            if min(px[sx, sy][:3]) > INK_MAX:
                seen[i] = 1
                continue
            members = []
            q = deque([(sx, sy)])
            seen[i] = 1
            while q:
                cx, cy = q.popleft()
                members.append((cx, cy))
                for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1),
                               (cx - 1, cy - 1), (cx + 1, cy - 1), (cx - 1, cy + 1), (cx + 1, cy + 1)):
                    if 0 <= nx < w and 0 <= ny < h:
                        ni = ny * w + nx
                        if not seen[ni] and min(px[nx, ny][:3]) <= INK_MAX:
                            seen[ni] = 1
                            q.append((nx, ny))
            comps.append(members)
    if not comps:
        return 0, 0
    largest_len = max(len(c) for c in comps)
    cutoff = largest_len * ISLAND_MAX_RATIO
    islands = 0
    cleared = 0
    for c in comps:
        if len(c) == largest_len:
            continue
        drop = len(c) < cutoff
        if not drop:
            # A detached, uniformly pale patch on a white cyclorama is never real subject matter.
            tones = [min(px[x, y][:3]) for x, y in c]
            if sum(tones) / len(tones) >= 118:
                drop = True
        if drop:
            islands += 1
            for mx, my in c:
                px[mx, my] = (255, 255, 255)
                cleared += 1
    return islands, cleared


HAIRLINE_RADIUS = 6
HAIRLINE_MAX_DENSITY = 0.28
HAIRLINE_MIN_TONE = 100


def remove_hairlines(px, w, h):
    """Erase 1-3px stray strokes floating in the backdrop.

    Real bodywork sits in dense ink neighbourhoods; a scanning/eraser artifact is a
    lone thin stroke surrounded almost entirely by white, so local ink density separates them.
    """
    ink = [[0] * (w + 1) for _ in range(h + 1)]
    for y in range(h):
        rows = ink[y + 1]
        prev = ink[y]
        run = 0
        for x in range(w):
            if min(px[x, y][:3]) <= INK_MAX:
                run += 1
            rows[x + 1] = prev[x + 1] + run

    def density(x, y):
        x0 = max(0, x - HAIRLINE_RADIUS)
        y0 = max(0, y - HAIRLINE_RADIUS)
        x1 = min(w, x + HAIRLINE_RADIUS + 1)
        y1 = min(h, y + HAIRLINE_RADIUS + 1)
        total = ink[y1][x1] - ink[y0][x1] - ink[y1][x0] + ink[y0][x0]
        return total / float((x1 - x0) * (y1 - y0))

    targets = []
    for y in range(h):
        for x in range(w):
            tone = min(px[x, y][:3])
            if tone > INK_MAX or tone < HAIRLINE_MIN_TONE:
                continue
            if density(x, y) <= HAIRLINE_MAX_DENSITY:
                targets.append((x, y))
    for x, y in targets:
        px[x, y] = (255, 255, 255)
    return len(targets)


SUBJECT_LOSS_LIMIT = 0.06


def subject_mass(px, w, h):
    """Count pixels that clearly belong to the subject rather than the backdrop."""
    n = 0
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y][:3]
            if min(r, g, b) <= 200 or (max(r, g, b) - min(r, g, b)) > 24:
                n += 1
    return n


def process(path):
    img = Image.open(path).convert("RGB")
    w, h = img.size
    px = img.load()
    if not is_studio_shot(px, w, h):
        return None

    before_mass = subject_mass(px, w, h)
    original = img.copy()

    gray_changed = whiten_gray_background(px, w, h)
    gray_changed += remove_hairlines(px, w, h)
    blobs, blob_px = remove_pure_black_blobs(px, w, h)
    islands, island_px = remove_orphan_islands(px, w, h)
    blobs += islands
    blob_px += island_px

    after_mass = subject_mass(px, w, h)
    if before_mass and (before_mass - after_mass) / float(before_mass) > SUBJECT_LOSS_LIMIT:
        # The cleanup bit into the product itself (typical for white bodywork on a
        # white cyclorama) — discard it rather than ship a mangled photo.
        img = original
        return ("REVERTED", before_mass, after_mass)

    if gray_changed or blobs:
        ext = os.path.splitext(path)[1].lower()
        if ext in (".jpg", ".jpeg"):
            img.save(path, "JPEG", quality=94, subsampling=0)
        else:
            img.save(path, "PNG")
        return gray_changed, blobs, blob_px
    return 0, 0, 0


def main():
    targets = sys.argv[1:]
    if not targets:
        print("usage: fix_images.py <relative image paths...>")
        return
    for rel in targets:
        path = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
        if not os.path.exists(path):
            print(f"MISSING {rel}")
            continue
        result = process(path)
        if result is None:
            print(f"skip (not studio) {rel}")
            continue
        if result[0] == "REVERTED":
            print(f"REVERTED {rel}: mass {result[1]} -> {result[2]} (would damage subject)")
            continue
        gray, blobs, blob_px = result
        if gray or blobs:
            print(f"FIXED {rel}: gray_px={gray} blobs={blobs} blob_px={blob_px}")
        else:
            print(f"clean {rel}")


if __name__ == "__main__":
    main()
