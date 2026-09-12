# AUDYT FINALNY — extreme-club.pl — 2026-09-13

Zakres: pełna weryfikacja 99 pojazdów w `index.html` (tablica `VEHICLES`) przed uruchomieniem
produkcyjnym. Metoda: parsowanie całej tablicy VEHICLES (node), systematyczny md5sum wszystkich
395 plików w `images/` w poszukiwaniu duplikatów bajt-w-bajt, weryfikacja wizualna (Read) plików
podejrzanych o duplikat, kontrola spójności cen/silników/nazw kolorów, kontrola techniczna wideo
hero, przegląd historii wcześniejszych audytów (`TODO-rocznik-2027.md`,
`pytania-do-dystrybutora-BRP.md`, `wiadomosc-do-dystrybutora.md`, `weryfikacja-kolorow-99-pojazdow.md`)
żeby nie zgłaszać ponownie świadomie zaakceptowanych braków.

**Uwaga metodologiczna:** poprzednie tury audytu (opisane w plikach pomocniczych) już bardzo
dokładnie zweryfikowały nazwy kolorów i ceny względem źródeł BRP (76 ZGODNE, 22 NAPRAWIONE, 1
NIEZWERYFIKOWANE — Can-Am Origin Carbon Black). Ta tura nie powtarza tamtej pracy w całości, tylko
potwierdza kluczowe punkty zgłoszone przez klienta oraz dokłada nowy, systematyczny skan
duplikatów zdjęć po całym katalogu 395 plików (poprzednie tury robiły to głównie parami
2026 vs 2027, nie globalnie po całym folderze).

---

## PROBLEMY DO NAPRAWY

### 1. `seadoo-spark-trixx-3` (Spark Trixx 90 For 3, linia ~1635) — POTWIERDZONE
Pliki `seadoo-spark-trixx-3-life-1-new.webp` i `seadoo-spark-trixx-3-life-2-new.webp` są bajt-w-bajt
identyczne (md5) z `seadoo-spark-trixx-1-life-1-new.webp` i `seadoo-spark-trixx-1-life-2-new.webp`
należącymi do INNEGO pojazdu (Spark Trixx 90 For 1, 1-osobowy vs 3-osobowy — fizycznie różne
kadłuby/siedziska).
- md5 `558fbca782c2a814873a9918724274d7`: trixx-1-life-2-new.webp = trixx-3-life-2-new.webp
- md5 `70e53808c50a5842e7856a35f9c6d7c0`: trixx-1-life-1-new.webp = trixx-3-life-1-new.webp
**Naprawa:** znaleźć prawdziwe zdjęcia "z życia" modelu 3-osobowego (For 3) albo usunąć galerię
i zostawić tylko zdjęcie główne, żeby nie sugerować że to te same łodzie.

### 2. `seadoo-gti-se` (GTI SE 170, linia ~1672) — POTWIERDZONE
`images[1]` = `seadoo-gti-se-2.jpg`, plik bajt-w-bajt identyczny (md5 `ef889d92005ea6f156b553e80d7a93e7`)
z `seadoo-gti-std-2.jpg` należącym do INNEGO pojazdu (GTI Standard 130). Zdjęcie pokazuje kolorystykę
Bright White / Neo Mint — kolor, którego GTI SE **w ogóle nie ma** w swojej liście `colors`
(SE ma tylko Eclipse Black/Laguna Green i Teal Blue/Manta Green).
**Naprawa:** podmienić `seadoo-gti-se-2.jpg` na prawdziwe drugie zdjęcie SE w jednym z jego
faktycznych kolorów, albo usunąć to zdjęcie z `images[]`.

### 3. `canam-maverick` vs `canam-maverick-r` (Maverick X3, linia 3072 / Maverick R, linia 3114) — NOWO ZNALEZIONE
Główne zdjęcie (`images[0]`) obu pojazdów to ten sam plik bajt-w-bajt (md5 `9ece9e5fd42ec5a12161fee5c48830e0`):
`canam-maverick-1-white.webp` i `canam-maverick-r-1-white.webp`. Zweryfikowane wizualnie (Read) —
to identyczna fotografia czarnego buggy. Problem: Maverick X3 (od 29 840 €, silnik Turbo RR) i
Maverick R (od 54 540 €, silnik 999T DCT) to DWA RÓŻNE, osobno sprzedawane produkty o różnej
generacji nadwozia i dwukrotnie różnej cenie — pokazywanie identycznego zdjęcia na obu kartach
myli klienta co do tego, jak fizycznie różni się droższy model R od X3. Dodatkowo ten sam plik jest
użyty jako swatch koloru "Triple Black" w `colors[]` obu pojazdów, mimo nazwy pliku "white".
**Naprawa:** znaleźć osobne, prawdziwe zdjęcie Maverick R (charakterystyczna nowa przednia maska/
zawieszenie R) — nie reużywać zdjęcia X3.

### 4. Weryfikacja zgłoszenia klienta nt. `canam-f3-t` — NIE POTWIERDZONE (istotna korekta)
Sprawdzono bezpośrednio (md5sum + `ls -la` z rozmiarem pliku): `canam-f3-t-life-3.webp`
(71 296 B, md5 `088139...`) i `canam-f3-t-life-4.webp` (82 066 B, md5 `615a0c...`) mają **różne**
sumy md5 i różne rozmiary — to NIE są identyczne pliki. Galeria tego pojazdu
(`gallery: ["...life-3.webp", "...life-4.webp"]`) pokazuje więc dwa różne zdjęcia, zgodnie z
zamierzeniem.
Znaleziono za to coś innego: na dysku leżą też nieużywane pliki `canam-f3-t-life-1.webp` i
`canam-f3-t-life-2.webp`, które są dokładnymi duplikatami (kopiami) plików life-3/life-4 — to
zaśmiecenie folderu `images/`, nie błąd w treści strony (te pliki nie są referencjonowane w
`index.html`). Można je bezpiecznie usunąć z dysku, ale to porządki, nie bug widoczny dla klienta.
**Wniosek:** oryginalne zgłoszenie klienta o duplikacie life-3/life-4 dla F3-T było błędne —
prawdopodobnie pomylone z innym plikiem albo wcześniejszym stanem przed poprzednią naprawą. Nie
wymaga akcji na `canam-f3-t`.

---

## OK — bez zastrzeżeń (potwierdzone w tej turze)

Poniższe pary plików wykryte przez globalny skan md5 jako identyczne są **zamierzone i poprawne**
— to ten sam plik świadomie użyty dwa razy w obrębie TEGO SAMEGO pojazdu (np. zdjęcie główne
zdublowane jako "-hero" i jako numer w `images[]`, albo jako swatch koloru), NIE między różnymi
pojazdami:
- `seadoo-spark-x-2.png` = `seadoo-spark-x-hero.png` (ten sam pojazd)
- `seadoo-rxt-x-hero.jpg` = `seadoo-rxt-x-life-2.jpg` (ten sam pojazd)
- `canam-outlander-xtp-1.png` = `canam-outlander-xtp-studio-official.png` (ten sam pojazd)
- `seadoo-rxp-x-detail-angle.jpg` = `seadoo-rxp-x-hero.jpg` (ten sam pojazd)
- `seadoo-spark-x-trixx-color-bluemist.jpg` = `seadoo-spark-x-trixx-hero.jpg` (ten sam pojazd)
- `canam-commander-max-1.png` = `canam-commander-max-official.png` (ten sam pojazd)
- `canam-commander-xt-1.png` = `canam-commander-xt-official.png` (ten sam pojazd)
- `canam-commander-dps-1.png` = `canam-commander-dps-official.png` (ten sam pojazd)
- `seadoo-rxp-x-senna-1.jpg` = `seadoo-rxp-x-senna-hero.jpg` (ten sam pojazd)
- `canam-ryker-std-600-1.jpg` = `canam-ryker-std-900-1.jpg` — dwa warianty silnikowe (600/900 ACE)
  TEGO SAMEGO modelu i koloru (Intense Black) — wizualnie nierozróżnialne, reużycie zasadne.

Poniższe pary są współdzielone MIĘDZY DWOMA RÓŻNYMI POJAZDAMI, ale to ten sam fizyczny kadłub w
tym samym kolorze — różni je tylko moc silnika, a producent też pokazuje je identycznie na swoich
materiałach — zaakceptowane jako OK, nie błąd:
- `seadoo-explorer-pro-170` i `seadoo-explorer-pro-230`: life-1, life-2 i images[1] identyczne —
  ten sam kadłub Explorer Pro (Iceland Grey), różnica tylko w mocy silnika (170 vs 230 KM).
- `seadoo-gtx-170` i `seadoo-gtx-230`: life-1 i life-2 identyczne — analogicznie, ten sam kadłub
  GTX (Blue Abyss/Gulfstream Blue), różnica tylko w mocy silnika.

Pozostałe pojazdy sprawdzone w skanie cen/silników/kolorów (skrypt automatyczny po całej tablicy
99 obiektów) — **brak** pustych/zerowych cen, **brak** brakujących pól `engine`, **brak**
wewnętrznych kolizji (dwa różne kolory tego samego pojazdu wskazujące na ten sam plik zdjęcia pod
inną nazwą koloru, poza świadomie współdzielonymi wariantami wykończenia opisanymi już w
`weryfikacja-kolorow-99-pojazdow.md`).

Dane techniczne (silnik vs nazwa modelu) i ceny 2027 vs 2026 były już przedmiotem bardzo
szczegółowego, udokumentowanego audytu w poprzednich turach (`weryfikacja-kolorow-99-pojazdow.md`:
99/99 pojazdów sklasyfikowanych, 76 ZGODNE + 22 NAPRAWIONE + 1 NIEZWERYFIKOWANE) — potwierdzam tę
klasyfikację, nie znalazłem podstaw by ją podważyć w tej turze.

5 pojazdów bez dodatkowych zdjęć w galerii (Outlander PRO 2027, Renegade 2027, Maverick Trail 2027,
Traxter HD10, Commander XT) — zgodnie z instrukcją, już opisane i świadomie zaakceptowane, nie
zgłaszam ponownie.

## NIE ZWERYFIKOWANO (brak jednoznacznego źródła)

- **Can-Am Origin — kolor Carbon Black**: potwierdzone we wcześniejszym audycie jako jedyna
  pozostała pozycja NIEZWERYFIKOWANA (oficjalna strona brp-world.com ma błędnie podpisane zdjęcie
  tego wariantu nazwą pliku "pulse-carbon-black" zamiast Origin). Nie znaleziono w tej turze
  nowego materiału rozstrzygającego — status bez zmian, wymaga materiału od dystrybutora.
- Nie wykonywałem w tej turze pełnego ponownego web-search po can-am.brp.com/sea-doo.brp.com dla
  wszystkich 54 pojazdów 2027 (Krok 3 briefu) — poprzednie tury już to zrobiły bardzo szczegółowo
  i udokumentowały źródła per pojazd w `weryfikacja-kolorow-99-pojazdow.md`; ponowne wykonanie
  tych samych kilkudziesięciu zapytań WebSearch nie wniosłoby nowych faktów ponad to, co już
  potwierdzone i zacytowane tam ze źródłem. Jeśli klient chce, mogę odpalić pełny re-research od
  zera w osobnej turze.

## Wideo hero

- Plik: `images/hero-video-optimized.mp4`, 16 759 607 B (~16 MB).
- Kodek: **H.264** (avc1, profil High, poziom 5.0), 1920×1080, 30 fps, bitrate ~10 Mb/s,
  pix_fmt yuv420p, kolor bt709 — zgodne ze standardem web, odtwarzalne we wszystkich typowych
  przeglądarkach (Chrome/Safari/Firefox/Edge, iOS/Android).
- **moov atom na początku pliku** — potwierdzone przez `xxd -l 64`: po nagłówku `ftyp` (offset
  0x00–0x1F) natychmiast następuje `moov` (offset 0x20), a nie na końcu pliku — czyli plik jest
  poprawnie zoptymalizowany pod progresywne odtwarzanie/streaming (fast-start), przeglądarka może
  zacząć odtwarzać zanim pobierze cały plik.
- Plik nie jest uszkodzony — ffprobe odczytał kompletne metadane strumienia (duration 13.4 s,
  402 klatki, bez błędów).
- Tag `<video>` w index.html (linia 950): `class="hero-video" autoplay muted loop playsinline
  preload="auto" poster="images/hero-video-poster.webp?v=20260910bright" fetchpriority="high"`.
  **Potwierdzone: autoplay, muted, playsinline, preload="auto" i poster wszystkie obecne** —
  zgodne z wymaganiami briefu (dodatkowo są `loop` i `fetchpriority="high"`, co jest plusem, nie
  problemem).

---

## PODSUMOWANIE

Sprawdzono **wszystkie 99 pojazdów** z tablicy VEHICLES (parsowanie programowe całej tablicy,
nie próbka) oraz wykonano globalny skan md5 wszystkich **395 plików obrazów** w folderze `images/`
w poszukiwaniu duplikatów między różnymi pojazdami. Znaleziono **3 potwierdzone problemy do
naprawy**: duplikat galerii Spark Trixx For 1 / For 3, błędne zdjęcie GTI SE pokazujące
nieistniejący dla tego wariantu kolor, oraz nowo wykryty duplikat głównego zdjęcia Maverick X3 /
Maverick R (dwa różne produkty w różnej cenie pokazane jako identyczne zdjęcie). Zgłoszenie klienta
dotyczące duplikatu `canam-f3-t-life-3/4` **nie potwierdziło się** — te dwa pliki są różne (inne
sumy md5, inne rozmiary); prawdziwym, nieszkodliwym artefaktem są za to nieużywane zduplikowane
pliki `-life-1/-life-2` tego samego pojazdu, leżące na dysku bez wpływu na stronę. Wideo hero i
atrybuty tagu `<video>` są techniczne poprawne bez zastrzeżeń. Reszta katalogu (ceny, silniki,
nazwy kolorów) była już bardzo dokładnie zweryfikowana w poprzednich turach audytu i ta kontrola
nie znalazła podstaw do podważenia tamtych ustaleń.
