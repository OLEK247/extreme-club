# -*- coding: utf-8 -*-
import base64, html as H, io, json, os, re, subprocess, sys, tempfile
import pymupdf
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PL = os.path.join(ROOT, "karty-katalogowe-PL")
OUT = os.path.join(ROOT, "karty-katalogowe")
BROWSER = os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\Application\brave.exe")
WZOR = os.path.join(PL, "WZOR-sea-doo-spark-x-trixx-110.html")

DETAILED = {
    "seadoo-spark-x-trixx": ("WZOR-sea-doo-spark-x-trixx-110.html", "Rotax® 1000 ACE™ – 110 · Kadłub Spark® · Lekka i pełna zabawy platforma", "„Psotnik na wodzie, jeszcze bardziej niż kiedykolwiek.”"),
    "seadoo-spark-x": ("sea-doo-spark-x-110-for-3.html", None, None),
    "seadoo-fishpro-trophy": ("sea-doo-fishpro-trophy-170.html", None, None),
    "seadoo-gtr-2027": ("sea-doo-gtr-230.html", None, None),
    "seadoo-gtr-x-2027": ("sea-doo-gtr-x-300.html", None, None),
}

with open(WZOR, encoding="utf-8") as f:
    TPL = f.read()

CSS = re.search(r"<style>(.*?)</style>", TPL, re.S).group(1)
CSS = CSS.replace(
    "margin:34px 0 12px; padding:9px 14px; background:var(--accent);\n    border-left:3px solid var(--accent-dark); border-radius:0 4px 4px 0;",
    "margin:34px 0 12px; padding:9px 14px; background:var(--bg-soft);\n    border-left:2px solid var(--accent); border-radius:0;")
CSS = CSS.replace(".topbar img.logo{height:46px;}", ".topbar img.logo{height:64px;}")
CSS = CSS.replace("background:var(--bg-soft); height:340px;}", "background:#fff; height:340px;}")
CSS = re.sub(r"@media print\{.*\}\s*$", "", CSS.strip(), flags=re.S)
CSS += """
  .hero{padding:18px 24px;}
  .hero img.contain{object-fit:contain; object-position:center;}
  .model-tag{margin-bottom:6px;}
  h1{margin-bottom:6px;}
  .tagline{margin:12px 0 22px;}
  .color-block{margin-top:18px;}
  @page{size:A4; margin:14mm 0 14mm;}
  @page:first{margin-top:0;}
  .page{padding:30px 40px 0;}
  tr, li, .desc-item, .swatch-item, .contact-band, .footer-note{break-inside:avoid;}
  h2.section{break-after:avoid;}
  table.spec{break-inside:auto;}
  .page{zoom:.86;}
"""
CONTACT = re.search(r'(<div class="contact-band">.*?)\s*<div class="footer-note">', TPL, re.S).group(1)
BRP_IMG = re.search(r'<img class="brp-mark"[^>]*>', TPL).group(0)
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'


def logo_src():
    im = Image.open(os.path.join(ROOT, "LOGO EXTREME nowe  kompas.png"))
    im = im.crop(im.getbbox())
    im = im.resize((420, round(420 * im.height / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()

LOGO = logo_src()


def img_src(path):
    src = Image.open(path).convert("RGBA")
    im = Image.new("RGB", src.size, "white")
    im.paste(src, mask=src.split()[3])
    if im.width > 1400:
        im = im.resize((1400, round(1400 * im.height / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "JPEG", quality=88)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()


def fmt(x):
    if isinstance(x, float):
        return (f"{x:.1f}".rstrip("0").rstrip(".") if x % 1 else str(int(x))).replace(".", ",")
    return f"{x:,}".replace(",", " ") if isinstance(x, int) and x >= 10000 else str(x)


def e(s):
    return H.escape(str(s), quote=False)


OVERRIDES = {
    "seadoo-gtr-2027": {"Masa sucha (olej, płyn chłodzący, bez paliwa)": "361 kg", "Stosunek mocy do masy (KM / kg)": "0,64"},
}


def parse_detailed(fname):
    t = open(os.path.join(PL, fname), encoding="utf-8").read()
    body = t.split('<div class="contact-band">')[0]
    d = {"title": re.search(r"<h1>(.*?)</h1>", body).group(1).strip(),
         "hero": re.search(r'<div class="hero"[^>]*>\s*<img src="([^"]+)"', body).group(1),
         "colors": re.findall(r'linear-gradient\(135deg,(#[0-9a-fA-F]+) 0%,#[0-9a-fA-F]+ 50%,(#[0-9a-fA-F]+) 50%.*?<span class="swatch-name">(.*?)</span>', body, re.S),
         "sections": []}
    d["colors"] = [(n, a, b) for a, b, n in d["colors"]]
    parts = re.split(r'<h2 class="section">(.*?)</h2>', body)[1:]
    for title, chunk in zip(parts[::2], parts[1::2]):
        if '<table class="spec">' in chunk:
            rows = re.findall(r'<td class="label">(.*?)</td><td class="value">(.*?)</td>', chunk, re.S)
            d["sections"].append((title, "table", rows))
        elif '<ul class="features">' in chunk:
            items = []
            for li in re.findall(r"<li>.*?</svg>(.*?)</li>", chunk, re.S):
                m = re.match(r"\s*<span><b>(.*?)</b><em>(.*?)</em></span>", li, re.S)
                items.append((m.group(1), m.group(2)) if m else re.sub(r"</?span>", "", li).strip())
            d["sections"].append((title, "list", items))
        else:
            items = re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", chunk, re.S)
            d["sections"].append((title, "desc", items))
    fn = re.search(r'<div class="footer-note">\s*<div>(.*?)</div>', t, re.S).group(1).strip()
    d["footnote"] = fn
    return d


def generic(v, spec):
    electric = v["category"] == "electric" or spec.get("battery_capacity_kwh")
    secs = []
    cap = []
    if spec.get("rider_capacity"): cap.append(("Liczba miejsc", fmt(spec["rider_capacity"])))
    if spec.get("fuel_capacity_l") and not electric: cap.append(("Pojemność zbiornika paliwa", f'{fmt(spec["fuel_capacity_l"])} l'))
    if spec.get("storage_capacity_l"): cap.append(("Łączna pojemność schowków", f'{fmt(spec["storage_capacity_l"])} l'))
    if spec.get("towing_capacity_kg"): cap.append(("Uciąg (holowanie)", f'{fmt(spec["towing_capacity_kg"])} kg'))
    if cap: secs.append(("Pojemność", "table", cap))
    dims = [(l, f"{fmt(spec[k])} cm") for k, l in [("length_cm", "Długość"), ("width_cm", "Szerokość"), ("height_cm", "Wysokość"), ("ground_clearance_cm", "Prześwit")] if spec.get(k)]
    if dims: secs.append(("Wymiary", "table", dims))
    eng = [("Silnik", e(v["engine"]))] if v.get("engine") else []
    if electric:
        if spec.get("motor_power_hp"): eng.append(("Moc silnika elektrycznego", f'{fmt(spec["motor_power_hp"])} KM'))
        if spec.get("battery_capacity_kwh"): eng.append(("Pojemność akumulatora", f'{fmt(spec["battery_capacity_kwh"])} kWh'))
        if spec.get("range_km"): eng.append(("Zasięg", f'do {fmt(spec["range_km"])} km'))
        if spec.get("charge_time"): eng.append(("Czas ładowania", e(spec["charge_time"])))
    else:
        if spec.get("engine_displacement_cc"): eng.append(("Pojemność skokowa", f'{fmt(spec["engine_displacement_cc"])} cm³'))
        if spec.get("engine_power_hp"): eng.append(("Moc", f'{fmt(spec["engine_power_hp"])} KM'))
    if eng: secs.append(("Napęd" if electric else "Silnik", "table", eng))
    mass = []
    if spec.get("dry_weight_kg"):
        mass.append(("Masa sucha", f'{fmt(spec["dry_weight_kg"])} kg'))
        hp = spec.get("engine_power_hp") or spec.get("motor_power_hp")
        if hp: mass.append(("Stosunek mocy do masy (KM / kg)", fmt(round(hp / spec["dry_weight_kg"], 2))))
    if mass: secs.append(("Masa", "table", mass))
    if v.get("highlights"): secs.append(("Najważniejsze cechy", "list", [e(h) for h in v["highlights"]]))
    descs = []
    for i, p in enumerate(v.get("fullDesc") or []):
        descs.append(("O modelu" if i == 0 else "", e(p)))
    for f in v.get("features") or []:
        descs.append((e(f["title"]), e(f["text"])))
    if v.get("forWho"): descs.append(("Dla kogo", e(v["forWho"])))
    if descs: secs.append(("Szczegółowe opisy", "desc", descs))
    return secs


def section_html(title, kind, data):
    out = [f'  <h2 class="section">{title}</h2>']
    if kind == "table":
        out.append('  <table class="spec">')
        out += [f'    <tr><td class="label">{a}</td><td class="value">{b}</td></tr>' for a, b in data]
        out.append("  </table>")
    elif kind == "list":
        out.append('  <ul class="features">')
        for it in data:
            if isinstance(it, tuple):
                out.append(f"    <li>{CHECK}<span><b>{it[0]}</b><em>{it[1]}</em></span></li>")
            else:
                out.append(f"    <li>{CHECK}<span>{it}</span></li>")
        out.append("  </ul>")
    else:
        out.append('  <div class="descriptions">')
        for h3, p in data:
            out.append('    <div class="desc-item">' + (f"\n      <h3>{h3}</h3>" if h3 else "") + f"\n      <p>{p}</p>\n    </div>")
        out.append("  </div>")
    return "\n".join(out) + "\n"


def card_html(v, specs):
    brand = "Sea-Doo®" if v["category"] == "seadoo" else "Can-Am®"
    year = v.get("myYear")
    det = DETAILED.get(v["id"])
    if det:
        d = parse_detailed(det[0])
        ov = OVERRIDES.get(v["id"], {})
        d["sections"] = [(t, k, [(a, ov.get(a, b)) for a, b in rows] if k == "table" else rows) for t, k, rows in d["sections"]]
        title, hero, colors, secs, footnote = d["title"], d["hero"], d["colors"], d["sections"], d["footnote"]
        subtitle = det[1] or e(v["engine"])
        tagline = det[2] or e(v["desc"])
        year = 2027
        hero_cls = ' class="contain"'
    else:
        title = f"{brand} {e(v['name'])}"
        cols = v.get("colors") or []
        p = cols[0]["image"] if cols and cols[0].get("image") else v["images"][0]
        hero = img_src(os.path.join(ROOT, p))
        colors = [(e(c["name"]), c["hex1"], c.get("hex2") or c["hex1"]) for c in cols]
        secs = generic(v, specs)
        subtitle = " · ".join(x for x in [e(v["engine"]), e(v["highlights"][1]) if len(v.get("highlights", [])) > 1 else ""] if x)
        tagline = "„" + e(v["desc"]) + "”"
        footnote = "Karta ma charakter informacyjny i poglądowy — nie stanowi oferty w rozumieniu Kodeksu Cywilnego. Dane techniczne wg oficjalnej specyfikacji BRP dla wybranej wersji. Aktualny cennik na extreme-club.pl.<br>\n      "
        hero_cls = ' class="contain"'
        footnote +=f"Nazwy handlowe i oznaczenia techniczne ({brand}, Rotax®, BRP itd.) pozostawiono w oryginalnej formie. Pozostała treść została przetłumaczona na język polski."
    meta_top = f"Katalog pojazdów — rocznik {year}" if year else "Katalog pojazdów"
    tag = (f"MODEL {year} &nbsp;·&nbsp; " if year else "") + e(v["segment"]).upper()
    sw = "\n".join(f'''      <div class="swatch-item">
        <span class="swatch-split" style="background:linear-gradient(135deg,{a} 0%,{a} 50%,{b} 50%,{b} 100%);"></span>
        <span class="swatch-name">{n}</span>
      </div>''' for n, a, b in colors)
    color_block = (f'''  <div class="color-block">
    <p class="color-label">{"Dostępny kolor" if len(colors) == 1 else "Dostępne kolory"}</p>
    <div class="color-swatches">
{sw}
    </div>
  </div>
''') if colors else ""
    out = f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>{re.sub("<[^>]+>", "", title)} — Karta katalogowa</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div class="page" id="page">

  <div class="topbar">
    <img class="logo" src="{LOGO}" alt="Extreme Club">
    <div class="meta">
      <b>{meta_top}</b><br>
      Karta katalogowa PL · {brand}
    </div>
  </div>

  <div class="hero">
    <img{hero_cls} src="{hero}" alt="{re.sub("<[^>]+>", "", title)}">
  </div>

  <p class="model-tag">{tag}</p>
  <h1>{title}</h1>
  <p class="subtitle">{subtitle}</p>
  <p class="tagline">{tagline}</p>

{color_block}
'''
    for s in secs:
        out += "\n" + section_html(*s)
    out += f'''
  {CONTACT}

  <div class="footer-note">
    <div>
      {footnote}
    </div>
    {BRP_IMG}
  </div>

</div>
</body>
</html>
'''
    return out


def render(html_text, pdf_path, tmpdir):
    hp = os.path.join(tmpdir, "card.html")
    raw = os.path.join(tmpdir, "card.pdf")
    open(hp, "w", encoding="utf-8").write(html_text)
    if os.path.exists(raw): os.remove(raw)
    subprocess.run([BROWSER, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
                    "--virtual-time-budget=8000", f"--print-to-pdf={raw}", "file:///" + hp.replace("\\", "/")],
                   check=True, capture_output=True, timeout=180)
    d = pymupdf.open(raw)
    d.save(pdf_path, garbage=4, deflate=True)
    d.close()

def main():
    only = sys.argv[1:]
    V = json.load(open(os.path.join(ROOT, "cenniki", "_all_vehicles.json"), encoding="utf-8"))
    s27 = json.load(open(os.path.join(ROOT, "cenniki", "specs_2027.json"), encoding="utf-8"))
    sm = json.load(open(os.path.join(ROOT, "cenniki", "specs_merged.json"), encoding="utf-8"))
    tmp = tempfile.mkdtemp()
    done = 0
    for v in V:
        if only and v["id"] not in only: continue
        spec = s27.get(v["id"]) or sm.get(v["id"])
        render(card_html(v, spec or {}), os.path.join(OUT, v["id"] + ".pdf"), tmp)
        done += 1
        print("ok", v["id"], flush=True)
    print("built", done)


if __name__ == "__main__":
    main()
