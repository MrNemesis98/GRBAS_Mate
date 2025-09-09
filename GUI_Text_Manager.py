def window_title():
    return "GRBAS_Mate v1.0"


def label_main_headline_background():
    return "     GRBAS_Mate   [ɡʁæps mæɪtʰ]"


def label_menu_title(menu):
    if menu.lower() == "info":
        return "Version Information"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Parameter Descriptions"

    elif menu.lower() == "study":
        return "Study Mode"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_1(menu):
    if menu.lower() == "info":
        return "Version Information"

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
        return "Parameter Descriptions"

    elif menu.lower() == "study":
        return "Study Mode"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Version Information"

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

    elif menu.lower() == "study":
        return "Study Mode"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Version Information"

    elif menu.lower() == "faq":
        return "User Guide"

    elif menu.lower() == "home":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              In addition to the regular five parameters, this software also provides audio material and
              descriptions for the characteristics Instability (I) and Fluency (F).
            </p>
            <p>Both extend the original scale to IF-GRBAS, which is useful in context of dysphonia assessment, 
            especially spasmodic dysphonia.
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

    elif menu.lower() == "study":
        return "Study Mode"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"


def label_text_4(menu, var_1=0):
    if menu.lower() == "info":
        return "Version Information"

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
        return "Parameter Descriptions"

    elif menu.lower() == "study":
        return "Study Mode"

    elif menu.lower() == "training":
        return "Training Mode"

    elif menu.lower() == "settings":
        return "Settings"

    else:
        return "Unkown Value!"
