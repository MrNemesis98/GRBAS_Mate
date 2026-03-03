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
import sys
import subprocess
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication


def resource_path(rel: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(sys.argv[0]))  # stabiler als "."
    return os.path.join(base, rel)


class RestartManager:
    _armed = False
    _cmd = None
    _cwd = None

    @staticmethod
    def _build_command():
        main_mod = sys.modules.get("__main__")
        main_file = getattr(main_mod, "__file__", None)

        if getattr(sys, "frozen", False) or main_file is None:
            return [sys.executable] + sys.argv[1:]
        else:
            script = os.path.abspath(main_file)
            return [sys.executable, script] + sys.argv[1:]

    @staticmethod
    def arm_restart():
        if RestartManager._armed:
            return

        RestartManager._armed = True
        RestartManager._cmd = RestartManager._build_command()
        if getattr(sys, "frozen", False):
            RestartManager._cwd = os.path.dirname(sys.executable)
        else:
            main_mod = sys.modules.get("__main__")
            main_file = getattr(main_mod, "__file__", None)
            RestartManager._cwd = os.path.dirname(os.path.abspath(main_file)) if main_file else os.getcwd()

        app = QApplication.instance()

        def spawn():
            creationflags = 0
            startupinfo = None
            if os.name == "nt":
                creationflags = (
                        subprocess.CREATE_NO_WINDOW
                        | subprocess.DETACHED_PROCESS
                        | subprocess.CREATE_NEW_PROCESS_GROUP
                )

                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = 0  # SW_HIDE

            env = os.environ.copy()

            # 1) Wichtig: erzwingt, dass PyInstaller onefile NICHT den parent-extract wiederverwendet
            env["PYINSTALLER_RESET_ENVIRONMENT"] = "1"

            # 2) optional, aber ich empfehle es: PyInstaller-Home-Dir aus der Parent-Env entfernen
            # (die Namen können je nach Version variieren; schadet nicht)
            for k in ("_MEIPASS2", "_PYI_APPLICATION_HOME_DIR"):
                env.pop(k, None)

            subprocess.Popen(
                RestartManager._cmd,
                cwd=RestartManager._cwd,
                close_fds=True,
                creationflags=creationflags,
                startupinfo=startupinfo,
                env=env,
            )

        app.aboutToQuit.connect(spawn)
        QTimer.singleShot(0, app.quit)
