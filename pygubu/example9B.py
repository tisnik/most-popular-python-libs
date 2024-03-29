"""Pygubu and Tkinter: using check boxes."""

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

# Example9B.py

import tkinter as tk
from tkinter import messagebox, ttk

import pygubu


class Example9App(pygubu.TkApplication):
    """Class representing a Tkinter based application."""

    def _create_ui(self):
        """Construct and initializes all UI-related data structures."""
        # step #1: Create a builder
        self.builder = builder = pygubu.Builder()

        # step #2: Load an ui file
        builder.add_from_file("example9.ui")

        # step #2B: Specify path to images and other resources
        builder.add_resource_path(".")

        # step #3: Create the mainwindow
        self.mainwindow = builder.get_object("MainWindow", self.master)

        # step #4: Configure callbacks
        builder.connect_callbacks(self)

        # step #5: Set variables
        vars = self.builder.tkvariables
        vars["checkbutton_a"].set("no")
        vars["checkbutton_b"].set("no")
        vars["checkbutton_c"].set("no")

        root.bind("<Control-q>", lambda event: self.on_quit_button_click())

    def on_quit_button_click(self):
        root.destroy()

    def on_button_display_selections_click(self):
        vars = self.builder.tkvariables

        message = (
            "Checkbutton A: {}\n"
            "Checkbutton B: {}\n"
            "Checkbutton C: {}\n".format(
                vars["checkbutton_a"].get(),
                vars["checkbutton_b"].get(),
                vars["checkbutton_c"].get(),
            )
        )
        messagebox.askokcancel("Selections", message)


if __name__ == "__main__":
    # needed to have a menu
    root = tk.Tk()

    # style
    style = ttk.Style()

    # run the application
    app = Example9App(root)
    app.run()
