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
        return "Centre d’information"

    elif menu.lower() == "copyright":
        return "Informations de copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Enregistrements des paramètres"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Paramètres"

    else:
        return "Valeur inconnue !"


def label_text_1(menu, var_1=0, software_version=""):
    if menu.lower() == "info":
        # Version Information
        if var_1 == 1:
            text = f"""
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Version actuellement installée de ce logiciel :	{software_version}
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Cette première version contient des descriptions détaillées de chaque paramètre de l’échelle GRBAS, 
                    largement utilisée, y compris son extension IF‑GRBAS. De plus, des enregistrements d’exemple en libre 
                    accès sont fournis pour chaque paramètre, avec plusieurs niveaux de sévérité.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Ce logiciel, ainsi que son matériel en libre accès, vise à contribuer au domaine de la phonétique 
                    clinique et à servir d’outil dans un contexte d’étude, pour l’auto‑évaluation à domicile, voire pour 
                    le diagnostic ORL.
                </p>"""
            return text
        # Future Outlook
        elif var_1 == 2:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        GRBAS_Mate est toujours en cours de développement. Les versions futures seront dotées de davantage
                        d’enregistrements d’exemple pour l’échelle IF‑GRBAS. L’intégration d’échelles et de systèmes de mesure alternatifs,
                        tels que le CAPE‑V, est également envisageable.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Un mode d’entraînement est aussi prévu, permettant d’écouter des enregistrements et de les évaluer
                        selon l’échelle IF‑GRBAS. Cela peut être considéré comme un défi visant à tester la capacité de l’utilisateur
                        à reconnaître les sept paramètres dans des enregistrements de voix réellement dysphoniques.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        La dernière étape consistera en un outil d’analyse automatique de la qualité vocale, intégré à ce logiciel.
                        Cela fera partie d’un projet de mémoire de master et est prévu pour l’automne 2026.
                    </p>"""
            return text
        # Copyright
        elif var_1 == 3:
            text = """<p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2026
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Ce logiciel a été publié sous licence MIT, déclarée comme suit:
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
                  En utilisant GRBAS_Mate ou l'un de ses composants, vous acceptez toutes ces conditions. 
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Astuce : n'hésitez pas à consulter les options relatives aux droits d'auteur dans le menu des paramètres!
                </p>"""
            return text

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Il s’agit d’une application gratuite permettant aux utilisateurs d’écouter de nombreux exemples de différentes
                    dysfonctions vocales et de les associer à des références d’experts.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Elle a été conçue comme matériel d’étude pour les cours ou l’auto‑apprentissage, mais peut aussi servir d’outil d’assistance
                dans un contexte professionnel.
                </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Cette première version fournit des enregistrements d’exemple de plusieurs paramètres selon l’échelle GRBAS couramment utilisée,
                avec différents niveaux de sévérité.
                </p>
                """
        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dans ce menu, vous pouvez explorer des <span style="font-weight:bold;color:#0B839C;">descriptions</span>
                    claires et concises de chaque paramètre IF‑GRBAS.
                    Utilisez les flèches pour naviguer entre les pages ou choisissez directement dans l’aperçu ci‑dessous.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Si vous souhaitez ignorer les descriptions, vous pouvez accéder aux exemples audio via le menu des enregistrements
                    (troisième option dans la barre de navigation à gauche).
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Il est également possible d’accéder directement aux enregistrements dédiés au paramètre sélectionné
                    en cliquant sur le casque dans le coin droit.
                    </p>
                    
                    """
        elif var_1 == 2:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Instabilité</span> de la voix.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Cela renvoie au degré d’irrégularité et aux fluctuations de la stabilité de la voix.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Une voix instable semble déséquilibrée et peut varier fortement en intensité et en hauteur (pitch).
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    L’instabilité ne fait pas partie de l’échelle GRBAS <span style="font-weight:bold;color:#0B839C;">originale</span>,
                    mais peut être utilisée pour l’<span style="font-weight:bold;color:#7030A0;">étendre</span>.
                    </p>
                    """
        elif var_1 == 3:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La <span style="font-weight:bold;color:#7030A0;">fluidité</span> d’une voix est comparable au
                    flux de la parole.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Elle décrit à quel point la voix paraît régulière, souple et « fluide » lors de la parole.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Cela concerne principalement le rythme de la parole, la structure des pauses et la continuité.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La fluidité ne fait pas partie de l’échelle GRBAS <span style="font-weight:bold;color:#0B839C;">originale</span>,
                    mais peut être utilisée pour l’<span style="font-weight:bold;color:#7030A0;">étendre</span>.
                    </p>
                    """
        elif var_1 == 4:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    L’<span style="font-weight:bold;color:#7030A0;">extension</span> de l’échelle GRBAS a été introduite
                    afin de mieux saisir les caractéristiques des voix dysphoniques, de manière plus nuancée, et d’améliorer la sensibilité
                    de l’échelle pour certains symptômes.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    L’échelle est souvent étendue en ajoutant des paramètres qui décrivent mieux les caractéristiques des voix dysphoniques,
                    selon le contexte et les objectifs de la recherche concernée.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Pour une justification détaillée de cette extension, veuillez consulter l’étude suivante :
                        <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                            style="text-decoration:none; color:#1a73e8;">
                            Voice Quality and Dysphonia (OSF project - view-only)
                        </a>
                    </p>"""
        elif var_1 == 5:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Le <span style="font-weight:bold;color:#0B839C;">grade</span> d’enrouement de la voix.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    L’enrouement résulte de plusieurs caractéristiques, notamment la rugosité, le souffle et la tension.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Il peut être décrit comme l’impression globale de la voix en fonction de ces paramètres individuels.
                    </p>
                    """
        elif var_1 == 6:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Rugosité</span> de la voix.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Elle correspond à la perception de vibrations irrégulières des plis vocaux, donnant à la voix un caractère
                    rugueux ou « râpeux ».
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    
                    </p>
                    """
        elif var_1 == 7:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Souffle</span> de la voix.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Il s’agit de la fuite audible d’air dans la voix.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Cela peut indiquer une fermeture incomplète des cordes vocales.
                    </p>
                    """
        elif var_1 == 8:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Faiblesse de la voix.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">
Asthénie</span> décrit dans quelle mesure la voix
                    paraît faible ou peu sonore.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Cette caractéristique résulte d’une diminution de la tension des cordes vocales.
                    </p>
                    """
        elif var_1 == 9:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Impression de tension de la voix.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">
Tension</span> décrit le degré d’hyperfonction
                    ou de surmenage des muscles laryngés,
                    ce qui affecte les cordes vocales et est donc audible dans la voix.
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
        return "Mode d’étude"

    elif menu.lower() == "training":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Le mode d’entraînement est actuellement en cours de développement.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Dans ce mode, vous pourrez tester vos compétences et vos connaissances en évaluant des enregistrements
                de voix dysphoniques. À partir d’un ensemble de matériel audio, vous devrez attribuer le paramètre correct
                ainsi que le niveau de sévérité correspondant.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Ce mode s’appuie sur l’idée du test de catégories issu de l’expérience en ligne de l’étude
                <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
                </a>
                .
                </p>
                """
        return text

    elif menu.lower() == "settings":
        return "Paramètres"

    else:
        return "Valeur inconnue !"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Centre d’information"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    L’échelle GRBAS est un outil d’évaluation des troubles de la voix.
                    Elle est souvent utilisée pour estimer la sévérité de la dysphonie, mesurer et documenter l’efficacité d’une thérapie,
                    et aider les experts à établir un diagnostic.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                L’abréviation GRBAS correspond aux cinq caractéristiques : Grade (G), Rugosité (R), Souffle (B),
                Asthénie (A) et Tension (S).
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                L’évaluation de ces paramètres repose sur un système de notation allant de 0 (aucune déviation par rapport à une voix normale)
                à 3 (déviation sévère).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Enregistrements des paramètres"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Paramètres"

    else:
        return "Valeur inconnue !"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Centre d’information"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "home":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              En plus des cinq paramètres standard, ce logiciel fournit également du matériel audio et des descriptions
              pour les caractéristiques Instabilité (I) et Fluidité (F).
            </p>
            <p>Ces deux paramètres étendent l’échelle originale à IF‑GRBAS, ce qui est utile dans le contexte de l’évaluation de la dysphonie,
            en particulier la dysphonie spasmodique.
            <p>
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Pour une justification détaillée de cette extension, veuillez consulter l’étude suivante :
              <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
              </a>
            </p>"""

        return text

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Enregistrements des paramètres"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Paramètres"

    else:
        return "Valeur inconnue !"


def label_text_4(menu, var_1=0):

    if menu.lower() == "info":
        return "Centre d’information"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

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
            text = "Instabilité (2/9)"
        elif var_1 == 3:
            text = "Fluidité (3/9)"
        elif var_1 == 4:
            text = "Extension (4/9)"
        elif var_1 == 5:
            text = "Grade (5/9)"
        elif var_1 == 6:
            text = "Rugosité (6/9)"
        elif var_1 == 7:
            text = "Souffle (7/9)"
        elif var_1 == 8:
            text = "Asthénie (8/9)"
        elif var_1 == 9:
            text = "Tension (9/9)"
        else:
            text = "N/V"
        return text

    elif menu.lower() == "recordings":
        return "Sélection des filtres"

    elif menu.lower() == "training":
        return "Bientôt disponible :"

    elif menu.lower() == "settings":
        return "Paramètres"

    else:
        return "Valeur inconnue !"


def label_text_5(menu):
    if menu.lower() == "info":
        return "Informations sur la version"

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
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial; color: #DB8004;">
                    Remarque : avant d’utiliser ce logiciel, veuillez consulter la déclaration de copyright (premier menu en haut à droite).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Fichiers audio filtrés"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        text = """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 22px; color: #8B0000;">
                    Remarque : pour appliquer toutes les modifications, l’application doit être redémarrée.
                </p>"""
        return text

    else:
        return "Valeur inconnue !"


def label_text_6(menu, var=0):
    if menu.lower() == "info":
        return "Centre d’information"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Lecteur multimédia"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFF;">
                        Définir l’apparence visuelle de GRBAS_Mate
                    </p>"""
        elif var == 2:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                            Gérer les mentions de copyright dans GRBAS_Mate
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                                Contrôler le comportement du lecteur multimédia
                      </p>"""

    else:
        return "Valeur inconnue !"


def label_text_7(menu):
    if menu.lower() == "info":
        return "Centre d’information"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Paramètre"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Thème de couleur :
                            </p>"""

    else:
        return "Valeur inconnue !"


def label_text_8(menu, var=0):
    if menu.lower() == "info":
        return "Centre d’information"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Sévérité"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; 
            font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Langue :
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Qualité de rendu audio :
                      </p>"""

    else:
        return "Valeur inconnue !"


def label_text_9(menu):
    if menu.lower() == "info":
        return "Centre d’information"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Sexe du locuteur"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Paramètres"

    else:
        return "Valeur inconnue !"


def label_text_10(menu):
    if menu.lower() == "info":
        return "Centre d’information"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Type d’articulation"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Paramètres"

    else:
        return "Valeur inconnue !"


def label_text_11(menu):
    if menu.lower() == "info":
        return "Centre d’information"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Enregistrements"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Paramètres"

    else:
        return "Valeur inconnue !"


# Textual input for buttons --------------------------------------------------------------------------------------------

def button_assistance_1(menu):
    if menu.lower() == "info":
        return "Description de la version"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Enregistrements des paramètres"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Général / Interface"

    else:
        return "Valeur inconnue !"


def button_assistance_2(menu):
    if menu.lower() == "info":
        return "Perspectives futures"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Enregistrements des paramètres"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Options de copyright"

    else:
        return "Valeur inconnue !"


def button_assistance_3(menu):
    if menu.lower() == "info":
        return "Déclaration de copyright"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Enregistrements des paramètres"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Lecteur multimédia"

    else:
        return "Valeur inconnue !"


def button_assistance_4(menu):
    if menu.lower() == "info":
        return "Déclaration de copyright"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guide d’utilisation"

    elif menu.lower() == "home":
        return "Accueil"

    elif menu.lower() == "description":
        return "Descriptions des paramètres"

    elif menu.lower() == "recordings":
        return "Enregistrements des paramètres"

    elif menu.lower() == "training":
        return "Mode d’entraînement"

    elif menu.lower() == "settings":
        return "Redémarrer maintenant"

    else:
        return "Valeur inconnue !"


def QComboBox_parameter_filter():
    return ["(I) Instabilité", "(F) Fluidité", "(G) Grade", "(R) Rugosité",
            "(B) Souffle", "(A) Asthénie", "(S) Tension", "Toutes les options"]


def QComboBox_severity_filter():
    return ["Niveau 0", "Niveau 1", "Niveau 2", "Niveau 3", "Croissant 0-3", "Toutes les options"]


def QComboBox_gender_filter():
    return ["Homme", "Femme", "Toutes les options"]


def QComboBox_articulation_filter():
    return ["Voyelle", "Phrase", "Les deux dans un fichier", "Toutes les options"]


def QComboBox_colour_choice():
    return ["Clair", "Sombre"]


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
    return "   Afficher le copyright dans le menu Accueil"


def QCheckbox_copyright_headline():
    return "   Afficher le copyright dans le titre principal"


def QCheckbox_remember_faf():
    return "   Mémoriser les fichiers audio filtrés"


def QCheckbox_remember_mps():
    return "   Mémoriser les paramètres du lecteur"


def QCheckbox_autoplay_recordings():
    return "   Lire automatiquement les enregistrements après le chargement"


def QComboBox_audio_render_quality_choice():
    return ["Debug:\t\t1 FPS",
            "Éco:\t\t10 FPS",
            "Normal:\t33 FPS",
            "Élevé:\t\t60 FPS",
            "Ultra:\t\t100 FPS"]
