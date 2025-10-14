"""
Copyright © MrNemesis98, GitHub, 2025

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

This software contains modified audio material from the Perceptual Voice Quality Database:
https://data.mendeley.com/datasets/9dz247gnyb/1.


CC BY 4.0 licence description
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
    return ("   GRBAS_Mate   [ɡɹæps me͜ɪt̚]                               "
            "Copyright © MrNemesis98, GitHub, 2025") \
        if with_copyright else "   GRBAS_Mate   [ɡɹæps me͜ɪt̚]"


def label_menu_title(menu):
    if menu.lower() == "info":
        return "Version Information"

    elif menu.lower() == "copyright":
        return "Copyright Information"

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
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_1(menu, var_1=0):
    if menu.lower() == "info":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                This first version provides detailed descriptions for every parameter belonging to the commonly used 
                GRBAS scale, including its extension to IF-GRBAS. Furthermore open access sample recordings are provided
                for every parameter with a choice of different severity levels.
            </p>
            """
        return text

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    This is a free app interface that allows users to listen to numerous examples of different voice
                    dysfunctions and associate them with expert benchmark.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                It is created for home assessment, but can serve as an assistance tool in diagnosis for professional 
                context, too.
                </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                This first version provides sample recordings of several parameters according to the commonly used 
                GRBAS scale with different severity levels.
                </p>
                """
        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Within this menu you can explore clear, concise <span style="font-weight:bold;color:#0B839C;">
                    descriptions</span> of every IF-GRBAS parameter.
                    Use the arrow buttons to navigate between the single pages or choose directly from the overview below.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    There is also the possibility to jump straight to the dedicated recording menu for the parameter 
                    you’ve selected.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    If you want to skip the descriptions you can access the recordings in the training mode menu
                    (third option on the left navigational bar).
                    </p>
                    """
        elif var_1 == 2:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Instability</span> in the voice.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    This refers to the degree of irregularity and fluctuations in the stability of the voice.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    An unstable voice sounds unbalanced and can vary greatly in volume and pitch.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Instability is not part of the <span style="font-weight:bold;color:#0B839C;">original</span>
                     GRBAS-scale, but can be used to <span style="font-weight:bold;color:#7030A0;">extend</span> it.
                    </p>
                    """
        elif var_1 == 3:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    The <span style="font-weight:bold;color:#7030A0;">Fluency</span> of a voice is comparable to the 
                    flow of speech.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    It refers to how smooth and fluid the voice sounds when speaking.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    This mainly concerns the rhythm of speech, the structure of pauses, and continuity.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Fluency is not part of the <span style="font-weight:bold;color:#0B839C;">original</span>
                     GRBAS-scale, but can be used to <span style="font-weight:bold;color:#7030A0;">extend</span> it.
                    </p>
                    """
        elif var_1 == 4:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    The <span style="font-weight:bold;color:#7030A0;">Extension</span> of the the GRBAS scale was made 
                    to capture dysphonic voice features in a more nuanced way, improving the scale's sensitivity in 
                    addressing certain symptoms.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    The scale is often extended to include parameters that better address the characteristics of 
                    dysphonic voices, always depending on context and goals of the respective research.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    For a detailed rationale behind this scale extension please have a look at the following study:
                        <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                            style="text-decoration:none; color:#1a73e8;">
                            Voice Quality and Dysphonia (OSF project - view-only)
                        </a>
                    </p>"""
        elif var_1 == 5:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    The <span style="font-weight:bold;color:#0B839C;">Grade</span> of hoarseness in the voice.   
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Hoarseness is composed of various characteristics, including roughness, breathyness, and strain.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Hoarseness can be described as the overall impression of the voice depending on these 
                    individual parameters. 
                    </p>
                    """
        elif var_1 == 6:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Roughness</span> of the voice.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    This describes the perception of irregular vibration of the vocal folds, causing the voice to sound  
                    rough or scratchy.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    
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
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    This software as well as its open access material shall serve as a contribution to the research 
                    field of clinical phonetics and as a tool in practical context of home assessment or even 
                    ENT diagnostics.
                </p>
                """
        return text

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
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    The app is still under development and will be be equipped with more sample 
                    recordings and a training mode to challenge the user´s ability to recognize the seven IF-GRBAS
                    parameters in dysphonic voice recordings. Later on there is a mode for automatic voice diagnosis 
                    planned, too.
                </p>
                """
        return text

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


def label_text_4(menu, var_1=0, current_software_version=""):

    if menu.lower() == "info":
        return "Currently installed version: \t" + current_software_version

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
        return "Parameter Recordings"

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
                    Note: Before using this software please have a look at the copyright statement (second top right 
                    menu).
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


def label_text_6(menu):
    if menu.lower() == "info":
        return "Future Outlook:"

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
        return "Settings"

    else:
        return "Unkown Value!"


"""
Notes:
IFGRBAS 
-> R in Mitte, Breite: 60 zu 70 Höhe
Range: 130 (label_text_1) bis 1260+70= 1330 (button_switch_right) == 1200
da Breite gleich 60: 1200/2 = 600 und 60/2 = 30, 
also Startpunkt 130+600-30 == 700 und Endpunkt 130+600+30 == 760

alle Startpunkte:

I: 520-60 = 460
F: 580-60 = 520
-: 640-60 = 580
G: 700-60 = 640
R: 700
B: 700+60 = 760
A: 760+60 = 820
S: 820+60 = 880
"""