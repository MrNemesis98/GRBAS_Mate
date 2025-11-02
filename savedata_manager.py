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

"""
Settings for GRBAS_Mate:
- (L1) Language: English (default), Deutsch, Italiano, Espanol (, Polski)
- (CRS) Copyright Settings: Show_statement_in_home_menu, show_statement_in_headline_bar
- (AS) Audio Settings: Volume, Play_Recordings_Automatically

Language Settings already implemented here.
"""


sd = open("src/sys/savedata.txt", "r")
raw_data = sd.readlines()
sd.close()

# Sector 1: Manage Language Settings -------------------------------------------------------------------------
lang_savedata = raw_data[0]
lang_savedata_list = lang_savedata.split('/')
lang_savedata_list.remove(lang_savedata_list[0])

current_language = str((lang_savedata_list[0]))


def update_savedata():
    global current_language

    # Save data from other sectors before overwriting
    sd = open("src/sys/savedata.txt", "r")
    new_savedata = sd.readlines()
    lang_data = new_savedata[0]
    sd.close()

    # write savedata.txt, update database data only
    sd = open("src/sys/savedata.txt", "w")
    text = ("L1:/" + str(current_language) +
            "/\n")
    sd.write(text)
    sd.close()


def get_current_language():
    global current_language
    return current_language


def set_current_language(lang="en"):
    global current_language
    current_language = lang
    update_savedata()


print(get_current_language())
set_current_language()
print(get_current_language())

"""
# Sector 2: Manage system variables for console.py ---------------------------------------------------------------------
system_data = data[1]
variables_list = system_data.split('/')
variables_list.remove(variables_list[0])
first_start = (variables_list[0].split(":")[1])
term_output_policy = (variables_list[1].split(":")[1])
one_line_output = (variables_list[2].split(":")[1])
headline_printing = (variables_list[3].split(":")[1])
alphabetical_output = variables_list[4].split(":")
auto_scan_filters = variables_list[5].split(":")[1]
output_detail_level = (variables_list[6].split(":")[1])
system_sound_level = (variables_list[7].split(":")[1])
request_error = (variables_list[8].split(":")[1])


def update_system_data():
    global data
    global first_start
    global term_output_policy
    global one_line_output
    global headline_printing
    global alphabetical_output
    global auto_scan_filters
    global output_detail_level
    global system_sound_level
    global request_error

    # Save data from other sectors before overwriting
    sd = open("src/data/savedata.txt", "r")
    data = sd.readlines()
    sd.close()

    # write savedata.txt, update system data only
    sd = open("src/data/savedata.txt", "w")
    text = ((database_data + "sys:" +
             "/fs:" + str(first_start) +
             "/top:" + str(term_output_policy) +
             "/onel:" + str(one_line_output) +
             "/hdlp:" + str(headline_printing) +
             "/" + str(alphabetical_output[0]) + ":" + str(alphabetical_output[1]) +
             "/asf:" + str(auto_scan_filters) +
             "/odlvl:" + str(output_detail_level) +
             "/ssl:" + str(system_sound_level) +
             "/re:" + str(request_error) +
             "/\n"))
    sd.write(text)
    sd.close()


def get_first_start():
    global first_start
    return True if first_start == "1" else False


def set_first_start(fs=False):
    global first_start
    first_start = "1" if fs else "0"
    update_system_data()


def get_term_output_policy():
    global term_output_policy
    return int(term_output_policy)


def get_term_output_policy_as_text():
    global term_output_policy
    if term_output_policy == "1":
        return "\t2) Term Output Policy:\t\tonly found terms"
    elif term_output_policy == "2":
        return "\t2) Term Output Policy:\t\tonly not found terms"
    else:
        return "\t2) Term Output Policy:\t\tall terms"


def set_term_output_policy(top):
    global term_output_policy
    term_output_policy = top
    update_system_data()


def get_one_line_output():
    global one_line_output
    return True if one_line_output == "1" else False


def get_one_line_output_as_text():
    global one_line_output
    if one_line_output == "1":
        return "\t3) Output Format:\t\tone-line"
    else:
        return "\t3) Output Format:\t\tmulti-line"


def set_one_line_output(onel):
    global one_line_output
    one_line_output = "1" if onel else "0"
    update_system_data()


def get_headline_printing():
    global headline_printing
    return int(headline_printing)


def get_headline_printing_as_text():
    global headline_printing
    if headline_printing == "1":
        return "\t4) Headline Printing:\t\tonly at top of excel"
    elif headline_printing == "2":
        return "\t4) Headline Printing:\t\tfor every new document scanned in"
    else:
        return "\t4) Headline Printing:\t\tfor every new term printed"


def set_headline_printing(hdlp):
    global headline_printing
    headline_printing = hdlp
    update_system_data()


def get_alphabetical_output():
    global alphabetical_output
    alphabetical = False
    ascending = False
    if alphabetical_output[0].split("=")[1] == "1":
        alphabetical = True
    if alphabetical_output[1].split("=")[1] == "1":
        ascending = True
    return alphabetical, ascending


def get_alphabetical_output_as_text():
    abc, asc = get_alphabetical_output()

    if abc and asc:
        return "\t5) Alphabetical Output:\t\talphabetical, ascending"
    elif abc and not asc:
        return "\t5) Alphabetical Output:\t\talphabetical, descending"
    else:
        return "\t5) Alphabetical Output:\t\tnon-alphabetical"


def set_alphabetical_output(abc, asc):
    global alphabetical_output
    alphabetical_output[0] = "abc=1" if abc else "abc=0"
    alphabetical_output[1] = "asc=1" if asc else "asc=0"
    update_system_data()


def get_auto_scan_filters():
    global auto_scan_filters
    return auto_scan_filters


def get_auto_scan_filters_as_text():
    global auto_scan_filters

    if auto_scan_filters == "Noun":
        return "\t6) Auto Scan PoS Filters:\tnouns only"
    elif auto_scan_filters == "Verb":
        return "\t6) Auto Scan PoS Filters:\tverbs only"
    elif auto_scan_filters == "Adjective":
        return "\t6) Auto Scan PoS Filters:\tadjectives only"
    elif auto_scan_filters == "Adverb":
        return "\t6) Auto Scan PoS Filters:\tadverbs only"
    elif auto_scan_filters == "Preposition":
        return "\t6) Auto Scan PoS Filters:\tprepositions only"
    elif auto_scan_filters == "Phrase":
        return "\t6) Auto Scan PoS Filters:\tphrases only"
    elif auto_scan_filters == "Noun, Verb, Adjective, Adverb, Preposition, Phrase":
        return "\t6) Auto Scan PoS Filters:\tall pos types, no restrictions"
    else:
        return "\t6) Auto Scan PoS Filters:\t" + str(auto_scan_filters)


def set_auto_scan_filters(asf):
    global auto_scan_filters
    auto_scan_filters = asf
    update_system_data()


def get_output_detail_level():
    global output_detail_level
    return int(output_detail_level)


def get_output_detail_level_as_text():
    global output_detail_level

    if output_detail_level == "1":
        return "\t7) Output Detail Level:\t\tlevel 1, term data"
    elif output_detail_level == "2":
        return "\t7) Output Detail Level:\t\tlevel 2, morph data"
    else:
        return "\t7) Output Detail Level:\t\tlevel 3, all data"


def set_output_detail_level(odlvl):
    global output_detail_level
    output_detail_level = odlvl
    update_system_data()


def get_system_sound_level():
    global system_sound_level
    return int(system_sound_level)


def get_system_sound_level_as_text():
    global system_sound_level
    if system_sound_level == "1":
        return "\t8) System Sound Level:\t\tlevel 1, no sounds"
    elif system_sound_level == "2":
        return "\t8) System Sound Level:\t\tlevel 2, notifications only"
    else:
        return "\t8) System Sound Level:\t\tlevel 3, all sounds"


def set_system_sound_level(ssl):
    global system_sound_level
    system_sound_level = ssl
    update_system_data()


def get_request_error():
    global request_error
    return int(request_error)


def set_request_error(error_code):
    global request_error
    request_error = str(error_code)
    update_system_data()
"""