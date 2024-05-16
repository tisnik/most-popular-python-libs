#!/usr/bin/python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2023  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from __future__ import annotations

import sys
from typing import NewType, Sequence, Tuple

import pygame

# Nutno importovat kvůli konstantám QUIT atd.
from pygame.locals import *

# Velikost okna aplikace
WIDTH = 320
HEIGHT = 240

# Definice nových datových typů
RGB = NewType("RGB", Tuple[int, int, int])

# Konstanty s n-ticemi představujícími základní barvy
BLACK: RGB = RGB((0, 0, 0))
RED: RGB = RGB((255, 0, 0))
GRAY: RGB = RGB((128, 128, 128))
YELLOW: RGB = RGB((255, 255, 0))

CAPTION = "Sprites in Pygame"


# Třída představující sprite zobrazený jako jednobarevný čtverec.
class BlockySprite(pygame.sprite.Sprite):
    # Konstruktor
    def __init__(self, color: RGB, size: int, x: int, y: int):
        # Nejprve je nutné zavolat konstruktor předka,
        # tj. konstruktor třídy pygame.sprite.Sprite:
        pygame.sprite.Sprite.__init__(self)

        # Vytvoření obrázku představujícího vizuální obraz spritu:
        self.image = pygame.Surface([size, size])
        self.image.fill(color)

        # Vytvoření obalového obdélníku
        # (velikost se získá z rozměru obrázku)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Počáteční rychlost spritu
        self.speed_x = 0
        self.speed_y = 0

    # Nastavení barvy spritu, který kolidoval s hráčem
    def yellowColor(self) -> None:
        self.image.fill(YELLOW)

    # Nastavení barvy spritu, který nekolidoval s hráčem
    def grayColor(self) -> None:
        self.image.fill(GRAY)


def initDisplay(caption: str) -> pygame.Surface:
    # Vytvoření okna pro vykreslování
    display = pygame.display.set_mode([WIDTH, HEIGHT])

    # Nastavení titulku okna
    pygame.display.set_caption(caption)

    return display


def createSprites() -> Tuple[pygame.sprite.Group[BlockySprite], pygame.sprite.Group[BlockySprite], BlockySprite]:
    # Objekt sdružující všechny sprity
    all_sprites: pygame.sprite.Group[BlockySprite] = pygame.sprite.Group()

    # Objekt sdružující všechny sprity kromě hráče
    all_sprites_but_player: pygame.sprite.Group[BlockySprite] = pygame.sprite.Group()

    # Vytvoření několika typů spritů
    #                    barva  x   y velikost
    wall1 = BlockySprite(GRAY, 50, 10, 10)
    wall2 = BlockySprite(GRAY, 15, 100, 100)
    wall3 = BlockySprite(GRAY, 15, 100, 150)
    wall4 = BlockySprite(GRAY, 15, 200, 100)
    wall5 = BlockySprite(GRAY, 15, 200, 150)
    wall6 = BlockySprite(GRAY, 15, 150, 100)
    wall7 = BlockySprite(GRAY, 15, 150, 150)
    player = BlockySprite(RED, 40, WIDTH // 2 - 20, HEIGHT // 2 - 20)

    # Přidání několika dalších spritů do seznamu
    # (jen jeden sprite - ten poslední - bude ve skutečnosti pohyblivý)
    all_sprites.add(wall1)
    all_sprites.add(wall2)
    all_sprites.add(wall3)
    all_sprites.add(wall4)
    all_sprites.add(wall5)
    all_sprites.add(wall6)
    all_sprites.add(wall7)
    all_sprites.add(player)

    # Seznam všech nepohyblivých spritů
    all_sprites_but_player.add(wall1)
    all_sprites_but_player.add(wall2)
    all_sprites_but_player.add(wall3)
    all_sprites_but_player.add(wall4)
    all_sprites_but_player.add(wall5)
    all_sprites_but_player.add(wall6)
    all_sprites_but_player.add(wall7)

    return all_sprites, all_sprites_but_player, player


# Posun všech spritů ve skupině na základě jejich rychlosti
def move_sprites(sprite_group: pygame.sprite.Group[BlockySprite], playground_width: int, playground_height:int) -> None:
    for sprite in sprite_group:
        # Posun spritu
        sprite.rect.x = sprite.rect.x + sprite.speed_x
        sprite.rect.y = sprite.rect.y + sprite.speed_y
        # Kontrola, zda sprite nenarazil do okrajů okna
        if sprite.rect.x < 0:
            sprite.rect.x = 0
            sprite.speed_x = 0
        if sprite.rect.x + sprite.rect.width > playground_width:
            sprite.rect.x = playground_width - sprite.rect.width
            sprite.speed_x = 0
        if sprite.rect.y < 0:
            sprite.rect.y = 0
            sprite.speed_y = 0
        if sprite.rect.y + sprite.rect.height > playground_height:
            sprite.rect.y = playground_height - sprite.rect.height
            sprite.speed_y = 0


# Vykreslení celé scény na obrazovku
def draw_scene(display: pygame.Surface, background_color: RGB, sprite_group: pygame.sprite.Group[BlockySprite]) -> None:
    # Vyplnění plochy okna černou barvou
    display.fill(background_color)
    # Vykreslení celé skupiny spritů do bufferu
    sprite_group.draw(display)
    # Obnovení obsahu obrazovky (překlopení zadního a předního bufferu)
    pygame.display.update()


# Změna barvy spritu na základě kolize s hráčem
def change_colors(sprite_group: pygame.sprite.Group[BlockySprite], hit_list: Sequence[pygame.sprite.Sprite]) -> None:
    # Projít všemi sprity ze skupiny, kterou detekovala kolizní funkce
    for sprite in sprite_group:
        if sprite in hit_list:
            sprite.yellowColor()
        else:
            sprite.grayColor()


# Zjistí kolize spritu se "stěnami" (nepohyblivými sprity)
def check_collisions(player: BlockySprite, sprite_group: pygame.sprite.Group[BlockySprite]) -> None:
    # Vytvoření seznamu spritů, které kolidují s hráčem
    hit_list = pygame.sprite.spritecollide(player, sprite_group, False)
    # Změna barev kolidujících spritů
    change_colors(sprite_group, hit_list)
    collisions = len(hit_list)
    # Přenastavení titulku okna
    caption = CAPTION + ": collisions " + str(collisions)
    pygame.display.set_caption(caption)


def mainLoop(display: pygame.Surface, clock: pygame.time.Clock,
        all_sprites: pygame.sprite.Group[BlockySprite],
        all_sprites_but_player: pygame.sprite.Group[BlockySprite], player: BlockySprite) -> None:
    while True:
        # Načtení a zpracování všech událostí z fronty
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # Stiskem kurzorových kláves je možné měnit směr pohybu spritu
                elif event.key == pygame.K_LEFT:
                    player.speed_x = -3
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = +3
                elif event.key == pygame.K_UP:
                    player.speed_y = -3
                elif event.key == pygame.K_DOWN:
                    player.speed_y = +3
            if event.type == KEYUP:
                # Puštění kurzorových kláves vede k zastavení pohybu spritu
                if event.key == pygame.K_LEFT:
                    player.speed_x = 0
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = 0
                elif event.key == pygame.K_UP:
                    player.speed_y = 0
                elif event.key == pygame.K_DOWN:
                    player.speed_y = 0

        move_sprites(all_sprites, display.get_width(), display.get_height())
        check_collisions(player, all_sprites_but_player)
        draw_scene(display, BLACK, all_sprites)
        clock.tick(20)


def main() -> None:
    # Inicializace knihovny Pygame
    pygame.init()

    clock = pygame.time.Clock()
    display = initDisplay(CAPTION)

    all_sprites, all_sprites_but_player, player = createSprites()

    mainLoop(display, clock, all_sprites, all_sprites_but_player, player)


if __name__ == "__main__":
    main()


# finito
