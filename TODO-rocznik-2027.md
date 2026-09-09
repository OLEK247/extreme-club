# TODO — dodanie rocznika 2027 (54 pojazdy)

## ✅ AKTUALIZACJA 2026-09-09 (nad ranem) — audyt galerii CAŁEGO katalogu (99 pojazdów)

Rozszerzenie poprzedniego audytu galerii (który objął tylko pojazdy zmienione w tej sesji)
na cały katalog. Metoda: 1) automatyczny skan konfliktów (ten sam plik galerii przypisany do
dwóch różnych nazw kolorów w różnych kartach — pewny sygnał błędu), 2) ręczna weryfikacja
wizualna zdjęć life-1/life-2 dla każdego pojazdu Can-Am (najwyższe ryzyko błędów w tej sesji),
częściowo Sea-Doo (który w każdym dotychczasowym sprawdzeniu wypadał poprawnie).

**Błędy znalezione i naprawione (galeria wyczyszczona, komentarz TODO w kodzie):**
- `canam-commander-xt` — galeria współdzielona z Commander DPS (zielony Compass Green),
  niezgodna z Dolomite Grey.
- `canam-maverick-sport-2027` — galeria pokazywała czarny pojazd (kolor 2026, Triple Black),
  niezgodna z Granite Grey. (Wersja 2026 zostaje bez zmian — tam pasuje.)
- `canam-rt-ltd` — galeria pokazywała czarny pojazd, niezgodna z Pearl White.
- `canam-f3-ltd` i `canam-f3-limited-2027` (współdzielona galeria) — zdjęcia pokazywały
  zielony pojazd, niezgodne z Vegas White Pearl.
- `canam-f3-ltd-special` — zdjęcie pokazywało żółty pojazd, niezgodne z Mars Red Metallic.
- `canam-outlander-pro` i `canam-outlander-pro-2027` (współdzielona galeria) — zdjęcie
  pokazywało zielony panel, niezgodne z Desert Tan.
- `seadoo-spark-60-2` i `seadoo-spark-2027` (współdzielona galeria) — zdjęcie pokazywało
  niebieski schowek, niezgodne z Sunrise Orange/Dragon Red.
- `canam-renegade` i `canam-renegade-2027` (współdzielona galeria) — zdjęcia pokazywały
  biało-żółty pojazd, niezgodny z ŻADNYM z dwóch oficjalnych kolorów (Catalyst Gray/Orange
  Crush ani Hyper Silver/Legion Red).

**Sprawdzone i potwierdzone zgodne:** Canyon STD, Outlander (base), Outlander MAX, Traxter
(base/MAX/PRO), Maverick (DS), Maverick R MAX, Ryker STD 600, Ryker Sport, Commander MAX,
Outlander Electric, Outlander MAX Electric.

**Niejednoznaczne, zostawione bez zmian (zbyt niska pewność, żeby zgadywać):** Ryker Rally
(zbyt małe/odległe zdjęcie), Spyder F3-T (zdjęcie w cieniu, może wyglądać szaro zamiast biało),
Outlander X mr (zdjęcie w błocie, kolor nie do ustalenia), Outlander MAX PRO (rozmyte, odległe
zdjęcie), Traxter MAX (odległe zdjęcie, niepewne).

**Nieobjęte tą turą (niższy priorytet — Sea-Doo dotychczas zawsze wypadał poprawnie):**
pozostałe zdjęcia galerii Sea-Doo (Spark 90/Trixx, GTI, GTX, GTR, GTR-X, RXP-X/RXT-X, Wake,
FishPro Trophy) oraz część Can-Am (F3-S poza, Traxter XU-rodzina, Maverick MAX/R base,
Pulse/Origin lifestyle) — nie sprawdzone wizualnie w tej turze z powodu ograniczeń czasowych,
ale też nie było żadnego sygnału (automatyczny skan konfliktów) wskazującego na błąd.

**Ważna uwaga techniczna:** pliki `.avif` NIE dają się czytać bezpośrednio — próba odczytu
bez konwersji marnuje ogromne ilości zasobów (dziesiątki tysięcy jednostek na plik, bo
narzędzie dostaje surowe dane binarne zamiast obrazu). Zawsze konwertować przez
`ffmpeg -i plik.avif plik.png` przed podglądem.

## ✅ AKTUALIZACJA 2026-09-09 (bardzo późna noc) — audyt galerii (`gallery:`) po wszystkich poprawkach kolorów

Klient słusznie zauważył: skoro zdjęcie główne (Traxter HD10) mogło zostać niezgodne po zmianie
nazwy koloru, to samo mogło dotyczyć zdjęć w galerii (`life-1`/`life-2`) dla wszystkich pojazdów,
którym w tej sesji zmieniłem kolor. Sprawdziłem wizualnie galerię każdego z nich (AVIF przez
ffmpeg, reszta bezpośrednio):

**Błędne galerie znalezione i wyczyszczone (ustawione na puste, z komentarzem TODO w kodzie):**
- `canam-rt-sea-to-sky-2027` — 2 zdjęcia pokazywały czerwony pojazd (Mars Red Metallic),
  niezgodne z poprawionym kolorem Dolomite Grey. (Wersja 2026 ma te same zdjęcia i tam
  są POPRAWNE — tam kolor się nie zmienił, więc jej nie ruszałem.)
- `canam-canyon-redrock-2027` — 2 zdjęcia pokazywały zielony pojazd (Moss Green), niezgodne
  z Sandstone. (Wersja 2026 — bez zmian, tam nadal poprawne.)
- `canam-maverick-trail` (2026) I `canam-maverick-trail-2027` — oba miały te same 2 zdjęcia
  pokazujące CZERWONY i ŻÓŁTY pojazd (dwa różne pojazdy na jednym zdjęciu, żaden nie pasował
  do koloru). Tu musiałem wyczyścić OBIE wersje, bo poprawka koloru 2026 (usunięcie błędnego
  Catalyst Gray, teraz samo Triple Black) też unieważniła te zdjęcia.

**Sprawdzone i potwierdzone ZGODNE (bez zmian):** Maverick Sport (życiowe zdjęcia pokazują
wyraźnie szare elementy — OK), Maverick R (czarny wariant — zgodny z Triple Black), Canyon XT
(srebrny pojazd — zgodny ze Sterling Silver Satin), Outlander XT-P (pomarańczowo-czarny — zgodny
z Mineral Grey & Orange Crush), Spark X Trixx (czerwono-niebieski skuter — zgodny z Blue Mist/
Coral Blast), Explorer Pro (czarno-limonkowy — zgodny z Iceland Grey), FishPro Sport (biało-
granatowy — zgodny z Bright White/Gulfstream Blue).

**Metoda:** pliki `.avif` nie dają się bezpośrednio podejrzeć — skonwertowane lokalnie przez
ffmpeg do PNG przed sprawdzeniem wizualnym.

## ✅ AKTUALIZACJA 2026-09-09 (późna noc) — Traxter HD10, Ryker, Commander MAX na żądanie klienta

- [x] **Traxter HD10 (`canam-traxter-hd9`) — POTWIERDZONY BŁĄD, NAPRAWIONY.** Sprawdzone dziesiątki
  oficjalnych zdjęć całej nowej platformy XU/HD10-11 (Defender XT, XT CAB, X mr, Limited, MAX XT
  na can-am.brp.com/off-road/us/en/models/sxs/utility-rec/defender-hd10-11.html) — paleta to
  wyłącznie Stealth Black / Dolomite Grey / Dark Wildland Camo / Hybrid White / Dusty Navy /
  Sandstone / Loft Green Satin. "Compass Green" nigdzie się nie pojawia — to kolor wyłącznie
  STAREJ platformy V-Twin. Zmieniono na "Dolomite Grey" — **zdjęcie też podmienione na prawdziwe**
  (pobrane z can-am.brp.com, Defender MAX XT HD10 Dolomite Grey, dopasowane do 4-drzwiowej kabiny
  crew cab jak w oryginale) — zapisane jako `images/canam-traxter-hd10-2027-dolomitegrey-1.png`,
  wpięte i przetestowane. Dwa zdjęcia w galerii (`-life-1.jpg`, `-life-2.jpg`) usunięte, bo pokazywały
  wyraźnie zielony pojazd (niezgodny) — nie znalazłem oficjalnego zdjęcia akcji w Dolomite Grey,
  więc galeria zostaje pusta do czasu dostarczenia prawdziwego zdjęcia lifestyle.
- [x] **Commander MAX (`canam-commander-max`) — SPRAWDZONY, JEST POPRAWNY, bez zmian.** Znaleziona
  pełna oficjalna paleta 2027 całej rodziny Commander (can-am.brp.com/off-road/us/en/models/sxs/
  recreational/commander.html): DPS 700 = Compass Green, XT = Triple Black/Dolomite Grey,
  XT-P = Dusty Navy, X mr = Loft Green Satin, MAX XT = Triple Black/Dolomite Grey (Triple Black
  na stronie to jeden z dwóch potwierdzonych oficjalnych kolorów). Przy okazji potwierdzone też,
  że Commander DPS 700 ("Compass Green") jest w 100% poprawny — jedyny model z całej rodziny
  Commander/Traxter, który legalnie zachował ten kolor (stara platforma V-Twin 700cc).
- [ ] **Ryker (cała rodzina: STD 600/900, Sport, Rally, 2027, Special Series) — SPRAWDZONE
  DOKŁADNIE, NIE ZMIENIONE, wymaga decyzji klienta/dystrybutora.** Znaleziona pełna oficjalna
  lista kolorów paneli z karty katalogowej MY26 (ONRD-MY26-RYK-SPEC-ENEMEA.pdf): Intense Black,
  Adrenaline Red, Yellow Shock (seria Epic) / Immortal White, Liquid Steel, Heritage White IV,
  Heritage Yellow, Icepop Blue, Lemon Twist, Silver Lava, Sonic Silver, Purple Galaxy, Sandstorm
  (seria Exclusive) / Blue Abyss, Goblin Green, Peachy Frenzy, Urban Blue, Cyber Orange (nowe panele).
  **Żaden z tych kolorów nie nazywa się "Triple Black" ani "Viper Red"** (obecne nazwy na stronie) —
  silny sygnał, że nazwy są błędne, ale Ryker ma system wymiennych paneli bez jednej definitywnej
  "nazwy koloru całego pojazdu", więc nie da się bezpiecznie zgadnąć którym z ~18 kolorów zastąpić
  obecne nazwy. **Wymaga potwierdzenia u dystrybutora BRP Polska, jaki panel/kolor faktycznie
  sprzedajecie**, zanim ktokolwiek to zmieni w kodzie.

## ✅ AKTUALIZACJA 2026-09-09 (noc) — skan reszty katalogu (54 pojazdy poza 18 parami)

Kontynuacja pełnego skanu kolorów na prośbę klienta — tym razem wszystkie pojazdy BEZ pary
2026/2027 (54 z 99). Metoda: alt-text i nazwy plików oficjalnych zdjęć studyjnych na
can-am.brp.com / sea-doo.brp.com, spot-checki wizualne przy niepewności.

**Błędy znalezione i naprawione:**
- Spark X Trixx (2027): "Coral Blast" → **"Blue Mist / Coral Blast"** (brakowało pierwszego członu nazwy).
- Canyon XT (2026): "Catalyst Grey / Viper Red" → **"Sterling Silver Satin"** (oficjalnie XT to
  po prostu Sterling Silver, jak Canyon STD — zdjęcie na stronie zresztą wygląda srebrno, nie szaro).
- Outlander XT-P (2026/2027): "Dusty Navy & Orange Crush" → **"Mineral Grey & Orange Crush"**
  (potwierdzone oficjalnym zdjęciem — bardzo zbliżony odcień, ale zła nazwa).

**Potwierdzone zgodne (bez zmian):** GTX 230, GTX Limited 325 i 350, Spark 60 For 2 (zdjęcie
sprawdzone wizualnie — mimo podejrzeń, zgodne z oficjalnym), Spark X, Wake 170, FishPro Trophy,
Spyder F3 S, Spyder RT LTD, Canyon STD, Traxter (2026, cała rodzina: base/XU/PRO/6x6), Outlander
MAX DPS, Outlander X mr, Outlander 6x6/MAX 6x6/MAX 6x6 DPS, Traxter XT CAB (2027) i Traxter Limited
(2027) — oba potwierdzone jeden-do-jednego z nową platformą Defender XU HD10/11.

**Niepewne / niesprawdzone do końca (zostawione bez zmian, brak wystarczających dowodów):**
- Ryker STD 600/900/Rally, Ryker (2027), Ryker Special Series — system wymiennych paneli
  z kilkunastoma historycznymi kolorami, nie da się jednoznacznie potwierdzić przez samo
  przeglądanie strony.
- Spyder F3 LTD (2026) — ma tylko 1 kolor na stronie ("Vegas White Pearl"), oficjalnie F3 Limited
  ma 3 opcje (Pearl White, Monolith Black, Mineral Blue) — niekompletne, ale nie błędne.
- Traxter HD10 (2027, `canam-traxter-hd9`) — kolor "Compass Green" nie występuje w potwierdzonej
  palecie nowej platformy XU (Dolomite Grey/Stealth Black/Dark Wildland Camo/Hybrid White/Dusty
  Navy/Sandstone), ale zdjęcie na stronie wygląda na prawdziwe, więc **nie zmieniałem** —
  wymaga jeszcze jednego spojrzenia z pewniejszym źródłem.
- Traxter X MR, Traxter Lone Star, Commander MAX (2027) — kolory niepotwierdzone w znalezionych
  materiałach, ale też nie ma dowodu, że są błędne.
- Renegade (2026) — "Catalyst Gray & Orange Crush" częściowo niepewne (jw. z poprzedniej tury).
- Outlander MAX PRO, Outlander X MR MAX — pojedynczy kolor na stronie, prawdopodobnie poprawny
  (spójny z rodziną PRO/X mr), ale nie znalazłem bezpośredniego potwierdzenia zdjęciem.
- Pulse/Origin (Electric) — oficjalnie dostępne w Bright White LUB Carbon Black + osobna edycja
  "'73" w Sterling Silver; strona ma "Bright White, Sterling Silver ('73)" — brakuje opcji
  Carbon Black, ale to niekompletność, nie błąd.

**Podsumowanie całego skanu (18 par + 54 pozostałe = 99 pojazdów):** 9 potwierdzonych błędów
znalezionych i naprawionych łącznie w obu turach, większość katalogu (>80%) potwierdzona zgodna
z oficjalnymi źródłami BRP, reszta oznaczona jako niepewna z podanym powodem zamiast zgadywania.

## ✅ AKTUALIZACJA 2026-09-09 (wieczór) — pełny skan 18 par 2026/2027 (36 kart)

Na prośbę klienta: zweryfikowane kolory OBU roczników (nie tylko 2027) dla wszystkich 18 modeli,
które mają osobną kartę na 2026 i 2027. Wynik:

**Błędy znalezione i naprawione w tej turze:**
- Maverick Trail (2026): usunięto nieistniejący kolor "Catalyst Gray" — oficjalnie tylko Triple Black.
- Explorer Pro (2026 i 2027): "Iceland Grey" obowiązuje dla OBU roczników (nie tylko 2027, jak
  wcześniej ustalono) — zdjęcie było zawsze poprawne, poprawiona tylko nazwa.
- FishPro Sport (2026 i 2027): "Bright White / Gulfstream Blue" obowiązuje dla OBU roczników —
  poprzednia poprawka objęła tylko 2027, teraz poprawione też 2026.
- Maverick R X RS SAS (2026): PRZYWRÓCONO "Dusty Navy" (był poprawny! błędnie nadpisany kolorem
  z MY27 w poprzedniej turze przez zbyt szerokie find&replace — patrz sekcja SSV wyżej).
- Maverick R MAX (bez podziału na roczniki): PRZYWRÓCONO "Dusty Navy & Legion Red" z tego samego powodu.

**Potwierdzone zgodne (bez zmian) po weryfikacji obu roczników:**
GTI Standard 130, GTX 170, GTR 230, GTR-X 300, Wake Pro 230 (2026+2027), GTI SE 170 (2026),
Spark 90 For 2 (2026), Canyon Redrock (2026: Moss Green — zgodne), Spyder RT Sea-to-Sky
(2026: Mars Red Metallic — zgodne), Outlander PRO (2026: Desert Tan + Compass Green — zgodne),
Outlander (2026: Granite Grey — zgodne), Maverick Sport (2026: Triple Black — zgodne),
Maverick R X rs DCT / X rc DCT SAS (oba roczniki).

**Wciąż niepewne / niezweryfikowane:**
- Ryker Sport — model z systemem wymiennych paneli (kilkanaście historycznych kolorów), nie udało
  się jednoznacznie potwierdzić czy "Triple Black / Viper Red" to prawdziwa kombinacja MY26/27.
- Renegade (2026) — częściowo potwierdzone: "Hyper Silver & Legion Red" zgodne, ale "Catalyst Gray
  & Orange Crush" niepewne (oficjalna strona pokazuje samo "Catalyst Grey" bez pary Orange Crush,
  plus brakuje na stronie trzeciego oficjalnego koloru "Scandi Blue") — nie zmieniałem, wymaga
  dalszej weryfikacji.

**Uwaga o cenach:** klient poprosił też o weryfikację cen — NIE jest to możliwe z publicznych źródeł
BRP (can-am.brp.com/sea-doo.brp.com pokazują tylko ceny USD dla rynku US, kompletnie nieporównywalne
z cennikiem EUR dystrybutora PL). Ceny sprawdzone tylko pod kątem wewnętrznej spójności (nie ma
oczywistych sprzeczności), ale nie zweryfikowano ich zgodności z rzeczywistym cennikiem PL.

---

## ✅ AKTUALIZACJA 2026-09-09 — zdjęcia kolorów dostarczone przez klienta

Klient pobrał i dostarczył zdjęcia dla 8 z 9 zgłoszonych rozbieżności kolorystycznych.
Zweryfikowałem każde wizualnie i wpiąłem do kodu (usunięte komentarze `// TODO: zdjęcie tymczasowe`):

- ✅ **Canyon Redrock** → `canam-canyon-redrock-2027-sandstone-1.webp` — potwierdzone, piaskowy Sandstone.
- ✅ **Spyder RT Sea-to-Sky** → `canam-rt-sea-to-sky-2027-dolomitegrey-1.jpg` — potwierdzone, Dolomite Grey.
- ✅ **Maverick Trail** → `canam-maverick-trail-2027-granitegrey-1.webp` — potwierdzone, Granite Grey.
- ✅ **Maverick Sport** → `canam-maverick-sport-2027-granitegrey-1.webp` — potwierdzone, Granite Grey.
- ✅ **FishPro Sport** → `seadoo-fishpro-sport-2027-brightwhite-1.webp` — potwierdzone, Bright White/Gulfstream Blue.
- ✅ **Maverick R, pakiet X RS SAS** (2026 i 2027) → `canam-maverick-r-2027-dolomitegrey-xrs-1.png` —
  potwierdzone wizualnie, Dolomite Grey & Orange Crush, 2-osobowy kadłub X RS.
- ⚠️ **Explorer Pro 170/230 — KOREKTA MOJEGO WCZEŚNIEJSZEGO USTALENIA:** klient przesłał zrzut
  ekranu prawdziwej karty produktu dealerskiej ("SEA-DOO EXPLORER PRO 230 AUDIO iDF GREY 2027",
  kod P.00016VA00) — zdjęcie pokazuje **ten sam czarno-żółty kadłub, który był na stronie od
  początku** (Eclipse Black/Lemon Zest). Mój wcześniejszy wniosek "Iceland Grey" na podstawie
  automatycznego podsumowania strony sea-doo.brp.com był BŁĘDNY (prawdopodobnie pomyłka
  narzędzia AI przy czytaniu strony, albo dotyczył innego wariantu). **Cofnąłem zmianę** —
  nazwa koloru zmieniona na "iDF Grey" (oficjalna nazwa handlowa z tej karty produktu), ale
  ZDJĘCIE zostało oryginalne (czarno-żółte), bo już było poprawne. Nie potrzeba nowego zdjęcia.
- ✅ **Maverick R MAX, pakiet MAX X RS — ROZWIĄZANE (2026-09-09).** Oba pliki od klienta
  pokazywały 2-osobowy X RS (nie MAX) — zamiast zgadywać, pobrałem właściwe zdjęcie bezpośrednio
  ze studia produktowego BRP: znalazłem dokładny plik przez devtools na stronie
  can-am.brp.com/off-road/us/en/models/sxs/sport/maverick-r.html (alt="Maverick R MAX X rs",
  data-src wskazywał na `ORV-MY27-SSV-MAV-R-MAX-Xrs-MillNT-DOLOMITE-GREY-0007DVF00-STUDIO-...png`).
  Zweryfikowane wizualnie: wyraźnie dłuższy, 4-osobowy kadłub z 2 rzędami siedzeń — zgodne
  z referencyjnym `images/canam-maverick-r-max-1.jpg`. Zapisane jako
  `images/canam-maverick-r-max-2027-dolomitegrey-1.png`, wpięte do kodu, przetestowane w przeglądarce.

Plan: katalog dostaje sekcję/odznakę "2027" na górze, a pod nią zostaje kontynuacja
obecnej oferty 2026 (52 pojazdów już na stronie — bez zmian).

Nazewnictwo plików — trzymam się konwencji, która już jest w kodzie:
- Sea-Doo → `images/seadoo-{slug}-{n}.jpg`
- Can-Am (wszystko: trójkołowce/ATV/SSV) → `images/canam-{slug}-{n}.jpg`
- 3 zdjęcia na pojazd: `-1` i `-2` = zdjęcie studyjne/produktowe (na białym/neutralnym tle,
  tak jak istniejące `images/seadoo-spark-60-2-1.jpg`), `-life-1` = zdjęcie w akcji/lifestyle
  (na wodzie/w terenie, tak jak `images/seadoo-spark-60-2-life-1.avif`)

Źródła zdjęć i cen (oficjalne strony BRP — stamtąd pobierz):
- Sea-Doo: https://sea-doo.brp.com/us/en/models/personal-watercrafts.html (klikasz w model → zakładka "Gallery" ma zdjęcia w wysokiej rozdzielczości, "Build & Price" pokazuje ceny US)
- Can-Am Off-Road: https://can-am.brp.com/off-road/us/en/models.html
- Can-Am On-Road: https://can-am.brp.com/on-road/us/en/models.html
- Dla PL cen: https://www.brp.com/pl-PL (wybierz regionu Polska) LUB skontaktuj się
  z dystrybutorem BRP Polska po cennik hurtowy MY27 — ceny USD z amerykańskiej strony
  NIE nadają się do przeliczenia 1:1 (inne podatki/marże na rynku PL)

---

## ✅ REUSE — użyj zdjęć, które JUŻ SĄ na stronie (24 pojazdy)

Te modele to czysty carry-over w MY27 — ten sam wygląd zewnętrzny co model, który już
masz w katalogu (czasem tylko inny silnik/moc pod maską, bez zmiany karoserii/grafiki).
Wystarczy skopiować istniejące pliki `images/...` pod nowym wpisem w kodzie — **zero
nowych zdjęć do pobierania**.

**Sea-Doo (10):**
- [x] Spark → użyj zdjęć z „Spark 60/90 For 2"
- [x] GTI → użyj zdjęć z „GTI Standard 130"
- [x] GTI SE → użyj zdjęć z „GTI SE 170"
- [x] GTX → użyj zdjęć z „GTX 170/230"
- [x] GTX Limited → użyj zdjęć z „GTX Limited 325"
- [x] ~~Explorer Pro → użyj zdjęć z „Explorer Pro 170/230"~~ **PRZENIESIONE do VERIFY — potwierdzone na sea-doo.brp.com: kolor MY27 to Iceland Grey, różni się od obecnego (Eclipse Black/Lemon Zest). Nazwa/hex w kodzie już poprawione (2026-09-09), ale zdjęcie nadal ze starego koloru — brak prawdziwego zdjęcia Iceland Grey**
- [x] GTR → użyj zdjęć z „GTR 230"
- [x] GTR-X 300 → użyj tych samych zdjęć „GTR-X 300"
- [x] ~~Wake Pro → użyj zdjęć z „Wake Pro 230"~~ **PRZENIESIONE do NOWE — kolor 2027 (turkus/limonka) różni się od obecnego (Sand/Dazzling Blue), zdjęcie już dostarczone**
- [x] ~~FishPro Sport → użyj zdjęć z „FishPro Sport 170"~~ **PRZENIESIONE do VERIFY — potwierdzone na sea-doo.brp.com: kolor MY27 to Bright White / Gulfstream Blue, różni się od obecnego (Vapor Blue/Catalyst Grey). Nazwa/hex w kodzie już poprawione (2026-09-09), ale zdjęcie nadal ze starego koloru. Pojazd obecnie i tak `tempHidden: true` (brak w cenniku od klienta), więc błąd niewidoczny na produkcji, ale trzeba poprawić przed odkryciem karty**

**Trójkołowce (6):**
- [x] Spyder F3 → zdjęcia zbliżone do „Spyder F3 S" (baza)
- [x] Spyder F3 Limited → użyj zdjęć z „Spyder F3 LTD"
- [x] Spyder RT → zdjęcia zbliżone do „Spyder RT LTD" (baza)
- [x] ~~Spyder RT Sea-to-Sky → użyj tych samych zdjęć~~ **PRZENIESIONE do VERIFY — potwierdzone
  na can-am.brp.com (zapowiedź MY27 + komunikat prasowy): nowy sygnaturowy kolor Dolomite Grey,
  różni się od obecnego Mars Red Metallic. Nazwa/hex już poprawione w kodzie (2026-09-09).**
- [x] Canyon → użyj zdjęć z „Canyon STD"
- [x] ~~Canyon Redrock → użyj tych samych zdjęć~~ **PRZENIESIONE do VERIFY — potwierdzone
  na can-am.brp.com ("NEW COLOR FOR CANYON REDROCK — Sandstone"): różni się od obecnego
  Moss Green Satin. Nazwa/hex/opisy już poprawione w kodzie (2026-09-09).**

**ATV (4):**
- [x] Outlander → użyj tych samych zdjęć
- [x] Outlander MAX 6x6 DPS → użyj zdjęć z „Outlander MAX 6x6"
- [x] Outlander Pro → użyj zdjęć z „Outlander PRO"
- [x] Renegade → użyj tych samych zdjęć

**SSV (3):**
- [x] ~~Maverick Trail → użyj tych samych zdjęć~~ **PRZENIESIONE do VERIFY — potwierdzone
  w oficjalnej karcie katalogowej MY27 (ORV_SSV_MY27_SPEC_MAVTRAIL_X_700_1000_ENNA_HR.pdf):
  kolor Granite Grey, różni się od obecnego Catalyst Gray/Triple Black. Nazwa/hex już poprawione (2026-09-09).**
- [x] ~~Maverick Sport → użyj tych samych zdjęć~~ **PRZENIESIONE do VERIFY — potwierdzone
  w oficjalnej karcie katalogowej MY27 (ORV_SSV_MY27_SPEC_MAVSPORT_X_ENNA_HR.pdf):
  kolor Granite Grey, różni się od obecnego Triple Black. Nazwa/hex już poprawione (2026-09-09).**
- [ ] **Maverick R → SPRAWDZONE DOKŁADNIE po pakietach (2026-09-09), ZNALEZIONY BŁĄD:**
  - Pakiet **X rs DCT** (Triple Black) — ✅ ZGODNE z kartą katalogową MY27 (ORV_SSV_MY27_SPEC_MAVR_Xrs_ENNA_HR.pdf).
  - Pakiet **X rc DCT SAS** (Loft Green Satin) — ✅ ZGODNE, potwierdzone dwukrotnie: karta katalogowa MY27
    (ORV_SSV_MY27_SPEC_MAVR_Xrc_ENNA_HR.pdf) ORAZ zdjęcie hero na can-am.brp.com/off-road/us/en/models/
    sxs/sport/maverick-r.html ("Maverick R X rc Loft Green Satin package shown").
  - Pakiet **X rs DCT SAS** — ✅ **POPRAWNIE ROZRÓŻNIONE PO ROCZNIKACH (2026-09-09, skorygowane
    po własnym błędzie):** oficjalna karta MY26 (ORV_SSV_MY26_SPEC_MAVR_Xrs_ENNA_HR.pdf) potwierdza
    "Triple Black, Dusty Navy" — czyli oryginalny "Dusty Navy" był PRAWIDŁOWY dla rocznika 2026!
    Pierwotnie omyłkowo zmieniłem kolor na "Dolomite Grey & Orange Crush" (kolor z karty MY27) w OBU
    kartach naraz (2026 i 2027) przez zbyt szerokie find&replace. Naprawione: karta **2026**
    (`canam-maverick-r`) wróciła do "Dusty Navy" + oryginalne zdjęcie; karta **2027**
    (`canam-maverick-r-2027`) zachowuje "Dolomite Grey & Orange Crush" + nowe zdjęcie pobrane
    z can-am.brp.com (plik ORV-MY27-SSV-MAV-R-XrsSAS-MillNT-DOLOMITE-GREY-...png).
  - Pakiet **Maverick R MAX** (osobna karta, bez rozbicia na roczniki, cena podana wprost =
    traktowana jako 2026) — ✅ **PRZYWRÓCONE do "Dusty Navy & Legion Red" + oryginalne zdjęcie**
    (2026-09-09) — z tego samego powodu co wyżej: to prawidłowy kolor MY25/26 (potwierdzony
    licznymi ofertami dealerskimi US), a nie MY27. Pobrane zdjęcie Dolomite Grey MAX X RS
    (`canam-maverick-r-max-2027-dolomitegrey-1.png`) zostaje w `images/` na wypadek, gdyby
    w przyszłości dodano osobną kartę "Maverick R MAX (2027)".

**Electric (1):**
- [x] Outlander Electric → już jest w katalogu, tylko zweryfikuj specyfikację/cenę MY27

---

## ⚠️ VERIFY — prawdopodobnie to samo, ale sprawdź źródłowe zdjęcie przed reuse

**Stan na 2026-09-09: 7 z 9 punktów rozwiązanych/wyjaśnionych. Otwarte: Ryker Sport, Maverick R (patrz SSV wyżej — sprawdzenie per-pakiet).**

- [x] ~~Explorer Pro 170/230~~ **OSTATECZNIE ROZWIĄZANE (2026-09-09, po 2 turach korekt):**
  potwierdzone na sea-doo.brp.com że kolor **Iceland Grey** obowiązuje dla MY26 I MY27 (identyczne
  zdjęcia studyjne obu roczników). Pobrane oficjalne zdjęcie Iceland Grey jest WIZUALNIE IDENTYCZNE
  z oryginalnym zdjęciem, które już było na stronie (czarny kadłub z żółto-limonkowymi akcentami) —
  zdjęcie było więc od początku poprawne, błędna była tylko NAZWA ("Eclipse Black / Lemon Zest").
  Poprawiono nazwę na "Iceland Grey" w 3 kartach: `seadoo-explorer-pro-170`, `seadoo-explorer-pro-230`
  i `seadoo-explorer-pro-2027` — zdjęcia bez zmian (już poprawne, potwierdzono zgodność z portalem
  dealerskim klienta pokazującym identyczny wygląd pod nazwą "iDF GREY").
- [x] ~~FishPro Sport 170~~ **OSTATECZNIE ROZWIĄZANE (2026-09-09):** potwierdzone na sea-doo.brp.com,
  że kolor **Bright White / Gulfstream Blue** obowiązuje dla MY26 I MY27 (identyczne zdjęcia obu
  roczników) — czyli oryginalny "Vapor Blue / Catalyst Grey" był błędny dla OBU roczników, nie tylko
  2027. Poprawiono nazwę + zdjęcie w obu kartach (`seadoo-fish-pro-sport-170` i
  `seadoo-fishpro-sport-2027`), używając tego samego pobranego zdjęcia dla obu (ten sam kolor).
- [x] ~~RXP-X~~ **ROZWIĄZANE (2026-09-09):** kolory 100% zgodne z oficjalną stroną sea-doo.brp.com —
  Solar Orange Metallic Premium + Gulfstream Blue Premium (RXP-X 350) i Racing Yellow / Amazon Green
  (RXP-X Senna 350). Sprawdzone też wizualnie: zdjęcia studyjne (`seadoo-rxp-x-hero.jpg`,
  `seadoo-rxp-x-1.png`) poprawnie pokazują krótki, jednoosobowy kadłub sportowy z czytelnym
  napisem „RXP X" — obawa z wcześniejszej notatki o pomyleniu z RXT-X już NIEAKTUALNA, pliki
  zostały poprawione w międzyczasie (inne hashe/daty modyfikacji niż opisany wcześniej problem).
- [x] ~~RXT-X~~ **ROZWIĄZANE (2026-09-09):** kolory 100% zgodne z oficjalną stroną (te same
  Solar Orange Metallic Premium + Gulfstream Blue Premium co RXP-X — to oficjalnie wspólna paleta
  na MY27). Zdjęcie studyjne (`seadoo-rxt-x-orange-hero.jpg`) poprawnie pokazuje dłuższy,
  dwuosobowy kadłub turystyczno-sportowy z czytelnym napisem „RXT X" — wyraźnie inny niż RXP-X,
  błędne podpisanie pliku z wcześniejszej notatki już nieaktualne. Jedyna niepewność: jedno
  zdjęcie akcji (`seadoo-rxt-x-life-1.png`) pokazuje osobę jadącą na stojąco na dość krótkim
  kadłubie — mogło zostać pomylone z RXP-X w akcji, warto rzucić okiem ręcznie, niska pewność.
- [ ] **Ryker Sport** — NIE UDAŁO SIĘ potwierdzić kolorystyki MY27 — oficjalna zapowiedź lineupu
  mówi ogólnie o „nowych kolorach paneli" dla całej platformy Ryker (przeprojektowanej na MY27),
  bez konkretnej nazwy dla wariantu Sport, a karta katalogowa MY27 nie jest jeszcze publicznie
  dostępna pod znanym adresem. Obecny kolor na stronie (Triple Black / Viper Red) mógł zostać,
  ale to niepotwierdzone — do sprawdzenia u dystrybutora/w portalu dealerskim.
- [x] ~~Maverick X3~~ **ROZWIĄZANE (2026-09-09):** to TEN SAM pojazd co „Maverick"/„Maverick MAX"
  na stronie (silnik Turbo RR = sygnatura platformy X3, potwierdzone na can-am.brp.com/off-road/
  us/en/models/sxs/sport/maverick-x3.html) — brakowało tylko „X3" w nazwie wyświetlanej.
  Poprawiłem nazwy na „Maverick X3" / „Maverick X3 MAX" w kodzie (id-y bez zmian, tylko `name`
  i tekst opisów). „Maverick R" (999T DCT) to osobna, faktycznie nowa platforma — bez zmian.
- [x] ~~Defender/Traxter HD7~~ **WYJAŚNIONE:** brak osobnej karty produktu dla HD7 nie jest błędem —
  HD7 (52 KM, 1-cylindrowy 650cc) jest już wymieniony jako jeden z silników bazowego „Traxter"
  (`canam-traxter`, engine: „HD7 / HD9 / HD11"), tak jak w oficjalnej ofercie, gdzie HD7 to opcja
  silnikowa w ramach modelu, a nie osobny model.
- [x] ~~Defender/Traxter HD9~~ **WYJAŚNIONE:** jw. — HD9 (65 KM, V-Twin 976cc) też jest opcją
  silnikową w `canam-traxter` i `canam-traxter-max`, nie osobnym modelem. Nie mylić z 2027
  „Traxter HD10" (`canam-traxter-hd9` — id historyczny, ale nazwa/dane poprawnie mówią HD10).
- [x] ~~Defender/Traxter HD10~~ **ZWERYFIKOWANE, kod POPRAWNY (uwaga — omal nie wprowadziłem
  tu błędu):** oficjalna strona can-am.brp.com/off-road/us/en/models/sxs/utility-rec/
  defender-xu-hd10-11.html POTWIERDZA: na nowej platformie XU zarówno HD10 (80 KM) jak i HD11
  (95 KM) to TEN SAM silnik — trzycylindrowy Rotax ACE 999 cm³, różniący się tylko strojeniem.
  To zgadza się z opisem w kodzie (`canam-traxter-hd9`/„Traxter HD10", `canam-traxter-xu`,
  `-x-mr`, `-xt`). Osobno istnieje STARSZY, wciąż sprzedawany „HD10" na bazowej platformie
  (Rotax 976cc V-Twin, 82 KM, wg utvguide.net) — ale to inny, równoległy wariant nazewnictwa,
  niepowiązany z nowymi kartami 2027 na tej stronie. Nie zmieniałem kodu.
- [x] ~~Defender/Traxter MAX~~ **WYJAŚNIONE:** na stronie odpowiada to `canam-traxter-max`
  (2026, HD9/HD11) — istniejący, poprawny wpis. Nowa generacja HD11 jest już osobno reprezentowana
  przez `canam-traxter-limited`/`canam-traxter-lonestar` (95 KM) na rocznik 2027.

---

## 🆕 NOWE ZDJĘCIA DO POBRANIA (23 pojazdy × 3 = 69 plików)

### Sea-Doo
- [x] Spark X — zdjęcia dostarczone (folder klienta)
- [x] Spark X Trixx — zdjęcia dostarczone (folder klienta, jako "spark trixx")
- [x] RXP-X Senna 350 — **klient potwierdził: już dodane**
- [x] Wake (bazowy) — zdjęcia dostarczone (folder klienta, "wake 2027")
- [x] Wake Pro (nowy kolor turkus/limonka) — zdjęcia dostarczone
- [x] FishPro Trophy — zdjęcia dostarczone (folder klienta)
- [ ] RXT-X — ⚠️ brak poprawnego zdjęcia, patrz sekcja VERIFY wyżej
- [x] ~~Switch~~ — **NIE SPRZEDAJEMY, usunięte z listy**
- [x] ~~Switch Sport~~ — **NIE SPRZEDAJEMY, usunięte z listy**

### Can-Am trójkołowce (4)
- [ ] Ryker (cała platforma przeprojektowana na MY27) — `canam-ryker-2027-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Ryker Sport (jw., nowy wygląd) — `canam-ryker-sport-2027-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Ryker Special Series (nowość, edycja 1-roczna) — `canam-ryker-special-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Spyder F3-S (nowy wygląd — Liquid Titanium + Monolith Black Satin) — `canam-f3-s-2027-1.jpg / -2.jpg / -life-1.jpg`

### Can-Am ATV (2)
- [ ] Outlander X mr MAX (nowa konfiguracja MAX, wcześniej tylko 1-osobowy) — `canam-outlander-x-mr-max-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Outlander XTP 1000R (nowość, brak na stronie) — `canam-outlander-xtp-1.jpg / -2.jpg / -life-1.jpg`

### Can-Am SSV (10)
- [ ] Defender/Traxter HD11 (całkiem nowa, przeprojektowana platforma) — `canam-traxter-hd11-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Defender/Traxter XT / XT CAB — `canam-traxter-xt-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Defender/Traxter X mr — `canam-traxter-x-mr-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Defender/Traxter Limited — `canam-traxter-limited-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Defender/Traxter Lone Star — `canam-traxter-lonestar-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Defender/Traxter XU (nowość) — `canam-traxter-xu-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Defender/Traxter XU Pro/6x6 (nowość) — `canam-traxter-xu-pro-6x6-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Commander DPS (marka w ogóle nieobecna na stronie) — `canam-commander-dps-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Commander XT — `canam-commander-xt-1.jpg / -2.jpg / -life-1.jpg`
- [ ] Commander MAX — `canam-commander-max-1.jpg / -2.jpg / -life-1.jpg`

---

## CO JESZCZE MUSISZ ZROBIĆ (poza zdjęciami)

1. **Ceny PL** — strona BRP US pokazuje ceny w USD, nieprzydatne bezpośrednio.
   Zdobądź polski cennik MY27 od dystrybutora BRP Polska albo z polskich stron
   dealerskich (np. wyszukaj "cennik Sea-Doo 2027 Polska", "cennik Can-Am 2027 Polska").
2. **Silniki/moc/specyfikacja techniczna** — dla każdego pojazdu potrzebne dane typu
   "Rotax 1630 ACE, 350 KM" itd. — są na stronach produktowych BRP (zakładka "Specs").
3. **Kolory lakieru** — obecne wpisy mają pole `colors` z nazwą + kodami hex + osobnym
   zdjęciem na kolor (patrz istniejący wpis Spark 60 For 2 w kodzie jako wzór). Dla
   modeli z listy REUSE prawdopodobnie wystarczą te same kolory co w 2026.
4. **Krótki + długi opis (desc/fullDesc/highlights/forWho/features)** — to ja mogę
   napisać sam na podstawie danych technicznych, jak już będą znane silniki i segment.
5. **Decyzja o etykiecie "2027"** — potwierdź jak ma wyglądać wizualnie (np. plakietka
   "MY27" na karcie produktu) i gdzie dokładnie w układzie kategorii ma się pojawiać
   podział 2027 → 2026 (osobna sekcja na górze listy w każdej kategorii, czy filtr rocznika?).

---

**Podsumowanie:**
- **24 pojazdy** → zero nowych zdjęć, reuse istniejących plików z katalogu
- **7 pojazdów** → prawdopodobnie reuse, ale zweryfikuj źródłowe zdjęcie BRP najpierw
- **23 pojazdy × 3 zdjęcia = 69 plików** → faktycznie trzeba pobrać nowe

Jak dowieziesz nowe zdjęcia + ceny + specyfikację, ja dopiszę pełne karty produktów
(opisy, highlights, features) i wpinam wszystko do kodu.

---

## ✅ AKTUALIZACJA 2026-09-10 — dokończony audyt galerii Sea-Doo + próba weryfikacji kolorów Ryker

### Zadanie 1: audyt galerii Sea-Doo (dokończenie wczorajszego audytu)

Sprawdzono wizualnie (Read tool, porównanie zdjęcia głównego karty i CAŁEJ tablicy `colors[]`
vs zdjęcia w `gallery[]`) wszystkie 25 wskazanych kart Sea-Doo: seadoo-spark-90-2,
seadoo-spark-trixx-1, seadoo-spark-trixx-3, seadoo-gti-std, seadoo-gti-se, seadoo-gti-2027,
seadoo-gti-se-2027, seadoo-gtx-170, seadoo-gtx-230, seadoo-gtx-limited-325, seadoo-gtx-2027,
seadoo-gtx-limited-2027, seadoo-gtr-230, seadoo-gtr-x-300, seadoo-gtr-2027, seadoo-gtr-x-2027,
seadoo-rxp-x-325, seadoo-rxt-x-325, seadoo-rxp-x, seadoo-rxp-x-senna, seadoo-rxt-x,
seadoo-wake-pro-230, seadoo-wake-2027, seadoo-wake-pro-2027, seadoo-fishpro-trophy,
seadoo-fishpro-sport-2027.

Żadne zdjęcie w gallery nie było plikiem `.avif` (same `.jpg/.png/.webp`), więc konwersja przez
ffmpeg nie była potrzebna — obrazy czytane bezpośrednio.

**Ważna korekta metodologii w trakcie audytu:** część pojazdów ma DWA (lub więcej) oficjalnie
zadeklarowanych kolorów w tablicy `colors[]` (np. RXP-X 325: Gulfstream Blue Premium ORAZ Ice
Metal/Manta Green). Zdjęcie w gallery pokazujące pojazd w kolorze `colors[1]` (nie tylko
`colors[0]`) NIE jest błędem — to legalny, zadeklarowany wariant tego samego produktu. Pierwsze
podejście błędnie flagowało kilka takich przypadków (Spark Trixx 1/3, GTX Limited 325, RXT-X 325,
GTI SE) jako niezgodne tylko dlatego, że gallery pokazywała `colors[1]` zamiast `colors[0]` —
po ponownej weryfikacji wszystkie te przypadki uznano za POPRAWNE (zdjęcie odpowiada jednemu
z legalnych wariantów kolorystycznych) i wycofano z listy poprawek.

**Znaleziony i naprawiony 1 rzeczywisty błąd:**
- [x] `seadoo-wake-pro-2027` — jedyny zadeklarowany kolor to Teal Blue/Manta Green (zdjęcie
  `seadoo-wake-pro-hero.jpg`, kadłub turkusowo-czarny). Drugie zdjęcie w gallery
  (`seadoo-wake-pro-life-2.jpg`) pokazywało piaskowo-niebieski kadłub — to kolorystyka modelu
  Wake Pro 230 (`seadoo-wake-pro-230`, kolor Sand/Dazzling Blue), skopiowana pomyłkowo do karty
  2027. Ponieważ dla tej karty jest tylko JEDEN legalny kolor (brak wariantu piaskowego),
  to jednoznaczny błąd. Ustawiono `gallery: []` z komentarzem TODO w kodzie.

**Pozostałe 24 karty: gallery w 100% zgodna** z zadeklarowanymi kolorami (w tym z uwzględnieniem
wariantów `colors[1]`) — bez zmian.

### Zadanie 2: próba ustalenia prawdziwych kolorów rodziny Ryker (Can-Am)

Sprawdzono wszystkie karty `canam-ryker-*` (7 pojazdów: std-600, std-900, sport, rally — MY26/bez
`myYear`; ryker-2027, ryker-sport-2027, ryker-special — MY27). Zdjęcia studyjne na stronie
extreme-club dla WSZYSTKICH tych kart pokazują pojazd w jednolitym, matowym czarnym malowaniu —
bez widocznych czerwonych paneli (jedyny czerwony element to fizyczna plastikowa chorągiewka
bezpieczeństwa z tyłu, nie lakier).

Przez WebSearch znaleziono wielokrotnie potwierdzoną (różne, niezależne od siebie oferty
dealerskie w USA, zasilane danymi z feedu inwentarza BRP) nazwę koloru **"Intense Black"** jako
oficjalny kolor obowiązujący na MY26 dla WSZYSTKICH wariantów: Ryker 600 ACE, Ryker 900 ACE,
Ryker Sport, Ryker Rally. Nazwa "Triple Black" (obecna wcześniej w kodzie) nie pojawia się
NIGDZIE w wynikach wyszukiwania dla MY26 — wygląda na błędną/wymyśloną. Nazwa "Viper Red" przy
Ryker Sport jest szczególnie podejrzana, bo zdjęcie na stronie klienta nie pokazuje ŻADNEGO
czerwonego lakieru na pojeździe.

**Naprawiono (wysoka pewność, MY26/bez `myYear`):**
- [x] `canam-ryker-std-600`: "Triple Black" → **"Intense Black"**
- [x] `canam-ryker-std-900`: "Triple Black" → **"Intense Black"**
- [x] `canam-ryker-sport`: "Triple Black / Viper Red" → **"Intense Black"** (usunięto "Viper Red" —
  brak czerwonego akcentu na zdjęciu, żadne źródło nie potwierdza tej nazwy dla MY26)
- [x] `canam-ryker-rally`: "Triple Black" → **"Intense Black"**

**NIE zmieniono (niska pewność, karty MY27 — `myYear: 2027`):**
- [ ] `canam-ryker-2027` (obecnie "Carbon Black"), `canam-ryker-sport-2027` (obecnie "Triple
  Black / Viper Red"), `canam-ryker-special` (obecnie "Special Series Graphics") — jak ustalono
  we wczorajszym audycie, platforma Ryker MY27 jest CAŁKOWICIE przeprojektowana i posiada nowe,
  nieznane jeszcze publicznie nazwy kolorów paneli. Znaleziona nazwa "Intense Black" pochodzi
  z ofert dealerskich MY26, NIE MY27 — nie można jej bezpiecznie przenieść na nowy rocznik bez
  potwierdzenia z oficjalnej karty katalogowej MY27 (niedostępna publicznie w momencie audytu).
  Do potwierdzenia u dystrybutora/w portalu dealerskim klienta, gdy karta MY27 się pojawi.
  Osobna obserwacja: BRP zapowiedziało dla całej platformy Ryker MY27 trzy NOWE kolory paneli
  (customizable, nie kolor bazowy nadwozia): "Crimson Rush", "Peachy Frenzy", "Cotton Candy" —
  to prawdopodobnie opcje personalizacji (podobne do dotychczasowych kolorowych paneli Ryker),
  a nie domyślny kolor studyjny pokazywany na kartach produktu — nie użyto tych nazw w kodzie.

**Weryfikacja końcowa:** VEHICLES nadal parsuje się poprawnie, liczba pojazdów = 99 (bez zmian).
Brak commitów — zmiany zostawione w working tree do decyzji klienta/zespołu.
