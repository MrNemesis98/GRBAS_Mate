"""
Copyright © MrNemesis98, GitHub, 2026

Co-Author of this file:
- Institution:
- Mail:
- Github:

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
        return "Centrum Informacji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Nagrania parametrów"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Ustawienia"

    else:
        return "Nieznana wartość!"


def label_text_1(menu, var_1=0, software_version=""):
    if menu.lower() == "info":
        # Version Information
        if var_1 == 1:
            text = f"""
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Aktualnie zainstalowana wersja:	{software_version}
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Ta pierwsza wersja zawiera opisy wszystkich parametrów skali GRBAS,
                    wraz z jej rozszerzeniem IF-GRBAS. Dodatkowo dostępne są otwarte nagrania
                    referencyjne dla każdego parametru w kilku poziomach nasilenia.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Program i materiały open access mają wspierać fonetykę kliniczną
                    oraz służyć do nauki, oceny domowej i (w razie potrzeby) diagnostyki laryngologicznej.
                </p>"""
            return text
        # Future Outlook
        elif var_1 == 2:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        GRBAS_Mate jest nadal rozwijany. Kolejne wersje będą zawierały więcej nagrań
                        dla skali IF-GRBAS. Możliwe jest też dodanie innych skal, np. CAPE-V.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Planowany jest także tryb treningowy: odsłuch nagrań i ocena wg IF-GRBAS.
                        To będzie test umiejętności rozpoznawania siedmiu parametrów w głosach dysfonicznych.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Ostatnim krokiem ma być automatyczna analiza jakości głosu, zintegrowana z programem.
                        Będzie to część projektu pracy magisterskiej (plan: jesień 2026).
                    </p>"""
            return text
        # Copyright
        elif var_1 == 3:
            text = """<p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2026
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                To oprogramowanie opublikowano na licencji MIT (tekst licencji):
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
                  Korzystając z GRBAS_Mate lub jego komponentów, akceptujesz powyższe warunki. 
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Wskazówka: Zobacz opcje praw autorskich w menu ustawień!
                </p>"""
            return text

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    To darmowa aplikacja, która pozwala odsłuchiwać liczne przykłady zaburzeń głosu
                    i porównywać je z eksperckim wzorcem.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Powstała z myślą o nauce, ale może też wspierać ocenę domową oraz praktykę kliniczną.
                </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Ta wersja udostępnia nagrania parametrów skali GRBAS w różnych poziomach nasilenia.
                </p>
                """
        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    W tym menu znajdziesz jasne, zwięzłe <span style="font-weight:bold;color:#0B839C;">
                    opisy</span> wszystkich parametrów IF-GRBAS.
                    Użyj strzałek, aby przechodzić między stronami, albo wybierz temat z listy poniżej.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Jeśli chcesz pominąć opisy, przykładowe nagrania znajdziesz w menu nagrań
                    (trzecia opcja na lewym pasku nawigacji).
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Możesz też przejść bezpośrednio do nagrań wybranego parametru, klikając słuchawki
                    w prawym rogu.
                    </p>

                    """
        elif var_1 == 2:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Niestabilność</span> głosu.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Oznacza stopień nieregularności i wahań stabilności głosu.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Głos niestabilny brzmi „chwiejnie” i może silnie zmieniać głośność oraz wysokość.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Niestabilność nie należy do <span style="font-weight:bold;color:#0B839C;">oryginalnej</span>
                     skali GRBAS, ale może ją <span style="font-weight:bold;color:#7030A0;">rozszerzać</span>.
                    </p>
                    """
        elif var_1 == 3:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Płynność</span> głosu jest porównywalna do płynności mowy.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Odnosi się do tego, jak gładko i swobodnie brzmi głos podczas mówienia.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Dotyczy głównie rytmu mowy, pauz oraz ciągłości wypowiedzi.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Płynność nie należy do <span style="font-weight:bold;color:#0B839C;">oryginalnej</span>
                     skali GRBAS, ale może ją <span style="font-weight:bold;color:#7030A0;">rozszerzać</span>.
                    </p>
                    """
        elif var_1 == 4:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#7030A0;">Rozszerzenie</span> skali GRBAS wprowadzono,
                    aby bardziej szczegółowo opisać cechy głosu dysfonicznego i zwiększyć czułość skali
                    wobec wybranych objawów.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Skala bywa rozszerzana o parametry lepiej oddające charakterystykę dysfonii,
                    zależnie od kontekstu i celów badania.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Uzasadnienie tego rozszerzenia znajdziesz w poniższym opracowaniu:
                        <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                            style="text-decoration:none; color:#1a73e8;">
                            Voice Quality and Dysphonia (projekt OSF - podgląd)
                        </a>
                    </p>"""
        elif var_1 == 5:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Stopień</span> chrypki w głosie.   
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Chrypka składa się z kilku cech, m.in. szorstkości, oddechowości i napięcia.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Można ją opisać jako ogólne wrażenie głosu wynikające z tych parametrów. 
                    </p>
                    """
        elif var_1 == 6:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Szorstkość</span> głosu.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    To wrażenie nieregularnych drgań fałdów głosowych, przez co głos brzmi
                    szorstko lub „drapiąco”.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">

                    </p>
                    """
        elif var_1 == 7:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Oddechowość</span> głosu.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Odnosi się do słyszalnego „uciekania” powietrza w głosie.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Może wskazywać na niepełne zwarcie fałdów głosowych.
                    </p>
                    """
        elif var_1 == 8:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Wrażenie słabości głosu.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nAsthenia</span> opisuje, na ile głos
                    brzmi słabo lub cicho.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Jest to zwykle efekt obniżonego napięcia fałdów głosowych.
                    </p>
                    """
        elif var_1 == 9:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Wrażenie napięcia głosu.  
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">\nNapięcie</span> opisuje stopień hiperfunkcji
                    lub nadmiernego wysiłku mięśni krtani,
                    co wpływa na fałdy głosowe i jest słyszalne w głosie.
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
        return "Tryb nauki"

    elif menu.lower() == "training":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Tryb treningowy jest obecnie w fazie rozwoju.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                W tym trybie będziesz mógł sprawdzić umiejętności, oceniając nagrania głosów
                dysfonicznych. Dla danego materiału audio przypiszesz poprawny parametr i poziom nasilenia. 
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Tryb opiera się na idei testu kategoryzacji z eksperymentu online w badaniu
                <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (projekt OSF - podgląd)
                </a>
                .
                </p>
                """
        return text

    elif menu.lower() == "settings":
        return "Ustawienia"

    else:
        return "Nieznana wartość!"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Centrum Informacji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Skala GRBAS służy do oceny zaburzeń głosu.
                    Często stosuje się ją do oceny nasilenia dysfonii, dokumentowania efektów terapii
                    oraz jako wsparcie w stawianiu diagnozy.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Skrót GRBAS oznacza pięć cech: Stopień (G), Szorstkość (R), Oddechowość (B),
                Asthenia (A) oraz Napięcie (S).
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Ocena opiera się na skali punktowej od 0 (brak odchyleń od normy)
                do 3 (silne odchylenie).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Nagrania parametrów"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Ustawienia"

    else:
        return "Nieznana wartość!"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Centrum Informacji"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "home":
        text = """
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Oprócz pięciu podstawowych parametrów, program udostępnia też nagrania i opisy
              cech Niestabilność (I) oraz Płynność (F).
            </p>
            <p>Obie cechy rozszerzają skalę do IF-GRBAS, co bywa użyteczne w ocenie dysfonii,
            zwłaszcza w dysfonii spastycznej.
            <p>
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Uzasadnienie tego rozszerzenia znajdziesz w poniższym opracowaniu:
              <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (projekt OSF - podgląd)
              </a>
            </p>"""

        return text

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Nagrania parametrów"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Ustawienia"

    else:
        return "Nieznana wartość!"


def label_text_4(menu, var_1=0):

    if menu.lower() == "info":
        return "Centrum Informacji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

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
        return "Wybór filtrów"

    elif menu.lower() == "training":
        return "Wkrótce:"

    elif menu.lower() == "settings":
        return "Ustawienia"

    else:
        return "Nieznana wartość!"


def label_text_5(menu):
    if menu.lower() == "info":
        return "Informacje o wersji"

    elif menu.lower() == "copyright":
        text = """<p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                  Copyright © MrNemesis98, GitHub, 2025
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                Oprogramowanie opublikowano na licencji MIT (tekst licencji):
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
                  Korzystając z GRBAS_Mate lub jego komponentów, akceptujesz powyższe warunki. 
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                Wskazówka: Zobacz opcje praw autorskich w menu ustawień!
                </p>
                """
        return text

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        text = """
                <p style="text-align: justify; line-height: 1.2; font-family: Arial; color: #DB8004;">
                    Uwaga: Przed użyciem programu zobacz oświadczenie o prawach autorskich
                    (pierwsze menu w prawym górnym rogu).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Przefiltrowane pliki"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        text = """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 22px; color: #8B0000;">
                    Uwaga: Aby zastosować zmiany, aplikację trzeba uruchomić ponownie.
                </p>"""
        return text

    else:
        return "Nieznana wartość!"


def label_text_6(menu, var=0):
    if menu.lower() == "info":
        return "Centrum Informacji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Odtwarzacz"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFF;">
                        Ustal wygląd interfejsu GRBAS_Mate
                    </p>"""
        elif var == 2:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                            Zarządzaj napisami copyright w GRBAS_Mate
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                                Steruj zachowaniem odtwarzacza
                      </p>"""

    else:
        return "Nieznana wartość!"


def label_text_7(menu):
    if menu.lower() == "info":
        return "Centrum Informacji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Parametr"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Motyw kolorów:
                            </p>"""

    else:
        return "Nieznana wartość!"


def label_text_8(menu, var=0):
    if menu.lower() == "info":
        return "Centrum Informacji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Nasilenie"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; 
            font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Język:
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Jakość renderu audio:
                      </p>"""

    else:
        return "Nieznana wartość!"


def label_text_9(menu):
    if menu.lower() == "info":
        return "Centrum Informacji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Płeć lektora"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Ustawienia"

    else:
        return "Nieznana wartość!"


def label_text_10(menu):
    if menu.lower() == "info":
        return "Centrum Informacji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Rodzaj artykulacji"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Ustawienia"

    else:
        return "Nieznana wartość!"


def label_text_11(menu):
    if menu.lower() == "info":
        return "Centrum Informacji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Nagrania"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Ustawienia"

    else:
        return "Nieznana wartość!"


# Textual input for buttons --------------------------------------------------------------------------------------------

def button_assistance_1(menu):
    if menu.lower() == "info":
        return "Opis wersji"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Nagrania parametrów"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Ogólne / GUI"

    else:
        return "Nieznana wartość!"


def button_assistance_2(menu):
    if menu.lower() == "info":
        return "Plany rozwoju"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Nagrania parametrów"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Opcje praw"

    else:
        return "Nieznana wartość!"


def button_assistance_3(menu):
    if menu.lower() == "info":
        return "Copyright Statement"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Nagrania parametrów"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Odtwarzacz"

    else:
        return "Nieznana wartość!"


def button_assistance_4(menu):
    if menu.lower() == "info":
        return "Copyright Statement"

    elif menu.lower() == "copyright":
        return "Prawa autorskie"

    elif menu.lower() == "faq":
        return "Instrukcja użytkownika"

    elif menu.lower() == "home":
        return "Strona główna"

    elif menu.lower() == "description":
        return "Opisy parametrów"

    elif menu.lower() == "recordings":
        return "Nagrania parametrów"

    elif menu.lower() == "training":
        return "Tryb treningowy"

    elif menu.lower() == "settings":
        return "Uruchom ponownie"

    else:
        return "Nieznana wartość!"


def QComboBox_parameter_filter():
    return ["(I) Niestabilność", "(F) Płynność", "(G) Stopień", "(R) Szorstkość",
            "(B) Oddechowość", "(A) Asthenia", "(S) Napięcie", "Wszystkie"]


def QComboBox_severity_filter():
    return ["Poziom 0", "Poziom 1", "Poziom 2", "Poziom 3", "Rosn. 0-3", "Wszystkie"]


def QComboBox_gender_filter():
    return ["Mężczyzna", "Kobieta", "Wszystkie"]


def QComboBox_articulation_filter():
    return ["Samogłoska", "Zdanie", "Oba w 1 pliku", "Wszystkie"]


def QComboBox_colour_choice():
    return ["Jasny", "Ciemny"]


def QComboBox_language_choice():
    return ["English", "Deutsch", "Italiano", "Español", "Français", "Polski", "Türkçe"]


def QCheckbox_copyright_home():
    return "   Pokaż prawa aut. w Home"


def QCheckbox_copyright_headline():
    return "   Pokaż prawa aut. w nagłówku"


def QCheckbox_remember_faf():
    return "   Pamiętaj filtrowane pliki"


def QCheckbox_remember_mps():
    return "   Pamiętaj ustawienia playera"


def QCheckbox_autoplay_recordings():
    return "   Autoplay po wczytaniu"


def QComboBox_audio_render_quality_choice():
    return ["Debug:\t\t1 FPS",
            "Eco:\t\t10 FPS",
            "Normal:\t33 FPS",
            "High:\t\t60 FPS",
            "Ultra:\t\t100 FPS"]
