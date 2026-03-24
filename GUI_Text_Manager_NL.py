"""
Copyright © MrNemesis98, GitHub, 2026

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files, to deal in the software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, and to
permit persons to whom the software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
software. The program is provided “as is”, without warranty of any kind, express or implied, including but not
limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.
In no event shall the author(s) or copyright holder(s) be liable for any claim, damages or other liability, whether
in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or
other dealings in the software.

By using GRBAS_Mate or one of its components you agree to all these conditions.

------------------------------------------------------------------------------------------------------------------------

This software contains partially modified audio material from the Perceptual Voice Quality Database:
https://data.mendeley.com/datasets/9dz247gnyb/4.
Walden, Patrick R. (2022), “Perceptual Voice Qualities Database (PVQD)”, Mendeley Data, V4, doi: 10.17632/9dz247gnyb.4


CC BY 4.0 licence description (https://creativecommons.org/licenses/by/4.0/)
The files associated with this dataset are licensed under a Creative Commons Attribution 4.0 International licence.
What does this mean?

You can share, copy and modify this dataset so long as you give appropriate credit, provide a link to the CC BY license,
and indicate if changes were made, but you may not do so in a way that suggests the rights holder has endorsed you or
your use of the dataset. Note that further permission may be required for any content within the dataset that is
identified as belonging to a third party.
"""


def window_title():
    return "GRBAS_Mate v1.0"


def label_main_headline_background(with_copyright=False):
    return ("   GRBAS_Mate   [ɡɹæps me͜ɪt̚]"
            "\t\tCopyright © MrNemesis98, GitHub, 2026") \
        if with_copyright else "   GRBAS_Mate   [ɡɹæps me͜ɪt̚]"


def label_menu_title(menu):
    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "copyright":
        return "Copyrightinformatie"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijving"

    elif menu.lower() == "recordings":
        return "Voorbeeldopnames"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Instellingen"

    else:
        return "Onbekende waarde!"


def label_text_1(menu, var_1=0, software_version=""):
    if menu.lower() == "info":
        # Versie-informatie
        if var_1 == 1:
            text = f"""
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Momenteel geïnstalleerde versie van deze software:\t{software_version}
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Deze eerste versie bevat gedetailleerde beschrijvingen van elke parameter van de veelgebruikte
                    GRBAS-schaal, inclusief de uitbreiding naar IF-GRBAS. Daarnaast zijn er open-access voorbeeldopnames 
                    beschikbaar voor elke parameter, met een keuze uit verschillende ernstniveaus.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Deze software en het open-access materiaal zijn bedoeld als bijdrage aan het onderzoeksgebied 
                    van de klinische fonetiek en als hulpmiddel in studiecontext, voor thuisevaluatie of zelfs 
                    KNO-diagnostiek.
                </p>"""
            return text
        # Toekomstperspectief
        elif var_1 == 2:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        GRBAS_Mate is nog in ontwikkeling. Toekomstige versies zullen worden uitgerust met meer
                        voorbeeldopnames voor de IF-GRBAS-schaal. Ook het toevoegen van alternatieve schalen en meetsystemen,
                        zoals CAPE-V, is mogelijk.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Er is ook een trainingsmodus gepland waarin er naar opnames geluisterd kan worden en ze beoordeeld
                        kunnen worden volgens de IF-GRBAS-schaal. Op deze manier kan getest worden of
                        de gebruiker de zeven parameters in opnames met echte dysfone stemmen kan herkennen.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Als laatste zal een hulpmiddel voor automatische analyse van stemkwaliteit worden geïntegreerd in
                        deze software. Dit zal deel uitmaken van een masterthesisproject en is gepland voor de herfst van 2026.
                    </p>"""
            return text
        # Copyright
        elif var_1 == 3:
            text = """<p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2026
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Deze software is gepubliceerd onder MIT-licentie, die als volgt is geformuleerd:
                  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
                  associated documentation files, to deal in the software without restriction, including without
                  limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
                  of the software, and to permit persons to whom the software is furnished to do so, subject to the 
                  following conditions:
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  The above copyright notice and this permission notice shall be included in all copies or substantial 
                  portions of the software. The program is provided “as is”, without warranty of any kind, express or 
                  implied, including but not limited to the warranties of merchantability, fitness for a particular 
                  purpose and noninfringement. In no event shall the author(s) or copyright holder(s) be liable for any 
                  claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, 
                  out of or in connection with the software or the use or other dealings in the software.
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial; color: #DB8004;">
                  Door GRBAS_Mate of een van de onderdelen ervan te gebruiken, gaat u akkoord met al deze voorwaarden. 
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Tip: Bekijk gerust de copyrightopties in het instellingenmenu!
                </p>"""
            return text

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dit is een gratis app-interface waarmee gebruikers naar voorbeelden van verschillende
                    stemstoornissen kunnen luisteren en deze kunnen koppelen aan een expert-benchmark.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                De app is ontwikkeld als studiemateriaal voor colleges of zelfstudie, maar kan ook dienen als
                ondersteunend hulpmiddel in een professionele context.
                </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Deze eerste versie bevat voorbeeldopnames van meerdere parameters volgens de veelgebruikte
                GRBAS-schaal, met verschillende ernstniveaus.
                </p>
                """
        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    In dit menu kun je een heldere en beknopte <span style="font-weight:bold;color:#0B839C;">
                    beschrijving</span> van elke IF-GRBAS-parameter raadplegen.
                    Gebruik de pijltjestoetsen om door de pagina’s te navigeren of kies direct uit het overzicht hieronder.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Als je de beschrijvingen wilt overslaan, kun je voorbeeldaudio openen via het menu Opnames
                    (derde optie in de linkse navigatiebalk).
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Je kunt ook rechtstreeks springen naar de opnames voor de geselecteerde parameter 
                    door op de koptelefoon in de rechterhoek te klikken.
                    </p>
                    """
        elif var_1 == 2:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Instabiliteit</span> in de stem.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dit verwijst naar de mate van onregelmatigheid en schommelingen in de stabiliteit van de stem.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Een instabiele stem klinkt onevenwichtig en kan sterk variëren in volume en toonhoogte.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Instabiliteit maakt geen deel uit van de <span style="font-weight:bold;color:#0B839C;">
                    oorspronkelijke</span>
                     GRBAS-schaal, maar kan worden gebruikt om deze <span style="font-weight:bold;color:#7030A0;">
                     uit te breiden</span>.
                    </p>
                    """
        elif var_1 == 3:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    De <span style="font-weight:bold;color:#7030A0;">Vloeiendheid</span> van een stem is vergelijkbaar met de
                    vloeiendheid van spraak.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Het verwijst naar hoe soepel en vloeiend de stem klinkt tijdens het spreken.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dit betreft vooral het spreekritme, de structuur van pauzes en de continuïteit.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Vloeiendheid maakt geen deel uit van de <span style="font-weight:bold;color:#0B839C;">oorspronkelijke</span>
                     GRBAS-schaal, maar kan worden gebruikt om deze <span style="font-weight:bold;color:#7030A0;">uit te breiden</span>.
                    </p>
                    """
        elif var_1 == 4:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    De <span style="font-weight:bold;color:#7030A0;">uitbreiding</span> van de GRBAS-schaal is ontwikkeld
                    om dysfone stemkenmerken op een meer genuanceerde manier te kunnen beschrijven, en zo de gevoeligheid van de
                    schaal te vergroten bij het beoordelen van bepaalde symptomen.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    De schaal wordt vaak uitgebreid met parameters die de kenmerken van dysfone stemmen beter vastleggen,
                    afhankelijk van de context en de doelen van het betreffende onderzoek.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Voor een uitgebreide onderbouwing van deze schaaluitbreiding kun je de volgende studie raadplegen:
                        <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                            style="text-decoration:none; color:#1a73e8;">
                            Voice Quality and Dysphonia (OSF project - view-only)
                        </a>
                    </p>"""
        elif var_1 == 5:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    De <span style="font-weight:bold;color:#0B839C;">Graad</span> van heesheid in de stem.   
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Heesheid bestaat uit verschillende kenmerken, waaronder ruwheid, ademigheid en spanning.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Heesheid kan worden opgevat als de algemene indruk van de stem op basis van deze afzonderlijke
                    parameters.
                    </p>
                    """
        elif var_1 == 6:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Ruwheid</span> van de stem.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dit beschrijft de ervaring van een onregelmatige vibratie van de stembanden, wat resulteert in een 
                    ruw of rasperig stemgeluid.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    
                    </p>
                    """
        elif var_1 == 7:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Ademigheid</span> van de stem.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dit verwijst naar het hoorbaar ontsnappen van lucht in de stem.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dit kan wijzen op een onvolledige sluiting van de stembanden.
                    </p>
                    """
        elif var_1 == 8:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Zwakte van de stem.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nAsthenie</span> beschrijft in welke mate het stemgeluid
                    zwak of stil is.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dit kenmerk is het resultaat van verminderde spanning van de stembanden.
                    </p>
                    """
        elif var_1 == 9:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Een gespannen indruk van de stem.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nSpanning</span> beschrijft de mate van hyperfunctie 
                    of overspanning van de spieren in het strottenhoofd.
                    Dit beïnvloedt de stembanden en is dus hoorbaar in het stemgeluid.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    
                    </p>
                    """
        else:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    N/V
                    </p>
                    """
        return text

    elif menu.lower() == "recordings":
        return "Studiemodus"

    elif menu.lower() == "training":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                De trainingsmodus is momenteel in ontwikkeling.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                In deze modus kun je je vaardigheden en kennis testen door opnames van dysfone stemmen te beoordelen.
                Je krijgt een set audiomateriaal en moet de juiste parameter en het juiste ernstniveau toekennen.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Deze modus is gebaseerd op het idee van de categorietest uit het online experiment van de studie
                <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
                </a>
                .
                </p>
                """
        return text

    elif menu.lower() == "settings":
        return "Instellingen"

    else:
        return "Onbekende waarde!"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    De GRBAS-schaal is een instrument om stemstoornissen te beoordelen.
                    De schaal wordt vaak gebruikt om de ernst van dysfonie te evalueren, het succes van therapie te meten en te
                    documenteren, en experts te ondersteunen bij het stellen van een diagnose.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                De afkorting GRBAS staat voor de vijf kenmerken: Graad (G), Ruwheid (R), Ademigheid (Breathyness) (B),
                Asthenie (A) en Spanning (S).
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                De beoordeling van deze parameters is gebaseerd op een scoresysteem met waarden van
                0 (geen afwijking van normaal stemgebruik) tot 3 (ernstige afwijking).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Voorbeeldopnames"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Instellingen"

    else:
        return "Onbekende waarde!"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "home":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Naast de vijf standaardparameters biedt deze software ook audiomateriaal en beschrijvingen voor de
              kenmerken Instabiliteit (I) en Vloeiendheid (Fluency) (F).
            </p>
            <p>Deze kenmerken breiden de oorspronkelijke schaal uit naar IF-GRBAS, wat nuttig is in de context van
            dysfoniebeoordeling, vooral bij spasmodische dysfonie.
            <p>
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Voor een uitgebreide onderbouwing van deze schaaluitbreiding kun je de volgende studie raadplegen:
              <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
              </a>
            </p>"""

        return text

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Voorbeeldopnames"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Instellingen"

    else:
        return "Onbekende waarde!"


def label_text_4(menu, var_1=0):

    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        if var_1 == 1:
            text = "Introductie (1/3)"
        elif var_1 == 2:
            text = "Introductie (2/3)"
        elif var_1 == 3:
            text = "Introductie (3/3)"
        else:
            text = "N/V"

        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = "Introductie (1/9)"
        elif var_1 == 2:
            text = "Instabiliteit (2/9)"
        elif var_1 == 3:
            text = "Vloeiendheid (3/9)"
        elif var_1 == 4:
            text = "Uitbreiding (4/9)"
        elif var_1 == 5:
            text = "Graad (5/9)"
        elif var_1 == 6:
            text = "Ruwheid (6/9)"
        elif var_1 == 7:
            text = "Ademigheid (7/9)"
        elif var_1 == 8:
            text = "Asthenie (8/9)"
        elif var_1 == 9:
            text = "Spanning (9/9)"
        else:
            text = "N/V"
        return text

    elif menu.lower() == "recordings":
        return "Filterselectie"

    elif menu.lower() == "training":
        return "Binnenkort beschikbaar:"

    elif menu.lower() == "settings":
        return "Instellingen"

    else:
        return "Onbekende waarde!"


def label_text_5(menu):
    if menu.lower() == "info":
        return "Versie-informatie"

    elif menu.lower() == "copyright":
        text = """
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2025
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                Deze software is gepubliceerd onder MIT-licentie, die als volgt is geformuleerd:
                  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
                  associated documentation files, to deal in the software without restriction, including without
                  limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
                  of the software, and to permit persons to whom the software is furnished to do so, subject to the 
                  following conditions:
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                  The above copyright notice and this permission notice shall be included in all copies or substantial 
                  portions of the software. The program is provided “as is”, without warranty of any kind, express or 
                  implied, including but not limited to the warranties of merchantability, fitness for a particular 
                  purpose and noninfringement. In no event shall the author(s) or copyright holder(s) be liable for any 
                  claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, 
                  out of or in connection with the software or the use or other dealings in the software.
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial; color: #DB8004;">
                  By using GRBAS_Mate or one of its components you agree to all these conditions. 
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                Tip: Bekijk gerust de copyrightopties in het instellingenmenu!
                </p>
                """
        return text

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial; color: #DB8004;">
                    Let op: bekijk vóór gebruik van deze software de copyrightverklaring (eerste menu rechtsboven).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Gefilterde audiobestanden"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        text = """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 22px; color: #8B0000;">
                    Let op: om alle wijzigingen toe te passen moet de app opnieuw worden gestart.
                </p>"""
        return text

    else:
        return "Onbekende waarde!"


def label_text_6(menu, var=0):
    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Mediaspeler"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFF;">
                        Bepaal het uiterlijk van GRBAS_Mate
                    </p>"""
        elif var == 2:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                            Beheer copyrightmeldingen binnen GRBAS_Mate
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                                Bepaal de Instellingen van de Mediaspeler
                      </p>"""

    else:
        return "Onbekende waarde!"


def label_text_7(menu):
    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Parameter"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Kleurthema:
                            </p>"""

    else:
        return "Onbekende waarde!"


def label_text_8(menu, var=0):
    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Ernst"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; 
            font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Taal:
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 25px; color: 
            #FFFFFF;">Audio Framerate:</p>"""

    else:
        return "Onbekende waarde!"


def label_text_9(menu):
    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Geslacht van spreker"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Instellingen"

    else:
        return "Onbekende waarde!"


def label_text_10(menu):
    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Type articulatie"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Instellingen"

    else:
        return "Onbekende waarde!"


def label_text_11(menu):
    if menu.lower() == "info":
        return "Informatiecentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Opnames"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Instellingen"

    else:
        return "Onbekende waarde!"


# Textual input for buttons --------------------------------------------------------------------------------------------

def button_assistance_1(menu):
    if menu.lower() == "info":
        return "Versie-informatie"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Voorbeeldopnames"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Algemeen / GUI"

    else:
        return "Onbekende waarde!"


def button_assistance_2(menu):
    if menu.lower() == "info":
        return "Toekomstperspectief"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Voorbeeldopnames"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Copyrightopties"

    else:
        return "Onbekende waarde!"


def button_assistance_3(menu):
    if menu.lower() == "info":
        return "Copyrightverklaring"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Voorbeeldopnames"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Mediaspeler"

    else:
        return "Onbekende waarde!"


def button_assistance_4(menu):
    if menu.lower() == "info":
        return "Copyrightverklaring"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Gebruikershandleiding"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschrijvingen"

    elif menu.lower() == "recordings":
        return "Voorbeeldopnames"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Nu opnieuw starten"

    else:
        return "Onbekende waarde!"


def QComboBox_parameter_filter():
    return ["(I) Instabiliteit", "(F) Vloeiendheid", "(G) Graad", "(R) Ruwheid",
            "(B) Ademigheid", "(A) Asthenie", "(S) Spanning", "Alle opties"]


def QComboBox_severity_filter():
    return ["Niveau 0", "Niveau 1", "Niveau 2", "Niveau 3", "Oplopend 0-3", "Alle opties"]


def QComboBox_gender_filter():
    return ["Man", "Vrouw", "Alle opties"]


def QComboBox_articulation_filter():
    return ["Klinker", "Zin", "Beiden in één bestand", "Alle opties"]


def QComboBox_colour_choice():
    return ["Licht", "Donker"]


def QComboBox_language_choice():
    return ["English",
            "Deutsch",
            "Italiano",
            "Español",
            "Français",
            "Lëtzebuergesch",
            "Nederlands",
            "Polski",
            "Türkçe"]


def QCheckbox_copyright_home():
    return "   Toon copyrightmelding in startmenu"


def QCheckbox_copyright_headline():
    return "   Toon copyrightmelding in hoofdtitel"


def QCheckbox_remember_faf():
    return "   Sla Gefilterde Audiobestanden op"


def QCheckbox_remember_mps():
    return "   Sla Instellingen van Mediaspeler op"


def QCheckbox_autoplay_recordings():
    return "   Speel Opnames automatisch af"


def QComboBox_audio_render_quality_choice():
    return ["Debug:\t\t1 FPS",
            "Eco:\t\t10 FPS",
            "Normal:\t33 FPS",
            "High:\t\t60 FPS",
            "Ultra:\t\t100 FPS"]
