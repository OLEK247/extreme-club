# Audyt kategorii Sea-Doo / Trójkołowce / ATV / Electric — 2026-09-13

Zakres: te same kryteria co w audycie SSV (kompletność modeli/wariantów silnikowych względem
oficjalnego cennika/oferty BRP na MY2027 + orientacyjna weryfikacja cen u polskich dealerów).
Metoda: eksport tablicy `VEHICLES` z `index.html` (node), WebSearch/WebFetch po oficjalnych
źródłach BRP (sea-doo.brp.com, can-am.brp.com, komunikaty prasowe ir.brp.com/prnewswire.com) oraz
próba znalezienia polskich cenników (perfectmoto.pl, fanjet.pl, brpbroker.pl). Przed startem
przeczytano `TODO-rocznik-2027.md`, `pytania-do-dystrybutora-BRP.md`, `AUDYT-FINALNY-2026-09-13.md`
— świadomie zaakceptowane wcześniej braki (puste galerie, niezweryfikowany Origin Carbon Black,
brak 2. zdjęcia F3/RT LTD) NIE są tu powtarzane.

---

## Sea-Doo — status

**34 pojazdy w katalogu** (18 bez `myYear` = MY2026, 16 z `myYear:2027`).

Oficjalna pełna lista MY2027 wg sea-doo.brp.com (kategorie Rec-Lite/Recreation/Touring/
Performance/Tow-Sports/Sport-Fishing): Spark, Spark X, Spark X Trixx, GTI, GTI SE, GTX, GTX
Limited 350, Explorer Pro, GTR, GTR-X 300, RXP-X 350, RXT-X 350, Wake, Wake Pro, FishPro Sport,
FishPro Trophy. Dodatkowo limitowana edycja RXP-X Senna 350 (komunikat prasowy BRP, sierpień
2026, produkcja 1991 szt.).

**BRAKUJĄCE MODELE/WARIANTY:** brak. Wszystkie 16 pozycji z powyższej oficjalnej listy mają
odpowiednik w katalogu (włącznie z limitowaną edycją RXP-X Senna 350 — `seadoo-rxp-x-senna`).
Źródło: sea-doo.brp.com/us/en/models.html (fetch 2026-09-13) + prnewswire.com/BRP IR (komunikat
"Sea-Doo Revamps 2027 Lineup...", sierpień 2026).

**CENY DO WERYFIKACJI:** nie znaleziono jednoznacznego polskiego cennika dealerskiego 2027 dla
Sea-Doo (perfectmoto.pl ma tylko archiwalny PDF cennika 2023, aktualny cennik chowany za
formularzem; fanjet.pl bez publicznie dostępnego cennika PWC 2027). Zgodnie z zasadą "nie zgaduj"
— **nie znaleziono źródła cenowego**, ceny w katalogu pozostają niesprawdzone względem polskiego
rynku w tej turze (były już częściowo weryfikowane w poprzednich audytach względem dealerów US,
patrz `weryfikacja-kolorow-99-pojazdow.md`).

**OK — bez zastrzeżeń** poza punktem cenowym: kompletność modelowa potwierdzona w 100%.

---

## Can-Am trójkołowce — status

**23 pojazdy w katalogu** (11 bez `myYear`, 12 z `myYear:2027`).

Oficjalna aktualizacja MY2027 (komunikat prasowy BRP "Can-Am Elevates its 2027 3-Wheel Lineup",
sierpień 2026): Ryker (nowy silnik 52 KM na wersji bazowej, 80 KM na Sport i na nowej,
jednorocznej edycji Ryker Special Series), Spyder F3-S (nowa ramka Liquid Titanium + nadwozie
Monolith Black Satin), Spyder RT Sea-to-Sky i Spyder F3 Limited Special Series (nowy kolor
Dolomite Grey), Canyon Redrock (nowy kolor Sandstone).

**BRAKUJĄCE MODELE/WARIANTY:** brak nowych, nieobecnych w katalogu modeli/silników. Wszystkie
wymienione w komunikacie prasowym pozycje mają odpowiedniki: `canam-ryker-2027`,
`canam-ryker-sport-2027`, `canam-ryker-special` (Special Series), `canam-f3-s-2027`,
`canam-f3-ltd-special` (F3 Limited Special Series — uwaga: to wpis bez `myYear:2027` w kodzie,
osobna sprawa techniczna, nie brak treściowy), `canam-rt-sea-to-sky-2027`,
`canam-canyon-redrock-2027`. Ta kategoria była już bardzo szczegółowo przeszukana we
wcześniejszych turach (`pytania-do-dystrybutora-BRP.md`, punkt 1 i 4) — potwierdzam tamte
ustalenia, nowy research nie ujawnił żadnego dodatkowego brakującego wariantu silnikowego.

**CENY DO WERYFIKACJI:** ceny linii On-Road 2027 były już zaktualizowane w poprzedniej turze na
podstawie PerfectMoto.pl/Taurus Sea Power (patrz `pytania-do-dystrybutora-BRP.md`, sekcja 1) —
8 cen zweryfikowanych i poprawionych. W tej turze nie znaleziono nowego, dodatkowego źródła
cenowego wykraczającego poza to co już wykorzystano — bez zmian.

**OK — bez zastrzeżeń.**

---

## Can-Am ATV — status

**14 pojazdów w katalogu** (8 bez `myYear`, 6 z `myYear:2027`).

Oficjalna struktura MY2027 wg can-am.brp.com/off-road/atv.html oraz komunikatu prasowego BRP
("Can-Am Unveils 2027 Side-by-Side and All-Terrain Vehicles"): rodzina Outlander (Outlander
Electric, Outlander PRO, Outlander 6x6, Outlander 500/700, Outlander 1000/1000R) oraz Renegade.
Na poziomie trimów (dealerzy US, np. daxpowersports.com) potwierdzone istnienie m.in.: Outlander
MAX XT-P, Outlander MAX Backcountry, Outlander MAX Limited, Outlander MAX DPS, Outlander XT.

**BRAKUJĄCE MODELE/WARIANTY (potencjalne, wymaga potwierdzenia):**
- **Outlander MAX Limited** i **Outlander MAX Backcountry** — oficjalne, osobno nazwane trimy
  wysokiej specyfikacji (10,25" wyświetlacz, GPS, zawieszenie Smart-Shox na wybranych wersjach)
  potwierdzone u dealerów US (daxpowersports.com — "Outlander MAX XT 700", forum can-amforum.com).
  Katalog ma generyczne karty `canam-outlander-max` i `canam-outlander-max-pro`, ale **nie ma
  osobnej pozycji dla "Limited" ani "Backcountry"** jako nazwanych wariantów wykończenia — podobny
  wzorzec do braków znalezionych wcześniej w kategorii SSV (Traxter X MR itd., gdzie generyczna
  karta nie pokrywała wszystkich nazwanych trimów). **Nie jest to pewne** — katalog może celowo
  używać uproszczonej struktury "rodzina + zakres cen" zamiast pełnej listy trimów (tak jak inne
  kategorie w tym serwisie) — wymaga decyzji właściciela strony, czy to ma być pełny odpowiednik
  cennika importera, czy uproszczony katalog marketingowy.
  Źródło: daxpowersports.com (oferta "Can-Am Outlander MAX XT 700 2027"), can-amforum.com wątek
  "Outlander 700 MAX DPS vs Outlander 700 MAX XT".
- **Outlander XT** (non-MAX, wersja z 10,25" ekranem/GPS) — potwierdzona jako osobno
  komunikowana nowość MY2027 (dotyczy XT i Backcountry z nowym ekranem), ale katalog nie ma
  osobnej karty "Outlander XT" — jest tylko generyczny `canam-outlander` (silnik "500/700/850/
  1000R") i `canam-outlander-xtp` (XT-P, inny trim performance). Do potwierdzenia, czy to
  faktycznie brakujący SKU, czy mieści się pod istniejącą generyczną kartą.

**Renegade — bez zmian, potwierdzone.** BRP oficjalnie NIE wprowadził nowej generacji Renegade na
MY2027 (autoevolution.com, atvconnection.com forum) — obecne silniki 650/1000R pozostają aktualne,
zgodne z kartami `canam-renegade` i `canam-renegade-2027` w katalogu. Brak żadnego nowego wariantu
do dodania.

**CENY DO WERYFIKACJI:** ceny ATV 2027 były już zweryfikowane i częściowo zaktualizowane w
poprzedniej turze (`TODO-rocznik-2027.md`, sekcja "cennik importera dla ATV i SSV 2027",
PerfectMoto.pl/Taurus Sea Power) — 4 z 14 pozycji poprawione. Pozostałe pozycje (m.in.
`canam-outlander-pro-2027`, `canam-outlander-max-6x6-dps-2027`) już wcześniej świadomie
pozostawione bez zmian z powodu niejednoznacznego mapowania trimów — potwierdzam tę decyzję, nie
znaleziono w tej turze nowego, jednoznacznego źródła rozstrzygającego.

---

## Can-Am elektryczne — status

**4 pojazdy w katalogu**: `canam-pulse` (Pulse), `canam-origin` (Origin), `canam-outlander-electric`
(Outlander Electric), `canam-outlander-max-electric` (Outlander MAX Electric) — żaden nie ma
`myYear:2027` w kodzie (wszystkie traktowane jako "bieżący" rocznik bez oznaczenia).

Oficjalna oferta elektryczna BRP: motocykle **Can-Am Pulse** i **Can-Am Origin** (linia on-road,
wprowadzone jako MY2025/2026, kontynuowane) oraz ATV **Outlander Electric** i **Outlander MAX
Electric** (linia off-road, potwierdzona kontynuacja na MY2027 na can-am.brp.com/off-road/.../
outlander-electric.html). Nie znaleziono żadnego dodatkowego, nowego modelu elektrycznego BRP
(np. nie istnieje elektryczny SSV ani elektryczny Spyder/Ryker na dziś).

**BRAKUJĄCE MODELE/WARIANTY:** brak. Wszystkie 4 istniejące, oficjalne produkty elektryczne BRP
mają odpowiednik w katalogu. Jedyna niepewność: czy Pulse/Origin powinny mieć w kodzie
`myYear: 2027` (na oficjalnej stronie can-am.brp.com nadal figurują jako aktualna oferta, bez
jawnego rocznika w URL) — kwestia kosmetyczna/techniczna, nie brak modelu.

**CENY DO WERYFIKACJI:** nie znaleziono żadnego polskiego dealerskiego cennika obejmującego
Origin/Pulse (fanjet.pl, brpbroker.pl — brak publicznych cenników elektrycznych motocykli;
motogen.pl ma tylko dane techniczne/recenzję, bez aktualnego cennika 2027). Zgodnie z zasadą
"nie zgaduj" — **nie znaleziono źródła cenowego**, ceny 16 899 €/17 499 €/18 990 €/20 560 €
pozostają niesprawdzone w tej turze.

**OK — bez zastrzeżeń** co do kompletności modelowej.

---

## Podsumowanie

Sprawdzono łącznie **75 pojazdów** w 4 kategoriach: Sea-Doo (34), Can-Am trójkołowce (23), Can-Am
ATV (14), Can-Am elektryczne (4). Nie znaleziono żadnego jednoznacznie brakującego modelu/wariantu
silnikowego w kategoriach Sea-Doo, trójkołowce i elektryczne — katalog jest kompletny względem
oficjalnej oferty BRP na MY2027. W kategorii ATV znaleziono **2 potencjalne braki wymagające
decyzji właściciela** (nazwane trimy Outlander MAX Limited/Backcountry oraz osobny Outlander XT) —
niepewne, bo katalog może celowo stosować uproszczoną strukturę "rodzina + zakres cen" zamiast
pełnej listy trimów dealerskich. Weryfikacja cen: **nie znaleziono jednoznacznego polskiego
źródła cenowego** dla Sea-Doo ani dla linii elektrycznej (Origin/Pulse) — ceny tych dwóch
kategorii pozostają niesprawdzone; ceny trójkołowców i ATV były już zweryfikowane/zaktualizowane
w poprzednich turach audytu i nie wymagały dalszych zmian w tej turze. Łącznie: **0 potwierdzonych
błędów, 2 niepewne punkty do decyzji właściciela, 2 kategorie bez znalezionego źródła cenowego**
(sam brak źródła nie jest błędem — to jawnie oznaczony stan "do weryfikacji").
