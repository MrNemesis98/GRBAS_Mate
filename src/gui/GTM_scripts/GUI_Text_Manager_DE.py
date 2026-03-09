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
        return "Copyright"

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
                    Instabilität ist ist nicht Teil der <span style="font-weight:bold;color:#0B839C;">originalen</span>
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
                    Diese Beschreibung bezieht sich vor allem auf den Rythmus des Sprechens, die Struktur der Pausen
                    und die allgemeine Kontinuität.
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
                    Heiserkeit besteht aus mehreren untergeordneten Parametern, zu denen Rauigkeit, Behauchtheit und
                    Angespanntheit (Anstrengung) in der Stimme gehören.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dementsprechend kann Heiserkeit als übergeordneter Eindruck dieser drei individuellen Parameter 
                    angesehen werden.
                    </p>
                    """
        elif var_1 == 6:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Rauigkeit</span> in der Stimme.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Fachlich gesehen beschriebt dieser Parameter den Anteil an unregelmäßigen Vibrationen der 
                    Stimmlippen, aus dem sich das Bild einer vertrockneten, kratzigen Stimme ergibt.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dieses Stimmenmuster ist besonders typisch für Raucher.
                    </p>
                    """
        elif var_1 == 7:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Breathyness</span> of the voice.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    This refers to the audible escape of air in the voice.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    This may indicate incomplete closure of the vocal cords.
                    </p>
                    """
        elif var_1 == 8:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Weakness of the voice.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nAsthenia</span> describes the extent to which the 
                    voice appears weak or quiet.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    This characteristic is the result of reduced tension in the vocal cords.
                    </p>
                    """
        elif var_1 == 9:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    A tense impression of the voice.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nStrain</span> describes the degree of hyperfunction 
                    or overexertion of the laryngeal muscles, 
                    which affects the vocal cords and is therefore audible in the voice.
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
        return "Study Mode"

    elif menu.lower() == "training":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                The training mode is currently under development.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Within this mode you will be able to test your skills and knowledge by evaluating recordings of 
                dypshonic voices. Given a set of audio material you will have to assign the correct parameter and 
                severity level. 
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                This mode is based on the idea of the category test from the online experiment of the study 
                <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
                </a>
                .
                </p>
                """
        return text

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Information Center"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    The GRBAS scale is a tool for assessing voice disorders. 
                    It is often used to evaluate the severity 
                    of dysphonia, measure and document the success of therapy, and assist experts in making a diagnosis. 
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                The abbreviation GRBAS stands for the five characteristics Grade (G), Roughness (R), Breathyness (B), 
                Asthenia (A) and Strain (S). 
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                The assessment of these parameters is based on a scoring system with values 
                ranging from 0 (no deviation from normal voice patterns) to 3 (severe deviation).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Parameter Recordings"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Information Center"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "home":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              In addition to the regular five parameters, this software also provides audio material and
              descriptions for the characteristics Instability (I) and Fluency (F).
            </p>
            <p>Both extend the original scale to IF-GRBAS, which is useful in context of dysphonia assessment, 
            especially spasmodic dysphonia.
            <p>
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              For a detailed rationale behind this scale extension please have a look at the following study:
              <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
              </a>
            </p>"""

        return text

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Parameter Recordings"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_4(menu, var_1=0):
    if menu.lower() == "info":
        return "Information Center"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        if var_1 == 1:
            text = "Introduction (1/3)"
        elif var_1 == 2:
            text = "Introduction (2/3)"
        elif var_1 == 3:
            text = "Introduction (3/3)"
        else:
            text = "N/V"

        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = "Introduction (1/9)"
        elif var_1 == 2:
            text = "Instability (2/9)"
        elif var_1 == 3:
            text = "Fluency (3/9)"
        elif var_1 == 4:
            text = "Extension (4/9)"
        elif var_1 == 5:
            text = "Grade (5/9)"
        elif var_1 == 6:
            text = "Roughness (6/9)"
        elif var_1 == 7:
            text = "Breathyness (7/9)"
        elif var_1 == 8:
            text = "Asthenia (8/9)"
        elif var_1 == 9:
            text = "Strain (9/9)"
        else:
            text = "N/V"
        return text

    elif menu.lower() == "recordings":
        return "Filter Selection"

    elif menu.lower() == "training":
        return "Coming Soon:"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_5(menu):
    if menu.lower() == "info":
        return "Version Information"

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
        return "User Guide"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial; color: #DB8004;">
                    Hinweis: Bei Erstverwendung dieser App bitte die Copyright Bestimmungen im Info-Center einsehen 
                    (erstes Menü oben rechts).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Filtered Audio Files"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        text = """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 22px; color: #8B0000;">
                    Note: For applying all changes the app needs to be restarted.
                </p>"""
        return text

    else:
        return "Unkown Value!"


def label_text_6(menu, var=0):
    if menu.lower() == "info":
        return "Information Center"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Media Player"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFF;">
                        Define The Visual Appearance of GRBAS_Mate
                    </p>"""
        elif var == 2:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                    Manage Copyright Notices within GRBAS_Mate
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                                Control the Behaviour of the Media Player
                      </p>"""

    else:
        return "Unkown Value!"


def label_text_7(menu):
    if menu.lower() == "info":
        return "Information Center"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Parameter"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Colour Theme:
                            </p>"""

    else:
        return "Unkown Value!"


def label_text_8(menu, var=0):
    if menu.lower() == "info":
        return "Information Center"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Severity"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; 
            font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Language:
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Audio Render Quality:
                      </p>"""

    else:
        return "Unkown Value!"


def label_text_9(menu):
    if menu.lower() == "info":
        return "Information Center"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Gender of Speaker"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_10(menu):
    if menu.lower() == "info":
        return "Information Center"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Type of Articulation"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_11(menu):
    if menu.lower() == "info":
        return "Information Center"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Recordings"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


# Textual input for buttons --------------------------------------------------------------------------------------------

def button_assistance_1(menu):
    if menu.lower() == "info":
        return "Version Description"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Parameter Recordings"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "General / GUI"

    else:
        return "Unkown Value!"


def button_assistance_2(menu):
    if menu.lower() == "info":
        return "Future Outlook"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Parameter Recordings"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Copyright Options"

    else:
        return "Unkown Value!"


def button_assistance_3(menu):
    if menu.lower() == "info":
        return "Copyright Statement"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Parameter Recordings"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Media Player"

    else:
        return "Unknown Value!"


def button_assistance_4(menu):
    if menu.lower() == "info":
        return "Copyright Statement"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "recordings":
        return "Parameter Recordings"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Restart Now"

    else:
        return "Unknown Value!"


def QComboBox_parameter_filter():
    return ["(I) Instability", "(F) Fluency", "(G) Grade", "(R) Roughness",
            "(B) Breathyness", "(A) Asthenia", "(S) Strain", "All Options"]


def QComboBox_severity_filter():
    return ["Level 0", "Level 1", "Level 2", "Level 3", "Asc. 0-3", "All Options"]


def QComboBox_gender_filter():
    return ["Male", "Female", "All Options"]


def QComboBox_articulation_filter():
    return ["Vowel", "Sentence", "Both in 1 file", "All Options"]


def QComboBox_colour_choice():
    return ["Light", "Dark"]


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
    return "   Show Copyright Notice in Home Menu"


def QCheckbox_copyright_headline():
    return "   Show Copyright Notice in Main Headline"


def QCheckbox_remember_faf():
    return "   Remember Filtered Audio Files"


def QCheckbox_remember_mps():
    return "   Remember Media Player Settings"


def QCheckbox_autoplay_recordings():
    return "   Play Recordings Automatically after Loading"


def QComboBox_audio_render_quality_choice():
    return ["Debug:\t\t1 FPS",
            "Eco:\t\t10 FPS",
            "Normal:\t33 FPS",
            "High:\t\t60 FPS",
            "Ultra:\t\t100 FPS"]
