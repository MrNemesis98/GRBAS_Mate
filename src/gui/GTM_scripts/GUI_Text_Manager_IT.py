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
    return (
        ("   GRBAS_Mate   [ɡɹæps me͜ɪt̚]\t\tCopyright © MrNemesis98, GitHub, 2026")
        if with_copyright
        else "   GRBAS_Mate   [ɡɹæps me͜ɪt̚]"
    )


def label_menu_title(menu):
    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "copyright":
        return "Informazioni sul copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Registrazioni dei parametri"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Impostazioni"

    else:
        return "Valore sconosciuto!"


def label_text_1(menu, var_1=0, software_version=""):
    if menu.lower() == "info":
        # Version Information
        if var_1 == 1:
            text = f"""
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Versione di questo software attualmente installata
                    :	{software_version}
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Questa prima versione del softwarecontiene descrizioni dettagliate di ogni parametro della scala GRBAS comunemente utilizzata, inclusa la sua estensione IF-GRBAS. Inoltre, sono disponibili registrazioni open source di esempi per ogni parametro, a diversi livelli della scala. # what do you mean by "severity levels"
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Questo software, insieme al suo materiale open access, intende contribuire al campo della fonetica clinica e fungere da strumento in contesti di studio, per l’autovalutazione a casa o persino per la diagnostica ORL.
                </p>"""
            return text
        # Future Outlook
        elif var_1 == 2:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        GRBAS_Mate è ancora in fase di sviluppo. Le versioni future saranno dotate di più registrazioni di esempi
                        per la scala IF-GRBAS. Sarà anche possibile includere scale e sistemi di misura alternativi, come CAPE-V.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Nelle versioni future, è prevista anche una Modalità Allenamento in cui si potranno ascoltare registrazioni e valutarle
                        basandosi sulla scala IF-GRBAS. Questa funzione servirà a mettera alla prova l'utente e ad affinare le sue capacità nell'individuare i sette parametri della scala in registrazioni con voci realmente disfoniche.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        La versione finale includerà uno strumento che permetterà l'analisi automatica della qualità vocale e sarà parte di un progetto di tesi magistrale ed è previsto per l’autunno 2026.
                    </p>"""
            return text
        # Copyright
        elif var_1 == 3:
            text = """<p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2026
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Questo software è stato pubblicato con licenza MIT, dichiarata come segue:
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
                  Utilizzando GRBAS_Mate o uno dei suoi componenti, l'utente accetta tutte queste condizioni.
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Suggerimento: dai un'occhiata alle opzioni relative al copyright nel menù impostazioni!
                </p>"""
            return text

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Questa è un'app gratuita che consente agli utenti di ascoltare numerosi esempi di diverse
                    disfunzioni vocali e associarli a delle scale di riferimento standard.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                È stata creata come materiale di studio per lezioni o autoapprendimento, ma può anche fungere da strumento di supporto
                in un contesto professionale.
                </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Questa prima versione fornisce esempi di registrazioni di diversi parametri della scala GRBAS,
                a diversi livelli.
                </p>
                """
        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    In questo menù puoi esplorare le<span style="font-weight:bold;color:#0B839C;">descrizioni</span>
                    di ogni parametro IF-GRBAS.
                    Utilizza i pulsanti freccia per navigare tra le pagine o sceglile direttamente dalla panoramica qui sotto.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Se vuoi saltare le descrizioni, puoi anche accedere a campioni audio tramite il menù registrazioni
                    (terza opzione nella barra di navigazione a sinistra).
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    È anche possibile passare direttamente alle registrazioni del parametro selezionato
                    facendo clic sull'icona a forma di cuffie nell’angolo destro.
                    </p>

                    """
        elif var_1 == 2:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Instabilità</span> della voce.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Si riferisce al grado di irregolarità e alle fluttuazioni nella stabilità della voce.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Una voce instabile suona sbilanciata e può variare molto in intensità e altezza (pitch).
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    L’instabilità non fa parte della scala GRBAS <span style="font-weight:bold;color:#0B839C;">originale</span>,
                     ma può essere usata per <span style="font-weight:bold;color:#7030A0;">estenderla</span>.
                    </p>
                    """
        elif var_1 == 3:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La <span style="font-weight:bold;color:#7030A0;">fluidità</span> di una voce si riferisce al
                    flusso del parlato.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Fa rifereimento a quanto la voce suoni scorrevole e fluida durante il parlato.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Riguarda principalmente il ritmo del parlato, la struttura delle pause e la continuità.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La fluidità non fa parte della scala GRBAS <span style="font-weight:bold;color:#0B839C;">originale</span>,
                     ma può essere usata per <span style="font-weight:bold;color:#7030A0;">estenderla</span>.
                    </p>
                    """
        elif var_1 == 4:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    L’<span style="font-weight:bold;color:#7030A0;">estensione</span> della scala GRBAS è stata introdotta
                    per includere le caratteristiche delle voci disfoniche in modo più accurato, migliorando la capacità della scala
                    nel descrivere determinati sintomi.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La scala viene spesso estesa includendo parametri che descrivono meglio le caratteristiche delle voci disfoniche,
                    sempre a seconda del contesto e degli obiettivi della ricerca.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Per una motivazione dettagliata di questa estensione, si prega di consultare il seguente studio:
                        <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                            style="text-decoration:none; color:#1a73e8;">
                            Voice Quality and Dysphonia (OSF project - view-only)
                        </a>
                    </p>"""
        elif var_1 == 5:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Il <span style="font-weight:bold;color:#0B839C;">grado</span> di raucedine nella voce.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La raucedine è composta da diverse caratteristiche, tra cui la sonorizzazione aspirata e lo sforzo.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Può essere descritta come l’impressione complessiva della voce in funzione di questi parametri individuali.
                    </p>
                    """
        elif var_1 == 6:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Raucedine</span>.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Descrive la percezione di una vibrazione irregolare delle pliche vocali, facendo sì che la voce suoni
                    ruvida o «graffiante».
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">

                    </p>
                    """
        elif var_1 == 7:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Sonorizzazione aspirata</span> della voce.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Si riferisce alla fuoriuscita udibile di aria nella voce.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Ciò può indicare una chiusura incompleta delle corde vocali.
                    </p>
                    """
        elif var_1 == 8:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Debolezza della voce.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">
Astenia</span> descrive in che misura la voce
                    appare debole o poco sonora.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Questa caratteristica è il risultato di una ridotta tensione nelle corde vocali.
                    </p>
                    """
        elif var_1 == 9:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Impressione di tensione nella voce.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">
Sforzo</span> descrive il grado di iperfunzione
                    o sovraccarico dei muscoli laringei,
                    che influisce sulle corde vocali ed è quindi udibile nella voce.
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
        return "Modalità Allenamento"

    elif menu.lower() == "allenamento":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                La modalità allenamento è attualmente in sviluppo.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                In questa modalità potrai mettere alla prova le tue competenze e conoscenze valutando registrazioni di voci disfoniche.
                Dato un insieme di materiale audio, dovrai assegnare il parametro corretto e il livello di gravità corrispondente.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Questa modalità si basa sull'idea del test di categoria proposto nell'esperimento online dello studio
                <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
                </a>
                .
                </p>
                """
        return text

    elif menu.lower() == "settings":
        return "Impostazioni"

    else:
        return "Valore sconosciuto!"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    La scala GRBAS è uno strumento per valutare i disturbi della voce.
                    Viene spesso utilizzata per stimare la gravità della disfonia, misurare e documentare il successo della terapia,
                    e assistere gli esperti nella formulazione di una diagnosi.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                L’abbreviazione GRBAS indica cinque caratteristiche: Grado (G), Raucedine (R), Sonorizzazione aspirata o "Breathiness" (B),
                Astenia (A) e Sforzo (S).
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                La valutazione di questi parametri si basa su un sistema di punteggio con valori
                che vanno da 0 (nessuna deviazione dai pattern vocali normali) a 3 (deviazione severa).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Registrazioni dei parametri"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Impostazioni"

    else:
        return "Valore sconosciuto!"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "home":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Oltre ai cinque parametri standard, questo software fornisce anche materiale audio e
              descrizioni per le caratteristiche Instabilità (I) e Fluidità (F).
            </p>
            <p>Entrambe estendono la scala originale a IF-GRBAS, utile nel contesto della valutazione della disfonia,
            soprattutto nella disfonia spasmodica.
            <p>
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Per una motivazione dettagliata di questa estensione, si prega di consultare il seguente studio:
              <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF project - view-only)
              </a>
            </p>"""

        return text

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Registrazioni dei parametri"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Impostazioni"

    else:
        return "Valore sconosciuto!"


def label_text_4(menu, var_1=0):

    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

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
            text = "Instabilità (2/9)"
        elif var_1 == 3:
            text = "Fluidità (3/9)"
        elif var_1 == 4:
            text = "Estensione (4/9)"
        elif var_1 == 5:
            text = "Grado (5/9)"
        elif var_1 == 6:
            text = "Raucedine (6/9)"
        elif var_1 == 7:
            text = "Sonorizzazione aspirata (7/9)"
        elif var_1 == 8:
            text = "Astenia (8/9)"
        elif var_1 == 9:
            text = "Sforzo (9/9)"
        else:
            text = "N/V"
        return text

    elif menu.lower() == "recordings":
        return "Selezione filtri"

    elif menu.lower() == "allenamento":
        return "Prossimamente:"

    elif menu.lower() == "settings":
        return "Impostazioni"

    else:
        return "Valore sconosciuto!"


def label_text_5(menu):
    if menu.lower() == "info":
        return "Informazioni sulla versione"

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
        return "Guida utente"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial; color: #DB8004;">
                    Nota: prima di usare questo software, consultare la dichiarazione di copyright (primo menu in alto a destra).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "File audio filtrati"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        text = """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 22px; color: #8B0000;">
                    Nota: per applicare tutte le modifiche è necessario riavviare l’app.
                </p>"""
        return text

    else:
        return "Valore sconosciuto!"


def label_text_6(menu, var=0):
    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Lettore multimediale"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFF;">
                        Definisci l’aspetto visivo di GRBAS_Mate
                    </p>"""
        elif var == 2:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                            Gestisci gli avvisi di copyright in GRBAS_Mate
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                                Controlla il comportamento del lettore multimediale
                      </p>"""

    else:
        return "Valore sconosciuto!"


def label_text_7(menu):
    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Parametro"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Tema colori:
                            </p>"""

    else:
        return "Valore sconosciuto!"


def label_text_8(menu, var=0):
    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Gravità"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2;
            font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Lingua:
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Qualità di rendering audio:
                      </p>"""

    else:
        return "Valore sconosciuto!"


def label_text_9(menu):
    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Genere del parlante"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Impostazioni"

    else:
        return "Valore sconosciuto!"


def label_text_10(menu):
    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Tipo di articolazione"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Impostazioni"

    else:
        return "Valore sconosciuto!"


def label_text_11(menu):
    if menu.lower() == "info":
        return "Centro informazioni"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Registrazioni"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Impostazioni"

    else:
        return "Valore sconosciuto!"


# Textual input for buttons --------------------------------------------------------------------------------------------


def button_assistance_1(menu):
    if menu.lower() == "info":
        return "Descrizione della versione"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Registrazioni dei parametri"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Generale / Interfaccia"

    else:
        return "Valore sconosciuto!"


def button_assistance_2(menu):
    if menu.lower() == "info":
        return "Prospettive future"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Registrazioni dei parametri"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Opzioni di copyright"

    else:
        return "Valore sconosciuto!"


def button_assistance_3(menu):
    if menu.lower() == "info":
        return "Dichiarazione di copyright"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Registrazioni dei parametri"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Lettore multimediale"

    else:
        return "Valore sconosciuto!"


def button_assistance_4(menu):
    if menu.lower() == "info":
        return "Dichiarazione di copyright"

    elif menu.lower() == "copyright":
        return "Copyright"

    elif menu.lower() == "faq":
        return "Guida utente"

    elif menu.lower() == "home":
        return "Home"

    elif menu.lower() == "description":
        return "Descrizioni dei parametri"

    elif menu.lower() == "recordings":
        return "Registrazioni dei parametri"

    elif menu.lower() == "allenamento":
        return "Modalità Allenamento"

    elif menu.lower() == "settings":
        return "Riavvia ora"

    else:
        return "Valore sconosciuto!"


def QComboBox_parameter_filter():
    return [
        "(I) Instabilità",
        "(F) Fluidità",
        "(G) Grado",
        "(R) Raucedine",
        "(B) Sonorizzazione aspirata",
        "(A) Astenia",
        "(S) Sforzo",
        "Tutte le opzioni",
    ]


def QComboBox_severity_filter():
    return [
        "Livello 0",
        "Livello 1",
        "Livello 2",
        "Livello 3",
        "Cresc. 0-3",
        "Tutte le opzioni",
    ]


def QComboBox_gender_filter():
    return ["Maschio", "Femmina", "Tutte le opzioni"]


def QComboBox_articulation_filter():
    return ["Vocale", "Frase", "Entrambi in 1 file", "Tutte le opzioni"]


def QComboBox_colour_choice():
    return ["Chiaro", "Scuro"]


def QComboBox_language_choice():
    return [
        "English",
        "Deutsch",
        "Italiano",
        "Español",
        "Français",
        "Lëtzebuergesch",
        "Nederlands",
        "Polski",
        "Türkçe",
    ]


def QCheckbox_copyright_home():
    return "   Mostra avviso di copyright nel menu Home"


def QCheckbox_copyright_headline():
    return "   Mostra avviso di copyright nel titolo principale"


def QCheckbox_remember_faf():
    return "   Ricorda i file audio filtrati"


def QCheckbox_remember_mps():
    return "   Ricorda le impostazioni del lettore"


def QCheckbox_autoplay_recordings():
    return "   Riproduci automaticamente le registrazioni dopo il caricamento"


def QComboBox_audio_render_quality_choice():
    return [
        "Debug:\t\t1 FPS",
        "Eco:\t\t10 FPS",
        "Normale:\t33 FPS",
        "Alta:\t\t60 FPS",
        "Ultra:\t\t100 FPS",
    ]
