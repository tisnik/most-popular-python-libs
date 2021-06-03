"""Pygubu and Tkinter: main menu in main window (resources not setup)."""

#
#  (C) Copyright 2020  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#
# example2B.py

import tkinter as tk
import pygubu


class Example2App(pygubu.TkApplication):
    """Class representing a Tkinter based application."""

    def _create_ui(self):
        """Construct and initializes all UI-related data structures."""
        # step #1: Create a builder
        self.builder = builder = pygubu.Builder()

        # step #2: Load an ui file
        builder.add_from_file('example2.ui')

        # step #3: Create the mainwindow
        self.mainwindow = builder.get_object('MainWindow', self.master)

        # step #4: Set main menu
        self.mainmenu = menu = builder.get_object('MainMenu', self.master)
        self.set_menu(menu)

        # step $5: Configure callbacks
        builder.connect_callbacks(self)


if __name__ == '__main__':
    # needed to have a menu
    root = tk.Tk()

    # run the application
    app = Example2App(root)
    app.run()
