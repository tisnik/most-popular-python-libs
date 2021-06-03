"""Pygubu and Tkinter: main menu in main window, callback functions, tearoff menu (working example)."""

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

# Example4.py

import tkinter as tk
import pygubu


class Example4App(pygubu.TkApplication):
    """Class representing a Tkinter based application."""

    def _create_ui(self):
        """Construct and initializes all UI-related data structures."""
        # step #1: Create a builder
        self.builder = builder = pygubu.Builder()

        # step #2: Load an ui file
        builder.add_from_file('example4.ui')

        # step #2B: Specify path to images and other resources
        builder.add_resource_path(".")

        # step #3: Create the mainwindow
        self.mainwindow = builder.get_object('MainWindow', self.master)

        # step #4: Set main menu
        self.mainmenu = menu = builder.get_object('MainMenu', self.master)
        self.set_menu(menu)

        # step #5: Configure callbacks
        builder.connect_callbacks(self)

    def on_button_clicked(self):
        """Define handler for Quit button."""
        tk.messagebox.showinfo('Message', 'You clicked on Quit button')
        root.destroy()

    def on_command_quit_selected(self):
        """Define handler for Quit command."""
        tk.messagebox.showinfo('Message', 'You selected Quit command')
        root.destroy()


if __name__ == '__main__':
    # needed to have a menu
    root = tk.Tk()

    # run the application
    app = Example4App(root)
    app.run()
