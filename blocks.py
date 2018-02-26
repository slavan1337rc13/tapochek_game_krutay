from random import randint
from pygame import *
from weapon import *
#from start import sprite_kill_anim


platform_width = 27
platform_height = 27
platform_color = '#008000'

class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\blocks\\platform.png')
        self.rect = Rect(x, y, platform_width, platform_height)

class SpeedPlatform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\blocks\\goodplatform.png')
        self.rect = Rect(x, y, platform_width, platform_height)

class DiePlatform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\blocks\\die.png')
        self.rect = Rect(x, y, platform_width, platform_height)

class DoorPlatform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\blocks\\door.png')
        self.rect = Rect(x, y, platform_width, platform_height)

class BulletsForGun(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\player\\pistols\\strikes\\pistol_clip.png')
        self.rect = Rect(x, y, platform_width, platform_height)

class Banans(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\player\\pistols\\strikes\\bananas2.png')
        self.rect = Rect(x, y, platform_width, platform_height)

class Hp_regen(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\hp\\HPREGEN.png')
        self.rect = Rect(x, y, platform_width, platform_height)

class Fly_Monsters(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\monsters\\flymonstr.png')
        self.rect = Rect(x, y, platform_width, platform_height)
        self.cant_take_monay = False
        self.x_move = -3
        self.platformDie = False
        self.faseDie = 0
        self.y_move = 1

    def update(self, player, platforms, flymonsters, sprites, pistols):
        if not self.platformDie:
            self.rect.x += self.x_move
            self.rect.y += self.y_move
            self.collade(self.x_move, self.y_move, platforms, pistols)
        if self.platformDie:
            self.rect.y += 3
        if self.rect.y > 1000:
            player.score += 3
            player.bananas += 3
            if self in flymonsters:
                flymonsters.remove(self)
            if self in sprites:
                sprites.remove(self)
            self.kill()
        if Rect.colliderect(self.rect, player):
            print('player x:', player.rect.x)
            print('monster x :', self.rect.x)
            print('player y:', player.rect.y)
            print('monster y:', self.rect.y)
            if not player.smert:
                if player.rect.x < self.rect.x+60 and player.rect.x > self.rect.x-60 and player.rect.y < self.rect.y-10:
                    #print('kill')
                    self.platformDie = True
                    self.cant_take_monay = True
                    '''
                    if self in monsters:
                        monsters.remove(self)
                    if self in sprites:
                        sprites.remove(self)
                    self.kill()
                    '''
                else:
                    if not self.cant_take_monay:
                        if not self.platformDie:
                            player.smert = True
            return [sprites, flymonsters]

    def collade(self, x_move, y_move, platforms, pistols):
        if not self.platformDie:
            p1 = None
            for platform in platforms:
                if sprite.collide_rect(self, platform):
                    if x_move > 0:
                        self.rect.right = platform.rect.left
                        self.x_move = -3

                    if x_move < 0:
                        self.rect.left = platform.rect.right
                        self.x_move = 3

                    if y_move > 0:
                        self.on_ground = True
                        self.rect.bottom = platform.rect.top
                        self.y_move = -self.y_move

                    if y_move < 0:
                        self.rect.top = platform.rect.bottom
                        self.y_move = -self.y_move
            for each in pistols:
                if self == each.killed:
                    each.monstr_videl = True
                    self.platformDie = True

class Monsters(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\monsters\\Monster.png')
        self.rect = Rect(x, y, platform_width, platform_height)
        self.go_right = True
        self.go_left = True
        self.on_ground = False
        self.cant_take_monay = False
        self.x_move = -3
        self.platformDie = False
        self.faseDie = 0
        self.y_move = 0
        self.gravity = 1

    def update(self, player, platforms, monsters, sprites, pistols):
        self.rect.x += self.x_move

        if not self.on_ground:
            self.y_move += self.gravity
        self.on_ground = False
        self.rect.y += self.y_move
        m = self.collade(0, self.y_move, platforms, pistols, monsters)
        if m is not None:
            monsters = m
        m = self.collade(self.x_move, 0, platforms, pistols, monsters)
        if m is not None:
            monsters = m
        if self.rect.y > 2000:
            if self in monsters:
                monsters.remove(self)
            if self in sprites:
                sprites.remove(self)
            self.kill()
            player.bananas += 3
            player.score += 3
            return [sprites, monsters]
        if Rect.colliderect(self.rect, player):
            print('player x:', player.rect.x)
            print('monster x :', self.rect.x)
            print('player y:', player.rect.y)
            print('monster y:', self.rect.y)
            if not player.smert:
                if player.rect.x < self.rect.x+25 and player.rect.x > self.rect.x-25 and player.rect.y < self.rect.y-10:
                    #print('kill')
                    self.platformDie = True
                    player.prishok = True
                    self.cant_take_monay = True
                    '''
                    if self in monsters:
                        monsters.remove(self)
                    if self in sprites:
                        sprites.remove(self)
                    self.kill()
                    '''
                else:
                    if not self.cant_take_monay:
                        if not self.platformDie:
                            player.smert = True
            return [sprites, monsters]

    def collade(self, x_move, y_move, platforms, pistols, monsters):
        if not self.platformDie:
            p1 = None
            for platform in platforms:
                if sprite.collide_rect(self, platform):
                    if x_move > 0:
                        self.rect.right = platform.rect.left
                        self.x_move = -3

                    if x_move < 0:
                        self.rect.left = platform.rect.right
                        self.x_move = 3

                    if y_move > 0:
                        self.on_ground = True
                        self.rect.bottom = platform.rect.top
                        self.y_move = 0

                    if y_move < 0:
                        self.rect.top = platform.rect.bottom
                        self.y_move = 0
            for each in pistols:
                if self == each.killed:
                    each.monstr_videl = True
                    self.platformDie = True
        return monsters

class Money(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\money\\money2.png')
        self.rect = Rect(x, y, platform_width, platform_height)

class Pushka(sprite.Sprite):
    def __init__(self, player):
        sprite.Sprite.__init__(self)
        self.image = image.load("recource\\textures\\player\\pistols\\banana.gif")
        self.rect = Rect(player.rect.x, player.rect.y, platform_width, platform_height)
        self.killed = False
        self.monstr_videl = False
        if player.x_move < 0:
            self.x_move = -2
        else:
            self.x_move = 2

    def updata(self, monsters, sprites, platforms, pistols, flymonsters):
        self.rect.x += self.x_move

        sp = self.collade(monsters, platforms, sprites, pistols, flymonsters)

        sprites = sp[0]
        pistols = sp[1]

        self.rect.x += self.x_move

        sp = self.collade(monsters, platforms, sprites, pistols, flymonsters)

        sprites = sp[0]
        pistols = sp[1]

        self.rect.x += self.x_move

        sp = self.collade(monsters, platforms, sprites, pistols, flymonsters)

        sprites = sp[0]
        pistols = sp[1]

        return [sprites, pistols]


    def collade(self, monsters, platforms, sprites, pistols, flymonsters):
        for platform in platforms:
                if sprite.collide_rect(self, platform):
                    self.kill()
                    if self in pistols:
                        pistols.remove(self)
                    if self in sprites:
                        sprites.remove(self)

        for monster in monsters:
            if sprite.collide_rect(self, monster):
                self.killed = monster
        for flymonster in flymonsters:
            if sprite.collide_rect(self, flymonster):
                self.killed = flymonster
        if self.monstr_videl:
            self.kill()
            if self in pistols:
                pistols.remove(self)
            if self in sprites:
                sprites.remove(self)

        return [sprites, pistols]
class Chekpoint(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.rect = Rect(x, y-30, 64, 80)
        self.image = image.load('recource\\textures\\chekpoint\\flag.bmp')

class Boss(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = image.load('recource\\textures\\monsters\\boss.png')
        self.rect = Rect(x, y, 96, 96)
        self.go_right = True
        self.go_left = True
        self.on_ground = False
        self.cant_take_monay = False
        self.x_move = -3
        self.hp = 20
        self.platformDie = False
        self.faseDie = 0
        self.y_move = 0
        self.gravity = 1
        self.died = False

    def updata(self, player, platforms, monsters, sprites, pistols):
        self.rect.x += self.x_move

        if not self.on_ground:
            self.y_move += self.gravity
        self.on_ground = False
        self.rect.y += self.y_move
        m = self.collade(0, self.y_move, platforms, pistols, monsters)
        if m is not None:
            monsters = m
        m = self.collade(self.x_move, 0, platforms, pistols, monsters)
        if m is not None:
            monsters = m
        if self.platformDie:
            if self.rect.y > 800:
                if self in sprites:
                    sprites.remove(self)
                self.kill()
                if not self.cant_take_monay:
                    player.score += 50
                    player.bananas += 50
                    self.died = True
                    self.cant_take_monay = True
                return [sprites]
        if self.hp < 1:
            self.platformDie = True
        if Rect.colliderect(self.rect, player):
            print('player x:', player.rect.x)
            print('monster x :', self.rect.x)
            print('player y:', player.rect.y)
            print('monster y:', self.rect.y)
            if not player.smert:
                if player.rect.x < self.rect.x+45 and player.rect.x > self.rect.x-45 and player.rect.y < self.rect.y-10:
                    #print('kill')
                    self.hp -= 0.5
                    player.prishok = True

                    '''
                    if self in monsters:
                        monsters.remove(self)
                    if self in sprites:
                        sprites.remove(self)
                    self.kill()
                    '''
                else:
                    player.smert = True
            return [sprites, monsters]

    def collade(self, x_move, y_move, platforms, pistols, monsters):
        if not self.platformDie:
            p1 = None
            for platform in platforms:
                if sprite.collide_rect(self, platform):
                    if x_move > 0:
                        self.rect.right = platform.rect.left
                        self.x_move = -3

                    if x_move < 0:
                        self.rect.left = platform.rect.right
                        self.x_move = 3

                    if y_move > 0:
                        self.on_ground = True
                        self.rect.bottom = platform.rect.top
                        self.y_move = 0

                    if y_move < 0:
                        self.rect.top = platform.rect.bottom
                        self.y_move = 0
            for each in pistols:
                if self == each.killed:
                    each.monstr_videl = True
                    self.hp -= each.damage
        return monsters
