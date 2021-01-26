import pygame
import os
import time
from baseez import *

class GameClosed(Exception):
    pass

class CloseWriting(Exception):
    pass

class _KeyBase:
    def __init__(self, keyname=None, keynum=None):
        if keyname == None and keynum == None:
            raise TypeError("no key identifiers(keynum, keyname) provided")
        if keynum != None:
            self.key = keynum
            self.name = pygame.key.name(keynum)
        elif keyname != None:
            self.name = keyname
            self.key = pygame.key.key_code(keyname)
    
    def get(self):
        return self.key

class Key(_KeyBase):
    RETURN = _KeyBase(keynum = pygame.K_RETURN)
    BACKSPACE = _KeyBase(keynum = pygame.K_BACKSPACE)
    SPACE = _KeyBase(keynum = pygame.K_SPACE)
    ESC = _KeyBase(keynum = pygame.K_ESCAPE)

class Image:
    def __init__(self, path: str):
        self.image = pygame.image.load(path)
    def get(self):#, instance, owner):
        return self.image

class Object:
    def __init__(self, image: Image = None, pos: Vector2 = Vector2.ZERO):
        self.image = image
        self.pos = pos
    
    def get_blit(self):
        box = self.image.get().get_rect()
        box.center = self.pos.get()
        return self.image.get(), box
    
    def change_pos(self, new_pos):
        self.pos = new_pos

class AnimatedObject(Object):
    def __init__(self, dir_path: str, pos: Vector2 = Vector2.ZERO, frames_between_animation_tick: int = 0):
        self.animation_frames = self._get_animation_frames(dir_path)
        super().__init__(self.animation_frames[0], pos)
        self.fbat = frames_between_animation_tick
        self.paused = False
        self.frame = 0
        self.frame_timer = self.fbat
        self.frame_number = len(self.animation_frames)
    
    def _get_animation_frames(self, path):
        frames = []
        for frame_path in os.listdir(path):
            frames.append(Image(path+"/"+frame_path))
        return frames
    
    def tick(self):
        if not self.paused:
            if self.frame_timer == 0:
                self.frame_timer = self.fbat+1
                self.image = self.animation_frames[self.frame]
                self.frame += 1
                if self.frame > self.frame_number-1:
                    self.frame = 0
            self.frame_timer -= 1
    
    def get_blit(self):
        box = self.image.get().get_rect()
        box.center = self.pos.get()
        self.tick()
        return self.image.get(), box


    def pause_animation(self):
        self.paused = False

    def resume_animation(self):
        self.paused = True

class Font:
    def __init__(self, name: str, size: int = 20, sysfont: bool = False):
        if not sysfont:
            self.font = pygame.font.Font(name, size)
        else:
            self.font = pygame.font.SysFont(name, size)
    
    def get(self):
        return self.font

class Text:
    def __init__(self, font: Font, text: str, pos: Vector2 = Vector2.ZERO, color: Color = Color.BLACK):
        self.text = text
        self.font = font
        self.color = color
        self.pos = pos
        self.image = self.font.get().render(self.text, self.color)

    def change_text(self, text: str, *trash):
        self.text = text
        self.render()
    
    def change_color(self, color: Color = Color.BLACK):
        self.color = color
        self.render()
    
    def change_font(self, font):
        self.font = font
        self.render()
    
    def render(self):
        self.image = self.font.get().render(self,text, self.color)
    
    def get(self):
        return self.image
    
    def get_blit(self):
        box = self.image.get().get_rect()
        box.center = self.pos.get()
        return self.image.get, box

class EventListener:
    def __init__(self, event, function):
        self.event = event
        self.result = function
    
    def tick(self):
        if self.event():
            self.result()

class Box(pygame.Rect):
    pass

class MouseOverBox(EventListener, Object):
    def __init__(self, box: Box, press_function, pos: Vector2 = Vector2.ZERO, cooldown = 0):
        Object.__init__(self, None, pos)#print (list(super()))
        EventListener.__init__(self, self.event_check, press_function)
        self.box = box#image.get().get_rect()
        self.box.center = pos
        self.cooldown = cooldown
        self.max_cooldown = cooldown
    
    def tick(self):
        self.cooldown -= 1
        if self.cooldown < 1:
            self.cooldown = self.max_cooldown
            if self.event():
                self.result()
    
    def change_pos(self, new_pos):
        self.pos = new_pos
        self.box.center = self.pos
    
    def event_check(self):
        mouse = pygame.mouse.get_pos()
        return self.box.collidepoint(mouse)

class MouseOverImage(MouseOverBox):
    def __init__(self, image: Image, press_function, pos: Vector2 = Vector2.ZERO, cooldown = 0):
        MouseOverBox.__init__(self, image.get.get_rect(), press_function, pos, cooldown)

class MouseOverAnimatedImage(MouseOverBox, AnimatedObject):
    def __init__(self, dir_path: str, press_function, pos: Vector2 = Vector2.ZERO, cooldown = 0, frames_between_animation_tick: int = 0):
        self.animation_frames = self._get_animation_frames(dir_path)
        MouseOverBox.__init__(self, self.animation_frames[0].get.get_rect(), press_function, pos, cooldown)#super().__init__(self.animation_frames[0], pos)
        self.fbat = frames_between_animation_tick
        self.paused = False
        self.frame = 0
        self.frame_timer = self.fbat
        self.frame_number = len(self.animation_frames)
    
    def tick(self):
        if not self.paused:
            if self.frame_timer == 0:
                self.frame_timer = self.fbat+1
                self.image = self.animation_frames[self.frame]
                self.frame += 1
                if self.frame > self.frame_number-1:
                    self.frame = 0
            self.frame_timer -= 1
        
        self.cooldown -= 1
        if self.cooldown < 1:
            self.cooldown = self.max_cooldown
            if self.event():
                self.result()

class ClickBox(EventListener, Object):
    def __init__(self, box: Box, press_function, pos: Vector2 = Vector2.ZERO, cooldown = 0.2):
        Object.__init__(self, None, pos)#print (list(super()))
        EventListener.__init__(self, self.event_check, press_function)
        self.box = box#image.get().get_rect()
        self.box.center = pos
        self.cooldown = cooldown
        self.max_cooldown = cooldown
    
    def tick(self):
        self.cooldown -= 1
        if self.cooldown < 1:
            self.cooldown = self.max_cooldown
            if self.event():
                self.result()
    
    def change_pos(self, new_pos):
        self.pos = new_pos
        self.box.center = self.pos
    
    def event_check(self):
        if pygame.mouse.get_presses()[0]:
            mouse = pygame.mouse.get_pos()
            return self.box.collidepoint(mouse)
        else:
            return False

class ClickImage(ClickBox):
    def __init__(self, image: Image, press_function, pos: Vector2 = Vector2.ZERO, cooldown = 0.2):
        ClickBox.__init__(self, image.get.get_rect(), press_function, pos, cooldown)

class ClickAnimatedImage(MouseOverBox, AnimatedObject):
    def __init__(self, dir_path: str, press_function, pos: Vector2 = Vector2.ZERO, cooldown = 0, frames_between_animation_tick: int = 0):
        self.animation_frames = self._get_animation_frames(dir_path)
        MouseOverBox.__init__(self, self.animation_frames[0].get.get_rect(), press_function, pos, cooldown)#super().__init__(self.animation_frames[0], pos)
        self.fbat = frames_between_animation_tick
        self.paused = False
        self.frame = 0
        self.frame_timer = self.fbat
        self.frame_number = len(self.animation_frames)
    
    def tick(self):
        if not self.paused:
            if self.frame_timer == 0:
                self.frame_timer = self.fbat+1
                self.image = self.animation_frames[self.frame]
                self.frame += 1
                if self.frame > self.frame_number-1:
                    self.frame = 0
            self.frame_timer -= 1
        
        self.cooldown -= 1
        if self.cooldown < 1:
            self.cooldown = self.max_cooldown
            if self.event():
                self.result()

class App:
    #disabled = False
    def __init__(self, title: str, dimensions: tuple, background: Color = None, speed: int = 60, icon: Image = None):
        pygame.init()
        self.screen = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(title)
        if icon:
            pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.speed = speed
        self.object_array = []
        self.event_listener_array = []
        self.background = background
        self.title = title
        self.icon = icon
        self.disabled = False
        self.dimensions = dimensions

    def tick(self):
        if not self.disabled:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.disabled = True
                    pygame.quit()
                    return
                    #print ("shuting down")
            
            self._display_all()
            self._listen_for_events()

            self.clock.tick(self.speed)
        #else:
        #    print ("bye!")
        #    pygame.quit()
    
    def _display_all(self):
        if self.background != None:
            self.screen.fill(self.background)
        for obj in self.object_array:
            if obj.image != None:
                self.screen.blit(*obj.get_blit())
            #box = pygame.image.load("D:/Rasmus/python/chicken game/art/chicken_l_golden.png").get_rect()
                #box.center = (100, 100)
                #self.screen.blit(pygame.image.load("D:/Rasmus/python/chicken game/art/chicken_l_golden.png"), box)#print ("doing blit")
        pygame.display.update()
    
    def _listen_for_events(self):
        for listener in self.event_listener_array:
            listener.tick()

    def add_object(self, obj):
        self.object_array.append(obj)
        #print (self.object_array)
    
    def add_event_listener(self, listener):
        self.event_listener_array.append(listener)
    
    def run(self):
        return MainLoop(self).run()
    
    def reset(self):
        self.__init__(self.title, self.dimensions, self.background, self.speed, self.icon)
        self.disabled = False
    
    def disable(self):
        self.disabled = True
        pygame.quit()

class MainLoop:
    def __init__(self, app: App):
        self.app = app
    
    def run(self):
        while not self.app.disabled:
            self.app.tick()
            #print ("tick!")

class UserSingleLineText(Text):
    def await_user_input(self, app: App, text_change_call = lambda text, key: self.change_text(text, key), cooldown = 0.1):
        def key_await():
            key_gotten = False
            while not key_gotten:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        key_gotten = True
                        raise GameClosed()
                    elif event.type == pygame.KEYDOWN:
                        return Key(keynum = event.key)
        closed = False
        while not closed:
            key = key_await()
            if key.key == Key.RETURN:
                closed = True
                text_change_call("", key)
            else:
                text_change_call(self.text+key.name, key)
                app._display_all()
            time.sleep(cooldown)

class UserText(UserSingleLineText):
    def _change_call(self, text, key):
        self.change_text(text)
        if key.key == Key.RETURN:
            self.change_text(self.text+"\n")
        elif key.key == self.close_key:
            self.continue_with_writing = False
            raise CloseWriting
    def await_user_input(self, app: App, close_key = Key.ESC, cooldown = 0.1):
        self.continue_with_writing = True
        self.close_key = close_key
        while self.continue_with_writing:
            try:
                super().await_user_input(app, text_change_call = self._change_call, cooldown = cooldown)
            except CloseWriting:
                pass