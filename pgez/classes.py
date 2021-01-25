import pygame
import os
import baseez

class Image:
    def __init__(self, path: str):
        self.image = pygame.image.load(path)
    def get(self):#, instance, owner):
        return self.image

class Object:
    def __init__(self, image: Image, pos: Vector2 = Vector2.ZERO):
        self.image = image
        self.pos = pos
    
    def get_blit(self):
        box = self.image.get().get_rect()
        box.center = self.pos.get()
        return self.image.get(), box

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

    def change_text(self, text: str):
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
        self.background = background
        self.title = title
        self.icon = icon
        self.disabled = False

    def tick(self):
        if not self.disabled:
            if self.background != None:
                self.screen.fill(self.background)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.disabled = True
                    pygame.quit()
                    return
                    #print ("shuting down")
            for obj in self.object_array:
                self.screen.blit(*obj.get_blit())
                #box = pygame.image.load("D:/Rasmus/python/chicken game/art/chicken_l_golden.png").get_rect()
                #box.center = (100, 100)
                #self.screen.blit(pygame.image.load("D:/Rasmus/python/chicken game/art/chicken_l_golden.png"), box)#print ("doing blit")
            pygame.display.update()
            self.clock.tick(self.speed)
        #else:
        #    print ("bye!")
        #    pygame.quit()
    
    def add_object(self, obj: Object):
        self.object_array.append(obj)
        print (self.object_array)
    
    def run(self):
        return MainLoop(self).run()
    
    def reset(self):
        pygame.init()
        self.disabled = False

class MainLoop:
    def __init__(self, app: App):
        self.app = app
    
    def run(self):
        while not self.app.disabled:
            self.app.tick()
            #print ("tick!")