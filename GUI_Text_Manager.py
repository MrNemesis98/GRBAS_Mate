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
