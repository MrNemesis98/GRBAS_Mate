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
        return "Info-Center"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Parameter Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Einstellungen"

    else:
        return "Unkown Value!"


def label_text_1(menu, var_1=0, software_version=""):
    if menu.lower() == "info":
        # Version Information
        if var_1 == 1:
            text = f"""
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Aktuell installierte Version dieser Software:\t{software_version}
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Diese erste Softwareversion umfasst detaillierte Beschreibungen einzelner Parameter der 
                    standardisierten GRBAS-Skala, inklusive ihrer Erweiterung zu IF-GRBAS. Darüber hinaus werden 
                    Audio-Hörbeispiele für jeden Parameter mit Filtern zur Schweregrad-Differenzierung zur 
                    Verfügung gestellt.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Diese Software, sowie all ihre frei zugänglichen Komponenten, sollen als wissenschaftlicher Beitrag 
                    im Bereich der klinischen Phonetik dienen. Ebenso als Werkzeug für Selbststudien oder ggf. 
                    professionelle Diagnosen.
                </p>"""
            return text
        # Future Outlook
        elif var_1 == 2:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        GRBAS_Mate befindet sich in stetiger Entwicklung. In zukünftigen Versionen werden mehr auditive 
                        Hörbeispiele bereit gestellt. Auch die Inklusion weiterer Skalen zur Stimmbewertung, wie z.B. 
                        CAPE-V, wäre möglich.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Grundsätzlich ist auch ein Trainingsmodus geplant, in welchem aktiv Hörbeispiele zur IF-GRBAS 
                        Skala vom Nutzer bewertet werden können. Auf diese Weise können die eigenen Fähigkeiten in 
                        Sachen Parametererkennung und Festlegung des Schweregrads anhand realer Patientenaufnahmen
                        auf die Probe gestellt werden.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Die finale Phase wird ein Interface zur Automatisierten Stimmdiagnose ausmachen, welches fest
                        in diese Software integriert werden soll. Dies wird Teil eines Master Projektes sein und ist für 
                        den Herbst 2026 geplant.
                    </p>"""
            return text
        # Copyright
        elif var_1 == 3:
            text = """<p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2026
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                 Diese Software ist unter der MIT Lizenz publiziert. Die originale Fassung lautet:
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
                  Bei Nutzung von GRBAS_Mate oder einer beteiligten Komponente stimmen Sie den genannten Bedingungen zu. 
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Tipp: Schauen Sie bei den Copyright Optionen in den Einstellungen vorbei!
                </p>"""
            return text

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dies ist eine kostenlose App, mit welcher Nutzer eine Vielzahl verschiedener Audioaufnahmen von
                    Patienten mit Stimmstörungen anhören können, deren Klassifizierung zuvor professionellen Bewertungen
                    unterlag.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Die Software ist als Unterrichtsmaterial im Studium oder Selbststudium gedacht, kann aber ebenso als 
                unterstützendes Werkzeug im professionellen Kontext dienen.
                </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Diese erste Version bietet Beispiel-Aufnahmen zu den Parametern der sogenannten GRBAS-Skala an,
                unterteilt nach verschiedenen Schweregraden.
                </p>
                """
        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    In diesem Menü können die <span style="font-weight:bold;color:#0B839C;">
                    Beschreibungen</span> der einzelnen IF-GRBAS Parameter nachgeschlagen werden.
                    Die Navigation zwischen den Seiten erfolgt über die Pfeile rechts.
                    Alternativ kann ein Parameter direkt über die untere Auflistung aufgerufen werden.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Wenn Sie direkt zu den Beispiel-Aufnahmen 
                    übergehen möchten, wählen Sie das Aufnahmenmenü (dritte Option in linker Übersicht).
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Zusätzlich gibt es die Möglichkeit, über das Kopfhörersymbol rechts unten direkt die Aufnahmen für 
                    den aktuellen Parameter aufzurufen.
                    </p>

                    """
        elif var_1 == 2:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Instabilität</span> in the voice.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Damit ist der Grad an Unregelmäßigkeit / Fluktuation in der Stimme beschrieben.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Eine instabile Stimme klingt unausgewogen und variiert stark in der sprecher-typischen Lautstärke.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Instabilität ist nicht Teil der <span style="font-weight:bold;color:#0B839C;">originalen</span>
                     GRBAS-Skala, kann aber zu ihrer <span style="font-weight:bold;color:#7030A0;">Erweiterung</span>
                     genutzt werden, abhängig vom Forschungsziel.
                    </p>
                    """
        elif var_1 == 3:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Der <span style="font-weight:bold;color:#7030A0;">Fluss</span> einer Stimme ist vergleichbar mit 
                    dem Redefluss eines Sprechers.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Ähnlich wie Wasser kann eine Stimme in ihrer Erzeugung fließend oder stockend erscheinen.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
<<<<<<< Updated upstream:src/gui/GTM_scripts/GUI_Text_Manager_DE.py
                    Diese Beschreibung bezieht sich vor allem auf den Rythmus des Sprechens, die Struktur der Pausen
                    und die allgemeine Kontinuität.
=======
                    Dies äußert sich vor allem im Rythmus, in der Struktur der Pausen, sowie der Kontinuität.
>>>>>>> Stashed changes:GUI_Text_Manager_DE.py
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Fluss ist nicht Teil der <span style="font-weight:bold;color:#0B839C;">originalen</span>
                     GRBAS-Skala, kann aber zu ihrer <span style="font-weight:bold;color:#7030A0;">Erweiterung</span>
                     genutzt werden, abhängig vom Forschungsziel.
                    </p>
                    """
        elif var_1 == 4:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
<<<<<<< Updated upstream:src/gui/GTM_scripts/GUI_Text_Manager_DE.py
                    Die <span style="font-weight:bold;color:#7030A0;">Erweiterung</span> von GRBAS auf IF-GRBAS
                     erhöht die Sensibilität der Skala beim Erfassen bestimmter Symptome in dysphonischen Stimmmustern.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Grundsätzlich wird eine Skala zur Stimmqualitätsbewertung oft mit einzelnen Parametern erweitert, 
                    welche zusätzliche Charakteristiken von 
                    Stimmstörungen abdecken sollen. Dies hängt von Forschungskontext ab.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Die folgende Studie bietet eine detailliertere Erläuterung der IF-GRBAS Erweiterung:
=======
                    Die <span style="font-weight:bold;color:#7030A0;">Erweiterung</span> der GRBAS-Skala dient dazu, 
                    mehr Facetten von dysphonischen Stimmmustern zu erfassen, indem durch die zusätzlichen Parameter
                    die Sensibilität der Skala gegenüber bestimmten Symptomen geschärft wird.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Es ist üblich, Skalen mit Parametern zu erweitern, wenn sich diese zur Erfassung eines bestimmten 
                    Krankheitsbildes besser eignen, als die Standardskala. Dies geschieht stets in Abhängigkeit vom 
                    jeweiligen Forschungsziel.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Eine Erläuterung der hier vorliegenden Erweiterung kann in der folgenden Studie eingesehen werden:
>>>>>>> Stashed changes:GUI_Text_Manager_DE.py
                        <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                            style="text-decoration:none; color:#1a73e8;">
                            Voice Quality and Dysphonia (OSF Project - nur Vorschau)
                        </a>
                    </p>"""
        elif var_1 == 5:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Der <span style="font-weight:bold;color:#0B839C;">Grad</span> an Heiserkeit in der Stimme.   
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
<<<<<<< Updated upstream:src/gui/GTM_scripts/GUI_Text_Manager_DE.py
                    Heiserkeit besteht aus mehreren untergeordneten Parametern, zu denen Rauigkeit, Behauchtheit und
                    Angespanntheit (Anstrengung) in der Stimme gehören.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dementsprechend kann Heiserkeit als übergeordneter Eindruck dieser drei individuellen Parameter 
                    angesehen werden.
=======
                    Heiserkeit beschreibt das Zusammenspiel mehrerer Parameter, darunter Rauigkeit, Behauchtheit und 
                    Anstrengung.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Heiserkeit kann als Gesamteindruck der Stimme auf Basis dieser Parameter beschrieben werden.
>>>>>>> Stashed changes:GUI_Text_Manager_DE.py
                    </p>
                    """
        elif var_1 == 6:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Rauigkeit</span> in der Stimme.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
<<<<<<< Updated upstream:src/gui/GTM_scripts/GUI_Text_Manager_DE.py
                    Fachlich gesehen beschriebt dieser Parameter den Anteil an unregelmäßigen Vibrationen der 
                    Stimmlippen, aus dem sich das Bild einer vertrockneten, kratzigen Stimme ergibt.
=======
                    Dies äußert sich in der Wahrnehmung von unregelmäßigen Schwingungen der Stimmlippen, die zu einem 
                    kratzigen Unterton in der Stimme führen.
>>>>>>> Stashed changes:GUI_Text_Manager_DE.py
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dieses Stimmenmuster ist besonders typisch für Raucher.
                    </p>
                    """
        elif var_1 == 7:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Behauchtheit</span> in der Stimme.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dies bezieht sich auf ein hörbares Entweichen von Luft während der Stimmproduktion.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dies könnte ein Hinweis auf eine unvollständige Schließung der Stimmlippen sein.
                    </p>
                    """
        elif var_1 == 8:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Die Schwäche einer Stimme.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nAsthenie</span> beschreibt das Ausmaß zu welchem die 
                    Stimme kraftlos, schwach oder entsprechend leise wirkt.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Diese Charakteristik ist das Resultat einer verringerten Spannfähigkeit der Stimmlippen.
                    </p>
                    """
        elif var_1 == 9:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Beanspruchung der Stimme. 
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nAnstrengung</span> beschreibt das Maß an Überfunktion,
                    Überanstrengung oder Verausgabung der Muskeln im Kehlkopf, welche für die Beweglichkeit der 
                    Stimmlippen zuständig sind. 
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Das Ergebnis ist ein krampfartiger Unterton in der Stimme.
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
        return "Parameter Aufnahmen"

    elif menu.lower() == "training":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Der Trainingsmodus befindet sich noch in der Entwicklung.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Das Training bietet dir die Möglichkeit, dein Wissen und deine Fähigkeiten bei der Bewertung von 
                realen Aufnahmen dysphonischer Stimmen auf die Probe zu stellen.
                Aus einer Sammlung von Audiomaterial musst du einer bestimmten Aufnahme den richtigen IF-GRBAS Parameter 
                mit dem entsprechenden Schweregrad zuweisen.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Dieser Modus basiert auf dem Parametertest (category test) aus dem Online-Experiment zur folgenden 
                Studie:
                <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
                </a>
                .
                </p>
                """
        return text

    elif menu.lower() == "settings":
        return "Einstellungen"

    else:
        return "Unbekannter Wert!"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Info-Center"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Die GRBAS-Skala ist ein Werkzeug zur Bewertung von Stimmqualität.
                    Sie wird oft zur Evaluation des Schweregrades einer Stimmstörung, sowie zur Messung und 
                    Dokumentation des Erfolgs einer anschließenden Therapie verwendet.
                    Damit dient sie als Diagnose-Assistenz im professionellen Kontext oder zur Forschung.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Die Abkürzung GRBAS steht für die fünf Grundparameter: Grad an Heiserkeit (G), Rauigkeit (R), 
                Behauchtheit (B), Asthenie / Schwäche (A) und Anstrengung (S).
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Die Anwendung jedes Parameters basiert auf einem Bewertungssystem von 0 (keine Abweichung vom
                normalen Stimmmuster) zu 3 (schwerst-mögliche Abweichung). Mit dieser Bewertung ist der jeweilige 
                Schweregrad beschrieben.
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Parameter Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Einstellungen"

    else:
        return "Unbekannter Wert!"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Info-Center"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "home":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Ergänzend zu den fünf Grundparametern bietet diese Software Beschreibungen und Hörbeispiele
              die die Parameter Instbilität (I) und FLuss (F) an.
            </p>
            <p>
            Beide erweitern die Skala zu IF-GRBAS, was sich im Kontext der Bewertung von Stimmstörungen
             (Dysphonien), vor allem der sogenannten spasmodischen Dysphonie, als nützlich erwiesen hat.
            <p>
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Eine Erläuterung der hier vorliegenden Skalen-Erweiterung kann in der folgenden Studie eingesehen werden:
              <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
              </a>
            </p>"""

        return text

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Parameter Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Einstellungen"

    else:
        return "Unbekannter Wert!"


def label_text_4(menu, var_1=0):
    if menu.lower() == "info":
        return "Info-Center"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        if var_1 == 1:
            text = "Einführung (1/3)"
        elif var_1 == 2:
            text = "Einführung (2/3)"
        elif var_1 == 3:
            text = "Einführung (3/3)"
        else:
            text = "N/V"

        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = "Einführung (1/9)"
        elif var_1 == 2:
            text = "Instabilität (2/9)"
        elif var_1 == 3:
            text = "Stimmfluss (3/9)"
        elif var_1 == 4:
            text = "Erweiterung (4/9)"
        elif var_1 == 5:
            text = "Grad an Heiserkeit (5/9)"
        elif var_1 == 6:
            text = "Rauigkeit (6/9)"
        elif var_1 == 7:
            text = "Behauchtheit (7/9)"
        elif var_1 == 8:
            text = "Asthenie (8/9)"
        elif var_1 == 9:
            text = "Anstrengung (9/9)"
        else:
            text = "N/V"
        return text

    elif menu.lower() == "recordings":
        return "Auswahl an Filtern"

    elif menu.lower() == "training":
        return "Bald verfügbar:"

    elif menu.lower() == "settings":
        return "Einstellungen"

    else:
        return "Unbekannter Wert!"


def label_text_5(menu):
    if menu.lower() == "info":
        return "Versions Logbuch"

    elif menu.lower() == "copyright":
        text = """
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2025
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                Diese Software wurde unter rMIT Lizenz veröffentlicht, welche im englischen Original wie folgt 
                beschrieben ist:
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
                  Mit der Nutzung von GRBAS_Mate und all seiner Komponenten stimmen Sie allen oben genannten Bedingungen
                  widerspruchslos zu.
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                Tipp: Schauen Sie sich gerne die Copyright Optionen in den Einstellungen an!
                </p>
                """
        return text

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial; color: #DB8004;">
                    Hinweis: Bei Erstverwendung dieser App bitte die Copyright Bestimmungen im Info-Center einsehen 
                    (erstes Menü oben rechts).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Gefilterte Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        text = """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 22px; color: #8B0000;">
                    Hinweis: Für die gewählten Einstellungen muss die App neu gestartet werden!
                </p>"""
        return text

    else:
        return "Unbekannter Wert!"


def label_text_6(menu, var=0):
    if menu.lower() == "info":
        return "Info-Center"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Media Player"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFF;">
                        Nehmen Sie visuelle Veränderungen vor 
                    </p>"""
        elif var == 2:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                    Verwalten SIe die Copyright Hinweise
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                                Steuern Sie das Verhalten des Media Players
                      </p>"""

    else:
        return "Unbekannter Wert!"


def label_text_7(menu):
    if menu.lower() == "info":
        return "Info-Center"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Parameter Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Farbgebung:
                            </p>"""

    else:
        return "Unbekannter Wert!"


def label_text_8(menu, var=0):
    if menu.lower() == "info":
        return "Info-Center"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Schweregrad"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; 
            font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Sprache:
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Audio Framerate:
                      </p>"""

    else:
        return "Unbekannter Wert!"


def label_text_9(menu):
    if menu.lower() == "info":
        return "Info-Center"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Geschlecht des Sprechers"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Einstellungen"

    else:
        return "Unbekannter Wert!"


def label_text_10(menu):
    if menu.lower() == "info":
        return "Info-Center"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Artikulationsart"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Einstellungen"

    else:
        return "Unbekannter Wert!"


def label_text_11(menu):
    if menu.lower() == "info":
        return "Info-Center"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Parameter Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Einstellungen"

    else:
        return "Unbekannter Wert!"


# Textual input for buttons --------------------------------------------------------------------------------------------

def button_assistance_1(menu):
    if menu.lower() == "info":
        return "Versions Logbuch"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Parameter Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Allgemein / GUI"

    else:
        return "Unbekannter Wert!"


def button_assistance_2(menu):
    if menu.lower() == "info":
        return "Zukunftspläne"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Parameter Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Copyright Optionen"

    else:
        return "Unbekannter Wert!"


def button_assistance_3(menu):
    if menu.lower() == "info":
        return "Copyright Erklärung"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Parameter Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Media Player"

    else:
        return "Unbekannter Wert!"


def button_assistance_4(menu):
    if menu.lower() == "info":
        return "Copyright Erklärung"

    elif menu.lower() == "copyright":
        return "Copyright Information"

    elif menu.lower() == "faq":
        return "Benutzerhandbuch"

    elif menu.lower() == "home":
        return "Hauptmenü"

    elif menu.lower() == "description":
        return "Parameter Beschreibungen"

    elif menu.lower() == "recordings":
        return "Parameter Hörbeispiele"

    elif menu.lower() == "training":
        return "Trainingsmodus"

    elif menu.lower() == "settings":
        return "Jetzt neustarten!"

    else:
        return "Unbekannter Wert!"


def QComboBox_parameter_filter():
    return ["(I) Instabilität", "(F) Fluss", "(G) Grad (Heiserkeit)", "(R) Rauigkeit",
            "(B) Behauchtheit", "(A) Asthenie", "(S) Anstrengung", "Alle Optionen"]


def QComboBox_severity_filter():
    return ["Level 0", "Level 1", "Level 2", "Level 3", "Aufst. 0-3", "Alle Optionen"]


def QComboBox_gender_filter():
    return ["Männlich", "Weiblich", "Alle Optionen"]


def QComboBox_articulation_filter():
    return ["Vokal", "Ganzer Satz", "Beides in 1 Datei", "Alle Optionen"]


def QComboBox_colour_choice():
    return ["Hell", "Dunkel"]


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
    return "   Zeige Copyright Hinweis in Hauptmenü"


def QCheckbox_copyright_headline():
    return "   Zeige Copyright Hinweis als Überschrift"


def QCheckbox_remember_faf():
    return "   Behalte gefilterte Hörbeispiele"


def QCheckbox_remember_mps():
    return "   Behalte Media Player Einstellungen"


def QCheckbox_autoplay_recordings():
    return "  Spiele Aufnahmen nach dem Laden autom. ab"


def QComboBox_audio_render_quality_choice():
    return ["Debug:\t\t1 FPS",
            "Eco:\t\t10 FPS",
            "Normal:\t33 FPS",
            "Hoch:\t\t60 FPS",
            "Ultra:\t\t100 FPS"]
