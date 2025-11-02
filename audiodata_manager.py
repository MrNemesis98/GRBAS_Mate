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

import os
from pathlib import Path

recordings_path = Path(__file__).resolve().parent / 'src' / 'rec'


def get_param_recs(parameter=None, severity_level=None, gender=None, include_multilevel_files=True):

    found_files = []

    # 1) parameter filter --------------------------------------------------------------------------
    if parameter is None:
        path = recordings_path / 'param'
        for file in os.listdir(path / "I"):
            if file.endswith('.wav'):
                found_files.append(file)
        for file in os.listdir(path / "F"):
            if file.endswith('.wav'):
                found_files.append(file)
        for file in os.listdir(path / "G"):
            if file.endswith('.wav'):
                found_files.append(file)
        for file in os.listdir(path / "R"):
            if file.endswith('.wav'):
                found_files.append(file)
        for file in os.listdir(path / "B"):
            if file.endswith('.wav'):
                found_files.append(file)
        for file in os.listdir(path / "A"):
            if file.endswith('.wav'):
                found_files.append(file)
        for file in os.listdir(path / "S"):
            if file.endswith('.wav'):
                found_files.append(file)
        for file in os.listdir(path / "None"):
            if file.endswith('.wav'):
                found_files.append(file)
    else:
        path = recordings_path / 'param' / parameter
        found_files = [f for f in os.listdir(path) if f.endswith(".wav")]

    # 2) severity level filter ---------------------------------------------------------------------
    if severity_level is None:
        pass
    else:
        if include_multilevel_files:
            found_files = [f for f in found_files if f"_level{severity_level}" in f or f"_levels0123" in f]
        else:
            found_files = [f for f in found_files if f"_level{severity_level}" in f]

    # 3) gender of speaker filter ------------------------------------------------------------------
    if gender is None:
        pass
    else:
        found_files = [f for f in found_files if f"_{gender[0].lower()}_" in f]

    return found_files


# print(get_param_recs(parameter=None, severity_level=0, gender=None, include_multilevel_files=False))
