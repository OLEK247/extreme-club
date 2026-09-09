# -*- coding: utf-8 -*-
import json, os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, KeepTogether, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import Flowable

BASE  = os.path.dirname(os.path.abspath(__file__))
ROOT  = os.path.dirname(BASE)
IMAGES = os.path.join(ROOT, "images")
OUT_DIR = os.path.join(ROOT, "karty-katalogowe")
os.makedirs(OUT_DIR, exist_ok=True)

MODEL_YEAR = "2026"

with open(os.path.join(BASE, "specs_merged.json"), encoding="utf-8") as _f:
    TECH_SPECS = json.load(_f)

FONTS_DIR = "C:/Windows/Fonts"
pdfmetrics.registerFont(TTFont("Arial",        os.path.join(FONTS_DIR, "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold",   os.path.join(FONTS_DIR, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic", os.path.join(FONTS_DIR, "ariali.ttf")))

ACCENT   = colors.HexColor("#0EA5E9")
DARK     = colors.HexColor("#14181c")
MUTED    = colors.HexColor("#5b6570")
BORDER   = colors.HexColor("#dde2e6")
PANEL    = colors.HexColor("#f4f7f9")
HEADER_BG= colors.HexColor("#0c1a27")
WHITE    = colors.white

COMPANY_NAME    = "EXTREME CLUB"
COMPANY_ADDRESS = "ul. Nowa 88, 83-031 Łęgowo"
COMPANY_PHONE   = "Tel. 501 564 518"
COMPANY_EMAIL   = "kontakt@extreme-club.pl"
COMPANY_WEB     = "www.extreme-club.pl"

styles = getSampleStyleSheet()
def S(name, **kw):
    return ParagraphStyle(name, parent=styles["Normal"], **kw)

sEyebrow   = S("ey", fontName="Arial-Bold",   fontSize=7.5,  textColor=ACCENT,  leading=10,   tracking=2)
sYear      = S("yr", fontName="Arial-Bold",   fontSize=7.5,  textColor=MUTED,   leading=10,   alignment=TA_RIGHT)
sCompany   = S("co", fontName="Arial-Bold",   fontSize=9.5,  textColor=DARK,    leading=12,   alignment=TA_RIGHT)
sMeta      = S("me", fontName="Arial",        fontSize=7.5,  textColor=MUTED,   leading=10.5, alignment=TA_RIGHT)
sName      = S("nm", fontName="Arial-Bold",   fontSize=30,   textColor=DARK,    leading=32,   spaceBefore=2, spaceAfter=2)
sTagline   = S("tg", fontName="Arial-Italic", fontSize=9.5,  textColor=MUTED,   leading=13,   spaceAfter=4)
sPrice     = S("pr", fontName="Arial-Bold",   fontSize=13,   textColor=ACCENT,  leading=15)
sSecHead   = S("sh", fontName="Arial-Bold",   fontSize=7.8,  textColor=ACCENT,  leading=10,   spaceBefore=5, spaceAfter=2, tracking=1.5)
sLabel     = S("lb", fontName="Arial",        fontSize=8.2,  textColor=MUTED,   leading=11.5)
sValue     = S("vl", fontName="Arial-Bold",   fontSize=8.8,  textColor=DARK,    leading=12)
sCheckItem = S("ci", fontName="Arial",        fontSize=8.5,  textColor=DARK,    leading=12)
sColorName = S("cn", fontName="Arial",        fontSize=8,    textColor=DARK,    leading=11)
sFooter    = S("ft", fontName="Arial-Italic", fontSize=7,    textColor=MUTED,   leading=9.5)
sHeaderWht = S("hw", fontName="Arial-Bold",   fontSize=8,    textColor=WHITE,   leading=11,   alignment=TA_RIGHT)
sHeaderCat = S("hc", fontName="Arial-Bold",   fontSize=8,    textColor=ACCENT,  leading=11)
sEngHead   = S("eh", fontName="Arial-Bold",   fontSize=8.5,  textColor=DARK,    leading=11,   spaceBefore=4)


class ColorDot(Flowable):
    def __init__(self, hex1, hex2, size=10):
        super().__init__()
        self.hex1, self.hex2, self.size = hex1, hex2, size
        self.width = self.height = size

    def draw(self):
        c, s = self.canv, self.size
        c.saveState()
        p = c.beginPath(); p.circle(s/2, s/2, s/2); c.clipPath(p, stroke=0)
        c.setFillColor(colors.HexColor(self.hex1)); c.rect(0, 0, s/2, s, fill=1, stroke=0)
        c.setFillColor(colors.HexColor(self.hex2)); c.rect(s/2, 0, s/2, s, fill=1, stroke=0)
        c.restoreState()
        c.setStrokeColor(BORDER); c.setLineWidth(0.5)
        c.circle(s/2, s/2, s/2, fill=0, stroke=1)


class HRule(Flowable):
    def __init__(self, width, color=BORDER, thickness=0.7):
        super().__init__(); self.width=width; self.rcolor=color; self.thickness=thickness; self.height=self.thickness
    def draw(self):
        self.canv.setStrokeColor(self.rcolor); self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)


def fmt_num(x):
    if isinstance(x, float):
        s = f"{x:.1f}".rstrip("0").rstrip(".") if x % 1 else str(int(x))
        return s.replace(".", ",")
    return str(x)


def tech_groups(v):
    spec = TECH_SPECS.get(v.get("id"), {})
    electric = "electric" in v.get("id","").lower() or spec.get("battery_capacity_kwh")

    capacity = []
    if spec.get("rider_capacity"):
        capacity.append(("Liczba osób", f'{fmt_num(spec["rider_capacity"])}'))
    if spec.get("fuel_capacity_l") and not electric:
        capacity.append(("Zbiornik paliwa", f'{fmt_num(spec["fuel_capacity_l"])} l'))
    if spec.get("storage_capacity_l"):
        capacity.append(("Pojemność schowków", f'{fmt_num(spec["storage_capacity_l"])} l'))
    if spec.get("towing_capacity_kg"):
        capacity.append(("Udźwig holowniczy", f'{fmt_num(spec["towing_capacity_kg"])} kg'))

    dims = []
    for k, lbl, unit in [("length_cm","Długość","cm"),("width_cm","Szerokość","cm"),("height_cm","Wysokość","cm"),("ground_clearance_cm","Prześwit","cm")]:
        if spec.get(k):
            dims.append((lbl, f'{fmt_num(spec[k])} {unit}'))

    engine_rows = []
    if electric:
        if spec.get("motor_power_hp"): engine_rows.append(("Moc silnika el.", f'{fmt_num(spec["motor_power_hp"])} KM'))
        if spec.get("battery_capacity_kwh"): engine_rows.append(("Akumulator", f'{fmt_num(spec["battery_capacity_kwh"])} kWh'))
        if spec.get("range_km"): engine_rows.append(("Zasięg", f'do {fmt_num(spec["range_km"])} km'))
        if spec.get("charge_time"): engine_rows.append(("Ładowanie (20→80%)", spec["charge_time"]))
    else:
        if spec.get("engine_displacement_cc"): engine_rows.append(("Pojemność", f'{fmt_num(spec["engine_displacement_cc"])} cm³'))
        if spec.get("engine_power_hp"): engine_rows.append(("Moc", f'{fmt_num(spec["engine_power_hp"])} KM'))

    if spec.get("dry_weight_kg"):
        engine_rows.append(("Masa własna", f'{fmt_num(spec["dry_weight_kg"])} kg'))

    return capacity, dims, engine_rows


def top_header(v):
    logo_path = os.path.join(IMAGES, "logo-extreme.png")
    logo = Image(logo_path); logo._restrictSize(36*mm, 14*mm)

    cat_badge = Table([[Paragraph((v.get("segment") or v.get("categoryLabel","")).upper(), sHeaderCat)]],
                      colWidths=[None])
    cat_badge.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), colors.HexColor("#e8f6fd")),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),
    ]))

    right_col = [
        Paragraph(COMPANY_NAME, sCompany),
        Paragraph(COMPANY_ADDRESS, sMeta),
        Paragraph(f"{COMPANY_PHONE}  ·  {COMPANY_EMAIL}", sMeta),
        Paragraph(COMPANY_WEB, sMeta),
    ]

    tbl = Table([[logo, cat_badge, right_col]], colWidths=[40*mm, None, 75*mm])
    tbl.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("ALIGN",(1,0),(1,0),"LEFT"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    return tbl


def make_spec_table(rows, col_widths=(34*mm, None), alt_bg=True):
    tbl_rows = [[Paragraph(k, sLabel), Paragraph(v, sValue)] for k,v in rows]
    if not tbl_rows:
        return None
    style = [
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
        ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ("LINEBELOW",(0,0),(-1,-2),0.5,BORDER),
    ]
    if alt_bg:
        for i in range(0, len(tbl_rows), 2):
            style.append(("BACKGROUND",(0,i),(-1,i),PANEL))
    t = Table(tbl_rows, colWidths=list(col_widths))
    t.setStyle(TableStyle(style))
    return t


def section_label(text, line_width=90*mm):
    return [
        Paragraph(text, sSecHead),
        HRule(line_width, color=ACCENT, thickness=1.2),
        Spacer(1, 2),
    ]


def left_column(v, page_w):
    col_w = page_w * 0.52
    items = []

    # Model name + tagline + price
    items.append(Paragraph(v.get("name",""), sName))
    items.append(HRule(22*mm, ACCENT, 2.2))
    items.append(Spacer(1, 2*mm))
    if v.get("desc"):
        items.append(Paragraph(v["desc"], sTagline))
    items.append(Spacer(1, 1*mm))

    price_tbl = Table([[Paragraph("CENA OD", sSecHead), Paragraph(v.get("price",""), sPrice)]],
                      colWidths=[22*mm, None])
    price_tbl.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"BOTTOM"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    items.append(price_tbl)
    items.append(Spacer(1, 4*mm))

    # Colors
    colors_list = v.get("colors") or []
    if colors_list:
        items.extend(section_label("KOLORYSTYKA", col_w - 8*mm))
        for c in colors_list:
            row = Table([[ColorDot(c.get("hex1","#999"), c.get("hex2","#666")), Paragraph(c.get("name",""), sColorName)]],
                        colWidths=[14, None])
            row.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                                     ("LEFTPADDING",(0,0),(-1,-1),0),
                                     ("TOPPADDING",(0,0),(-1,-1),2),("BOTTOMPADDING",(0,0),(-1,-1),2)]))
            items.append(row)
        items.append(Spacer(1, 4*mm))

    capacity, dims, _ = tech_groups(v)

    if capacity:
        items.extend(section_label("POJEMNOŚĆ / ŁADOWNOŚĆ", col_w - 8*mm))
        t = make_spec_table(capacity, col_widths=(40*mm, None))
        if t: items.append(t)
        items.append(Spacer(1, 3*mm))

    if dims:
        items.extend(section_label("WYMIARY", col_w - 8*mm))
        t = make_spec_table(dims, col_widths=(34*mm, None))
        if t: items.append(t)
        items.append(Spacer(1, 3*mm))

    highlights = v.get("highlights") or []
    if highlights:
        items.extend(section_label("KLUCZOWE WYPOSAŻENIE", col_w - 8*mm))
        hi_rows = [[Paragraph("•", ParagraphStyle("dot", parent=sCheckItem, textColor=ACCENT, fontName="Arial-Bold", fontSize=9)),
                    Paragraph(h, sCheckItem)] for h in highlights]
        hi_tbl = Table(hi_rows, colWidths=[6*mm, None])
        hi_tbl.setStyle(TableStyle([
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),2),
            ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
        ]))
        items.append(hi_tbl)

    return items


def right_column(v, img_path, page_w):
    col_w = page_w * 0.44
    items = []

    if img_path:
        hero = Image(img_path)
        hero._restrictSize(col_w, 62*mm)
        img_tbl = Table([[hero]], colWidths=[col_w])
        img_tbl.setStyle(TableStyle([("ALIGN",(0,0),(-1,-1),"CENTER"),
                                     ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0)]))
        items.append(img_tbl)
        items.append(Spacer(1, 4*mm))

    _, _, engine_rows = tech_groups(v)

    if v.get("engine"):
        items.extend(section_label(f"SILNIK: {v['engine'].upper()}", col_w))
    elif engine_rows:
        items.extend(section_label("NAPĘD", col_w))

    if engine_rows:
        t = make_spec_table(engine_rows, col_widths=(38*mm, None))
        if t: items.append(t)
        items.append(Spacer(1, 3*mm))

    if v.get("forWho"):
        items.extend(section_label("DLA KOGO", col_w))
        box = Table([[Paragraph(v["forWho"], sCheckItem)]], colWidths=[col_w])
        box.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,-1),PANEL),
            ("LINEBEFORE",(0,0),(0,-1),2.2,ACCENT),
            ("LEFTPADDING",(0,0),(-1,-1),8),("RIGHTPADDING",(0,0),(-1,-1),6),
            ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6),
        ]))
        items.append(box)
        items.append(Spacer(1, 3*mm))

    items.extend(section_label("GWARANCJA", col_w))
    is_ryker = "ryker" in v.get("id", "")
    two_year = v.get("category") == "seadoo" or (v.get("category") == "trojkolowce" and not is_ryker)
    warranty_years = "2 lat" if two_year else "1 roku"
    items.append(Paragraph(f"Ograniczona gwarancja BRP na okres {warranty_years}.", sLabel))

    return items


def footer_row():
    note = ("Karta katalogowa ma charakter informacyjny i poglądowy — nie stanowi oferty w rozumieniu Kodeksu Cywilnego. "
            "Dane techniczne wg oficjalnej specyfikacji BRP dla wybranej wersji — mogą się różnić dla innych wariantów. "
            "Aktualny cennik na extreme-club.pl.")
    brp_logo_path = os.path.join(IMAGES, "brp-logo.png")
    items = [HRule(178*mm, BORDER, 0.6), Spacer(1, 2*mm), Paragraph(note, sFooter)]
    if os.path.exists(brp_logo_path):
        brp = Image(brp_logo_path); brp._restrictSize(9*mm, 9*mm)
        badge = Table([[brp, Paragraph("Autoryzowany Dealer BRP  ·  Sea-Doo  ·  Can-Am", sFooter)]],
                      colWidths=[11*mm, None])
        badge.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"MIDDLE"),("LEFTPADDING",(0,0),(-1,-1),0)]))
        items += [Spacer(1, 2*mm), badge]
    return [KeepTogether(items)]


def build_spec_sheet(v):
    filename = f"{v['id']}.pdf"
    path = os.path.join(OUT_DIR, filename)
    LM = RM = 16*mm
    TM = BM = 11*mm
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM)
    PW = A4[0] - LM - RM

    img_path = None
    colors_list = v.get("colors") or []
    if colors_list and colors_list[0].get("image"):
        img_path = os.path.join(ROOT, colors_list[0]["image"])
    elif v.get("images"):
        img_path = os.path.join(ROOT, v["images"][0])
    if img_path and not os.path.exists(img_path):
        img_path = None

    LEFT_W  = PW * 0.54
    RIGHT_W = PW * 0.46

    left  = left_column(v, PW)
    right = right_column(v, img_path, PW)

    body = Table([[left, right]], colWidths=[LEFT_W, RIGHT_W])
    body.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(0,0),7*mm),
        ("RIGHTPADDING",(1,0),(1,0),0),
        ("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))

    story = [
        top_header(v),
        Spacer(1, 3*mm),
        HRule(PW, BORDER, 0.7),
        Spacer(1, 4*mm),
        body,
        Spacer(1, 4*mm),
    ]
    story.extend(footer_row())

    features = v.get("features") or []
    if features:
        story.append(PageBreak())
        story.append(top_header(v))
        story.append(Spacer(1, 3*mm))
        story.append(HRule(PW, BORDER, 0.7))
        story.append(Spacer(1, 5*mm))
        story.append(Paragraph(f"Poznaj {v.get('name','')}", sName))
        story.append(HRule(24*mm, ACCENT, 2))
        story.append(Spacer(1, 5*mm))
        feat_cells = []
        for f in features:
            cell = [
                Table([[""]], colWidths=[14], rowHeights=[2],
                      style=TableStyle([("BACKGROUND",(0,0),(-1,-1),ACCENT)])),
                Spacer(1, 4),
                Paragraph(f.get("title",""), ParagraphStyle("ft2", parent=sValue, fontSize=9.5, leading=13)),
                Paragraph(f.get("text",""),  ParagraphStyle("ft3", parent=sLabel,  fontSize=8.2, leading=11.5)),
            ]
            feat_cells.append(cell)
        ncols = 2
        grid_rows = [feat_cells[i:i+ncols] for i in range(0, len(feat_cells), ncols)]
        for r in grid_rows:
            while len(r) < ncols: r.append("")
        grid = Table(grid_rows, colWidths=[87*mm]*ncols)
        grid.setStyle(TableStyle([
            ("VALIGN",(0,0),(-1,-1),"TOP"),
            ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),10*mm),
            ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),12*mm),
        ]))
        story.append(grid)
        story.extend(footer_row())

    doc.build(story)
    return filename


def main():
    with open(os.path.join(BASE, "vehicles.json"), encoding="utf-8") as f:
        vehicles = json.load(f)
    ok, failed = 0, []
    for v in vehicles:
        try:
            build_spec_sheet(v)
            ok += 1
        except Exception as e:
            failed.append((v.get("id"), str(e)))
    print(f"Wygenerowano {ok}/{len(vehicles)} kart katalogowych -> {OUT_DIR}")
    if failed:
        print("Błędy:")
        for vid, err in failed: print(f"  - {vid}: {err}")


if __name__ == "__main__":
    main()
