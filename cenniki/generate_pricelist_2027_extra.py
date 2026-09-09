# -*- coding: utf-8 -*-
# Cenniki PDF dla rocznika 2027: ATV, SSV (off-road) i trojkolowce.
# Dane cenowe pochodza z cennika detalicznego importera Taurus Sea Power sp. z o.o.,
# opublikowanego przez autoryzowanego dealera BRP perfectmoto.pl (ceny brutto EUR).
# SKU niedostepne z tego zrodla - kolumna zostaje pusta ("-") zamiast zmyslania kodow.

from reportlab.lib.units import mm
from generate_pricelist import build_pdf, footer_note

header_no_sku = ["Model", "Wersja / pakiet", "Silnik", "Kolor", "Cena"]

# ---------------------------------------------------------------------------
# CAN-AM ATV -- ROCZNIK 2027 (45 wersji)
# ---------------------------------------------------------------------------

atv27_youth = [
    ["Renegade X XC", "110 EFI", "110", "Orange Crush", "5 990"],
]

atv27_electric = [
    ["Outlander Electric", "T", "Electric", "Bright White", "18 990"],
    ["Outlander MAX Electric", "T", "Electric", "Bright White", "20 990"],
]

atv27_pro = [
    ["Outlander PRO", "HD5 T", "HD5", "Sandstone", "9 990"],
    ["Outlander PRO", "XU HD5 T", "HD5", "Sandstone", "11 990"],
    ["Outlander PRO", "XU HD7 T", "HD7", "Sandstone", "13 790"],
    ["Outlander PRO", "XU HD7 T ABS", "HD7", "Sandstone", "14 390"],
    ["Outlander MAX PRO", "XU HD7 T", "HD7", "Sandstone", "14 540"],
    ["Outlander MAX PRO", "XU HD10 T", "HD10", "Granite Grey", "17 990"],
    ["Outlander MAX PRO", "XU HD11 T", "HD11", "Dolomite Grey", "19 990"],
]

atv27_500_700 = [
    ["Outlander", "DPS 500 T ABS", "500", "Granite Grey", "11 790"],
    ["Outlander MAX", "DPS 500 T ABS", "500", "Granite Grey", "11 990"],
    ["Outlander MAX", "DPS 700 T ABS", "700", "Granite Grey", "13 890"],
    ["Outlander MAX", "XT 700 T ABS", "700", "Dolomite Grey", "15 890"],
    ["Outlander MAX", "DPS 700", "700", "Granite Grey", "11 990"],
    ["Outlander MAX", "XT 700", "700", "Dolomite Grey", "15 290"],
    ["Outlander", "X MR 700", "700", "Granite Grey", "15 290"],
]

atv27_1000 = [
    ["Outlander MAX", "DPS 1000R", "1000R", "Granite Grey", "17 990"],
    ["Outlander MAX", "XT 1000", "1000", "Fiery Red Metallic", "18 990"],
    ["Outlander", "XT-P 1000R", "1000R", "Dusty Navy & Orange Crush", "20 990"],
    ["Outlander MAX", "XT-P 1000R SAS", "1000R", "Dusty Navy & Orange Crush", "24 290"],
    ["Outlander MAX", "LTD 1000R T ABS SAS", "1000R", "Stealth Black", "24 990"],
    ["Outlander", "X MR 1000R", "1000R", "Loft Green Satin", "21 630"],
    ["Outlander MAX", "X MR 1000R", "1000R", "Loft Green Satin", "22 290"],
    ["Outlander MAX", "DPS 1000 T ABS", "1000", "Granite Grey", "16 490"],
    ["Outlander MAX", "DPS 1000R T ABS", "1000R", "Granite Grey", "18 490"],
    ["Outlander", "XT 1000 T ABS", "1000", "Fiery Red Metallic", "18 490"],
    ["Outlander MAX", "XT 1000 T ABS", "1000", "Fiery Red Metallic", "19 490"],
    ["Outlander", "XT-P 1000R T ABS", "1000R", "Dusty Navy & Orange Crush", "21 410"],
    ["Outlander", "XT-P 1000R T ABS SAS", "1000R", "Dusty Navy & Orange Crush", "23 990"],
    ["Outlander MAX", "XT-P 1000R T ABS", "1000R", "Dusty Navy & Orange Crush", "22 450"],
    ["Outlander MAX", "XT-P 1000R T ABS SAS", "1000R", "Dusty Navy & Orange Crush", "24 990"],
    ["Outlander MAX", "BACKCOUNTRY 1000R T", "1000R", "Multicam Dark Camo", "23 190"],
    ["Outlander MAX", "LTD 1000R T ABS SAS", "1000R", "Stealth Black", "24 990"],
    ["Outlander MAX", "BACKCOUNTRY 1000R", "1000R", "Multicam Dark Camo", "21 920"],
]

atv27_renegade = [
    ["Renegade", "X XC T ABS 650", "650", "Catalyst Gray & Orange Crush", "16 310"],
    ["Renegade", "X XC T ABS 1000R", "1000R", "Catalyst Gray & Orange Crush", "19 990"],
    ["Renegade", "X XC 1000R", "1000R", "Catalyst Gray & Orange Crush", "19 590"],
    ["Renegade", "X MR 1000R", "1000R", "Hyper Silver & Legion Red", "21 300"],
]

atv27_6x6 = [
    ["Outlander 6x6", "DPS 700 T", "700", "Granite Grey", "17 600"],
    ["Outlander MAX 6x6", "DPS 700 T", "700", "Granite Grey", "18 780"],
    ["Outlander 6x6", "DPS 1000 T", "1000", "Granite Grey", "19 390"],
    ["Outlander MAX 6x6", "DPS 1000 T", "1000", "Granite Grey", "20 990"],
    ["Outlander 6x6", "BACKCOUNTRY 1000R T", "1000R", "Stealth Black", "22 990"],
    ["Outlander MAX 6x6", "BACKCOUNTRY 1000R T", "1000R", "Stealth Black", "24 230"],
]

atv27_sections = [
    ("YOUTH", atv27_youth),
    ("ELECTRIC", atv27_electric),
    ("PRO", atv27_pro),
    ("500-700", atv27_500_700),
    ("1000 / 1000R", atv27_1000),
    ("RENEGADE", atv27_renegade),
    ("6x6", atv27_6x6),
]

col_widths_atv27 = [40 * mm, 42 * mm, 18 * mm, 46 * mm, 20 * mm]
build_pdf(
    "cennik-can-am-atv-2027.pdf", header_no_sku, atv27_sections, footer_note, col_widths_atv27,
    brp_tagline="Autoryzowany Dealer BRP &nbsp;|&nbsp; Can-Am ATV &nbsp;&middot;&nbsp; Rocznik 2027",
)


# ---------------------------------------------------------------------------
# CAN-AM SSV (OFF-ROAD) -- ROCZNIK 2027 (27 wersji)
# ---------------------------------------------------------------------------

ssv27_maverick_r = [
    ["Maverick R", "X RC DCT SAS", "999T", "Loft Green Satin", "60 990"],
    ["Maverick R", "X RS DCT", "999T", "Triple Black", "53 990"],
    ["Maverick R", "X RS DCT SAS", "999T", "Dolomite Grey & Orange Crush", "55 990"],
    ["Maverick R MAX", "X RS DCT SAS", "999T", "Dolomite Grey & Orange Crush", "58 830"],
]

ssv27_maverick = [
    ["Maverick", "DS", "Turbo RR", "Granite Grey", "29 990"],
    ["Maverick", "X DS", "Turbo RR", "Triple Black", "38 590"],
    ["Maverick", "X RC", "Turbo RR", "Loft Green Satin", "42 790"],
    ["Maverick", "X RS", "Turbo RR", "Triple Black", "40 890"],
    ["Maverick", "X RS SAS", "Turbo RR", "Dolomite Grey", "42 990"],
    ["Maverick MAX", "X RS SAS", "Turbo RR", "Dolomite Grey", "45 990"],
]

ssv27_maverick_trail = [
    ["Maverick Trail", "BASE T", "650", "Catalyst Gray", "16 590"],
    ["Maverick Trail", "DPS T ABS", "650", "Granite Grey", "18 590"],
    ["Maverick Trail", "DPS T ABS", "976 V-twin", "Granite Grey", "20 790"],
]

ssv27_maverick_sport = [
    ["Maverick Sport", "DPS T ABS", "1000R V-twin", "Granite Grey", "22 790"],
    ["Maverick Sport MAX", "DPS T ABS", "1000R V-twin", "Granite Grey", "24 890"],
]

ssv27_traxter = [
    ["Traxter", "BASE T", "1-cyl.", "Compass Green", "16 990"],
    ["Traxter", "XU T", "1-cyl.", "Compass Green", "20 890"],
    ["Traxter", "XU T ABS", "999 (G2)", "Compass Green", "24 990"],
    ["Traxter", "XU T ABS", "999 (G2)", "Stealth Black", "26 390"],
    ["Traxter", "XU T ABS", "999 (G2), 95 KM", "Stealth Black", "29 490"],
    ["Traxter MAX", "XU T ABS", "999 (G2, HD11)", "Stealth Black", "32 190"],
    ["Traxter PRO", "XU T ABS", "999 (G2)", "Compass Green", "27 990"],
    ["Traxter", "DPS", "V-twin", "Compass Green", "21 990"],
    ["Traxter MAX", "DPS", "V-twin", "Compass Green", "24 760"],
    ["Traxter", "X MR", "999 (G2)", "Loft Green Satin", "29 890"],
    ["Traxter 6x6", "DPS", "V-twin", "Compass Green", "26 340"],
    ["Traxter 6x6", "XU T", "999 (G2)", "Compass Green", "27 990"],
]

ssv27_sections = [
    ("MAVERICK R", ssv27_maverick_r),
    ("MAVERICK", ssv27_maverick),
    ("MAVERICK TRAIL", ssv27_maverick_trail),
    ("MAVERICK SPORT", ssv27_maverick_sport),
    ("TRAXTER", ssv27_traxter),
]

col_widths_ssv27 = [34 * mm, 38 * mm, 26 * mm, 46 * mm, 20 * mm]
build_pdf(
    "cennik-can-am-off-road-2027.pdf", header_no_sku, ssv27_sections, footer_note, col_widths_ssv27,
    brp_tagline="Autoryzowany Dealer BRP &nbsp;|&nbsp; Can-Am SSV &nbsp;&middot;&nbsp; Rocznik 2027",
)


# ---------------------------------------------------------------------------
# CAN-AM -- TROJKOLOWCE -- ROCZNIK 2027 (15 wersji)
# ---------------------------------------------------------------------------

trike27_ryker = [
    ["Ryker", "600", "900 ACE, 52 KM", "Deep Black", "12 530"],
    ["Ryker", "900", "900 ACE, 79 KM", "Deep Black", "13 580"],
    ["Ryker Sport", "-", "900 ACE, 80 KM", "Deep Black", "15 590"],
    ["Ryker Rally", "-", "900 ACE, 80 KM", "Deep Black", "17 550"],
]

trike27_f3 = [
    ["Spyder F3-S", "-", "1330 ACE SE6", "Monolith Black Satin", "25 720"],
    ["Spyder F3-S", "-", "1330 ACE SE6", "Circuit Yellow Metallic", "25 720"],
    ["Spyder F3 Limited", "-", "1330 ACE SE6", "Mineral Blue", "32 290"],
    ["Spyder F3 Limited Special Series", "-", "1330 ACE SE6", "Dolomite Grey", "34 590"],
]

trike27_rt = [
    ["Spyder RT Limited", "-", "1330 ACE SE6", "Mineral Blue", "34 990"],
    ["Spyder RT Limited", "-", "1330 ACE SE6", "Vegas White Pearl", "35 290"],
    ["Spyder RT Limited", "-", "1330 ACE SE6", "Carbon Black", "35 290"],
    ["Spyder RT Sea-to-Sky", "-", "1330 ACE SE6", "Dolomite Grey", "37 990"],
]

trike27_canyon = [
    ["Canyon", "-", "1330 ACE SE6", "Sterling Silver Satin", "28 240"],
    ["Canyon XT", "-", "1330 ACE SE6", "Sterling Silver Satin", "33 030"],
    ["Canyon Redrock", "-", "1330 ACE SE6", "Sandstone", "32 990"],
]

trike27_sections = [
    ("RYKER", trike27_ryker),
    ("SPYDER F3", trike27_f3),
    ("SPYDER RT", trike27_rt),
    ("CANYON", trike27_canyon),
]

col_widths_trike27 = [50 * mm, 30 * mm, 24 * mm, 44 * mm, 18 * mm]
build_pdf(
    "cennik-can-am-trojkolowce-2027.pdf", header_no_sku, trike27_sections, footer_note, col_widths_trike27,
    brp_tagline="Autoryzowany Dealer BRP &nbsp;|&nbsp; Can-Am On-Road &nbsp;&middot;&nbsp; Rocznik 2027",
)
