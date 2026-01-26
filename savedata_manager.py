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

"""
Settings list for GRBAS_Mate:

1) GUI:     -> Colour Theme: Light (0), Dark (1, default))                                                       Restart
            -> Language:    English     (0, default)                                                             Restart
                            Deutsch     (1)
                            Italiano    (2)
                            Español     (3)
                            Français     (4)
                            Polski      (5)
                            Türkçe      (6)

2) CRS (Copyright Settings):    -> Show_home_statement:       yes (1, default), no (0)                  
                                -> Show_headline_statement:   yes (1, default), no (0)
                                
3) MPS (Media Player Settings):     -> remember_filtered_audio_files:    yes (1), no (0, default)                
                                    -> remember_media_player_settings:   yes (1), no (0, default)
                                    -> auto_play_recordings:             yes (1), no (0, default)
                                    -> audio_render_quality:       Debug: 1FPS (1000),      (0)                  Restart
                                                                   Eco: 10 FPS (100ms),     (1)
                                                                   Normal: 30 FPS (33ms),   (2, default)
                                                                   High: 60 FPS (16ms),     (3)
                                                                   Ultra: 100 FPS (10ms)    (4)
"""


sd = open("src/sys/savedata.txt", "r")
raw_data = sd.readlines()
sd.close()


# Sector 1: Load GUI Settings ------------------------------------------------------------------------------------------
GUI_savedata = raw_data[0]
GUI_savedata_list = GUI_savedata.split('/')
GUI_savedata_list.remove(GUI_savedata_list[0])
GUI_savedata_list.remove(GUI_savedata_list[-1])

colour_theme = int((GUI_savedata_list[0]).split(":")[1])
current_language = int((GUI_savedata_list[1]).split(":")[1])


# Sector 2: Load Copyright Settings ------------------------------------------------------------------------------------
CRS_savedata = raw_data[1]
CRS_savedata_list = CRS_savedata.split('/')
CRS_savedata_list.remove(CRS_savedata_list[0])
CRS_savedata_list.remove(CRS_savedata_list[-1])

show_home_statement = int((CRS_savedata_list[0]).split(":")[1])
show_headline_statement = int((CRS_savedata_list[1]).split(":")[1])

# Sector 3: Load Media Player Settings ---------------------------------------------------------------------------------
MPS_savedata = raw_data[2]
MPS_savedata_list = MPS_savedata.split('/')
MPS_savedata_list.remove(MPS_savedata_list[0])
MPS_savedata_list.remove(MPS_savedata_list[-1])

remember_filtered_audio_files = int((MPS_savedata_list[0]).split(":")[1])
remember_media_player_settings = int((MPS_savedata_list[1]).split(":")[1])
auto_play_recordings = int((MPS_savedata_list[2]).split(":")[1])
audio_render_quality = int((MPS_savedata_list[3]).split(":")[1])


# Sector 4: Generic Functions ------------------------------------------------------------------------------------------
def update_savedata():
    global colour_theme
    global current_language
    global show_home_statement
    global show_headline_statement
    global remember_filtered_audio_files
    global remember_media_player_settings
    global auto_play_recordings
    global audio_render_quality

    # write savedata.txt
    sd = open("src/sys/savedata.txt", "w")
    text = ("GUI" +
            "/theme:" + str(colour_theme) +
            "/lang:" + str(current_language) + "/\n" +
            "CRS" +
            "/home:" + str(show_home_statement) +
            "/hdln:" + str(show_headline_statement) + "/\n" +
            "MPS" +
            "/rmmbr_faf:" + str(remember_filtered_audio_files) +
            "/rmmbr_mps:" + str(remember_media_player_settings) +
            "/apr:" + str(auto_play_recordings) +
            "/arq:" + str(audio_render_quality) + "/\n")
    sd.write(text)
    sd.close()


def set_all_settings_to_default():
    global colour_theme
    global current_language
    global show_home_statement
    global show_headline_statement
    global remember_filtered_audio_files
    global remember_media_player_settings
    global auto_play_recordings
    global audio_render_quality

    colour_theme = 1
    current_language = 0

    show_home_statement = 1
    show_headline_statement = 1

    remember_filtered_audio_files = 0
    remember_media_player_settings = 0
    auto_play_recordings = 0
    audio_render_quality = 2

    update_savedata()


# Sector 5: Manage GUI Settings ----------------------------------------------------------------------------------------
def get_colour_theme():
    global colour_theme
    return colour_theme


def set_colour_theme(value):
    global colour_theme
    colour_theme = value if value in [0, 1] else 1
    update_savedata()


def get_current_language():
    global current_language
    return current_language


def set_current_language(value):
    global current_language
    current_language = value if value in [0, 1, 2, 3, 4, 5, 6] else 0
    update_savedata()


# Sector 6: Manage CRS Settings ----------------------------------------------------------------------------------------
def get_show_home_statement():
    global show_home_statement
    return show_home_statement


def set_show_home_statement(value):
    global show_home_statement
    show_home_statement = value if value in [0, 1] else 1
    update_savedata()


def get_show_headline_statement():
    global show_headline_statement
    return show_headline_statement


def set_show_headline_statement(value):
    global show_headline_statement
    show_headline_statement = value if value in [0, 1] else 1
    update_savedata()


# Sector 7: Manage MPS Settings ----------------------------------------------------------------------------------------
def get_remember_filtered_audio_files():
    global remember_filtered_audio_files
    return remember_filtered_audio_files


def set_remember_filtered_audio_files(value):
    global remember_filtered_audio_files
    remember_filtered_audio_files = value if value in [0, 1] else 0
    update_savedata()


def get_remember_media_player_settings():
    global remember_media_player_settings
    return remember_media_player_settings


def set_remember_media_player_settings(value):
    global remember_media_player_settings
    remember_media_player_settings = value if value in [0, 1] else 0
    update_savedata()


def get_auto_play_recordings():
    global auto_play_recordings
    return auto_play_recordings


def set_auto_play_recordings(value):
    global auto_play_recordings
    auto_play_recordings = value if value in [0, 1] else 0
    update_savedata()


def get_audio_render_quality():
    global audio_render_quality
    return audio_render_quality


def set_audio_render_quality(value):
    global audio_render_quality
    audio_render_quality = value if value in [0, 1, 2, 3, 4] else 2
    update_savedata()


# Refreshing settings for next release:
# set_all_settings_to_default()
