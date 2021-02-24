"""Long statement strings and other space consuming data definitions for testing are declared here.

This is done to avoid clutter in main test files.
"""
from typing import Any
from typing import List
from typing import Tuple

import pytest

parl_to_kaldi_pairs: List[Tuple[str, str]] = [
    (
        "Ensimmäiseen käsittelyyn esitellään päiväjärjestyksen 5. asia. Käsittelyn pohjana on "
        "sosiaali- ja terveysvaliokunnan mietintö StVM 16/2017 vp. Yleiskeskustelu asiasta päättyi "
        "30.11.2017 pidetyssä täysistunnossa. Nyt käsitellään muutosehdotukset.",
        "ensimmäiseen käsittelyyn esitellään päiväjärjestyksen viides asia käsittelyn pohjana on "
        "sosiaali ja terveysvaliokunnan mietintö kuusitoista yleiskeskustelu asiasta päättyi "
        "kolmaskymmenes yhdettätoista kaksituhattaseitsemäntoista pidetyssä täysistunnossa nyt "
        "käsitellään muutosehdotukset",
    ),
    (
        "Arvoisa puhemies! Kristillisdemokraatit tukevat hallituksen päätöstä valmiuslain 86, 88, "
        "93, 94 ja 109 §:ien sekä 95 §:n ja siitä johtuvien 96—103 §:ien toimivaltuuden käytön ja "
        "soveltamisen jatkamisesta sekä 87 §:n toimivaltuuksien käyttöönotosta ja jatkamisesta.",
        "arvoisa puhemies kristillisdemokraatit tukevat hallituksen päätöstä valmiuslain pykälien "
        "kahdeksankymmentäkuusi kahdeksankymmentäkahdeksan yhdeksänkymmentäkolme "
        "yhdeksänkymmentäneljä ja satayhdeksän sekä yhdeksännenkymmenennenviidennen pykälän ja "
        "siitä johtuvien pykälien yhdeksänkymmentäkuusi viiva satakolme toimivaltuuden käytön ja "
        "soveltamisen jatkamisesta sekä kahdeksannenkymmenennenseitsemännen pykälän "
        "toimivaltuuksien käyttöönotosta ja jatkamisesta",
    ),
    (
        "Arvoisa puhemies! Valtioneuvosto on antanut eduskunnalle valmiuslain mukaisten "
        "toimivaltuuksien käytön jatkoa koskevia asetuksia. Asetuksilla jatketaan hallituksen "
        "aiemmin päättämiä toimia, joita koskevien asetusten voimassaolo päättyy 13.4.2020. Nyt "
        "esitetyillä asetuksilla jatketaan toimivaltuuksien käyttöä 13.5.2020 asti. "
        "Toimenpiteisiin liittyen on annettu yhteensä neljä valtioneuvoston asetusta: "
        "valtioneuvoston asetus valmiuslain 86, 88, 93, 94 ja 109 §:issä säädettyjen "
        "toimivaltuuksien käytön jatkamisesta, asetus valmiuslain 87 §:ssä säädettyjen "
        "toimivaltuuksien käytön jatkamisesta, asetus valmiuslain 87 §:ssä säädettyjen "
        "toimivaltuuksien käyttöönotosta sekä asetus valmiuslain 95 §:n 2 momentissa säädetyn "
        "toimivaltuuden käytön ja 96—103 §:ien soveltamisen jatkamisesta. Valtioneuvosto haluaa "
        "jatkaa rajoituksia lähiopetuksessa eri koulutusasteilla. Tämä tarkoittaa, että opetuksen "
        "poikkeusjärjestelyjä jatketaan 13. toukokuuta asti.",
        "arvoisa puhemies valtioneuvosto on antanut eduskunnalle valmiuslain mukaisten "
        "toimivaltuuksien käytön jatkoa koskevia asetuksia asetuksilla jatketaan hallituksen "
        "aiemmin päättämiä toimia joita koskevien asetusten voimassaolo päättyy kolmastoista "
        "neljättä kaksituhattakaksikymmentä nyt esitetyillä asetuksilla jatketaan toimivaltuuksien "
        "käyttöä kolmastoista viidettä kaksituhattakaksikymmentä asti toimenpiteisiin liittyen on "
        "annettu yhteensä neljä valtioneuvoston asetusta valtioneuvoston asetus valmiuslain "
        "pykälissä kahdeksankymmentäkuusi kahdeksankymmentäkahdeksan yhdeksänkymmentäkolme "
        "yhdeksänkymmentäneljä ja satayhdeksän säädettyjen toimivaltuuksien käytön jatkamisesta "
        "asetus valmiuslain kahdeksannessakymmenennessäseitsemännessä pykälässä säädettyjen "
        "toimivaltuuksien käytön jatkamisesta asetus valmiuslain "
        "kahdeksannessakymmenennessäseitsemännessä pykälässä säädettyjen toimivaltuuksien "
        "käyttöönotosta sekä asetus valmiuslain yhdeksännenkymmenennenviidennen pykälän toisessa "
        "momentissa säädetyn toimivaltuuden käytön ja pykälien yhdeksänkymmentäkuusi viiva "
        "satakolme soveltamisen jatkamisesta valtioneuvosto haluaa jatkaa rajoituksia "
        "lähiopetuksessa eri koulutusasteilla tämä tarkoittaa että opetuksen poikkeusjärjestelyjä "
        "jatketaan kolmastoista toukokuuta asti",
    ),
    (
        "Käsittelyssä olevassa lakialoitteessa esitetään myös lyhytaikaisesti lasten parissa töitä "
        "tekevien henkilöiden rikostaustan selvittämistä poistamalla lain 2 §:n 3 momentista "
        "rikostaustan tarkastusta rajoittava kolmen kuukauden aikaraja työsuhteen kestolle. "
        "Lisäksi tässä lakialoitteessa velvoitettaisiin työnantajaa pyytämän työntekijältä "
        "rikostaustaote jo mahdolliseen sijaisrekisteriin rekisteröitymisen yhteydessä, ja tätä "
        "varten lain 3 §:ään lisättäisiin uusi, 4 momentti.",
        "käsittelyssä olevassa lakialoitteessa esitetään myös lyhytaikaisesti lasten parissa töitä "
        "tekevien henkilöiden rikostaustan selvittämistä poistamalla lain toisen pykälän "
        "kolmannesta momentista rikostaustan tarkastusta rajoittava kolmen kuukauden aikaraja "
        "työsuhteen kestolle lisäksi tässä lakialoitteessa velvoitettaisiin työnantajaa pyytämän "
        "työntekijältä rikostaustaote jo mahdolliseen sijaisrekisteriin rekisteröitymisen "
        "yhteydessä ja tätä varten lain kolmanteen pykälään lisättäisiin uusi neljäs momentti",
    ),
    (
        "Tämä hallituksen esitys varmistaa näiden opistojen riittävän rahoituksen valtionosuuksien "
        "merkittävän nousun myötä — siis 57:stä enintään 80 prosenttiin. Arvoisa puhemies! Olemme "
        "kuitenkin tyytymättömiä siihen, että vaikeasti vammaisille järjestettävä koulutus voisi "
        "esityksen mukaan saada valtionosuutta enimmillään vain 80 prosenttia, kun "
        "maahanmuuttajien kotoutumiskoulutuksen valtionosuus olisi jatkossa täydet 100 prosenttia. "
        "Pidämmekin esitystä tältä osin epäjohdonmukaisena ja ehdotamme lakiehdotusta "
        "muutettavaksi siten, että kotouttamiskoulutusta ja vaikeavammaisten koulutusta koskevien "
        "valtionosuuksien prosenttiosuudet olisivat yhtenevät eli tässä tapauksessa molemmat 80 "
        "prosenttia. Esitämme vastalauseemme mukaisia muutosehdotuksia lain 9 ja 10 §:iin.",
        "tämä hallituksen esitys varmistaa näiden opistojen riittävän rahoituksen valtionosuuksien "
        "merkittävän nousun myötä siis viidestäkymmenestäseitsemästä enintään kahdeksaankymmeneen "
        "prosenttiin arvoisa puhemies olemme kuitenkin tyytymättömiä siihen että vaikeasti "
        "vammaisille järjestettävä koulutus voisi esityksen mukaan saada valtionosuutta "
        "enimmillään vain kahdeksankymmentä prosenttia kun maahanmuuttajien kotoutumiskoulutuksen "
        "valtionosuus olisi jatkossa täydet sata prosenttia pidämmekin esitystä tältä osin "
        "epäjohdonmukaisena ja ehdotamme lakiehdotusta muutettavaksi siten että "
        "kotouttamiskoulutusta ja vaikeavammaisten koulutusta koskevien valtionosuuksien "
        "prosenttiosuudet olisivat yhtenevät eli tässä tapauksessa molemmat kahdeksankymmentä "
        "prosenttia esitämme vastalauseemme mukaisia muutosehdotuksia lain pykäliin yhdeksän ja "
        "kymmenen",
    ),
    (
        "Ympäristövaliokunta ei ollut tämän lakiesityksen käsittelyssä yksimielinen, vaan vihreät, "
        "vasemmistoliitto ja RKP jättivät eriävän mielipiteen. Yksityiskohtaisessa, "
        "pykäläkohtaisessa käsittelyssä teen tämän eriävän mielipiteen mukaiset muutosehdotukset "
        "65 ja 169 §:iin, jotka tarkoittavat, että nämä pykälät säilytetään ennallaan. Se, että "
        "kullanhuuhdonnan jatkolupa pitenee 3:sta 10 vuoteen, on varsin merkittävä muutos, samoin "
        "se, että toimintaa saa jatkaa, vaikka luvasta olisi valitettu. Esimerkiksi Metsähallitus "
        "lausunnossaan toivoi jatkoajan pidennyksen maltillistamista. Myös Lapin ely-keskus toi "
        "lausunnossaan esiin sen, että tämän muutoksen vaikutuksia ympäristöön ei hallituksen "
        "esityksessä ole arvioitu riittävästi.",
        "ympäristövaliokunta ei ollut tämän lakiesityksen käsittelyssä yksimielinen vaan vihreät "
        "vasemmistoliitto ja rkp jättivät eriävän mielipiteen yksityiskohtaisessa "
        "pykäläkohtaisessa käsittelyssä teen tämän eriävän mielipiteen mukaiset muutosehdotukset "
        "pykäliin kuusikymmentäviisi ja satakuusikymmentäyhdeksän jotka tarkoittavat että nämä "
        "pykälät säilytetään ennallaan se että kullanhuuhdonnan jatkolupa pitenee kolmesta "
        "kymmeneen vuoteen on varsin merkittävä muutos samoin se että toimintaa saa jatkaa vaikka "
        "luvasta olisi valitettu esimerkiksi metsähallitus lausunnossaan toivoi jatkoajan "
        "pidennyksen maltillistamista myös lapin ely keskus toi lausunnossaan esiin sen että "
        "tämän muutoksen vaikutuksia ympäristöön ei hallituksen esityksessä ole arvioitu "
        "riittävästi",
    ),
    (
        "Tällä hetkellä määräaika on kolme vuotta. Rikoslain 2 c luvun 5—14 §:ien kohdat "
        "säätelevät sitä, kuinka nopeasti ehdottomaan määräaikaiseen vankeusrangaistukseen "
        "tuomittu vanki vapautetaan ehdonalaiseen vapauteen. Keskeisimmät pykälät ovat 5 § ja 8 §. "
        "Niiden mukaisesti: 1) Pääsääntöisesti vanki päästetään ehdonalaiseen vapauteen, kun hän "
        "on kärsinyt rangaistuksestaan kaksi kolmasosaa tai alle 21-vuotiaana tehdyn rikoksen "
        "rangaistuksesta puolet. 2) Pääsäännöstä poiketaan, kun vanki ei ole suorittanut "
        "vankeusrangaistusta vankilassa rikosta edeltäneiden kolmen vuoden aikana. Tässä "
        "tapauksessa hänet päästetään ehdonalaiseen vapauteen, kun hän on kärsinyt "
        "rangaistuksestaan puolet tai alle 21-vuotiaana tehdyn rikoksen rangaistuksesta yhden "
        "kolmasosan. 3) Vankilassa todellisesti vietettyä aikaa voi lisäksi lyhentää valvottu "
        "koevapaus. Koevapauteen voi päästä 6 kuukautta ennen ehdonalaista vapauttamista. Tällöin "
        "vankia valvotaan vankilan ulkopuolella teknisin välinein tai muulla tavalla. Arvoisa "
        "puhemies! Näin esimerkiksi taposta 9 vuoden vankeusrangaistuksen saanut voi "
        "tosiasiallisesti olla vankilassa 4 vuotta. Alle 21-vuotiaana tehdystä törkeästä "
        "raiskauksesta 4 vuodeksi ehdottomaan vankeuteen tuomittu voi istua vankilassa vain 10 "
        "kuukautta. Kuten mainittu, nämä lieventävät tilanteet edellyttävät, että rikoksentekijä "
        "ei ole ollut vankilassa rikosta edeltäneiden kolmen vuoden aikana. Rikoslaki on näin "
        "ollen merkittävästi lievempi vangille, jolla joko ei ole lainkaan aikaisempia "
        "vankeusrangaistuksia tai jonka viimeisimmästä vankeusrangaistuksesta on sen verran paljon "
        "aikaa, että hän välillä ehtii olla kolme vuotta poissa vankilassa. — Tämä löytyy 5 §:n 2 "
        "momentin toisesta lauseesta.",
        "tällä hetkellä määräaika on kolme vuotta rikoslain kaksi c luvun pykälien viisi viiva "
        "neljätoista kohdat säätelevät sitä kuinka nopeasti ehdottomaan määräaikaiseen "
        "vankeusrangaistukseen tuomittu vanki vapautetaan ehdonalaiseen vapauteen keskeisimmät "
        "pykälät ovat viides pykälä ja kahdeksas pykälä niiden mukaisesti yksi pääsääntöisesti "
        "vanki päästetään ehdonalaiseen vapauteen kun hän on kärsinyt rangaistuksestaan kaksi "
        "kolmasosaa tai alle kaksikymmentäyksi vuotiaana tehdyn rikoksen rangaistuksesta puolet "
        "kaksi pääsäännöstä poiketaan kun vanki ei ole suorittanut vankeusrangaistusta vankilassa "
        "rikosta edeltäneiden kolmen vuoden aikana tässä tapauksessa hänet päästetään "
        "ehdonalaiseen vapauteen kun hän on kärsinyt rangaistuksestaan puolet tai alle "
        "kaksikymmentäyksi vuotiaana tehdyn rikoksen rangaistuksesta yhden kolmasosan kolme "
        "vankilassa todellisesti vietettyä aikaa voi lisäksi lyhentää valvottu koevapaus "
        "koevapauteen voi päästä kuusi kuukautta ennen ehdonalaista vapauttamista tällöin vankia "
        "valvotaan vankilan ulkopuolella teknisin välinein tai muulla tavalla arvoisa puhemies "
        "näin esimerkiksi taposta yhdeksän vuoden vankeusrangaistuksen saanut voi tosiasiallisesti "
        "olla vankilassa neljä vuotta alle kaksikymmentäyksi vuotiaana tehdystä törkeästä "
        "raiskauksesta neljäksi vuodeksi ehdottomaan vankeuteen tuomittu voi istua vankilassa vain "
        "kymmenen kuukautta kuten mainittu nämä lieventävät tilanteet edellyttävät että "
        "rikoksentekijä ei ole ollut vankilassa rikosta edeltäneiden kolmen vuoden aikana "
        "rikoslaki on näin ollen merkittävästi lievempi vangille jolla joko ei ole lainkaan "
        "aikaisempia vankeusrangaistuksia tai jonka viimeisimmästä vankeusrangaistuksesta on sen "
        "verran paljon aikaa että hän välillä ehtii olla kolme vuotta poissa vankilassa tämä "
        "löytyy viidennen pykälän toisen momentin toisesta lauseesta",
    ),
    (
        "Näen, että sähkökäyttöisen polkupyörän käytössä voi tulla myös ongelmia, mikäli joudutaan "
        "miettimään, onko ajoneuvo polkupyörä vaiko jalankulkija. Onneksemme lausuntojen johdosta "
        "tieliikennelain 45 ja 45 a §:iin on molempiin tehty täsmennys siitä, että jalankulkijan "
        "roolissa ollaan ainoastaan silloin, kun nopeus vastaa kävelynopeutta. Jalkakäytävällä "
        "tulee kulkea kävelynopeutta. Jos laitteen käyttäjä kulkee kävelynopeutta nopeammin, hänen "
        "tulee noudattaa polkupyöräilijän liikennesääntöjä. Lausunnossa ei yksiselitteisesti "
        "kerrota, mikä on kävelynopeus. Onko se minun käyttämäni kävelynopeus vai edustaja "
        "Essayahin käyttämä kilpakävelynopeus? Tulkinnanvaraa on mielestäni liikaa. Mielestäni "
        "esityksessä on hyvä lisäys myös lain 40 §:n 1 momentti, jossa jalankulun asemaa on "
        "lausuntojen johdosta vielä erikseen korostettu. Tässä kohdin säädetään jalankulkijan "
        "paikasta tiellä, että jalkakäytävän käyttö polkupyörällä olisi mahdollista vain silloin, "
        "jos se voidaan tehdä muita jalankulkijoita haittaamatta. Myös se, että kevyen "
        "sähköajoneuvon käyttäjä olisi polkupyöräilijä aina, jos käytettävissä ei ole "
        "jalkakäytävää, on hyvä tiedostaa. Tällöin polkupyöräilijän paikka on tiellä aina ajoradan "
        "oikea reuna riippumatta nopeudesta. Kevyille sähköajoneuvoille on esitetty "
        "luokkakohtaista 25 kilometrin tuntinopeusrajoitusta.",
        "näen että sähkökäyttöisen polkupyörän käytössä voi tulla myös ongelmia mikäli joudutaan "
        "miettimään onko ajoneuvo polkupyörä vaiko jalankulkija onneksemme lausuntojen johdosta "
        "tieliikennelain pykäliin neljäkymmentäviisi ja neljäkymmentäviisi a on molempiin tehty "
        "täsmennys siitä että jalankulkijan roolissa ollaan ainoastaan silloin kun nopeus vastaa "
        "kävelynopeutta jalkakäytävällä tulee kulkea kävelynopeutta jos laitteen käyttäjä kulkee "
        "kävelynopeutta nopeammin hänen tulee noudattaa polkupyöräilijän liikennesääntöjä "
        "lausunnossa ei yksiselitteisesti kerrota mikä on kävelynopeus onko se minun käyttämäni "
        "kävelynopeus vai edustaja essayahin käyttämä kilpakävelynopeus tulkinnanvaraa on "
        "mielestäni liikaa mielestäni esityksessä on hyvä lisäys myös lain neljännenkymmenennen "
        "pykälän ensimmäinen momentti jossa jalankulun asemaa on lausuntojen johdosta vielä "
        "erikseen korostettu tässä kohdin säädetään jalankulkijan paikasta tiellä että "
        "jalkakäytävän käyttö polkupyörällä olisi mahdollista vain silloin jos se voidaan tehdä "
        "muita jalankulkijoita haittaamatta myös se että kevyen sähköajoneuvon käyttäjä olisi "
        "polkupyöräilijä aina jos käytettävissä ei ole jalkakäytävää on hyvä tiedostaa tällöin "
        "polkupyöräilijän paikka on tiellä aina ajoradan oikea reuna riippumatta nopeudesta "
        "kevyille sähköajoneuvoille on esitetty luokkakohtaista kahdenkymmenenviiden kilometrin "
        "tuntinopeusrajoitusta",
    ),
    (
        "Siirryn sitten siihen. — Perustuslakivaliokunnan arvioitavana on ollut valmiuslain 8 §:n "
        "nojalla annettu valtioneuvoston asetus valmiuslain 87 §:ssä säädetyn toimivaltuuden "
        "käytön jatkamisesta. Asetuksen 2 §:n mukaan valmiuslain 87 §:ssä säädettyä toimivaltuutta "
        "ohjata terveydenhuollon toimintaa mainitun pykälän 1 kohdassa tarkoitetulla tavalla "
        "voidaan soveltaa koko valtakunnan alueella. Valmiuslain 87 §:n 1 kohdan mukaan väestön "
        "terveydenhuollon turvaamiseksi 3 §:n 1, 2, 4 ja 5 kohdissa tarkoitetuissa poikkeusoloissa "
        "sosiaali- ja terveysministeriö voi päätöksellään velvoittaa lääketehtaan, "
        "lääketukkukaupan, apteekkiliikkeen harjoittamiseen oikeutetun sekä sellaisen yhteisön ja "
        "yksityisen elinkeinonharjoittajan, joka toimittaa terveydenhuollossa käytettäviä "
        "tavaroita tai palveluja taikka muuten toimii terveydenhuollon alalla, laajentamaan tai "
        "muuttamaan toimintaansa. Asetus tulee voimaan 14. päivänä toukokuuta 2020, ja se on "
        "voimassa vähintään 30. päivään kesäkuuta 2020. Perustuslakivaliokunta esittää, että "
        "valtioneuvoston asetus saa jäädä voimaan.",
        "siirryn sitten siihen perustuslakivaliokunnan arvioitavana on ollut valmiuslain "
        "kahdeksannen pykälän nojalla annettu valtioneuvoston asetus valmiuslain "
        "kahdeksannessakymmenennessäseitsemännessä pykälässä säädetyn toimivaltuuden käytön "
        "jatkamisesta asetuksen toisen pykälän mukaan valmiuslain "
        "kahdeksannessakymmenennessäseitsemännessä pykälässä säädettyä toimivaltuutta ohjata "
        "terveydenhuollon toimintaa mainitun pykälän ensimmäisessä kohdassa tarkoitetulla tavalla "
        "voidaan soveltaa koko valtakunnan alueella valmiuslain "
        "kahdeksannenkymmenennenseitsemännen pykälän ensimmäisen kohdan mukaan väestön "
        "terveydenhuollon turvaamiseksi kolmannen pykälän yksi kaksi neljä ja viisi kohdissa "
        "tarkoitetuissa poikkeusoloissa sosiaali ja terveysministeriö voi päätöksellään velvoittaa "
        "lääketehtaan lääketukkukaupan apteekkiliikkeen harjoittamiseen oikeutetun sekä sellaisen "
        "yhteisön ja yksityisen elinkeinonharjoittajan joka toimittaa terveydenhuollossa "
        "käytettäviä tavaroita tai palveluja taikka muuten toimii terveydenhuollon alalla "
        "laajentamaan tai muuttamaan toimintaansa asetus tulee voimaan neljäntenätoista päivänä "
        "toukokuuta kaksituhattakaksikymmentä ja se on voimassa vähintään "
        "kolmanteenkymmenenteen päivään kesäkuuta kaksituhattakaksikymmentä "
        "perustuslakivaliokunta esittää että valtioneuvoston asetus saa jäädä voimaan",
    ),
    (
        "Vuonna 2009 laaditun ja vuonna 2011 päivitetyn poliisin pitkän aikavälin "
        "henkilöstötarpeiden kehittämissuunnitelman mukaan vuonna 2020 poliisimiesten "
        "kokonaismäärän tarpeeksi on arvioitu 8 296 henkilötyövuotta, mihin lukuun ei sisälly "
        "kenttäjaksolla olevien määrä. Mielestäni tämä olisi sopiva poliisimäärä. Tämä luku on "
        "kuitenkin kaukana tuosta 6 300:sta, joka näillä näkymin on todellisuutta vuonna 2020. "
        "Tällä hetkellä meillä on poliiseja tuhatta asukasta kohden 1,31, mikä on ylivoimaisesti "
        "vähiten koko Pohjoismaissa. Myös hallinto- ja lupapalveluissa toimii poliisissa jo "
        "suhteessa vähemmän henkilöitä kuin useimmissa muissa valtion virastoissa. Lisävähennykset "
        "johtaisivat siihen, että poliisimiehet hoitaisivat myös näitä tehtäviä. En näe mitään "
        "järkeä tällaisessa toiminnassa. Muissa Pohjoismaissa poliisien määrää ja rahoitusta "
        "lisätään. Esimerkiksi Ruotsissa osoitetaan poliisille tälle kehyskaudelle lisärahoitusta "
        "2 miljardia kruunua. Pyrkimyksenä on 2 000 poliisimiehen ja 1 300 muun työntekijän "
        "lisäys. Samaan aikaan me Suomessa elämme lintukodossa ja toivomme, ettei meitä kukaan "
        "huomaisi. Samalla haluamme olla osa Eurooppaa mutta emme kuitenkaan toimi kuten "
        "eurooppalaisten kuuluisi toimia. Pitäisi ymmärtää, että sisäinen turvallisuus on "
        "suomalaisen demokratian ja hyvinvointiyhteiskunnan kivijalka. Erittäin myönteinen asia "
        "on, että Poliisiammattikorkeakoulun sisäänottoa ollaan kasvattamassa tänä vuonna 400 "
        "opiskelijalla. Viime vuonna valmistui edellisen hallituksen huomenlahjana vain 57 "
        "poliisimiestä, ja se ei riitä kattamaan eläköitymisvauhtia, joka on noin 300 joka vuosi. "
        "Edellisellä vaalikaudella toteutetun Pora III:n tavoitteena oli liikenteenvalvonnan tason "
        "säilyttäminen vähintään sillä tasolla, jolla se on ollut liikkuvan poliisin aikana. "
        "Raskaan liikenteen valvonta tulisi säilyttää vuoden 2012 tasolla.",
        "vuonna kaksituhattayhdeksän laaditun ja vuonna kaksituhattayksitoista päivitetyn poliisin "
        "pitkän aikavälin henkilöstötarpeiden kehittämissuunnitelman mukaan vuonna "
        "kaksituhattakaksikymmentä poliisimiesten kokonaismäärän tarpeeksi on arvioitu "
        "kahdeksantuhattakaksisataayhdeksänkymmentäkuusi henkilötyövuotta mihin lukuun ei sisälly "
        "kenttäjaksolla olevien määrä mielestäni tämä olisi sopiva poliisimäärä tämä luku on "
        "kuitenkin kaukana tuosta kuudestatuhannestakolmestasadasta joka näillä näkymin on "
        "todellisuutta vuonna kaksituhattakaksikymmentä tällä hetkellä meillä on poliiseja tuhatta "
        "asukasta kohden yksi pilkku kolmekymmentäyksi mikä on ylivoimaisesti vähiten koko "
        "pohjoismaissa myös hallinto ja lupapalveluissa toimii poliisissa jo suhteessa vähemmän "
        "henkilöitä kuin useimmissa muissa valtion virastoissa lisävähennykset johtaisivat siihen "
        "että poliisimiehet hoitaisivat myös näitä tehtäviä en näe mitään järkeä tällaisessa "
        "toiminnassa muissa pohjoismaissa poliisien määrää ja rahoitusta lisätään esimerkiksi "
        "ruotsissa osoitetaan poliisille tälle kehyskaudelle lisärahoitusta kaksi miljardia "
        "kruunua pyrkimyksenä on kahdentuhannen poliisimiehen ja tuhannenkolmensadan muun "
        "työntekijän lisäys samaan aikaan me suomessa elämme lintukodossa ja toivomme ettei meitä "
        "kukaan huomaisi samalla haluamme olla osa eurooppaa mutta emme kuitenkaan toimi kuten "
        "eurooppalaisten kuuluisi toimia pitäisi ymmärtää että sisäinen turvallisuus on "
        "suomalaisen demokratian ja hyvinvointiyhteiskunnan kivijalka erittäin myönteinen asia on "
        "että poliisiammattikorkeakoulun sisäänottoa ollaan kasvattamassa tänä vuonna "
        "neljälläsadalla opiskelijalla viime vuonna valmistui edellisen hallituksen huomenlahjana "
        "vain viisikymmentäseitsemän poliisimiestä ja se ei riitä kattamaan eläköitymisvauhtia "
        "joka on noin kolmesataa joka vuosi edellisellä vaalikaudella toteutetun pora kolmen "
        "tavoitteena oli liikenteenvalvonnan tason säilyttäminen vähintään sillä tasolla jolla se "
        "on ollut liikkuvan poliisin aikana raskaan liikenteen valvonta tulisi säilyttää vuoden "
        "kaksituhattakaksitoista tasolla",
    ),
    (
        "Tässäpä täysin hatusta vedetty koe [Puhemies koputtaa], jossa saman puheenvuoron sisällä "
        "on useampi (Kaisa Kansanedustaja: Nyt on asiaa!) välihuuto yms. sulkeiden sisällä olevaa "
        "joka poistetaan. Tällä testillä varmistetaan (Pertti Perusjamppa: Vastalause!], että "
        "käytetty säännöllinen lauseke (regexp) on laiska eikä ahne. Toisin sanoen lausekkeen "
        "osuma loppuu ensimmäiseen avatun sulkeen jälkeen kohdattuun sulkevaan sulkeeseen. [Tyyne "
        "Toisinajattelija: Tässä vielä virhe eli jäi sulje sulkematta!?",
        "tässäpä täysin hatusta vedetty koe jossa saman puheenvuoron sisällä on useampi välihuuto "
        "ynnä muuta sellaista sulkeiden sisällä olevaa joka poistetaan tällä testillä varmistetaan "
        "että käytetty säännöllinen lauseke on laiska eikä ahne toisin sanoen lausekkeen osuma "
        "loppuu ensimmäiseen avatun sulkeen jälkeen kohdattuun sulkevaan sulkeeseen",
    ),
]


@pytest.fixture
def parl_to_kaldi_test_pairs(request: Any) -> Tuple[str, str]:
    """Return an embedded statement from the above list using given index."""
    index: int = request.param
    return parl_to_kaldi_pairs[index]
