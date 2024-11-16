# src/automation.py

import os
from pywinauto import Application

class Automation:
    def open_folder(self, folder_path):
        # Открытие проводника Windows с указанным путем
        os.startfile(folder_path)

        # Если нужно, можно дополнительно использовать Pywinauto для управления проводником
        # Например, для навигации, создания папок и т.д.
        print(f"Открыта папка: {folder_path}")
