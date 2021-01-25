from .classes import pygame, Key, GameClosed

def keynum_to_keyname(keynum):
    return pygame.key.name(keynum)

def keyname_to_keynum(keyname):
    return pygame.key.key_code(keyname)

def await_user_input():
    key_gotten = False
    while not key_gotten:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                key_gotten = True
                raise GameClosed()
            elif event.type == pygame.KEYDOWN:
                return Key(keynum = event.key)