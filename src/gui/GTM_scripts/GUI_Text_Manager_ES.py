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
        return "Centro de información"

    elif menu.lower() == "copyright":
        return "Información de copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Grabaciones de parámetros"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "Ajustes"

    else:
        return "¡Valor desconocido!"


def label_text_1(menu, var_1=0, software_version=""):
    if menu.lower() == "info":
        # Version Information
        if var_1 == 1:
            text = f"""
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Versión actualmente instalada de este software:	{software_version}
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Esta primera versión contiene descripciones detalladas de cada parámetro de la escala GRBAS, de uso 
                    común, incluida su extensión IF-GRBAS. Además, se proporcionan grabaciones de ejemplo de libre 
                    acceso para cada parámetro, con distintos niveles de severidad.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Este software, así como su material de acceso abierto, pretende contribuir al campo de la fonética 
                    clínica y servir como herramienta en un contexto de estudio, para la autoevaluación en casa o incluso 
                    para el diagnóstico ORL.
                </p>"""
            return text
        # Future Outlook
        elif var_1 == 2:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        GRBAS_Mate sigue en desarrollo. Las versiones futuras estarán equipadas con más grabaciones de ejemplo
                        para la escala IF-GRBAS. También es posible incluir escalas y sistemas de medida alternativos, como CAPE-V.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        También se prevé un modo de entrenamiento en el que se puedan escuchar grabaciones y evaluarlas según la escala IF-GRBAS.
                        Esto puede considerarse un reto para la capacidad del usuario de reconocer los siete parámetros en grabaciones
                        con voces realmente disfonías.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        El paso final será una herramienta de análisis automático de la calidad vocal, integrada en este software.
                        Formará parte de un proyecto de tesis de máster y está previsto para el otoño de 2026.
                    </p>"""
            return text
        # Copyright
        elif var_1 == 3:
            text = """<p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2026
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Este software se publicó bajo licencia MIT, declarada de la siguiente manera:
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
                  Al utilizar GRBAS_Mate o cualquiera de sus componentes, usted acepta todas estas condiciones. 
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Sugerencia: ¡No dudes en echar un vistazo a las opciones de derechos de autor en el menú de configuración!
                </p>"""
            return text

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Esta es una aplicación gratuita que permite a los usuarios escuchar numerosos ejemplos de diferentes
                    disfunciones vocales y asociarlos con referencias de expertos.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Está pensada como material de estudio para clases o autoaprendizaje, pero también puede servir como herramienta de apoyo
                en un contexto profesional.
                </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Esta primera versión ofrece grabaciones de ejemplo de varios parámetros según la escala GRBAS, de uso común,
                con distintos niveles de severidad.
                </p>
                """
        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    En este menú puede explorar <span style="font-weight:bold;color:#0B839C;">descripciones</span> claras y concisas
                    de cada parámetro IF-GRBAS.
                    Utilice las flechas para navegar entre las páginas o elija directamente en el resumen de abajo.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Si desea omitir las descripciones, puede acceder a ejemplos de audio mediante el menú de grabaciones
                    (tercera opción en la barra de navegación izquierda).
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    También es posible ir directamente a las grabaciones dedicadas del parámetro seleccionado
                    haciendo clic en los auriculares en la esquina derecha.
                    </p>
                    
                    """
        elif var_1 == 2:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Inestabilidad</span> de la voz.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Se refiere al grado de irregularidad y a las fluctuaciones en la estabilidad de la voz.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Una voz inestable suena desequilibrada y puede variar mucho en intensidad y altura (pitch).
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La inestabilidad no forma parte de la escala GRBAS <span style="font-weight:bold;color:#0B839C;">original</span>,
                     pero puede utilizarse para <span style="font-weight:bold;color:#7030A0;">ampliarla</span>.
                    </p>
                    """
        elif var_1 == 3:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La <span style="font-weight:bold;color:#7030A0;">fluidez</span> de una voz es comparable al
                    flujo del habla.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Se refiere a lo suave y fluida que suena la voz al hablar.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Esto concierne principalmente al ritmo del habla, la estructura de las pausas y la continuidad.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La fluidez no forma parte de la escala GRBAS <span style="font-weight:bold;color:#0B839C;">original</span>,
                     pero puede utilizarse para <span style="font-weight:bold;color:#7030A0;">ampliarla</span>.
                    </p>
                    """
        elif var_1 == 4:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La <span style="font-weight:bold;color:#7030A0;">ampliación</span> de la escala GRBAS se realizó
                    para captar las características de las voces disfonías de manera más matizada, mejorando la sensibilidad de la escala
                    para abordar determinados síntomas.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La escala suele ampliarse para incluir parámetros que describan mejor las características de las voces disfonías,
                    siempre en función del contexto y los objetivos de la investigación correspondiente.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Para una justificación detallada de esta ampliación, consulte el siguiente estudio:
                        <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                            style="text-decoration:none; color:#1a73e8;">
                            Voice Quality and Dysphonia (OSF project - view-only)
                        </a>
                    </p>"""
        elif var_1 == 5:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    El <span style="font-weight:bold;color:#0B839C;">grado</span> de ronquera en la voz.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La ronquera se compone de varias características, entre ellas la rugosidad, la soplosidad y la tensión.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Puede describirse como la impresión global de la voz en función de estos parámetros individuales.
                    </p>
                    """
        elif var_1 == 6:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Rugosidad</span> de la voz.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Describe la percepción de una vibración irregular de los pliegues vocales, haciendo que la voz suene
                    áspera o «rasposa».
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    
                    </p>
                    """
        elif var_1 == 7:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Soplosidad</span> de la voz.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Se refiere a la salida audible de aire en la voz.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Esto puede indicar un cierre incompleto de las cuerdas vocales.
                    </p>
                    """
        elif var_1 == 8:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Debilidad de la voz.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">
Astenia</span> describe en qué medida la voz
                    parece débil o poco sonora.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Esta característica es el resultado de una tensión reducida en las cuerdas vocales.
                    </p>
                    """
        elif var_1 == 9:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Impresión de tensión en la voz.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">
Tensión</span> describe el grado de hiperfunción
                    o sobreesfuerzo de los músculos laríngeos,
                    lo que afecta a las cuerdas vocales y, por tanto, es audible en la voz.
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
        return "Modo de estudio"

    elif menu.lower() == "training":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                El modo de entrenamiento está actualmente en desarrollo.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                En este modo podrá poner a prueba sus habilidades y conocimientos evaluando grabaciones de voces disfonías.
                A partir de un conjunto de material de audio, deberá asignar el parámetro correcto y el nivel de severidad correspondiente.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Este modo se basa en la idea de la prueba de categorías del experimento en línea del estudio
                <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
                </a>
                .
                </p>
                """
        return text

    elif menu.lower() == "settings":
        return "Ajustes"

    else:
        return "¡Valor desconocido!"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Centro de información"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La escala GRBAS es una herramienta para evaluar trastornos de la voz.
                    A menudo se utiliza para estimar la severidad de la disfonía, medir y documentar el éxito de una terapia,
                    y ayudar a los expertos a formular un diagnóstico.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                La abreviatura GRBAS corresponde a cinco características: Grado (G), Rugosidad (R), Soplosidad (B),
                Astenia (A) y Tensión (S).
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                La evaluación de estos parámetros se basa en un sistema de puntuación con valores
                que van de 0 (sin desviación respecto a patrones vocales normales) a 3 (desviación severa).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Grabaciones de parámetros"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "Ajustes"

    else:
        return "¡Valor desconocido!"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Centro de información"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "home":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Además de los cinco parámetros habituales, este software también proporciona material de audio y
              descripciones de las características Inestabilidad (I) y Fluidez (F).
            </p>
            <p>Ambos amplían la escala original a IF-GRBAS, lo cual es útil en el contexto de la evaluación de la disfonía,
            especialmente en la disfonía espasmódica.
            <p>
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Para una justificación detallada de esta ampliación, consulte el siguiente estudio:
              <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
              </a>
            </p>"""

        return text

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Grabaciones de parámetros"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "Ajustes"

    else:
        return "¡Valor desconocido!"


def label_text_4(menu, var_1=0):

    if menu.lower() == "info":
        return "Centro de información"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

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
            text = "Inestabilidad (2/9)"
        elif var_1 == 3:
            text = "Fluidez (3/9)"
        elif var_1 == 4:
            text = "Extension (4/9)"
        elif var_1 == 5:
            text = "Grade (5/9)"
        elif var_1 == 6:
            text = "Rugosidad (6/9)"
        elif var_1 == 7:
            text = "Soplosidad (7/9)"
        elif var_1 == 8:
            text = "Astenia (8/9)"
        elif var_1 == 9:
            text = "Tensión (9/9)"
        else:
            text = "N/V"
        return text

    elif menu.lower() == "recordings":
        return "Selección de filtros"

    elif menu.lower() == "training":
        return "Próximamente:"

    elif menu.lower() == "settings":
        return "Ajustes"

    else:
        return "¡Valor desconocido!"


def label_text_5(menu):
    if menu.lower() == "info":
        return "Información de versión"

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
                Sugerencia: ¡No dudes en echar un vistazo a las opciones de derechos de autor en el menú de configuración!
                </p>
                """
        return text

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial; color: #DB8004;">
                    Nota: antes de usar este software, consulte la declaración de copyright (primer menú arriba a la derecha).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Archivos de audio filtrados"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        text = """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 22px; color: #8B0000;">
                    Nota: para aplicar todos los cambios, la aplicación debe reiniciarse.
                </p>"""
        return text

    else:
        return "¡Valor desconocido!"


def label_text_6(menu, var=0):
    if menu.lower() == "info":
        return "Centro de información"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Reproductor multimedia"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFF;">
                        Definir la apariencia visual de GRBAS_Mate
                    </p>"""
        elif var == 2:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                            Gestionar avisos de copyright en GRBAS_Mate
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                                Controlar el comportamiento del reproductor multimedia
                      </p>"""

    else:
        return "¡Valor desconocido!"


def label_text_7(menu):
    if menu.lower() == "info":
        return "Centro de información"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Parámetro"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Tema de color:
                            </p>"""

    else:
        return "¡Valor desconocido!"


def label_text_8(menu, var=0):
    if menu.lower() == "info":
        return "Centro de información"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Severidad"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; 
            font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Idioma:
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Calidad de renderizado de audio:
                      </p>"""

    else:
        return "¡Valor desconocido!"


def label_text_9(menu):
    if menu.lower() == "info":
        return "Centro de información"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Género del hablante"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "Ajustes"

    else:
        return "¡Valor desconocido!"


def label_text_10(menu):
    if menu.lower() == "info":
        return "Centro de información"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Tipo de articulación"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "Ajustes"

    else:
        return "¡Valor desconocido!"


def label_text_11(menu):
    if menu.lower() == "info":
        return "Centro de información"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Grabaciones"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "Ajustes"

    else:
        return "¡Valor desconocido!"


# Textual input for buttons --------------------------------------------------------------------------------------------

def button_assistance_1(menu):
    if menu.lower() == "info":
        return "Descripción de la versión"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Grabaciones de parámetros"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "General / Interfaz"

    else:
        return "¡Valor desconocido!"


def button_assistance_2(menu):
    if menu.lower() == "info":
        return "Perspectivas futuras"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Grabaciones de parámetros"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "Opciones de copyright"

    else:
        return "¡Valor desconocido!"


def button_assistance_3(menu):
    if menu.lower() == "info":
        return "Declaración de copyright"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Grabaciones de parámetros"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "Reproductor multimedia"

    else:
        return "¡Valor desconocido!"


def button_assistance_4(menu):
    if menu.lower() == "info":
        return "Declaración de copyright"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guía de usuario"

    elif menu.lower() == "home":
        return "Inicio"

    elif menu.lower() == "description":
        return "Descripciones de parámetros"

    elif menu.lower() == "recordings":
        return "Grabaciones de parámetros"

    elif menu.lower() == "training":
        return "Modo de entrenamiento"

    elif menu.lower() == "settings":
        return "Reiniciar ahora"

    else:
        return "¡Valor desconocido!"


def QComboBox_parameter_filter():
    return ["(I) Inestabilidad", "(F) Fluidez", "(G) Grado", "(R) Rugosidad",
            "(B) Soplosidad", "(A) Astenia", "(S) Tensión", "Todas las opciones"]


def QComboBox_severity_filter():
    return ["Nivel 0", "Nivel 1", "Nivel 2", "Nivel 3", "Asc. 0-3", "Todas las opciones"]


def QComboBox_gender_filter():
    return ["Hombre", "Mujer", "Todas las opciones"]


def QComboBox_articulation_filter():
    return ["Vocal", "Frase", "Ambos en 1 archivo", "Todas las opciones"]


def QComboBox_colour_choice():
    return ["Claro", "Oscuro"]


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
    return "   Mostrar aviso de copyright en el menú Inicio"


def QCheckbox_copyright_headline():
    return "   Mostrar aviso de copyright en el título principal"


def QCheckbox_remember_faf():
    return "   Recordar archivos de audio filtrados"


def QCheckbox_remember_mps():
    return "   Recordar ajustes del reproductor"


def QCheckbox_autoplay_recordings():
    return "   Reproducir grabaciones automáticamente tras cargar"


def QComboBox_audio_render_quality_choice():
    return ["Debug:\t\t1 FPS",
            "Eco:\t\t10 FPS",
            "Normal:\t33 FPS",
            "Alta:\t\t60 FPS",
            "Ultra:\t\t100 FPS"]
