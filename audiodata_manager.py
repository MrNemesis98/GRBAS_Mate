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

import os
from pathlib import Path

recordings_path = Path(__file__).resolve().parent / 'src' / 'rec'


def get_param_recs(parameter=None,
                   severity_level=None,
                   gender=None,
                   articulation="vs"):      # change that after creating single "v" and "s" audiofiles!!!

    found_files = []
    file_paths = []

    # 1) parameter filter --------------------------------------------------------------------------
    if parameter is None:                   # means "include all parameters"
        path = recordings_path / 'param'

        for file in os.listdir(path / "I"):
            if file.endswith('.wav'):
                found_files.append(file)
                file_paths.append(str(path / "I" / file))
        for file in os.listdir(path / "F"):
            if file.endswith('.wav'):
                found_files.append(file)
                file_paths.append(str(path / "F" / file))
        for file in os.listdir(path / "G"):
            if file.endswith('.wav'):
                found_files.append(file)
                file_paths.append(str(path / "G" / file))
        for file in os.listdir(path / "R"):
            if file.endswith('.wav'):
                found_files.append(file)
                file_paths.append(str(path / "R" / file))
        for file in os.listdir(path / "B"):
            if file.endswith('.wav'):
                found_files.append(file)
                file_paths.append(str(path / "B" / file))
        for file in os.listdir(path / "A"):
            if file.endswith('.wav'):
                found_files.append(file)
                file_paths.append(str(path / "A" / file))
        for file in os.listdir(path / "S"):
            if file.endswith('.wav'):
                found_files.append(file)
                file_paths.append(str(path / "S" / file))
        for file in os.listdir(path / "None"):
            if file.endswith('.wav'):
                found_files.append(file)
                file_paths.append(str(path / "None" / file))
    else:                                       # parameter = initial letter of selected parameter (i.e. "F")
        path = recordings_path / 'param' / parameter
        found_files = [f for f in os.listdir(path) if f.endswith(".wav")]
        file_paths = [str(path / f) for f in os.listdir(path) if f.endswith(".wav")]

    # 2) severity level filter ---------------------------------------------------------------------
    if severity_level is None:      # severity = None   ->   "All Options"
        pass
    elif severity_level == "4":     # special case: severity = 4   ->   "Asc. 0-3"
        found_files = [f for f in found_files if f"_levels0123" in f]
        file_paths = [f for f in file_paths if f"_levels0123" in f]
    else:                           # default case: severity number = number of level
        found_files = [f for f in found_files if f"_level{severity_level}" in f]
        file_paths = [f for f in file_paths if f"_level{severity_level}" in f]

    # 3) gender of speaker filter ------------------------------------------------------------------
    if gender is None:          # "All Options"
        pass
    else:
        if gender == "0":       # "Male"
            found_files = [f for f in found_files if f"_m_" in f]
            file_paths = [f for f in file_paths if f"_m_" in f]
        elif gender == "1":     # "Female"
            found_files = [f for f in found_files if f"_f_" in f]
            file_paths = [f for f in file_paths if f"_f_" in f]

    # 4) articulation type filter ------------------------------------------------------------------
    if articulation is None:       # "All Options"
        pass
    else:
        if articulation == "0":     # "Vowel"
            found_files = [f for f in found_files if f"_v_" in f]
            file_paths = [f for f in file_paths if f"_v_" in f]
        elif articulation == "1":   # "Sentence"
            found_files = [f for f in found_files if f"_s_" in f]
            file_paths = [f for f in file_paths if f"_s_" in f]
        elif articulation == "2":   # "Both in 1 file"
            found_files = [f for f in found_files if f"_vs_" in f]
            file_paths = [f for f in file_paths if f"_vs_" in f]

    return found_files, file_paths


files, paths = get_param_recs(parameter="B", severity_level=2, gender=None, articulation=None)

"""
for file in files:
    print(file)
for file in paths:
    print(file)
    """

# articulation filter is established but yet there are no single v or s files,
# only audiofiles that combine vs
