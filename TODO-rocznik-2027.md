# TODO — dodanie rocznika 2027 (54 pojazdy)

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
- [x] Explorer Pro → użyj zdjęć z „Explorer Pro 170/230"
- [x] GTR → użyj zdjęć z „GTR 230"
- [x] GTR-X 300 → użyj tych samych zdjęć „GTR-X 300"
- [x] ~~Wake Pro → użyj zdjęć z „Wake Pro 230"~~ **PRZENIESIONE do NOWE — kolor 2027 (turkus/limonka) różni się od obecnego (Sand/Dazzling Blue), zdjęcie już dostarczone**
- [x] FishPro Sport → użyj zdjęć z „FishPro Sport 170"

**Trójkołowce (6):**
- [x] Spyder F3 → zdjęcia zbliżone do „Spyder F3 S" (baza)
- [x] Spyder F3 Limited → użyj zdjęć z „Spyder F3 LTD"
- [x] Spyder RT → zdjęcia zbliżone do „Spyder RT LTD" (baza)
- [x] Spyder RT Sea-to-Sky → użyj tych samych zdjęć
- [x] Canyon → użyj zdjęć z „Canyon STD"
- [x] Canyon Redrock → użyj tych samych zdjęć

**ATV (4):**
- [x] Outlander → użyj tych samych zdjęć
- [x] Outlander MAX 6x6 DPS → użyj zdjęć z „Outlander MAX 6x6"
- [x] Outlander Pro → użyj zdjęć z „Outlander PRO"
- [x] Renegade → użyj tych samych zdjęć

**SSV (3):**
- [x] Maverick Trail → użyj tych samych zdjęć
- [x] Maverick Sport → użyj tych samych zdjęć
- [x] Maverick R → użyj tych samych zdjęć

**Electric (1):**
- [x] Outlander Electric → już jest w katalogu, tylko zweryfikuj specyfikację/cenę MY27

---

## ⚠️ VERIFY — prawdopodobnie to samo, ale sprawdź źródłowe zdjęcie przed reuse (7)

- [ ] **RXP-X** — POTWIERDZONE: nowy kolor pomarańczowo-czarny, różni się od obecnego
  (Gulfstream Blue / Ice Metal-Manta Green) — zdjęcia dostarczone, ale ⚠️ w folderze
  klienta były 2 komplety podpisane jako RXP-X, zero jako RXT-X — do wyjaśnienia
- [ ] **RXT-X** — ⚠️ BRAK prawdziwego zdjęcia — plik podpisany „rxtx" w folderze klienta
  okazał się być zdjęciem RXP-X (błędna nazwa pliku). Trzeba dociągnąć właściwe zdjęcie
  RXT-X 2027 (niebiesko-stalowy kadłub ze złotym napisem widziany w innym pliku, ale
  ten był podpisany jako „gtx limited" — też źle nazwany)
- [ ] **Maverick X3** — na stronie NIE MA dokładnie tej nazwy (jest tylko „Maverick"/
  „Maverick MAX") — ustal czy to ten sam pojazd pod inną nazwą, czy faktycznie brakujący model
- [ ] **Defender/Traxter HD7** — na stronie jest tylko generyczny „Traxter" bez rozbicia
  na warianty mocy — ustal który zdjęcie odpowiada temu wariantowi
- [ ] **Defender/Traxter HD9** — jw.
- [ ] **Defender/Traxter HD10** — jw., ewentualnie odpowiada „Traxter PRO"
- [ ] **Defender/Traxter MAX** — sprawdź czy to „Traxter MAX" ze strony, czy nowa generacja HD11

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
