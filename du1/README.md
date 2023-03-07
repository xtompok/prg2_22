# GTFS a nejfrekventovanější mezizastávkový úsek

## Zadání

Implementujte program, který načte jízdní řády z formátu [GTFS](https://developers.google.com/transit/gtfs/reference) a urči
nejfrekventovanější mezizastávkový úsek. 

Program bude reprezentovat jako objekty jednotlivé prvky alespoň následujících
souborů:
  - [`stops.txt`](https://developers.google.com/transit/gtfs/reference#stopstxt)
  - [`stop_times.txt`](https://developers.google.com/transit/gtfs/reference#stop_timestxt)
  - [`trips.txt`](https://developers.google.com/transit/gtfs/reference#tripstxt)
  - [`routes.txt`](https://developers.google.com/transit/gtfs/reference#routestxt)

Pro každý soubor bude existovat jemu odpovídající třída, každý prvek daného
souboru bude instancí dané třídy. Vzájemné vazby mezi objekty by měly být
zachovány pomocí referencí, tedy z objektu třídy `StopTime` se přes atribut `trip`
přejde na odpovídající objekt třídy `Trip`. 

Program by dále měl obsahovat třídu `StopSegment` reprezentující mezizastávkový
úsek s atributy `from` a `to` reprezentující výchozí a cílovou zastávku daného
úseku a dále atribut `trips` obsahující seznam objektů typu `Trip`
projíždějících přes daný mezizastávkový úsek v daném směru. Pro účely programu
bereme každý směr zvlášť. 

Program může předpokládat, že ve stejné složce jako je on sám je složka `gtfs/`
obsahující jednotlivé `.txt` soubory, program by je měl sám všechny načíst.

Program po načtení všech požadovaných vstupních souborů a vytvoření požadovaných
objektů program vypíše pět nejfrekventovanějších meizastávkových úseků (podle
počtu tripů, které přes něj vedou) a tyto úseky vypíše na výstup v pořadí od
nejfrekventovanějších po nejméně frekventované. Vypíše vždy jméno počáteční
zastávky, jméno koncové zastávky a počet spojů (trips) daným úsekem
projíždějících.

Základní verze cíleně ignoruje [`calendar.txt`](https://developers.google.com/transit/gtfs/reference#calendartxt) a [`calendar_dates.txt`](https://developers.google.com/transit/gtfs/reference#calendar_datestxt
), tudíž
budou výsledky zkreslené. Pro základní verzi je to v pořádku.

### Dokumentace
K aplikaci dodejte stručnou uživatelskou a vývojářskou dokumentaci a objektový
návrh, ve kterém popíšete architekturu aplikace - která třída drží jaká data a
jak jsou spolu propojeny. Propojení můžete znázornit i graficky (např. pomocí
UML např. v nástroji [Draw.io](https://app.diagrams.net/)). 

## Doporučení
Data si stáhněte z
[http://data.pid.cz/PID_GTFS.zip](http://data.pid.cz/PID_GTFS.zip).

Nejprve si nakreslete, jak bude architektura aplikace vypadat a jak se budou
předávat data a pak teprve programujte. Rozdělte si jednotlivé funkční celky
mezi sebe a domluvte se na rozhraní mezi nimi.

Využijte slovníků jako "slovníků", tedy můžete například držet id jako klíče a
jim odpovídající objekty jako hodnoty. Využijte toho, že klíčem může být i
n-tice.

Pro načítání GTFS souborů využijte modul [`csv`](https://docs.python.org/3/library/csv.html). Pro čitelnější načítání odolné
proti změnám pořadí sloupců se vám může hodit [`DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader).

Jednotlivé `.txt` soubory nedávejte do Gitu.

Pokud se vám něco nebude dařit, zkonzultujte to s ostatními ve skupině, pokud si
stále nebudete vědět rady, nebojte se ozvat, rád vám pomohu.

## Odevzdání
Odevzdávat budete zdrojové soubory a soubor(y) s dokumentací. Data o jízdních
řádech nejsou součástí odevzdání, dodám si vlastní do složky `gtfs`. Odevzdávejte
ideálně přes GitHub nebo podobnou službu, případně je možné poslat i vše
zabalené v zipu.

Deadline na odevzdání je 26. 3. 2022 v 8.03. Úkoly odeslané po deadlinu budou
brány jako neodevzdané. Pokud odevzdáte úkol vícekrát, budu hodnotit poslední
odevzdání před deadlinem.  Každému, kdo mi pošle úkol, odpovím, že jsem ho
přijal a že se mi podařilo zip rozbalit. Pokud neodpovím, urgujte.

### Předčasné odevzdání
Pokud odevzdáte úkol dopředu, zkusím se na něj podívat a napsat vám případné
nedostatky. Tato možnost není garantovaná, ale budu se snažit odbavovat úkoly co
nejrychleji. Zaručuji vám pouze to, že na úkoly se budu dívat v tom pořadí, v
jakém mi budou doručeny. Rovněž nezaručuji, že najdu v programu všechny chyby
napoprvé, tudíž pokud si nějaké nevšimnu, není to garance, že máte program
správně, závazné je pouze hodnocení po deadlinu. Pokud budete odevzdávat přes
GitHub, chyby vám vystavím jako Issue.

## Bodování
  * 4 b za funkční aplikaci
  * 3 b za kvalitu kódu
  * 3 b za dokumentaci

## Bonusové body

### Automatizovaná příprava dat (1 b)
Kromě aplikace samotné připravíte i skript, který stáhne aktuální jízdní řády a
rozbalí je do složky `gtfs/`. Využijte modulů `requests` a `zipfile`. Skript
může, ale nemusí, být součástí aplikace.

### Uvažování kalendáře pro výpočet (1 -- 2 b)
Program vezme jako první parametr (v `sys.argv[1]`) datum ve formátu
`DD.MM.YYYY` a bude uvažovat pouze spoje jedoucí daný den. Využijte modulu
[`datetime`](https://docs.python.org/3/library/datetime.html), ve variantě za 1 bod uvažujte pouze informace uvedené v
[`calendar.txt`](https://developers.google.com/transit/gtfs/reference#calendartxt), ve variantě za 2 body uvažujte navíc i seznam výjimek ze souboru
[`calendar_dates.txt`](https://developers.google.com/transit/gtfs/reference#calendar_datestxt).

### Výpis linek ve výstupech (1 b)
Při výpisu výstupů vypište kromě celkového počtu spojů projíždějících daným
úsekem i seznam čísel (jmen) linek daným úsekem projíždějících setříděný rozumně (alespoň dle abecedy).
