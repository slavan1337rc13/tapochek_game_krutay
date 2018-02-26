from pygame import *
import pyganim

move_speed = 0.4
player_width = 25
player_height = 32
player_color = '#fc6c85'
jump_power = 4
gravity = 0.3
extra_jump = 6
delay = 1
b_anim_jump = [(image.load('recource\\textures\\player\\j.png'), 1)]
b_anim_stay = [(image.load('recource\\textures\\player\\player1.png'), 1)]
b_anim_JumpLeft = [(image.load('recource\\textures\\player\\jl.png'), 1)]
b_anim_JumpRight = [(image.load('recource\\textures\\player\\jr.png'), 1)]
b_anim_left = [(image.load('recource\\textures\\player\\l1.png'), 1),
               (image.load('recource\\textures\\player\\l2.png'), 1),
               (image.load('recource\\textures\\player\\l3.png'), 1),
               (image.load('recource\\textures\\player\\l4.png'), 1),
               (image.load('recource\\textures\\player\\l5.png'), 1)]
b_anim_right = [(image.load('recource\\textures\\player\\r1.png'), 1),
               (image.load('recource\\textures\\player\\r2.png'), 1),
               (image.load('recource\\textures\\player\\r3.png'), 1),
               (image.load('recource\\textures\\player\\r4.png'), 1),
               (image.load('recource\\textures\\player\\r5.png'), 1)]
bgColor = "#ff0000"


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.t_anim_jump = pyganim.PygAnimation(b_anim_jump)
        self.t_anim_jump.play()
        self.t_anim_stay = pyganim.PygAnimation(b_anim_stay)
        self.t_anim_stay.play()
        self.t_anim_jumpLeft = pyganim.PygAnimation(b_anim_JumpLeft)
        self.t_anim_jumpLeft.play()
        self.t_anim_jumpRight = pyganim.PygAnimation(b_anim_JumpRight)
        self.t_anim_jumpRight.play()
        self.t_anim_left = pyganim.PygAnimation(b_anim_left)
        self.t_anim_left.play()
        self.t_anim_right = pyganim.PygAnimation(b_anim_right)
        self.t_anim_right.play()
        self.hp = 5
        self.dop_speed = 0
        self.smert = False
        self.x_move = 0
        self.y_move = 0
        self.plusscore = 0
        self.score = 0
        self.bananas = 5
        self.gun_bullets = 100
        self.umirat = False
        self.maxspeed = 0.4
        self.nadoLeft = False
        self.nadoRight = False
        self.times2 = 0
        self.times3 = 0
        self.x_start = x
        self.y_start = y
        self.slot = 0
        self.prishok = False
        self.remake = False
        self.image = image.load('recource\\textures\\player\\player1.png')
        self.image.set_colorkey(Color(bgColor))
        self.rect = Rect(x, y, player_width, player_height)
        self.next_level = False
        self.on_ground = False
        self.times = 0
        self.faseDie = 0
        self.savepoint = [55, 55, 5, 5, 5]

    def updata(self, left, right, up, shift, platforms, speedPlatforms, badPlatforms, door, sprites, moneys, banans, regen):
        self.plusscore = 0
        if self.umirat:
            if self.faseDie < 10:
                self.rect.y -= 3
            elif self.faseDie > 10:
                self.rect.y += 0.1
            self.faseDie += 1

        if move_speed + self.dop_speed > self.maxspeed:
            self.dop_speed = self.maxspeed - move_speed

        if self.times3 > 0:
            self.nadoLeft = False
            self.times3 = 0
            left = False

        if self.nadoLeft:
            left = True
            self.on_ground = True
            self.times3 += 1

        if self.times2 > 0:
            right = False
            self.nadoRight = False
            self.times2 = 0

        if self.nadoRight:
            right = True
            self.on_ground = True
            self.times2 += 1

        if left:
            self.x_move -= move_speed + self.dop_speed
            self.image.fill(Color(bgColor))
            self.t_anim_left.blit(self.image, (0, 0))

        if right:
            self.x_move += move_speed + self.dop_speed
            self.image.fill(Color(bgColor))
            self.t_anim_right.blit(self.image, (0, 0))

        if not (left or right):
            self.x_move = 0

        if self.prishok:
            up = True
            self.on_ground = True
            self.times += 1

        if self.times > 1:
            self.prishok = False
            self.times = 0
        if up:
            if self.x_move < 0:
                self.image.fill(Color(bgColor))
                self.t_anim_jumpLeft.blit(self.image, (0, 0))
            elif self.x_move > 0:
                self.image.fill(Color(bgColor))
                self.t_anim_jumpRight.blit(self.image, (0, 0))
            else:
                self.image.fill(Color(bgColor))
                self.t_anim_jump.blit(self.image, (0, 0))
            if self.on_ground:
                if shift:
                    self.y_move -= extra_jump
                else:
                    self.y_move -= jump_power
        if not self.on_ground:
            self.y_move += gravity
            self.rect.y += self.y_move

        if self.y_move == self.x_move and self.x_move == 0:
            self.image.fill(Color(bgColor))
            self.t_anim_stay.blit(self.image, (0, 0))

        self.on_ground = False

        self.rect.y += self.y_move
        if not self.umirat:
            p135 = self.collade(0, self.y_move, platforms, speedPlatforms, door, badPlatforms, moneys, banans, regen)

            p1 = p135[0]
            p3 = p135[1]
            p5 = p135[2]
            p7 = p135[3]

        self.rect.x += self.x_move
        if not self.umirat:
            p246 = self.collade(self.x_move, 0, platforms, speedPlatforms, door, badPlatforms, moneys, banans, regen)
            # print(p1, p2)
            p2 = p246[0]
            p4 = p246[1]
            p6 = p246[2]
            p8 = p246[3]

            if p1 is not None:
                sprites.remove(p1)
                speedPlatforms.remove(p1)
                p1.kill()

            if p2 is not None:
                speedPlatforms.remove(p2)
                sprites.remove(p2)
                p2.kill()

            if p3 is not None:
                sprites.remove(p3)
                moneys.remove(p3)
                p3.kill()

            if p4 is not None:
                sprites.remove(p4)
                if p4 in moneys:
                    moneys.remove(p4)
                p4.kill()

            if p5 is not None:
                sprites.remove(p5)
                banans.remove(p5)
                p5.kill()

            if p6 is not None:
                sprites.remove(p6)
                if p6 in banans:
                    banans.remove(p6)
                p6.kill()

            if p7 is not None:
                sprites.remove(p7)
                regen.remove(p7)
                p7.kill()

            if p8 is not None:
                sprites.remove(p8)
                if p8 in regen:
                    regen.remove(p8)
                p8.kill()
        return [sprites, speedPlatforms, moneys, banans, regen]

    def collade(self, x_move, y_move, platforms, speedPlatforms, door, badPlatforms, moneys, banans, regen):
        p1 = None
        p2 = None
        p3 = None
        p4 = None
        for platform in platforms:
            if sprite.collide_rect(self, platform):
                if x_move > 0:
                    self.rect.right = platform.rect.left
                    self.x_move = 0

                if x_move < 0:
                    self.rect.left = platform.rect.right
                    self.x_move = 0

                if y_move > 0:
                    self.on_ground = True
                    self.rect.bottom = platform.rect.top
                    self.y_move = 0
                if y_move < 0:
                    self.rect.top = platform.rect.bottom
                    self.y_move = 0
        for platform in speedPlatforms:
            if sprite.collide_rect(self, platform):
                if x_move > 0:
                    self.rect.right = platform.rect.left
                    self.x_move = 0
                    self.dop_speed += 0.1
                    self.remake = True
                if x_move < 0:
                    self.rect.left = platform.rect.right
                    self.x_move = 0
                    self.dop_speed += 0.1
                    self.remake = True
                if y_move > 0:
                    self.on_ground = True
                    self.rect.bottom = platform.rect.top
                    self.y_move = 0
                    self.dop_speed += 0.1
                    self.remake = True
                if y_move < 0:
                    self.rect.top = platform.rect.bottom
                    self.y_move = 0
                    self.dop_speed += 0.1
                    self.remake = True
                p1 = platform
        for platform in badPlatforms:
            if sprite.collide_rect(self, platform):
                if x_move > 0:
                    self.rect.right = platform.rect.left
                    self.hp -= 1
                    self.prishok = True
                    self.nadoLeft = True
                if x_move < 0:
                    self.rect.left = platform.rect.right
                    self.hp -= 1
                    self.prishok = True
                    self.nadoRight = True
                if y_move > 0:
                    self.on_ground = True
                    self.rect.bottom = platform.rect.top
                    self.hp -= 1
                    self.prishok = True
                if y_move < 0:
                    self.rect.top = platform.rect.bottom
                    self.hp -= 1
                    self.y_move += 5
        for banan in banans:
            if sprite.collide_rect(self, banan):
                p3 = banan
                self.bananas += 3
        for platform in moneys:
            if sprite.collide_rect(self, platform):
                self.score += 1
                p2 = platform
        for each in regen:
            if sprite.collide_rect(self, each):
                self.hp += 1
                p4 = each
        if sprite.collide_rect(self, door):
            self.next_level = True

        return [p1, p2, p3, p4]
