# Pytania do dystrybutora BRP Polska — status po samodzielnym researchu

Cel: zamknięcie ostatnich pozycji w katalogu extreme-club.pl bez dalszego angażowania dystrybutora
BRP Polska. Pełne uzasadnienie kolorów w pliku `weryfikacja-kolorow-99-pojazdow.md`.

**Aktualizacja 2026-09-09:** dystrybutor odpisał (poirytowany), że nie chce być pytany o rzeczy
możliwe do sprawdzenia samodzielnie na oficjalnych stronach BRP/Sea-Doo/Can-Am lub u innych
dealerów. W tej turze przeprowadzono szeroki research (oficjalne strony can-am.brp.com, brp-world.com,
oraz polscy dealerzy BRP: brpbroker.pl, fanjet.pl/sklep.fanjet.pl) i zamknięto samodzielnie **4 z 5**
pierwotnych punktów z `wiadomosc-do-dystrybutora.md`. Zostaje **0 punktów wymagających koniecznie
dystrybutora** do dalszego działania strony — patrz szczegóły niżej.

---

## ✅ 1. Cennik PLN/EUR — ROZWIĄZANE dla linii On-Road 2027 (Ryker/Spyder/Canyon)

**Przełomowe znalezisko:** PerfectMoto.pl (Brzozowski sp. k., autoryzowany dealer BRP) publikuje
komplet 15 wersji linii On-Road 2027 z cenami EUR brutto, a w stopce strony wprost podaje źródło:
*"Ceny pochodzą z cennika detalicznego importera (**Taurus Sea Power sp. z o.o.**) na rocznik 2027"*
— to POTWIERDZA, że Taurus Sea Power jest faktycznym importerem/dystrybutorem BRP w Polsce (i
prawdopodobnie to o nią chodziło dystrybutorowi, myląc nazwę z "Tauris" — niepowiązaną marką części).

Na tej podstawie **zaktualizowano 8 cen** pojazdów z rocznikiem 2027, które wcześniej miały
"Cena na zapytanie" (jednoznaczne dopasowanie model-kolor, bez zgadywania):
- `canam-ryker-2027` → od 12 530 €
- `canam-ryker-sport-2027` → od 15 590 €
- `canam-f3-s-2027` → od 25 720 €
- `canam-f3-limited-2027` → od 32 290 €
- `canam-rt-2027` → od 34 990 € (Mineral Blue), kolory Pearl White/Carbon Black → od 35 290 €
- `canam-rt-sea-to-sky-2027` → od 37 990 €
- `canam-canyon-2027` → od 28 240 €
- `canam-canyon-redrock-2027` → od 32 990 €

**Nie zmienione** (brak jednoznacznego dopasowania w liście 15 wersji PerfectMoto — celowo nie
zgadywano): `canam-ryker-special` (Ryker Special Series — nie ma go w tej liście 4 wersji Rykera),
`canam-f3-t`, `canam-f3-2027` (plain F3 — lista ma tylko F3-S i F3 Limited, nie osobne F3/F3-T).

Katalog dla pozostałych 91 pojazdów (2026 i starsze 2027) nadal wycenia w **EUR** zgodnie z
dotychczasową praktyką — to zgodne z rynkiem (polscy dealerzy BRP też podają EUR, przeliczane po
kursie NBP na fakturze).

**Nie wymaga już dystrybutora** dla tej linii produktowej.

---

## ✅ 2. Can-Am Origin — wariant Carbon Black — ROZWIĄZANE

Na oficjalnej stronie can-am.brp.com (US, model year 2026) znaleziono prawidłowy, oficjalny plik
studyjny Origin w Carbon Black pod adresem zawierającym poprawny kod wariantu `000J8TM00` (a nie
`000J7TM00`/"pulse-carbon-black" widziany wcześniej na brp-world.com, który faktycznie był błędnie
podpiętym zdjęciem Pulse). Zdjęcie pobrane, zweryfikowane wizualnie — to jednoznacznie **Origin**
(charakterystyczny dual-sport, szprychowe koła terenowe, plakietka "ROTAX" i "can-am" na baku), NIE
Pulse. Zapisane jako `images/canam-origin-2027-carbonblack-1.png` i dodane jako trzeci wariant
kolorystyczny do wpisu `canam-origin` w `index.html` (obok Bright White i Sterling Silver '73).
Sprawdzone parsowanie VEHICLES po edycji: 99/99, poprawne.

---

## ✅ 3. Ryker Special Series 2027 — unikalne zdjęcie — JUŻ ROZWIĄZANE (potwierdzone w tej turze)

Sprawdzono aktualny plik `images/canam-ryker-special-1.png` użyty we wpisie `canam-ryker-special`
— to już jest prawidłowe, unikalne zdjęcie Ryker Special Series MY27 (charakterystyczne złote/
"Liquid Titanium" felgi i akcenty na baku, zgodne z oficjalnym komunikatem prasowym BRP z
prnewswire.com sierpień 2026). Zweryfikowano przez porównanie z oficjalnym plikiem z can-am.brp.com
(`ONRD-MY27-3W-RYKER-Special-Series-900-ACE-9-Deep-Black-000F6VD00...`) — to ten sam pojazd/wariant,
tylko inny wariant tła. Wygląda na to, że to zostało już naprawione w poprzedniej sesji, a
`wiadomosc-do-dystrybutora.md` nie został zaktualizowany. **Nie wymaga żadnej dalszej akcji.**

---

## ✅ 4/5. Spyder F3 LTD — kolory — POTWIERDZONE KOMPLETNE

WebSearch po dealerach US (psutica.com, hicklinofames.com, headmotorco.com) i materiałach Can-Am
potwierdza: pełna oferta kolorystyczna **regularnego** F3 Limited MY27 to dokładnie **trzy** kolory —
czyli dokładnie te trzy, które już są w katalogu (`canam-f3-ltd`/`canam-f3-limited-2027`). Nazwa
pierwszego koloru: **potwierdzona jako "Vegas White Pearl"** (URL slug wprost na can-am.brp.com to
"vegas-white-pearl", zgodnie też z 4 niezależnymi polskimi ogłoszeniami/sklepami — Quadziorek.pl,
sprzedajemy.pl, otomoto.pl). Jedna z tur researchu błędnie zmieniła to na "Pearl White (Platinum)" —
poprawiono z powrotem na oficjalną nazwę. Istnieje dodatkowo
czwarty wariant "Dolomite Grey z metalicznymi złotymi drobinkami", ale to osobna, droższa edycja
**F3 Limited Special Series** (nie zwykły F3 Limited) — nie ma potrzeby dodawania go jako "koloru"
zwykłego F3 Limited, chyba że klient chce w przyszłości dodać ją jako osobny wpis w katalogu.
**Oferta kolorystyczna F3 LTD w katalogu jest kompletna, nie wymaga dystrybutora.**

---

## ✅ Drugie zdjęcie galerii Spyder F3 Limited — ROZWIĄZANE (2026-09-09, kolejna tura)

Znaleziono i zweryfikowano wizualnie prawdziwe zdjęcie prasowe F3 Limited w bieli/perłowym (z
oficjalnej galerii MY27 motorcycle.com, sierpień 2026) — studyjne zdjęcie 3/4 przód, z kuframi i
oparciem pasażera, zgodne stylistycznie z resztą katalogu. Pobrane i zapisane jako
`images/canam-f3-ltd-2027-gallery-2.jpg`, dodane jako drugi element `gallery` we wpisie
`canam-f3-limited-2027`. Parsowanie VEHICLES zweryfikowane: 99/99 poprawne.

## ⏳ Drugie zdjęcie galerii Spyder RT (biały/perłowy) — NADAL OTWARTE

**Jedyny punkt, którego nie udało się zamknąć.** W poprzedniej turze (2026-09-10) wykonano już ~8
różnych zapytań i sprawdzono kilkanaście dealerów US (Autotrader, Cycle Trader, MotoHunt, Craigslist,
dealerzy DX1: Hicklin Powersports, Rice's Rapid Motorsports, Leaders RPM, Factory Powersports,
Jackson Motorsports, Metro Motorsports) — jedyne dostępne zdjęcia Pearl White/Vegas White Pearl to
generyczna grafika katalogowa producenta na białym tle (nie prawdziwe zdjęcie z placu/hali, więc nie
pasuje stylistycznie do istniejącego zdjęcia "z życia"). W tej turze dodatkowo sprawdzono dealerów
polskich (brpbroker.pl, fanjet.pl) — **żaden nie prowadzi w ofercie modeli Spyder F3/RT** (skupiają
się na ATV/SSV/skuterach wodnych), więc nie mają własnych zdjęć.

**To jedyny punkt, przy którym realnie wyczerpano samodzielne możliwości researchu** — potrzebne jest
zdjęcie z rzeczywistego materiału marketingowego/systemu zdjęć dealerskich BRP (nie generyczna
grafika katalogowa), którego nie da się pozyskać przez publiczny web search. Jeśli dystrybutor nie
ma takiego zdjęcia pod ręką, sugerowane rozwiązanie: zostawić po 1 zdjęciu dla tych dwóch modeli
(nie jest to błąd merytoryczny — inne pojazdy z 2 zdjęciami mają je bo takie zdjęcia istniały; tu po
prostu nie istnieją publicznie dostępne dobrej jakości).

## ⏳ 5 pojazdów bez ŻADNEGO zdjęcia galerii (dodatkowego, poza głównym) — NOWE, 2026-09-10

Wyczerpujący research (kilkanaście zapytań, dealerzy US/PL, oficjalne strony BRP, komunikaty
prasowe) nie znalazł ANI JEDNEGO prawdziwego zdjęcia "z życia" (nie katalogowego) w odpowiednim
kolorze dla żadnego z tych 5 pojazdów:

1. **Outlander PRO (2027)** — kolory Desert Tan / Compass Green. Dostępne w sieci zdjęcia to inny
   kolor (Tundra Green, MY23) albo zwykłe zdjęcia katalogowe.
2. **Renegade (2027)** — kolory Catalyst Gray & Orange Crush / Hyper Silver & Legion Red. Wyniki
   wyszukiwania zdominowane przez model dziecięcy "Renegade 110" (inny pojazd) — dla wersji
   dorosłej 1000R tylko powielane zdjęcia katalogowe.
3. **Maverick Trail (2027)** — kolor Granite Grey. Jedyne znalezione zdjęcia w tym kolorze to
   wariant stylistyczny "Trail X" (inny pakiet niż nasza karta) — odrzucone jako niepasujące.
4. **Traxter HD10 (`canam-traxter-hd9`, 2027)** — kolor Dolomite Grey, nowa platforma XU. Stare
   pliki na dysku (`canam-traxter-hd9-life-1/2.jpg`) pokazują zielony pojazd (Compass Green) — już
   wcześniej świadomie odrzucone, ponownie potwierdzone jako niezgodne.
5. **Commander XT (2027)** — kolor Dolomite Grey. Dealerzy mają wyłącznie karty produktowe/studyjne.

**Pytanie:** Macie w materiałach marketingowych/systemie zdjęć dealerskich BRP prawdziwe zdjęcia
"z życia" (nie studyjne, białe tło) dla któregokolwiek z tych 5 pojazdów w podanych wyżej kolorach?
Wystarczy nawet 1 zdjęcie na pojazd — obecnie żaden z nich nie ma ANI JEDNEGO dodatkowego zdjęcia
w galerii, tylko zdjęcie główne.

---

## Jak odpowiedzieć (jeśli w ogóle potrzebne)

Poza punktem powyżej, nic więcej nie jest wymagane pilnie. Dodatkowo, opcjonalnie: **"Macie
dodatkowe, prawdziwe zdjęcie (nie katalogowe) Spyder F3 Limited lub Spyder RT w białym/perłowym
kolorze — inny kąt/scena niż to, które już mamy?"**
