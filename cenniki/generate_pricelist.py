# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGES = os.path.join(os.path.dirname(BASE), "images")

FONTS_DIR = "C:/Windows/Fonts"
pdfmetrics.registerFont(TTFont("Arial", os.path.join(FONTS_DIR, "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold", os.path.join(FONTS_DIR, "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic", os.path.join(FONTS_DIR, "ariali.ttf")))

ACCENT = colors.HexColor("#0EA5E9")
DARK_TEXT = colors.HexColor("#14181c")
MUTED = colors.HexColor("#5b6570")
BORDER = colors.HexColor("#e2e6ea")
ROW_ALT = colors.HexColor("#f1f3f5")

COMPANY_NAME = "EXTREME CLUB"
COMPANY_ADDRESS = "ul. Nowa 88, 83-031 Łęgowo"
COMPANY_PHONE = "Tel. 501 564 518"
COMPANY_EMAIL = "kontakt@extreme-club.pl"

styles = getSampleStyleSheet()
style_company = ParagraphStyle("company", parent=styles["Normal"], fontName="Arial-Bold", fontSize=13, textColor=DARK_TEXT, alignment=TA_RIGHT, leading=16)
style_meta = ParagraphStyle("meta", parent=styles["Normal"], fontName="Arial", fontSize=9.5, textColor=MUTED, alignment=TA_RIGHT, leading=13)
style_section = ParagraphStyle("section", parent=styles["Normal"], fontName="Arial-Bold", fontSize=10, textColor=colors.white, leading=13)
style_footer = ParagraphStyle("footer", parent=styles["Normal"], fontName="Arial-Italic", fontSize=8, textColor=MUTED)
style_cell = ParagraphStyle("cell", parent=styles["Normal"], fontName="Arial", fontSize=8.3, textColor=DARK_TEXT, leading=10)
style_cell_right = ParagraphStyle("cell_right", parent=style_cell, alignment=TA_RIGHT)
style_head_cell = ParagraphStyle("head_cell", parent=styles["Normal"], fontName="Arial-Bold", fontSize=9, textColor=colors.white, leading=11)
style_head_cell_right = ParagraphStyle("head_cell_right", parent=style_head_cell, alignment=TA_RIGHT)


def build_pdf(filename, header_cols, sections, footer_note, col_widths, brp_tagline="Autoryzowany Dealer BRP &nbsp;|&nbsp; Sea-Doo &middot; Can-Am", margin_mm=16):
    doc = SimpleDocTemplate(
        os.path.join(BASE, filename),
        pagesize=A4,
        leftMargin=margin_mm * mm, rightMargin=margin_mm * mm,
        topMargin=10 * mm, bottomMargin=10 * mm,
    )
    story = []

    logo_path = os.path.join(IMAGES, "logo-extreme.png")
    logo = Image(logo_path, width=42 * mm, height=42 * mm * (1))
    logo.drawWidth = 46 * mm
    logo.drawHeight = 46 * mm * 0.32
    logo._restrictSize(46 * mm, 20 * mm)

    company_block = [
        Paragraph(COMPANY_NAME, style_company),
        Paragraph(COMPANY_ADDRESS, style_meta),
        Paragraph(COMPANY_PHONE + " &nbsp;&nbsp; email: " + COMPANY_EMAIL, style_meta),
    ]

    header_table = Table(
        [[logo, company_block]],
        colWidths=[70 * mm, doc.width - 70 * mm],
    )
    header_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 4 * mm))

    n_cols = len(header_cols)
    header_row = [
        Paragraph(str(c), style_head_cell_right if i == n_cols - 1 else style_head_cell)
        for i, c in enumerate(header_cols)
    ]
    table_data = [header_row]
    row_styles = []
    row_idx = 1

    for section_title, rows in sections:
        table_data.append([Paragraph(section_title, style_section)] + [""] * (n_cols - 1))
        row_styles.append(("SPAN", (0, row_idx), (-1, row_idx)))
        row_styles.append(("BACKGROUND", (0, row_idx), (-1, row_idx), ACCENT))
        row_styles.append(("TOPPADDING", (0, row_idx), (-1, row_idx), 5))
        row_styles.append(("BOTTOMPADDING", (0, row_idx), (-1, row_idx), 5))
        row_idx += 1
        for i, r in enumerate(rows):
            wrapped_row = [
                Paragraph(str(c) if c else "-", style_cell_right if j == n_cols - 1 else style_cell)
                for j, c in enumerate(r)
            ]
            table_data.append(wrapped_row)
            if i % 2 == 1:
                row_styles.append(("BACKGROUND", (0, row_idx), (-1, row_idx), ROW_ALT))
            row_idx += 1

    tbl = Table(table_data, colWidths=col_widths, repeatRows=1)
    base_style = [
        ("BACKGROUND", (0, 0), (-1, 0), ACCENT),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("FONTNAME", (0, 1), (-1, -1), "Arial"),
        ("FONTSIZE", (0, 1), (-1, -1), 8.3),
        ("TEXTCOLOR", (0, 1), (-1, -1), DARK_TEXT),
        ("ALIGN", (-1, 0), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, 0), 0.75, ACCENT),
        ("LINEBELOW", (0, 1), (-1, -2), 0.4, BORDER),
        ("GRID", (0, 0), (-1, -1), 0.25, BORDER),
    ] + row_styles
    tbl.setStyle(TableStyle(base_style))
    story.append(tbl)

    brp_logo = Image(os.path.join(IMAGES, "brp-logo.png"))
    brp_logo._restrictSize(11 * mm, 11 * mm)
    footer_line = Table(
        [[brp_logo, Paragraph(brp_tagline, style_footer)]],
        colWidths=[13 * mm, doc.width - 13 * mm],
    )
    footer_line.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ]))
    story.append(KeepTogether([
        Spacer(1, 3 * mm),
        Paragraph(footer_note, style_footer),
        Spacer(1, 3 * mm),
        footer_line,
    ]))

    doc.build(story)
    print("Zapisano:", filename)


header_cols = ["SKU", "Model", "Wyposażenie", "Silnik", "Kolor", "Homologacja", "Cena"]

rec_sport_high = [
    ["0007XTD00", "Maverick", "DS", "Turbo RR", "Scandi Blue & Orange Crush", "INT - NRMM", "29 840"],
    ["0007KTD00", "Maverick", "X RC", "Turbo RR", "Loft Green Satin", "INT - NRMM", "41 990"],
    ["0007TTS00", "Maverick", "X RS", "Turbo RR", "Triple Black", "INT - NRMM", "39 990"],
    ["0007TTH00", "Maverick", "X RS SAS", "Turbo RR", "Dusty Navy Satin", "INT - NRMM", "42 290"],
    ["0009NT200", "Maverick MAX", "X RS SAS", "Turbo RR", "Dusty Navy Satin", "INT - NRMM", "45 990"],
    ["0007GTG00", "Maverick R", "X RC DCT SAS", "999T", "Loft Green Satin", "INT - NRMM", "63 400"],
    ["0007ATE00", "Maverick R", "X RS DCT", "999T", "Triple Black", "INT - NRMM", "54 540"],
    ["0007ATF00", "Maverick R", "X RS DCT SAS", "999T", "Dusty Navy", "INT - NRMM", "56 340"],
    ["0007DTB00", "Maverick R MAX", "X RS DCT SAS", "999T", "Dusty Navy & Legion Red", "INT - NRMM", "60 880"],
]

rec_sport_low = [
    ["0007RTA00", "Maverick Trail", "BASE T", "700", "Catalyst Gray", "T2b - 60km/h", "16 230"],
    ["0007HTD00", "Maverick Trail", "DPS T ABS", "700", "Triple Black", "T2b", "18 470"],
    ["0007FTA00", "Maverick Trail", "DPS T ABS", "1000", "Triple Black", "T2b", "21 120"],
    ["0009GTA00", "Maverick Sport", "DPS T ABS", "1000R", "Triple Black", "T2b", "21 900"],
    ["0009JTA00", "Maverick Sport MAX", "DPS T ABS", "1000R", "Triple Black", "T2b", "23 970"],
]

utility = [
    ["0006XTA00", "Traxter", "BASE T", "HD7", "Compass Green", "T1b - 60km/h", "16 990"],
    ["0006DTB00", "Traxter", "XU T", "HD7", "Compass Green", "T1b - 60km/h", "20 610"],
    ["0006WTE00", "Traxter", "BASE T", "HD9", "Compass Green", "T1b - 60km/h", "20 790"],
    ["0006NTC00", "Traxter", "XU T ABS", "HD9", "Dusty Navy Satin", "T1b", "25 290"],
    ["0006NTB00", "Traxter", "XU T ABS", "HD9", "Compass Green", "T1b", "24 210"],
    ["0007NTB00", "Traxter", "XU T ABS", "HD11", "Stealth Black", "T1b", "27 290"],
    ["0006BTA00", "Traxter MAX", "XU T ABS", "HD11", "Stealth Black", "T1b", "29 990"],
    ["0008VTA00", "Traxter PRO", "XU T ABS", "HD10", "Compass Green", "T1b", "27 490"],
    ["0008VTB00", "Traxter PRO", "XU T ABS", "HD10", "Stealth Black", "T1b", "28 310"],
    ["0008ETN00", "Traxter", "DPS", "HD9", "Compass Green", "INT - NRMM", "20 460"],
    ["0008RTM00", "Traxter MAX", "DPS", "HD9", "Compass Green", "INT - NRMM", "23 050"],
    ["0009VTC00", "Traxter 6x6", "DPS", "HD10", "Compass Green", "INT - NRMM", "25 430"],
]

sections = [
    ("REC-SPORT (64\" and up)", rec_sport_high),
    ("REC-SPORT (60\" and lower)", rec_sport_low),
    ("UTILITY", utility),
]

footer_note = "ceny Euro przeliczane na PLN wg kursu sprzedaży NBP tabela C"

col_widths_offroad = [22 * mm, 30 * mm, 28 * mm, 16 * mm, 40 * mm, 22 * mm, 20 * mm]
build_pdf("cennik-can-am-off-road.pdf", header_cols, sections, footer_note, col_widths_offroad)


# ---------------------------------------------------------------------------
# SEA-DOO
# ---------------------------------------------------------------------------

seadoo_header = ["SKU", "Model", "Silnik", "Kolor", "iBR", "Sound", "iDF", "Wyświetlacz", "Cena"]

seadoo_rec_lite = [
    ["00061TB00", "Spark 60 For 2", "60", "Sunrise Orange / Dragon Red", "X", "-", "-", "4.5\" Digital Display", "8 690"],
    ["00064TD00", "Spark 90 For 2", "90", "Dazzling Blue / Vapor Blue", "X", "-", "-", "4.5\" Digital Display", "11 600"],
    ["00067TC00", "Spark Trixx 90 For 1", "90", "Dragon Red / Bright White", "X", "-", "-", "4.5\" Digital Display", "11 690"],
    ["00067TD00", "Spark Trixx 90 For 1", "90", "Gulfstream Blue / Orange Crush", "X", "-", "-", "4.5\" Digital Display", "11 690"],
    ["00066TC00", "Spark Trixx 90 For 3", "90", "Dragon Red / Bright White", "X", "-", "-", "4.5\" Digital Display", "12 520"],
    ["00066TD00", "Spark Trixx 90 For 3", "90", "Gulfstream Blue / Orange Crush", "X", "-", "-", "4.5\" Digital Display", "12 520"],
]

seadoo_recreation = [
    ["00038TA00", "GTI Standard 130", "130", "Bright White / Neo Mint", "X", "-", "-", "4.5\" Digital Display", "14 770"],
    ["00030TG00", "GTI SE 170", "170", "Teal Blue / Manta Green", "X", "-", "X", "4.5\" Digital Display", "17 330"],
    ["00030TC00", "GTI SE 170", "170", "Laguna Green", "X", "X", "X", "4.5\" Digital Display", "18 380"],
]

seadoo_touring = [
    ["00011TC00", "GTX 170", "170", "Blue Abyss / Gulfstream Blue", "X", "-", "X", "7.6\" Digital Display", "19 210"],
    ["00012TC00", "GTX 230", "230", "Blue Abyss / Gulfstream Blue", "X", "-", "X", "7.6\" Digital Display", "21 210"],
    ["00012TB00", "GTX 230", "230", "Blue Abyss / Gulfstream Blue", "X", "X", "X", "7.6\" Color LCD Display", "22 610"],
    ["00026TB00", "GTX Limited 325", "325", "Teal Metallic", "X", "X", "X", "10.25\" Touchscreen Display", "30 490"],
    ["00026TA00", "GTX Limited 325", "325", "White Pearl Premium", "X", "X", "X", "10.25\" Touchscreen Display", "30 930"],
]

seadoo_performance = [
    ["00036TB00", "GTR 230", "230", "Eclipse Black / Reef Blue", "X", "-", "-", "4.5\" Digital Display", "18 970"],
    ["00024TC00", "GTR-X 300", "300", "Eclipse Black / Deep Marsala", "X", "-", "-", "7.6\" Digital Display", "22 990"],
    ["00023TH00", "RXP X 325", "325", "Ice Metal / Manta Green", "X", "-", "-", "7.6\" Digital Display", "26 690"],
    ["00023TB00", "RXP X 325", "325", "Gulfstream Blue Premium", "X", "X", "-", "10.25\" Touchscreen Display", "29 500"],
    ["00022TF00", "RXT X 325", "325", "Ice Metal / Manta Green", "X", "X", "-", "10.25\" Touchscreen Display", "28 980"],
    ["00022TC00", "RXT X 325", "325", "Gulfstream Blue Premium", "X", "X", "-", "10.25\" Touchscreen Display", "29 400"],
]

seadoo_adventure = [
    ["00017TB00", "Explorer Pro 170", "170", "Iceland Grey", "X", "X", "X", "10.25\" Touchscreen Display", "24 420"],
    ["00016TB00", "Explorer Pro 230", "230", "Iceland Grey", "X", "X", "X", "10.25\" Touchscreen Display", "25 740"],
]

seadoo_sport_fishing = [
    ["00018TC00", "FishPro Sport 170", "170", "White / Gulfstream Blue", "X", "-", "X", "7.6\" Digital Display", "21 700"],
]

seadoo_tow_sports = [
    ["00013TB00", "Wake Pro 230", "230", "Sand / Dazzling Blue", "X", "X", "X", "10.25\" Touchscreen Display", "24 310"],
]

seadoo_sections = [
    ("REC LITE", seadoo_rec_lite),
    ("RECREATION", seadoo_recreation),
    ("TOURING", seadoo_touring),
    ("PERFORMANCE", seadoo_performance),
    ("ADVENTURE", seadoo_adventure),
    ("SPORT FISHING", seadoo_sport_fishing),
    ("TOW SPORTS", seadoo_tow_sports),
]

col_widths_seadoo = [20 * mm, 30 * mm, 12 * mm, 38 * mm, 10 * mm, 12 * mm, 10 * mm, 32 * mm, 16 * mm]
build_pdf(
    "cennik-seadoo.pdf", seadoo_header, seadoo_sections, footer_note, col_widths_seadoo,
    brp_tagline="Autoryzowany Dealer BRP &nbsp;|&nbsp; Sea-Doo", margin_mm=14,
)


# ---------------------------------------------------------------------------
# SEA-DOO — ROCZNIK 2027
# ---------------------------------------------------------------------------

seadoo27_rec_lite = [
    ["00061VB00", "Spark 60 For 2", "60", "Sunrise Orange / Dragon Red", "X", "-", "-", "4.5\" Digital Display", "8 950"],
    ["00064VB00", "Spark Convenience 90 For 2", "90", "Dazzling Blue / Vapor Blue", "X", "-", "-", "4.5\" Digital Display", "11 770"],
    ["00068VA00", "Spark X 110 For 3 - Audio", "110", "Scandi Blue", "X", "Portable", "X", "4.5\" Digital Display", "15 490"],
    ["00069VE00", "Spark X Trixx 110 For 1", "110", "Gulfstream Blue / Orange Crush", "X", "-", "X", "4.5\" Digital Display", "13 350"],
    ["00069VB00", "Spark X Trixx 110 For 3", "110", "Scandi Blue", "X", "Portable", "X", "4.5\" Digital Display", "15 270"],
]

seadoo27_recreation = [
    ["00038VA00", "GTI Standard 130", "130", "Bright White / Neo Mint", "X", "-", "-", "4.5\" Digital Display", "15 390"],
    ["00030VH00", "GTI SE 170", "170", "Teal Blue / Manta Green", "X", "-", "X", "4.5\" Digital Display", "17 690"],
    ["00030VF00", "GTI SE 170", "170", "Laguna Green", "X", "Integrate", "X", "4.5\" Digital Display", "18 890"],
]

seadoo27_touring = [
    ["00025VD00", "GTX PRO 130 (Rental)", "130", "White / Neo Mint", "-", "-", "-", "4.5\" Digital Display", "13 790"],
    ["00025VA00", "GTX PRO 130 (Rental)", "130", "White / Neo Mint", "X", "-", "-", "4.5\" Digital Display", "15 290"],
    ["00011VC00", "GTX 170", "170", "Blue Abyss / Gulfstream Blue", "X", "Integrate", "X", "10.25\" Touchscreen Display", "21 990"],
    ["00012VC00", "GTX 230", "230", "Blue Abyss / Gulfstream Blue", "X", "Integrate", "X", "10.25\" Touchscreen Display", "24 290"],
    ["00026VB00", "GTX Limited 350", "350", "White Pearl Premium", "X", "Integrate", "X", "10.25\" Touchscreen Display", "32 990"],
    ["00026VC00", "GTX Limited 350", "350", "Mineral Blue / Liquid Titanium", "X", "Integrate", "X", "10.25\" Touchscreen Display", "32 550"],
]

seadoo27_performance = [
    ["00036VC00", "GTR 230", "230", "Eclipse Black / Icelandic Grey", "X", "-", "-", "4.5\" Digital Display", "19 620"],
    ["00024VA00", "GTR-X 300", "300", "Eclipse Black / Icelandic Grey", "X", "Integrate", "-", "10.25\" Touchscreen Display", "25 900"],
    ["00023VA00", "RXP-X 350", "350", "Gulfstream Blue Premium", "X", "-", "-", "7.6\" Digital Display", "28 890"],
    ["00023VH00", "RXP-X 350", "350", "Solar Orange", "X", "Integrate", "-", "10.25\" Touchscreen Display", "31 550"],
    ["00022VC00", "RXT-X 350", "350", "Gulfstream Blue Premium", "X", "Integrate", "-", "10.25\" Touchscreen Display", "30 990"],
    ["00022VD00", "RXT-X 350", "350", "Solar Orange / Icelandic Grey", "X", "Integrate", "-", "10.25\" Touchscreen Display", "30 990"],
    ["00020VB00", "RXP-X Senna 350", "350", "Racing Yellow / Amazon Green", "X", "Integrate", "-", "10.25\" Touchscreen Display", "37 250"],
]

seadoo27_adventure = [
    ["00016VA00", "Explorer Pro 230", "230", "Iceland Grey", "X", "Integrate", "X", "10.25\" Touchscreen Display", "26 590"],
]

seadoo27_sport_fishing = [
    ["00019VB00", "FishPro Trophy 170", "170", "Flint Grey / Orange Crush", "X", "Integrate", "X", "10.25\" Touchscreen Display", "28 260"],
]

seadoo27_tow_sports = [
    ["00035VE00", "Wake 170", "170", "Teal Blue / Grey", "X", "Integrate", "X", "4.5\" Digital Display", "19 990"],
    ["00013VC00", "Wake PRO 230", "230", "Teal Blue / Manta Green", "X", "Integrate", "X", "10.25\" Touchscreen Display", "24 990"],
]

seadoo27_sections = [
    ("REC LITE", seadoo27_rec_lite),
    ("RECREATION", seadoo27_recreation),
    ("TOURING", seadoo27_touring),
    ("PERFORMANCE", seadoo27_performance),
    ("ADVENTURE", seadoo27_adventure),
    ("SPORT FISHING", seadoo27_sport_fishing),
    ("TOW SPORTS", seadoo27_tow_sports),
]

build_pdf(
    "cennik-seadoo-2027.pdf", seadoo_header, seadoo27_sections, footer_note, col_widths_seadoo,
    brp_tagline="Autoryzowany Dealer BRP &nbsp;|&nbsp; Sea-Doo &nbsp;&middot;&nbsp; Rocznik 2027", margin_mm=14,
)


# ---------------------------------------------------------------------------
# ATV (Outlander / Renegade)
# ---------------------------------------------------------------------------

atv_header = ["SKU", "Model", "Wyposażenie", "Silnik", "Kolor", "Homologacja", "10.25\" T", "Cena"]

atv_mid_hp = [
    ["0001HTG00", "Outlander PRO", "STD T", "HD5", "Desert Tan", "T3b - 60km/h", "", "10 990"],
    ["0001BTC00", "Outlander", "DPS T ABS", "500", "Granite Grey", "T3b", "", "11 990"],
    ["0001LTA00", "Outlander PRO", "XU T", "HD5", "Compass Green", "T3b - 60km/h", "", "12 960"],
    ["0001VTG00", "Outlander MAX", "DPS T ABS", "500", "Granite Grey", "T3b", "", "12 990"],
    ["0001ETK00", "Outlander", "DPS T ABS", "700", "Granite Grey", "T3b", "", "12 990"],
    ["0001MTA00", "Outlander PRO", "XU T", "HD7", "Compass Green", "T3b - 60km/h", "", "13 570"],
    ["0001MTD00", "Outlander PRO", "XU T ABS", "HD7", "Compass Green", "T3b", "", "13 990"],
    ["0001WTL00", "Outlander MAX", "DPS T ABS", "700", "Granite Grey", "T3b", "", "13 990"],
    ["0002BTA00", "Outlander MAX PRO", "XU T", "HD7", "Compass Green", "T3a - 40km/h", "", "14 370"],
    ["0001YTE00", "Outlander MAX", "XT T ABS", "700", "Granite Grey", "T3b", "", "15 660"],
    ["0002BTB00", "Outlander MAX PRO", "XU T", "HD7", "Platinum Satin", "T3b - 60km/h", "", "14 590"],
    ["0001HTD00", "Outlander PRO", "STD", "HD5", "Desert Tan", "INT - NRMM", "", "10 890"],
    ["0001STD00", "Outlander", "X MR", "700", "Granite Grey", "INT - NRMM", "", "15 020"],
    ["0001WTH00", "Outlander MAX", "DPS", "700", "Granite Grey", "INT - NRMM", "", "13 370"],
    ["0001YTD00", "Outlander MAX", "XT", "700", "Platinum Satin", "INT - NRMM", "", "15 020"],
]

atv_high_hp = [
    ["0004HTA00", "Outlander", "XT-P", "1000R", "Mineral Grey & Orange Crush", "INT - NRMM", "", "20 750"],
    ["0004HTM00", "Outlander", "XT-P SAS", "1000R", "Mineral Grey & Orange Crush", "INT - NRMM", "X", "23 430"],
    ["0004LTC00", "Outlander", "X MR", "1000R", "Loft Green Satin", "INT - NRMM", "", "21 470"],
    ["0004RTB00", "Outlander MAX", "DPS", "1000R", "Granite Grey", "INT - NRMM", "", "17 880"],
    ["0004STF00", "Outlander MAX", "XT", "850", "Fiery Red", "INT - NRMM", "", "17 570"],
    ["0004VTC00", "Outlander MAX", "XT-P", "1000R", "Mineral Grey & Orange Crush", "INT - NRMM", "", "21 720"],
    ["0004VTP00", "Outlander MAX", "XT-P SAS", "1000R", "Mineral Grey & Orange Crush", "INT - NRMM", "X", "24 210"],
    ["0004WTJ00", "Outlander MAX", "LTD SAS", "1000R", "Dusty Navy Satin", "INT - NRMM", "X", "24 670"],
    ["0004ETH00", "Outlander", "XT T ABS", "850", "Fiery Red", "T3b", "", "16 950"],
    ["0004HTC00", "Outlander", "XT-P T ABS", "1000R", "Mineral Grey & Orange Crush", "T3b", "", "21 410"],
    ["0004HTL00", "Outlander", "XT-P T ABS SAS", "1000R", "Mineral Grey & Orange Crush", "T3b", "X", "23 990"],
    ["0004PTC00", "Outlander MAX", "DPS T ABS", "850", "Granite Grey", "T3b", "", "16 830"],
    ["0004RTA00", "Outlander MAX", "DPS T ABS", "1000R", "Granite Grey", "T3b", "", "18 250"],
    ["0004RTC00", "Outlander MAX", "DPS T ABS", "1000R", "Legion Red", "T3b", "", "18 250"],
    ["0004YTA00", "Outlander MAX PRO", "XU T", "HD8", "Granite Grey", "T3b - 60km/h", "", "17 680"],
    ["0004YTB00", "Outlander MAX PRO", "XU T", "HD8", "Desert Tan", "T3b - 60km/h", "", "17 680"],
    ["0004XTA00", "Outlander MAX PRO", "XU T", "HD10", "Platinum Silver Satin", "T3b - 60km/h", "", "19 900"],
    ["0004STD00", "Outlander MAX", "XT T ABS", "850", "Fiery Red", "T3b", "", "17 990"],
    ["0004VTB00", "Outlander MAX", "XT-P T ABS", "1000R", "Mineral Grey & Orange Crush", "T3b", "", "22 450"],
    ["0004VTN00", "Outlander MAX", "XT-P T ABS SAS", "1000R", "Mineral Grey & Orange Crush", "T3b", "X", "24 990"],
    ["0004WTK00", "Outlander MAX", "LTD T ABS SAS", "1000R", "Dusty Navy Satin", "T3b", "X", "24 990"],
]

atv_rec_sport = [
    ["0005RTA00", "Renegade", "X XC T ABS", "650", "Catalyst Gray & Orange Crush", "T3b", "", "16 310"],
    ["0005MTA00", "Renegade", "X XC T ABS", "1000R", "Catalyst Gray & Orange Crush", "T3b", "", "19 990"],
    ["0005VTA00", "Renegade", "X XC", "1000R", "Catalyst Gray & Orange Crush", "INT - NRMM", "", "19 590"],
    ["0005UTC00", "Renegade", "X MR", "1000R", "Hyper Silver & Legion Red", "INT - NRMM", "", "21 300"],
]

atv_6x6 = [
    ["0002ETD00", "Outlander 6X6", "DPS T", "700", "Granite Grey", "T3b - 60km/h", "", "17 600"],
    ["0002GTA00", "Outlander 6X6", "DPS T", "850", "Granite Grey", "T3b - 60km/h", "", "19 080"],
    ["0002HTC00", "Outlander MAX 6X6", "DPS T", "850", "Granite Grey", "T3b - 60km/h", "", "19 990"],
    ["0002JTA00", "Outlander 6X6", "BACKCOUNTRY T", "1000R", "Stealth Black", "T3b - 60km/h", "", "22 600"],
    ["0002KTB00", "Outlander MAX 6X6", "BACKCOUNTRY T", "1000R", "Stealth Black", "T3b - 60km/h", "", "23 850"],
]

atv_sections = [
    ("REC-UTE MID-HP", atv_mid_hp),
    ("REC-UTE HIGH-HP", atv_high_hp),
    ("REC-SPORT", atv_rec_sport),
    ("6x6", atv_6x6),
]

col_widths_atv = [20 * mm, 32 * mm, 26 * mm, 14 * mm, 34 * mm, 22 * mm, 12 * mm, 16 * mm]
build_pdf(
    "cennik-can-am-atv.pdf", atv_header, atv_sections, footer_note, col_widths_atv,
    brp_tagline="Autoryzowany Dealer BRP &nbsp;|&nbsp; Can-Am ATV",
)


# ---------------------------------------------------------------------------
# CAN-AM — TRÓJKOŁOWCE (3-wheel)
# ---------------------------------------------------------------------------

trike_header = ["SKU", "Model", "Pakiet wyposażenia", "Skrzynia biegów", "Kolor", "Homologacja", "Cena"]

trike_cruising = [
    ["000E6TJ00", "F3", "S", "1330 ACE SE6", "Monolith Black Metallic Satin", "EU", "25 350"],
    ["000E6TE00", "F3", "S", "1330 ACE SE6", "Circuit Yellow Metallic", "EU", "25 350"],
    ["000H9TC00", "F3", "LTD", "1330 ACE SE6", "Vegas White Pearl", "EU", "31 600"],
    ["000H7TD00", "F3", "LTD Special Series", "1330 ACE SE6", "Mars Red Metallic", "EU", "34 050"],
]

trike_touring = [
    ["000B9TF00", "RT", "LTD", "1330 ACE SE6", "Vegas White Pearl", "EU", "34 800"],
    ["000G1TC00", "RT", "LTD", "1330 ACE SE6", "Carbon Black", "EU", "34 800"],
    ["000G1TB00", "RT", "LTD", "1330 ACE SE6", "Mineral Blue", "EU", "34 800"],
    ["000G2TD00", "RT", "Sea-to-Sky", "1330 ACE SE6", "Mars Red Metallic", "EU", "37 000"],
]

trike_adventure = [
    ["000J1TB00", "CANYON", "STD", "1330 ACE SE6", "Sterling Silver", "EU", "28 240"],
    ["000J2TB00", "CANYON", "XT", "1330 ACE SE6", "Sterling Silver", "EU", "33 030"],
    ["000J3TB00", "CANYON", "Redrock", "1330 ACE SE6", "Moss Green", "EU", "35 220"],
]

trike_recreation = [
    ["000F1TB00", "RYKER", "STD", "600 ACE CVT", "-", "EU", "12 230"],
    ["000F2TB00", "RYKER", "STD", "900 ACE CVT", "-", "EU", "13 300"],
    ["000F5TB00", "RYKER", "Sport", "900 ACE CVT", "-", "EU", "15 200"],
    ["000F3TB00", "RYKER", "Rally", "900 ACE CVT", "-", "EU", "17 160"],
]

trike_sections = [
    ("CRUISING", trike_cruising),
    ("TOURING", trike_touring),
    ("ADVENTURE", trike_adventure),
    ("RECREATION", trike_recreation),
]

col_widths_trike = [24 * mm, 20 * mm, 34 * mm, 26 * mm, 40 * mm, 18 * mm, 18 * mm]
build_pdf(
    "cennik-can-am-trojkolowce.pdf", trike_header, trike_sections, footer_note, col_widths_trike,
    brp_tagline="Autoryzowany Dealer BRP &nbsp;|&nbsp; Can-Am On-Road",
)


# ---------------------------------------------------------------------------
# CAN-AM — ELEKTRYCZNE (Origin, Pulse, Outlander Electric)
# ---------------------------------------------------------------------------

electric_header = ["SKU", "Model", "Wersja", "Zasięg (km)", "Kolor", "Cena"]

electric_motorcycles = [
    ["000P1TA00", "Origin", "Rally Edition", "≈145", "Bright White", "17 499"],
    ["000P1TB00", "Origin", "Rally Edition", "≈145", "Sterling Silver ('73)", "17 499"],
    ["000P3TA00", "Pulse", "Sport Edition", "≈160", "Bright White", "16 899"],
    ["000P3TB00", "Pulse", "Sport Edition", "≈160", "Sterling Silver ('73)", "16 899"],
]

electric_atv = [
    ["0002WTC00", "Outlander", "Electric", "≈80", "Granite Grey", "18 990"],
    ["0002WTD00", "Outlander", "Electric", "≈80", "Bright White", "18 990"],
    ["0002VTA00", "Outlander MAX", "Electric", "≈80", "Bright White", "20 560"],
    ["0002VTB00", "Outlander MAX", "Electric", "≈80", "Granite Grey", "20 790"],
]

electric_sections = [
    ("MOTOCYKLE ELEKTRYCZNE", electric_motorcycles),
    ("QUADY ELEKTRYCZNE", electric_atv),
]

electric_footer_note = footer_note + " &middot; zasięg zależny od stylu jazdy i warunków terenowych"

col_widths_electric = [26 * mm, 32 * mm, 30 * mm, 24 * mm, 44 * mm, 20 * mm]
build_pdf(
    "cennik-can-am-elektryczne.pdf", electric_header, electric_sections, electric_footer_note, col_widths_electric,
    brp_tagline="Autoryzowany Dealer BRP &nbsp;|&nbsp; Can-Am Electric",
)
