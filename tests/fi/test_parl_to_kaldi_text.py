"""Test text preprocessing for Finnish."""
from typing import Tuple

import pytest

import aalto_asr_preprocessor.fi.parl_to_kaldi_text as recipe
import aalto_asr_preprocessor.preprocessor as prep


def test_unaccepted_chars() -> None:
    """Test that UnacceptedCharsError is raised when input text contains unknown characters.

    Translation mapping is intentionally left out to ensure the test characters are unknown.
    """
    with pytest.raises(prep.UnacceptedCharsError):
        prep.apply("éΩ∂πß∑∆", recipe.REGEXPS, recipe.UNACCEPTED_CHARS)


@pytest.mark.parametrize(
    "parl_to_kaldi_test_pairs",
    [(0), (1), (2), (3), (4), (5), (6), (7), (8), (9), (10)],
    indirect=True,
)
def test_kaldi_preprocessor_with_long_text(
    parl_to_kaldi_test_pairs: Tuple[str, str]
) -> None:
    """Test preprocessing recipe for preprocessing long text input into kaldi text file."""
    input_text, true_result = parl_to_kaldi_test_pairs
    result = prep.apply(
        input_text, recipe.REGEXPS, recipe.UNACCEPTED_CHARS, recipe.TRANSLATIONS
    )
    assert result == true_result


@pytest.mark.parametrize(
    "input_text, true_result",
    [
        ("unkarilainen Ádám Kósa", "unkarilainen adam kosa"),
        ("tuttuja autoja, kuten Škoda,", "tuttuja autoja kuten skoda"),
        ("Comme ça ja niin edelleen.", "comme ca ja niin edelleen"),
        ("tv-yhtiön RÚV:n resursseja", "tv yhtiön ruvn resursseja"),
        ("kuin à la Caruna", "kuin a la caruna"),
        ("on hieman déjà-vu‑olo.", "on hieman deja vu olo"),
        ("1—3-lapsisten perheiden", "yksi viiva kolme lapsisten perheiden"),
        ("1.—3.-luokkalaisten määrä", "ykkös viiva kolmas luokkalaisten määrä"),
        ("takasi 9.-luokkalaisille jatkon", "takasi yhdeksäs luokkalaisille jatkon"),
        (
            "1 000-1 500:ssa pyörivien",
            "tuhannessa viiva tuhannessaviidessäsadassa pyörivien",
        ),
        ("0-asteinen huone", "nolla asteinen huone"),
        (
            "0,4-hoitajamitoituksella näin",
            "nolla pilkku neljä hoitajamitoituksella näin",
        ),
        (
            "0—30-tuntisesta sopimuksesta",
            "nolla viiva kolmekymmentä tuntisesta sopimuksesta",
        ),
        ("0—6-vuotiaiden", "nolla viiva kuusi vuotiaiden"),
        ("65-vuotiaitten", "kuusikymmentäviisi vuotiaitten"),
        ("30—40-vuotiaiden", "kolmekymmentä viiva neljäkymmentä vuotiaiden"),
        ("40-sivuinen", "neljäkymmentä sivuinen"),
        ("2000-luvulla on", "kaksituhatta luvulla on"),
        ("Helsinki+40‑tavoitteista", "helsinki plus neljäkymmentä tavoitteista"),
        (
            "+40-Ety-kokouksen juhlatilaisuus",
            "plus neljäkymmentä ety kokouksen juhlatilaisuus",
        ),
        ("2+1-mallin", "kaksi plus yksi mallin"),
        ("5+5+5-malli", "viisi plus viisi plus viisi malli"),
        ("P5+1-maiden", "p viisi plus yksi maiden"),
        ("6+1-rytmitykseen", "kuusi plus yksi rytmitykseen"),
        ("1:13‑kriteerin", "yhden suhde kolmeentoista kriteerin"),
        ("7/24-yksiköissä", "seitsemän kautta kaksikymmentäneljä yksiköissä"),
        (
            "24/7-päivystysasioita",
            "kaksikymmentäneljä kautta seitsemän päivystysasioita",
        ),
        ("18/15‑malli on", "kahdeksantoista kautta viisitoista malli on"),
        ("1/13-mitoituksesta", "yksi kautta kolmetoista mitoituksesta"),
        ("10/90-jaosta", "kymmenen kautta yhdeksänkymmentä jaosta"),
        ("1/100-asiaa", "yksi kautta sata asiaa"),
        ("112-applikaatio tuolla", "yksi yksi kaksi applikaatio tuolla"),
        ("EU15-keskiarvoon", "eu viisitoista keskiarvoon"),
        ("Suomi2-opetukseen", "suomi kaksi opetukseen"),
        ("K18-tähtisadetikku", "k kahdeksantoista tähtisadetikku"),
        ("E4-tie", "e neljä tie"),
        ("G20-maat itse", "g kaksikymmentä maat itse"),
        ("5,5-miljoonainen kansa", "viisi pilkku viisi miljoonainen kansa"),
        (
            "1,72-kertaisen maksun",
            "yksi pilkku seitsemänkymmentäkaksi kertaisen maksun",
        ),
        (
            "PM2,5-aktiivihiilisuodatinsuojia",
            "pm kaksi pilkku viisi aktiivihiilisuodatinsuojia",
        ),
        ("8-kertaiset kantaväestöön", "kahdeksan kertaiset kantaväestöön"),
        ("10—20-kertaisia määriä", "kymmenen viiva kaksikymmentä kertaisia määriä"),
        (
            "16—17-vuotiaita nuoria",
            "kuusitoista viiva seitsemäntoista vuotiaita nuoria",
        ),
        ("H5N8-virus", "h viisi n kahdeksan virus"),
        ("ICD-10-tautiluokitukseen", "icd kymmenen tautiluokitukseen"),
        ("NB8-yhteistyö", "nb kahdeksan yhteistyö"),
        ("NEL1-tason", "nel yksi tason"),
        ("P5-rauhanvälitys", "p viisi rauhanvälitys"),
        ("R0-luku", "r nolla luku"),
        ("Ruoka2030-selonteko", "ruoka kaksituhattakolmekymmentä selonteko"),
        ("S400-ilmatorjuntaohjuksen", "s neljäsataa ilmatorjuntaohjuksen"),
        ("SORM-3-järjestelmä", "sorm kolme järjestelmä"),
        ("St1-niminen", "st yksi niminen"),
        (
            "Tahdon2013-kansalaisaloite",
            "tahdon kaksituhattakolmetoista kansalaisaloite",
        ),
        ("TV2-kanava", "tv kaksi kanava"),
        ("F-35-hävittäjän", "f kolmekymmentäviisi hävittäjän"),
        ("F35-hävittäjän", "f kolmekymmentäviisi hävittäjän"),
        ("A4-paperi", "a neljä paperi"),
        ("AM/121-ajokortilla", "am yksi kaksi yksi ajokortilla"),
        ("B-52-koneen", "b viisikymmentäkaksi koneen"),
        (
            "42.7-avunantolausekkeeseen",
            "neljäkymmentäkaksi piste seitsemän avunantolausekkeeseen",
        ),
        (
            "punamulta 2.0:n talouspolitiikka",
            "punamulta kaksi piste nollan talouspolitiikka",
        ),
        (
            "termillä Teollisuus 4.0.” Mutta",
            "termillä teollisuus neljä piste nolla mutta",
        ),
        (
            "Matkailu 4.0 ‑hanketta tuetaan",
            "matkailu neljä piste nolla hanketta tuetaan",
        ),
        ("vuonna 2019:kaan niitä", "vuonna kaksituhattayhdeksäntoistakaan niitä"),
        ("10:ksihän me arvioimme.", "kymmeneksihän me arvioimme"),
        ("että sitä 101:täkään ei enää ole", "että sitä sataayhtäkään ei enää ole"),
        ("lähemmäs 30:täkin monilla", "lähemmäs kolmeakymmentäkin monilla"),
        (
            "Oulussakinhan jo kehitetään 6G:täkin",
            "oulussakinhan jo kehitetään kuusi g täkin",
        ),
        ("jatkuu vielä pitkälle yli 20:n", "jatkuu vielä pitkälle yli kahdenkymmenen"),
        (
            "koskevan noin 10 000:ta yrittäjää",
            "koskevan noin kymmentätuhatta yrittäjää",
        ),
        ("pääsee jostakin 2 000:llakin", "pääsee jostakin kahdellatuhannellakin"),
        (
            "ei mahtunut 12+1:nkään joukkoon",
            "ei mahtunut kahdentoista plus yhdenkään joukkoon",
        ),
        (
            "ja 20:nkin prosentin rahoitusosuus",
            "ja kahdenkymmenenkin prosentin rahoitusosuus",
        ),
        (
            "ja 0,70:ssäkin taitaa olla",
            "ja nolla pilkku seitsemässäkymmenessäkin taitaa olla",
        ),
        ("MTV3:n uutiset", "mtv kolmen uutiset"),
        (
            "AR-15:n 30 patruunan lipas",
            "ar viidentoista kolmenkymmenen patruunan lipas",
        ),
        ("A2:n palkka- ja työillassa", "a kahden palkka ja työillassa"),
        (
            "Vaikka tämä 6Aika-rahoitus nyt loppuisi",
            "vaikka tämä kuusi aika rahoitus nyt loppuisi",
        ),
        ("kuulemma C21-kaupungit", "kuulemma c kaksikymmentäyksi kaupungit"),
        ("ja 5G-aikakaudella lennättää", "ja viisi g aikakaudella lennättää"),
        ("operaattoripohjainen 4G, joka", "operaattoripohjainen neljä g joka"),
        ("tästä Solvenssi II ‑direktiivin", "tästä solvenssi kaksi direktiivin"),
        ("se on IV-liitteessä", "se on neljännessä liitteessä"),
        (
            "käydään klo 16.30:een saakka",
            "käydään kello kuusitoista kolmeenkymmeneen saakka",
        ),
        (
            "12 kuukaudesta 18 kuukauteen",
            "kahdestatoista kuukaudesta kahdeksaantoista kuukauteen",
        ),
        (
            "noin 15—300 sotilasta. Suomen",
            "noin viisitoista viiva kolmesataa sotilasta suomen",
        ),
        ("vuoden 95 leikkauslista", "vuoden yhdeksänkymmentäviisi leikkauslista"),
        (
            "että 1.—3. lakiehdotus hylätään",
            "että ensimmäinen viiva kolmas lakiehdotus hylätään",
        ),
        ("124 EU-maasta on", "sadastakahdestakymmenestäneljästä eu maasta on"),
        (
            "ja myös tässä lain 2 §:ssähän tämä",
            "ja myös tässä lain toisessa pykälässähän tämä",
        ),
        (
            "sen olevan 1.7.17 alkaen",
            "sen olevan ensimmäinen seitsemättä seitsemäntoista alkaen",
        ),
        (
            "ensi vuoden 31.5. saakka.",
            "ensi vuoden kolmaskymmenesensimmäinen viidettä saakka",
        ),
        (
            "on lämmennyt vuoden 90 jälkeen",
            "on lämmennyt vuoden yhdeksänkymmentä jälkeen",
        ),
        (
            "arvioiden mukaan vuonna 24 ne",
            "arvioiden mukaan vuonna kaksikymmentäneljä ne",
        ),
        (
            "niin ikään vuosilomalain 30 §:n ja työaikalain 34 §:n nojalla mainituista asioista",
            "niin ikään vuosilomalain kolmannenkymmenennen pykälän ja työaikalain "
            "kolmannenkymmenennenneljännen pykälän nojalla mainituista asioista",
        ),
        (
            "voimassa vuoden 20 loppuun saakka. On hyvä",
            "voimassa vuoden kaksikymmentä loppuun saakka on hyvä",
        ),
        (
            "suunnitelma vuosille 2021—24 onkin",
            "suunnitelma vuosille kaksituhattakaksikymmentäyksi viiva kaksikymmentäneljä onkin",
        ),
        (
            "valmiuteen vuoden 24 tai 25 aikana",
            "valmiuteen vuoden kaksikymmentäneljä tai kaksikymmentäviisi aikana",
        ),
        (
            "päätökseen, vuodelta 18. Tuota päätöstä",
            "päätökseen vuodelta kahdeksantoista tuota päätöstä",
        ),
        (
            "nousi viime vuoden 50 000:sta 70 000:een lehtitietojen mukaan",
            "nousi viime vuoden viidestäkymmenestätuhannesta seitsemäänkymmeneentuhanteen "
            "lehtitietojen mukaan",
        ),
        (
            "äänin 151—27 hyväksymästä suorasta",
            "äänin sataviisikymmentäyksi viiva kaksikymmentäseitsemän hyväksymästä suorasta",
        ),
        (
            "pudotus 20 prosentista 10 prosenttiin sekä",
            "pudotus kahdestakymmenestä prosentista kymmeneen prosenttiin sekä",
        ),
        (
            "korotettaisiin 32,13 prosentista 42,13 prosenttiin ja",
            "korotettaisiin kolmestakymmenestäkahdesta pilkku kolmestatoista prosentista "
            "neljäänkymmeneenkahteen pilkku kolmeentoista prosenttiin ja",
        ),
        (
            "ja 16 maasta vähiten: Suomi, 3,3 per 100 000 asukasta",
            "ja kuudestatoista maasta vähiten suomi kolme pilkku kolme per satatuhatta asukasta",
        ),
        (
            "eli vuosien 25—28 valtakunnallisista",
            "eli vuosien kaksikymmentäviisi viiva kaksikymmentäkahdeksan valtakunnallisista",
        ),
        (
            "tästä 20—30 prosentista, tai",
            "tästä kahdestakymmenestä viiva kolmestakymmenestä prosentista tai",
        ),
        (
            "päiväjärjestyksen 3.—6. asiasta.",
            "päiväjärjestyksen kolmannesta viiva kuudennesta asiasta",
        ),
        (
            "muutaman kilometrin päästä St1:n bensa-aseman viereisestä kraanasta.",
            "muutaman kilometrin päästä st yhden bensa aseman viereisestä kraanasta",
        ),
        (
            "Me tarvitsemme EU27:lle selkeän oman eteenpäinmenostrategian",
            "me tarvitsemme eu kahdellekymmenelleseitsemälle selkeän oman eteenpäinmenostrategian",
        ),
        (
            "esimerkiksi G20:n, OECD:n ja EU:n johdolla",
            "esimerkiksi g kahdenkymmenen oecdn ja eun johdolla",
        ),
        (
            "tässä mietittiin COVID-19:n, koronan, vaikutusta",
            "tässä mietittiin covid yhdeksäntoista koronan vaikutusta",
        ),
        (
            "Leopard 2A6 ‑taistelupanssarivaunuhankinta",
            "leopard kaksi a kuusi taistelupanssarivaunuhankinta",
        ),
        (
            "näytteenottopisteestä numero 207A löytynyt",
            "näytteenottopisteestä numero kaksisataaseitsemän a löytynyt",
        ),
        (
            "Tässä 2 500—3 000:ssahan ei ole mukana",
            "tässä kahdessatuhannessaviidessäsadassa viiva kolmessatuhannessahan ei ole mukana",
        ),
        (
            "käytännössä 249 000:tta ihmistä sen takia",
            "käytännössä kahtasataaneljääkymmentäyhdeksäätuhatta ihmistä sen takia",
        ),
        (
            "Kertomus koskee oikeusasiamiesinstituution 99:ttä toimintavuotta.",
            "kertomus koskee oikeusasiamiesinstituution yhdeksättäkymmenettäyhdeksättä "
            "toimintavuotta",
        ),
        (
            "koskisi pääosin tuloluokkia 40 000:sta 60 000:teen euroon vuodessa",
            "koskisi pääosin tuloluokkia neljästäkymmenestätuhannesta kuuteenkymmeneentuhanteen "
            "euroon vuodessa",
        ),
        (
            "ei vaikka olisi hakenut 500:taa työpaikkaa",
            "ei vaikka olisi hakenut viittäsataa työpaikkaa",
        ),
        (
            "suhdeluku lasten ja kasvattajien välillä nousee 1/7:stä 1/8:aan",
            "suhdeluku lasten ja kasvattajien välillä nousee yhdestä per seitsemästä yhteen per "
            "kahdeksaan",
        ),
        (
            "soveltaa ajalla 16.3.—6.7.2020.",
            "soveltaa ajalla kuudestoista kolmatta viiva kuudes seitsemättä "
            "kaksituhattakaksikymmentä",
        ),
        (
            "hallitukselle 18.3.2020 tekemä esitys",
            "hallitukselle kahdeksastoista kolmatta kaksituhattakaksikymmentä tekemä esitys",
        ),
        (
            "Pääjohtaja valitaan kuusivuotiskaudeksi 1.1.2016—31.12.2021.",
            "pääjohtaja valitaan kuusivuotiskaudeksi ensimmäinen ensimmäistä "
            "kaksituhattakuusitoista viiva kolmaskymmenesensimmäinen kahdettatoista "
            "kaksituhattakaksikymmentäyksi",
        ),
        (
            "lakialoitteet 13—23/2019",
            "lakialoitteet kolmetoista viiva kaksikymmentäkolme kautta kaksituhattayhdeksäntoista",
        ),
        (
            "Vuosina 1990—2010 Hollannissa",
            "vuosina tuhatyhdeksänsataayhdeksänkymmentä viiva kaksituhattakymmenen hollannissa",
        ),
        (
            "yläkatto voitaisiin nostaa 2 000—2 500:aankin",
            "yläkatto voitaisiin nostaa kahteentuhanteen viiva kahteentuhanteenviiteensataankin",
        ),
        (
            "Tähän 72,6:eenkin pitää suhtautua niin",
            "tähän seitsemäänkymmeneenkahteen pilkku kuuteenkin pitää suhtautua niin",
        ),
        (
            "52 maan joukossa olemme 31:nen, vielä edellisellä mittausjaksolla 24:s.",
            "viidenkymmenenkahden maan joukossa olemme kolmaskymmenesensimmäinen vielä edellisellä "
            "mittausjaksolla kahdeskymmenesneljäs",
        ),
        (
            "on niin sanottu häviäjien Suomi eli Kehä III:n ulkopuolella oleva Suomi",
            "on niin sanottu häviäjien suomi eli kehä kolmen ulkopuolella oleva suomi",
        ),
        (
            "Itselläni on kokemusta nuoruudesta Datsun 120A F-II:n tuunaamisesta",
            "itselläni on kokemusta nuoruudesta datsun satakaksikymmentä a f kahden tuunaamisesta",
        ),
        (
            "Tässä on kyse siitä, että toimeenpannaan maksupalveludirektiivit III ja IV.",
            "tässä on kyse siitä että toimeenpannaan maksupalveludirektiivit kolme ja neljä",
        ),
        (
            "vuosille 21—24 on hävittäjähankintaan, HX-hankkeeseen, osoitettu 5,5 miljardia euroa",
            "vuosille kaksikymmentäyksi viiva kaksikymmentäneljä on hävittäjähankintaan hx "
            "hankkeeseen osoitettu viisi pilkku viisi miljardia euroa",
        ),
        (
            "kello on 13.30, ja suuren valiokunnan kokouksen",
            "kello on kolmetoista kolmekymmentä ja suuren valiokunnan kokouksen",
        ),
        (
            "viimeistään 3.4.2020 kello 10.",
            "viimeistään kolmas neljättä kaksituhattakaksikymmentä kello kymmenen",
        ),
        (
            "Lähetekeskusteluun varataan 1 tunti, kello 15.00—16.00. Mikäli",
            "lähetekeskusteluun varataan yksi tunti kello viisitoista nolla nolla viiva "
            "kuusitoista nolla nolla mikäli",
        ),
        (
            "momentille 30.40.44 lisätään vastaava määräraha",
            "momentille kolmekymmentä neljäkymmentä neljäkymmentäneljä lisätään vastaava määräraha",
        ),
        (
            "momentille 32.01.49 VTT Oy:n toiminnan",
            "momentille kolmekymmentäkaksi nolla yksi neljäkymmentäyhdeksän vtt oyn toiminnan",
        ),
        (
            "toimintamenojen momentin 32.01.03 määrärahat ovat noin 197 miljoonaa",
            "toimintamenojen momentin kolmekymmentäkaksi nolla yksi nolla kolme määrärahat ovat "
            "noin satayhdeksänkymmentäseitsemän miljoonaa",
        ),
        (
            "yleissopimuksen 3 artiklan 1. kohdan mukaan on",
            "yleissopimuksen kolmannen artiklan ensimmäisen kohdan mukaan on",
        ),
        (
            "lisätään rikoslain 21 lukuun uusi 7a § seuraavasti:",
            "lisätään rikoslain kahteenkymmeneenyhteen lukuun uusi seitsemäs a pykälä seuraavasti",
        ),
        (
            "tämä kyseinen lakikohta. 117 g §:ää muutetaan: siinä puolestaan",
            "tämä kyseinen lakikohta sadattaseitsemättätoista g pykälää muutetaan siinä puolestaan",
        ),
        (
            "on määritelty ulkomaalaislain 39  §:ssä, ja momentista 2 ilmenee, että",
            "on määritelty ulkomaalaislain kolmannessakymmenennessäyhdeksännessä pykälässä ja "
            "momentista kaksi ilmenee että",
        ),
        (
            "Esitän, että sinne lisätään ”Maksukyvyttömyys hylkäysperusteena” 6 b §:ksi eli että "
            "vakuutuksenantaja",
            "esitän että sinne lisätään maksukyvyttömyys hylkäysperusteena kuudenneksi b pykäläksi "
            "eli että vakuutuksenantaja",
        ),
        (
            "Perustuslakihan takaa 7 §:ssään sen, että jokaisella",
            "perustuslakihan takaa seitsemännessä pykälässään sen että jokaisella",
        ),
        (
            "Syyttelyllä tämä asia ei mene eteenpäin. (Eduskunnasta: Rakentava puhe!]",
            "syyttelyllä tämä asia ei mene eteenpäin",
        ),
        (
            "vastaan tähän. (Jukka Gustafsson: Kaipaan sitä vanhaa liittoa!] — No niin, ei",
            "vastaan tähän no niin ei",
        ),
        (
            "[Arvoisa puhemies! Kysymyksessä on siis eduskunnalle annettava tämän vuoden toiseen "
            "lisätalousarvioon liittyvä täydentävä hallituksen esitys.",
            "arvoisa puhemies kysymyksessä on siis eduskunnalle annettava tämän vuoden toiseen "
            "lisätalousarvioon liittyvä täydentävä hallituksen esitys",
        ),
    ],
)
def test_kaldi_preprocessor_with_short_text(input_text: str, true_result: str) -> None:
    """Test preprocessing recipe with short samples from the parliament transcripts."""
    result = prep.apply(
        input_text, recipe.REGEXPS, recipe.UNACCEPTED_CHARS, recipe.TRANSLATIONS
    )
    assert result == true_result
