# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter
import os

IMG_DIR = r"C:\Users\Jebany BOSS\Desktop\extreme-club\images"

files = [
    ("seadoo-gtx-170-new.png", "seadoo-gtx-170-new.webp"),
    ("seadoo-gtx-230-new.png", "seadoo-gtx-230-new.webp"),
    ("seadoo-gtr-230-new.png", "seadoo-gtr-230-new.webp"),
    ("seadoo-gtr-x-300-new.png", "seadoo-gtr-x-300-new.webp"),
    ("seadoo-wake-pro-230-new.png", "seadoo-wake-pro-230-new.webp"),
]

for src_name, dst_name in files:
    src = os.path.join(IMG_DIR, src_name)
    dst = os.path.join(IMG_DIR, dst_name)
    img = Image.open(src).convert("RGBA")
    img = img.filter(ImageFilter.GaussianBlur(radius=1.2))
    # Kompozytuj na biale tlo -> RGB, bez alpha
    bg = Image.new("RGB", img.size, (255, 255, 255))
    bg.paste(img, mask=img.split()[3])
    bg.save(dst, "WEBP", quality=85)
    print(f"{dst_name}: {os.path.getsize(dst)//1024}KB")

print("Gotowe.")
