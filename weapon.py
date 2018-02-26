from pygame import *

platform_width = 16
platform_height = 16

class Drop(sprite.Sprite):
    def __init__(self, x, y, bullets, bullets_in_oboima, maximum):
        self.image = image.load('')
        self.x_move = 0
        self.y_move = 4
        self.max = maximum
        self.oboima = bullets_in_oboima
        self.bullets = bullets
        self.name = ''
        self.rect = Rect(x, y, 32, 32)

    def upadate(self, platforms):

        for each in platforms:
            if sprite.collide_rect(self, each):
                if self.x_move > 0:
                    self.rect.left = each.rect.right
                    self.x_move = 0

                if self.x_move < 0:
                    self.rect.right = each.rect.left
                    self.x_move = 0

                if self.rect.y > each.rect.y-20:
                    self.rect.bottom = each.rect.top
                    self.y_move = 0

        self.rect.x += self.x_move
        self.rect.y += self.y_move


class Pushka(sprite.Sprite):
    def __init__(self, player):
        sprite.Sprite.__init__(self)

        self.damage = 0
        self.speed = 0
        self.cost = 0
        self.active = False
        self.slot = 0

        self.rect = Rect(player.rect.x, player.rect.y+8, platform_width, platform_height)
        self.killed = None
        self.monstr_videl = False
        if player.x_move < 0:
            self.x_move = -self.speed
        else:
            self.x_move = self.speed

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

class Banans(Pushka):
    def __init__(self, slot, player):
        sprite.Sprite.__init__(self)
        self.damage = 1
        self.speed = 3
        self.cost = 1
        self.active = False
        self.slot = slot
        self.image = image.load("recource\\textures\\player\\pistols\\banana.gif")

        self.rect = Rect(player.rect.x, player.rect.y, platform_width, platform_height)
        self.killed = None
        self.monstr_videl = False

        if player.x_move < 0:
            self.x_move = -self.speed
        else:
            self.x_move = self.speed

class Dropped_Gun(Drop):
    def __init__(self, x, y, bullets, bullet_in_oboima, maximum):
        sprite.Sprite.__init__(self)
        self.image = image.load("recource\\textures\\player\\pistols\\pistols\\pistolsmall.png")
        self.image2 = image.load("recource\\textures\\player\\pistols\\pistols\\pistol.png")
        self.x_move = 0
        self.y_move = 4
        self.bullets = bullets
        self.oboima = bullet_in_oboima
        self.name = 'Gun'
        self.max = maximum
        self.rect = Rect(x-33, y, 32, 32)

class Gun(Pushka):
    def __init__(self, slot, player):
        sprite.Sprite.__init__(self)
        self.damage = 9
        self.speed = 8
        self.cost = 4
        self.slot = slot

        self.sound = mixer.Sound("recource\\sound-trak\\gun.wav")
        self.sound.play()

        self.rect = Rect(player.rect.x, player.rect.y+8, platform_width, platform_height)
        self.killed = None
        self.monstr_videl = False

        if player.x_move < 0:
            self.x_move = -self.speed
            self.image = image.load("recource\\textures\\player\\pistols\\strikes\\bulletLeft.png")
        else:
            self.image = image.load("recource\\textures\\player\\pistols\\strikes\\bulletRight.png")
            self.x_move = self.speed

class Dropped_AK47(Drop):
    def __init__(self, x, y, bullets, bullet_in_oboima, maximum):
        sprite.Sprite.__init__(self)
        self.image = image.load("recource\\textures\\player\\pistols\\pistols\\AK47small.png")
        self.image2 = image.load("recource\\textures\\player\\pistols\\pistols\\AK47.png")
        self.x_move = 0
        self.y_move = 4
        self.bullets = bullets
        self.oboima = bullet_in_oboima
        self.name = 'AK47'
        self.max = maximum
        self.rect = Rect(x-33, y, 32, 32)

class AK47(Pushka):
    def __init__(self, slot, player):
        sprite.Sprite.__init__(self)
        self.damage = 2
        self.speed = 8
        self.cost = 4
        self.slot = slot

        self.sound = mixer.Sound("recource\\sound-trak\\ak47.wav")
        self.sound.play()

        self.rect = Rect(player.rect.x, player.rect.y+8, platform_width, platform_height)
        self.killed = None
        self.monstr_videl = False

        if player.x_move < 0:
            self.x_move = -self.speed
            self.image = image.load("recource\\textures\\player\\pistols\\strikes\\bulletLeft.png")
        else:
            self.image = image.load("recource\\textures\\player\\pistols\\strikes\\bulletRight.png")
            self.x_move = self.speed
