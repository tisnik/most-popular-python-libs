#!/usr/bin/python
# vim: set fileencoding=utf-8

# Demonstrační příklady využívající knihovnu Pygame

# Příklad číslo 7: výpis všech zjištěných informací o grafickém
#                  subsystému využívaném knihovnou Pygame.

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

import pygame

# Inicializace knihovny Pygame
pygame.init()


def yesno(val):
    if val:
        return "yes"
    else:
        return "no"


# Odkomentování si můžete vyzkoušet nastavit různé režimy
# pygame.display.set_mode([1024,768], pygame.FULLSCREEN | pygame.HWSURFACE, 32)


# Přečíst informaci o aktuálním nastavení grafického subsystému
displayInfo = pygame.display.Info()

pygame.display.quit()

# Vypsat přečtené informace o grafickém subsystému
print(
    "Desktop resolution:   %d x %d pixels"
    % (displayInfo.current_w, displayInfo.current_h)
)

if displayInfo.video_mem != 0:
    print("Video memory size:  %d MB" % displayInfo.video_mem)

print("bits per pixel:       %d" % displayInfo.bitsize)
print("bytes per pixel:      %d" % displayInfo.bytesize)

print("windowed mode:        " + yesno(displayInfo.hw))

print()

print("HW acceleration:      " + yesno(displayInfo.hw))
print("HW blitting:          " + yesno(displayInfo.blit_hw))
print("HW colorkey blitting: " + yesno(displayInfo.blit_hw_CC))
print("HW alpha blitting:    " + yesno(displayInfo.blit_hw_A))

print()

print("SW blitting:          " + yesno(displayInfo.blit_sw))
print("SW colorkey blitting: " + yesno(displayInfo.blit_sw_CC))
print("SW alpha blitting:    " + yesno(displayInfo.blit_sw_A))

print()

print("Masks:                " + str(displayInfo.masks))
print("Shifts:               " + str(displayInfo.shifts))
print("Losses:               " + str(displayInfo.losses))

pygame.quit()

# finito
