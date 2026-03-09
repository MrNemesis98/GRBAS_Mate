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
        return "Informatiounszentrum"

    elif menu.lower() == "copyright":
        return "Copyright-Informatioun"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Parameteropnamen"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Astellungen"

    else:
        return "Onbekannte Wäert!"


def label_text_1(menu, var_1=0, software_version=""):
    if menu.lower() == "info":
        # Version Information
        if var_1 == 1:
            text = f"""
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Aktuell installéiert Versioun vun dëser Software:	{software_version}
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dës éischt Versioun enthält detailléiert Beschreiwunge fir all Parameter vun der heefeg benotzter
                    GRBAS-Skala, inklusiv hirer Erweiderung op IF-GRBAS. Zousätzlech ginn et fräi zougänglech
                    Beispillopnamen fir all Parameter mat verschiddene Schwieregkeetsgraden.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dës Software an hiert Open-Access Material soll als Bäitrag zum Fuerschungsberäich vun der
                    klinescher Phonetik déngen an als Hëllefstool am Studie-Kontext, fir doheem ze bewäerten oder esouguer
                    fir HNO-Diagnostik.
                </p>"""
            return text
        # Future Outlook
        elif var_1 == 2:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        GRBAS_Mate ass nach an Entwécklung. Zukünfteg Versioune ginn mat méi Beispillopnamen fir d’IF‑GRBAS-Skala
                        ausgestatt. Och d’Integratioun vun alternativen Skalen a Mooss-Systemer, wéi z. B. CAPE‑V, ass méiglech.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Et ass och e Trainingsmodus geplangt, wou een Opnamen nolauschtere kann an se no der IF‑GRBAS-Skala bewäert.
                        Dat ass eng Erausfuerderung, fir d’Fäegkeet vum Benotzer ze testen, déi siwe Parameter an Opnamen mat
                        richteg dysphonesche Stëmmen z’erkennen.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        De leschte Schrëtt wäert en Tool fir automatesch Stëmmqualitéits-Analyse sinn, integréiert an dës Software.
                        Dat gëtt Deel vun engem Master-Thesis Projet a ass fir Hierscht 2026 geplangt.
                    </p>"""
            return text
        # Copyright
        elif var_1 == 3:
            text = """<p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2026
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Dës Software gouf ënner der MIT-Lizenz publizéiert, wéi folgend deklaréiert:
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
                  Duerch d'Benotzung vun GRBAS_Mate oder ee vu senge Komponenten stëmmt Dir all dëse Bedéngungen zou.  
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Tipp: Kuckt gäre d'Autorsrechteroptiounen am Astellungsmenü un!
                </p>"""
            return text

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dëst ass eng gratis App-Oberfläch, déi et de Benotzer erlaabt, vill Beispiller vu verschiddene Stëmmstéierungen
                    ze lauschteren an se mat Expert‑Referenzen ze verknëppen.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Si ass als Studimaterial fir Virliesungen oder Selbststudium geduecht, kann awer och als Hëllefstool am
                professionelle Kontext déngen.
                </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Dës éischt Versioun bitt Beispillopnamen vu verschiddene Parameteren no der heefeg benotzter
                GRBAS-Skala mat ënnerschiddleche Schwieregkeetsgraden.
                </p>
                """
        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    An dësem Menü kanns du kloer, kuerz <span style="font-weight:bold;color:#0B839C;">
                    Beschreiwungen</span> vun all IF‑GRBAS-Parameter entdecken.
                    Benotz d’Pfeilknäppercher fir tëscht de Säiten ze navigéieren oder wielt direkt aus der Iwwersiicht hei drënner.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Wann s du d’Beschreiwunge wëlls iwwersprangen, kanns du iwwer de Menü „Opnamen“ op Beispill-Audio zougräifen
                    (drëtt Optioun an der lénker Navigatiounsleeschte).
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Et gëtt och d’Méiglechkeet, direkt op d’jeweileg Opnamen fir de gewielte Parameter ze sprangen,
                    andeems s du op d’Kopfhörer uewe riets klicks.
                    </p>
                    
                    """
        elif var_1 == 2:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Instabilitéit</span> an der Stëmm.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dat bezitt sech op de Grad vun Onreegelméissegkeeten an Schwankungen an der Stabilitéit vun der Stëmm.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Eng instabil Stëmm kléngt onausgeglach a ka staark a Lautstäerkt a Pitch variéieren.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Instabilitéit ass net Deel vun der <span style="font-weight:bold;color:#0B839C;">origineller</span>
                     GRBAS-Skala, mee kann als <span style="font-weight:bold;color:#7030A0;">Erweiderung</span> benotzt ginn.
                    </p>
                    """
        elif var_1 == 3:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    D’<span style="font-weight:bold;color:#7030A0;">Fléissendkeet</span> vun enger Stëmm ass vergläichbar mam
                    Floss vun der Ried.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Si beschreift, wéi glat a flësseg d’Stëmm beim Schwätze kléngt.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dat betrëfft virun allem de Rhythmus vun der Sprooch, d’Struktur vun de Pausen an d’Kontinuitéit.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Fléissendkeet ass net Deel vun der <span style="font-weight:bold;color:#0B839C;">origineller</span>
                     GRBAS-Skala, mee kann als <span style="font-weight:bold;color:#7030A0;">Erweiderung</span> benotzt ginn.
                    </p>
                    """
        elif var_1 == 4:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    D’<span style="font-weight:bold;color:#7030A0;">Erweiderung</span> vun der GRBAS-Skala gouf gemaach,
                    fir dysphonesch Stëmmmerkmale méi differenzéiert ze erfaassen an d’Sensibilitéit vun der Skala
                    fir bestëmmte Symptomer ze verbesseren.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    D’Skala gëtt dacks erweidert, fir Parameteren opzëhuelen, déi d’Charakteristike vun dysphonesche Stëmmen
                    besser erfaassen — ëmmer ofhängeg vum Kontext an de Ziler vun der jeeweileger Fuerschung.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Fir eng detailléiert Begrënnung vun dëser Erweiderung kuck w. e. g. dës Studie:
                        <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                            style="text-decoration:none; color:#1a73e8;">
                            Voice Quality and Dysphonia (OSF project - view-only)
                        </a>
                    </p>"""
        elif var_1 == 5:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    De <span style="font-weight:bold;color:#0B839C;">Grad</span> vun Heesegkeet an der Stëmm.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Heesegkeet setzt sech aus verschiddene Charakteristiken zesummen, ënner anerem Rauheet, Loftëgkeet a Spannung.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Heesegkeet kann als Gesamteindruck vun der Stëmm beschriwwe ginn, ofhängeg vun dësen eenzele Parameteren.
                    </p>
                    """
        elif var_1 == 6:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Rauheet</span> vun der Stëmm.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dat beschreift d’Wouernahm vun onreegelméissege Schwéngungen vun de Stëmmbänner, wouduerch d’Stëmm
                    rau oder „kratzeg“ kléngt.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    
                    </p>
                    """
        elif var_1 == 7:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Loftëgkeet</span> vun der Stëmm.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dat bezitt sech op dat héierbart „Entwäiche“ vu Loft an der Stëmm.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dat kann op en onvollstännege Stëmmzoumaachen (Glottisschluss) hindeiten.
                    </p>
                    """
        elif var_1 == 8:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Weakness of the voice.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nAsthenie</span> beschreift, wéi staark d’Stëmm
                    schwaach oder leise wierkt.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dës Eegenschaft ass dacks d’Resultat vun enger reduzéierter Spannung an de Stëmmbänner.
                    </p>
                    """
        elif var_1 == 9:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    A tense impression of the voice.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nSpannung</span> beschreift de Grad vun Hyperfunktioun
                    oder Iwwerbelaaschtung vun de Kehlkopfmuskelen, 
                    wat d’Stëmmbänner beaflosst an dofir an der Stëmm héierbar ass.
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
        return "Studiumsmodus"

    elif menu.lower() == "training":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                De Trainingsmodus ass aktuell nach an Entwécklung.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                An dësem Modus kanns du deng Fäegkeeten a Wëssen testen, andeems s du Opname vun dysphonesche Stëmmen bewäerts.
                Du kriss eng Auswiel u Audiomaterial a muss de richtege Parameter an de passende Schwieregkeetsgrad zouuerdnen.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Dëse Modus baséiert op der Iddi vum Kategorie-Test aus dem Online-Experiment vun der Studie
                <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
                </a>
                .
                </p>
                """
        return text

    elif menu.lower() == "settings":
        return "Astellungen"

    else:
        return "Onbekannte Wäert!"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Informatiounszentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    D’GRBAS-Skala ass en Instrument fir Stëmmstéierungen ze bewäerten.
                    Si gëtt dacks benotzt, fir d’Schwieregkeet vun Dysphonie anzeschätzen, den Erfolleg vun enger Therapie ze moossen
                    an ze dokumentéieren, an Experten bei der Diagnos ze ënnerstëtzen.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                D’Ofkierzung GRBAS steet fir fënnef Charakteristiken: Grad (G), Rauheet (R), Loftëgkeet (B),
                Asthenie (A) a Spannung (S).
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                D’Bewäertung baséiert op engem Score-System mat Wäerter vun 0 (keng Ofwäichung vun der normaler Stëmm)
                bis 3 (staark Ofwäichung).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Parameteropnamen"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Astellungen"

    else:
        return "Onbekannte Wäert!"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Informatiounszentrum"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "home":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Nieft de fënnef Standardparameter bitt dës Software och Audiomaterial an
              Beschreiwunge fir d’Charakteristiken Instabilitéit (I) a Fléissendkeet (F).
            </p>
            <p>Beid erweideren déi originell Skala op IF‑GRBAS, wat am Kontext vun der Dysphonie‑Bewäertung nëtzlech ass,
            besonnesch bei spasmodischer Dysphonie.
            <p>
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Fir eng detailléiert Begrënnung vun dëser Skala-Erweiderung kuck w. e. g. dës Studie:
              <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
              </a>
            </p>"""

        return text

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Parameteropnamen"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Astellungen"

    else:
        return "Onbekannte Wäert!"


def label_text_4(menu, var_1=0):

    if menu.lower() == "info":
        return "Informatiounszentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        if var_1 == 1:
            text = "Aféierung (1/3)"
        elif var_1 == 2:
            text = "Aféierung (2/3)"
        elif var_1 == 3:
            text = "Aféierung (3/3)"
        else:
            text = "N/V"

        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = "Aféierung (1/9)"
        elif var_1 == 2:
            text = "Instabilitéit (2/9)"
        elif var_1 == 3:
            text = "Fléissendkeet (3/9)"
        elif var_1 == 4:
            text = "Erweiderung (4/9)"
        elif var_1 == 5:
            text = "Grad (5/9)"
        elif var_1 == 6:
            text = "Rauheet (6/9)"
        elif var_1 == 7:
            text = "Loftëgkeet (7/9)"
        elif var_1 == 8:
            text = "Asthenie (8/9)"
        elif var_1 == 9:
            text = "Spannung (9/9)"
        else:
            text = "N/V"
        return text

    elif menu.lower() == "recordings":
        return "Filterauswiel"

    elif menu.lower() == "training":
        return "Kënnt geschwënn:"

    elif menu.lower() == "settings":
        return "Astellungen"

    else:
        return "Onbekannte Wäert!"


def label_text_5(menu):
    if menu.lower() == "info":
        return "Versiouns-Informatioun"

    elif menu.lower() == "copyright":
        text = """
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2025
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                This software was published under MIT License, declared as follows:
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
                Hint: Feel free to have a look at the copyright options in the settings menu!
                </p>
                """
        return text

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial; color: #DB8004;">
                    Notiz: Ier s du dës Software benotz, kuck w. e. g. d’Copyright-Erklärung un (éischt Menü uewen riets).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Gefiltert Audiodateien"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        text = """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 22px; color: #8B0000;">
                    Notiz: Fir all Ännerungen unzewenden, muss d’App nei gestart ginn.
                </p>"""
        return text

    else:
        return "Onbekannte Wäert!"


def label_text_6(menu, var=0):
    if menu.lower() == "info":
        return "Informatiounszentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Mediaspiller"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFF;">
                        Bestëmmt d’visuellt Ausgesinn vu GRBAS_Mate
                    </p>"""
        elif var == 2:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                            Copyright-Hiwäiser am GRBAS_Mate verwalten
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                                D’Verhale vum Mediaspiller steieren
                      </p>"""

    else:
        return "Onbekannte Wäert!"


def label_text_7(menu):
    if menu.lower() == "info":
        return "Informatiounszentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Parameter"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Faarfthema:
                            </p>"""

    else:
        return "Onbekannte Wäert!"


def label_text_8(menu, var=0):
    if menu.lower() == "info":
        return "Informatiounszentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Schwieregkeetsgrad"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; 
            font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Sprooch:
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Audio-Renderqualitéit:
                      </p>"""

    else:
        return "Onbekannte Wäert!"


def label_text_9(menu):
    if menu.lower() == "info":
        return "Informatiounszentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Geschlecht vum Spriecher"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Astellungen"

    else:
        return "Onbekannte Wäert!"


def label_text_10(menu):
    if menu.lower() == "info":
        return "Informatiounszentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Artikulatiounstyp"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Astellungen"

    else:
        return "Onbekannte Wäert!"


def label_text_11(menu):
    if menu.lower() == "info":
        return "Informatiounszentrum"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Opnamen"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Astellungen"

    else:
        return "Onbekannte Wäert!"


# Textual input for buttons --------------------------------------------------------------------------------------------

def button_assistance_1(menu):
    if menu.lower() == "info":
        return "Versiounsbeschreiwung"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Parameteropnamen"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Allgemeng / GUI"

    else:
        return "Onbekannte Wäert!"


def button_assistance_2(menu):
    if menu.lower() == "info":
        return "Zukunftsperspektiv"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Parameteropnamen"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Copyright-Optiounen"

    else:
        return "Onbekannte Wäert!"


def button_assistance_3(menu):
    if menu.lower() == "info":
        return "Copyright-Erklärung"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Parameteropnamen"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Mediaspiller"

    else:
        return "Onbekannte Wäert!"


def button_assistance_4(menu):
    if menu.lower() == "info":
        return "Copyright-Erklärung"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Benotzerhandbuch"

    elif menu.lower() == "home":
        return "Start"

    elif menu.lower() == "description":
        return "Parameterbeschreiwungen"

    elif menu.lower() == "recordings":
        return "Parameteropnamen"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Elo nei starten"

    else:
        return "Onbekannte Wäert!"


def QComboBox_parameter_filter():
    return ["(I) Instabilitéit", "(F) Fléissendkeet", "(G) Grad", "(R) Rauheet",
            "(B) Loftëgkeet", "(A) Asthenie", "(S) Spannung", "All Optiounen"]


def QComboBox_severity_filter():
    return ["Niveau 0", "Niveau 1", "Niveau 2", "Niveau 3", "Opsteigend 0-3", "All Optiounen"]


def QComboBox_gender_filter():
    return ["Mann", "Fra", "All Optiounen"]


def QComboBox_articulation_filter():
    return ["Vokal", "Saz", "Béid an enger Datei", "All Optiounen"]


def QComboBox_colour_choice():
    return ["Hell", "Däischter"]


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
    return "   Copyright-Hiwäis am Startmenü weisen"


def QCheckbox_copyright_headline():
    return "   Copyright-Hiwäis an der Haaptiwwerschrëft weisen"


def QCheckbox_remember_faf():
    return "   Gefiltert Audiodateien späicheren"


def QCheckbox_remember_mps():
    return "   Mediaspiller-Astellungen späicheren"


def QCheckbox_autoplay_recordings():
    return "   Opnamen automatesch ofspillen nom Lueden"


def QComboBox_audio_render_quality_choice():
    return ["Debug:\t\t1 FPS",
            "Eco:\t\t10 FPS",
            "Normal:\t33 FPS",
            "Héich:\t\t60 FPS",
            "Ultra:\t\t100 FPS"]
