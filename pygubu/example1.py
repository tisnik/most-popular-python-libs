"""Pygubu and Tkinter: user interface initialization."""

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

# example1.py

import tkinter as tk
import pygubu


class Example1App:
    """Class representing a Tkinter based application."""

    def __init__(self):
        """Construct and initializes all UI-related data structures."""
        # step #1: Create a builder
        self.builder = builder = pygubu.Builder()

        # step #2: Load an ui file
        builder.add_from_file('example1.ui')

        # step #3: Create the mainwindow
        self.mainwindow = builder.get_object('Frame_1')

    def run(self):
        """Start the UI."""
        self.mainwindow.mainloop()


if __name__ == '__main__':
    # run the application
    app = Example1App()
    app.run()
