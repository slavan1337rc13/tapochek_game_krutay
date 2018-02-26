import pygame
from pygame import *
from player import Player
from blocks import Platform
from blocks import SpeedPlatform
from camera import Camera
from blocks import DiePlatform
from blocks import DoorPlatform
from blocks import Monsters
from blocks import Money
from blocks import Fly_Monsters
from weapon import Banans as BananPushka
from blocks import Boss
from blocks import Banans
from blocks import Hp_regen
from weapon import Gun
from blocks import Chekpoint
from blocks import BulletsForGun
from weapon import AK47
from weapon import Dropped_Gun
from weapon import Dropped_AK47

scrWidth = 1024
scrHeight = 768
display = (scrWidth, scrHeight)
bgColor = "#ff0000"
platformWidth = 32
platformHeigh = 32
platformDisplay = (platformWidth, platformHeigh)
platformColor = '#008000'
map = open('recource\\maps\\map1.txt', 'r')
map2 = open('recource\\maps\\map2.txt', 'r')
map3 = open('recource\\maps\\map3.txt', 'r')
map4 = open('recource\\maps\\map4.txt', 'r')
map5 = open('recource\\maps\\map5.txt', 'r')
levels = [[map.read().split("\n"),[55, 55], 5, 100, 100],[map2.read().split("\n"), [42*27, 4*27], 5, 5, 5], [map3.read().split("\n"), [55, 55], 5, 5, 5],
          [map4.read().split("\n"), [55, 55], 5, 5, 5], [map5.read().split("\n"), [55, 55], 5, 5, 5]]
#levels = [[map4.read().split("\n"), [55, 55], 5, 5], [map5.read().split("\n"), [55, 55], 5, 5]]

def camera_config(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + scrWidth / 2, -t + scrHeight / 2
    l = min(l, 0)
    l = max(scrWidth-camera.width, l)
    t = max(scrHeight-camera.height, t)
    t = min(0, t)
    return Rect(l, t, w, h)

def main():
    lvl = 0
    slot1 = [image.load("recource\\textures\\player\\pistols\\strikes\\bananas3.png"), 'Banans', 100, 10, 10]
    slot2 = [image.load("recource\\textures\\player\\pistols\\pistols\\pistol.png"), 'Gun', 100, 7, 7]
    slot3 = [image.load("recource\\textures\\player\\pistols\\pistols\\AK47.png"), 'AK47', 100, 30, 30]
    slot4 = [None, None, 0, 0, 0]
    timess = 0
    inventory = [slot1, slot2, slot3, slot4]
    for leval in levels:
        reload = False
        player = Player(leval[1][0], leval[1][1])
        player.hp = levels[lvl-1][2]
        player.score = levels[lvl-1][3]
        player.bananas = levels[lvl-1][4]
        level = leval[0]
        checkp = [55, 55]
        shift = False
        speedPlatforms = []
        pygame.init()
        screen = pygame.display.set_mode(display)
        fon = Surface(display)
        fon.fill(Color(bgColor))
        #fon = image.load('recource\\textures\\bgTextures\\kirpichi.jpg')
        sprites = pygame.sprite.Group()
        platforms = []
        banans = []
        monsters = []
        badPlatforms = []
        dropped = []
        weapones = []
        sprites.add(player)
        left = right = up = False
        timer = pygame.time.Clock()
        moneys = []
        flymonsters = []
        bullets = []
        regens = []
        chekpoints = []
        x = y = 0
        boss = None
        for all in level:
            for each in all:
                if each == '-':
                    pf = Platform(x, y)
                    sprites.add(pf)
                    platforms.append(pf)

                if each == '@':
                    pf = SpeedPlatform(x, y)
                    sprites.add(pf)
                    speedPlatforms.append(pf)

                if each == 'x':
                    pf = DiePlatform(x, y)
                    sprites.add(pf)
                    badPlatforms.append(pf)

                if each == '%':
                    pf = DoorPlatform(x, y)
                    sprites.add(pf)
                    door = pf
                if each == 'M':
                    pf = Monsters(x, y)
                    monsters.append(pf)
                    sprites.add(pf)
                if each == '$':
                    pf = Money(x, y)
                    moneys.append(pf)
                    sprites.add(pf)
                if each == 'L':
                    pf = Fly_Monsters(x, y)
                    flymonsters.append(pf)
                    sprites.add(pf)
                if each == 'B':
                    boss =  Boss(x, y)
                    monsters.append(boss)
                    sprites.add(boss)
                if each == 'b':
                    pf = Banans(x, y)
                    banans.append(pf)
                    sprites.add(pf)
                if each == 'h':
                    pf = Hp_regen(x, y)
                    sprites.add(pf)
                    regens.append(pf)
                if each == '+':
                    pf = Chekpoint(x, y)
                    sprites.add(pf)
                    chekpoints.append(pf)
                if each == 'P':
                    pf = BulletsForGun(x, y)
                    sprites.add(pf)
                    bullets.append(pf)
                x += platformWidth
            y += platformHeigh
            x = 0
        total_width = len(level[0]) * 32
        total_heigh = len(level) * 32
        camera = Camera(camera_config, total_width, total_heigh)
        black = (0, 0, 0)
        green = (0, 255, 0)
        red = (255, 0, 0)
        font = pygame.font.Font(None, 55)
        text = font.render("My text", True, black)
        font2 = pygame.font.Font(None, 100)
        banani = pygame.font.Font(None, 55)
        money = image.load('recource\\textures\\money\\money2.png')
        hpx = 180
        hpy = 32
        banx = 105
        more9 = False
        more99 = False
        more92 = False
        more992 = False
        bantextx = 143
        uminshilos = False
        times = 0
        pistols = []
        hps = []
        inventory_slots = [image.load('recource\\textures\\inventory\\inventory.png'), image.load('recource\\textures\\inventory\\inventory.png'),
                           image.load('recource\\textures\\inventory\\inventory.png'), image.load('recource\\textures\\inventory\\inventory.png')]
        for i in range(player.hp):
            hps.append(image.load('recource\\textures\\hp\\hp3.png'))
        timer.tick(30)
        banan = None
        banantext = None
        pygame.mixer.music.load("recource\\sound-trak\\menu.mp3")
        #pygame.mixer.music.play(-1, 0.0)
        now = 0
        while not player.next_level:
            hps = []
            for i in range(player.hp):
                hps.append(image.load('recource\\textures\\hp\\hp3.png'))
            for e in pygame.event.get():
                if e.type == QUIT:
                    raise SystemExit("Quit")
                if e.type == KEYDOWN and e.key == K_a:
                    left = True
                if e.type == KEYDOWN and e.key == K_d:
                    right = True
                if e.type == KEYDOWN and e.key == K_w:
                    up = True
                if e.type == KEYDOWN and e.key == K_LSHIFT:
                    shift = True
                if e.type == KEYDOWN and e.key == K_r:
                    reload = True
                if e.type == KEYDOWN and e.key == K_SPACE:
                    if inventory[player.slot][0] is not None:
                        if inventory[player.slot][1] == 'Banans':
                            if inventory[player.slot][2] > 0:
                                if inventory[player.slot][3] > 0:
                                    reload = False
                                    inventory[player.slot][3] -= 1
                                    pf = BananPushka(0, player)
                                    sprites.add(pf)
                                    pistols.append(pf)
                                    now = inventory[player.slot][2]
                        if inventory[player.slot][1] == 'Gun':
                            if inventory[player.slot][2] > 0:
                                if inventory[player.slot][3] > 0:
                                    reload = False
                                    inventory[player.slot][3] -= 1
                                    pf = Gun(1, player)
                                    sprites.add(pf)
                                    pistols.append(pf)
                                    now = inventory[player.slot][2]
                        if inventory[player.slot][1] == 'AK47':
                            if inventory[player.slot][2] > 0:
                                if inventory[player.slot][3] > 0:
                                    reload = False
                                    inventory[player.slot][3] -= 1
                                    pf = AK47(1, player)
                                    sprites.add(pf)
                                    pistols.append(pf)
                                    now = inventory[player.slot][2]

                    else:
                        player.banas = 0
                if e.type == KEYDOWN and e.key == K_q:
                    if inventory[player.slot][1] == 'Gun':
                        gun = Dropped_Gun(player.rect.x, player.rect.y, inventory[player.slot][2], inventory[player.slot][3], inventory[player.slot][4])
                        inventory[player.slot] =  [None, None, 0, 0, 0]
                        dropped.append(gun)
                        sprites.add(gun)

                    if inventory[player.slot][1] == 'AK47':
                        ak47 = Dropped_AK47(player.rect.x, player.rect.y, inventory[player.slot][2], inventory[player.slot][3], inventory[player.slot][4])
                        inventory[player.slot] =  [None, None, 0, 0, 0]
                        dropped.append(ak47)
                        sprites.add(ak47)
                if e.type == KEYDOWN and e.key == K_1:
                    player.slot = 0
                if e.type == KEYDOWN and e.key == K_2:
                    player.slot = 1
                if e.type == KEYDOWN and e.key == K_3:
                    player.slot = 2
                if e.type == KEYDOWN and e.key == K_4:
                    player.slot = 3

                if e.type == KEYUP and e.key == K_d:
                    right = False
                if e.type == KEYUP and e.key == K_a:
                    left = False
                if e.type == KEYUP and e.key == K_w:
                    up = False
                if e.type == KEYUP and e.key == K_LSHIFT:
                    shift = False
            if player.score > 9:
                if not more9:
                    hpx += 10
                    banx += 10
                    bantextx += 10
                    more9 = True
            if player.score > 99:
                if not more99:
                    hpx += 20
                    banx += 20
                    bantextx += 20
                    more99 = True
            if player.score < 9:
                if more9:
                    hpx -= 10
                    banx -= 10
                    bantextx -= 10
                    more9 = False
            if player.score < 99:
                if more99:
                    hpx -= 20
                    banx -= 20
                    bantextx -= 20
                    more99 = False
            if inventory[player.slot][2] > 9:
                if not more92:
                    hpx += 10
                    more92 = True
            if inventory[player.slot][2] > 99:
                if not more992:
                    hpx += 20
                    more992 = True
            if inventory[player.slot][2] < 9:
                if more92:
                    hpx -= 10
                    more92 = False
            if inventory[player.slot][2] < 99:
                if more992:
                    hpx -= 20
                    more992 = False
            for each in dropped:
                if sprite.collide_rect(player, each):
                    for each2 in range(len(inventory)):
                        if inventory[each2][0] is None:
                            inventory[each2] = [each.image2, each.name, each.bullets, each.oboima, each.max]
                            if each in dropped:
                                dropped.remove(each)
                            if each in sprites:
                                sprites.remove(each)
                            break
            for chekpoint in chekpoints:
                if sprite.collide_rect(player, chekpoint):
                    checkp = [chekpoint.rect.y, chekpoint.rect.x]
                    print(chekpoint.rect.y)
                    print(chekpoint.rect.x)
                    print('Savepoint')
            for bullet in bullets:
                if sprite.collide_rect(player, bullet):
                    for each in range(len(inventory)):
                        if inventory[each][1] == 'Gun':
                            inventory[each][2] += 15
                            if bullet in bullets:
                                bullets.remove(bullet)
                            if bullet in sprites:
                                sprites.remove(bullet)
                            bullet.kill()
            for banan1 in banans:
                if sprite.collide_rect(player, banan1):
                    if banan1 in banans:
                        banans.remove(banan1)
                    if banan1 in sprites:
                        sprites.remove(banan1)
                    banan1.kill()
                    player.bananas += 3
            for platform in moneys:
                if sprite.collide_rect(player, platform):
                    player.score += 1
                    if platform in platforms:
                        platforms.remove(platform)
                    if platform in sprites:
                        sprites.remove(platform)
                    platform.kill()
            for each in regens:
                if sprite.collide_rect(player, each):
                    player.hp += 1
                    if each in regens:
                        regens.remove(each)
                    if each in sprites:
                        sprites.remove(each)
                    each.kill()
            screen.blit(fon, (0, 0))
            text = font.render(str(player.score), True, black)
            for each in dropped:
                each.upadate(platforms)
            if inventory[player.slot][0] is not None:
                if inventory[player.slot][1] == 'AK47':
                    banantext = banani.render('{}/{}'.format(str(inventory[player.slot][3]), str(inventory[player.slot][2])), True, black)
                    banan = image.load('recource\\textures\\player\\pistols\\strikes\\bullet.png')
                if inventory[player.slot][1] == 'Gun':
                    banantext = banani.render('{}/{}'.format(str(inventory[player.slot][3]), str(inventory[player.slot][2])), True, black)
                    banan = image.load('recource\\textures\\player\\pistols\\strikes\\bullet.png')
                if inventory[player.slot][1] == 'Banans':
                    banantext = banani.render('{}/{}'.format(str(inventory[player.slot][3]),str(inventory[player.slot][2])), True, black)
                    banan = image.load('recource\\textures\\player\\pistols\\strikes\\bananas2.png')
            else:
                banan = None
                banantext = None
            camera.update(player)
            for each in flymonsters:
                fms = each.update(player, platforms, flymonsters, sprites, pistols)
                if fms is not None:
                    sprites = fms[0]
                    flymonsters = fms[1]
            if reload:
                timess += 1
                if timess > 10:
                    inventory[player.slot][3] += 1
                    inventory[player.slot][2] -= 1
                    timess = 0
                if inventory[player.slot][3] == inventory[player.slot][4]:
                    reload = False
                    timess = 0
            for each in pistols:
                sp = each.updata(monsters, sprites, platforms, pistols, flymonsters)
                if sp is not None:
                    sprites = sp[0]
                    pistols = sp[1]

            for each in monsters:
                sm = each.update(player, platforms, monsters, sprites, pistols)
                if sm is not None:
                    sprites = sm[0]
                    monsters = sm[1]
                if each == boss:
                    sm = each.updata(player, platforms, monsters, sprites, pistols)
                    if sm is not None:
                        sprites = sm[0]
            for each in sprites:
                screen.blit(each.image, camera.apply(each))
            for each in range(len(inventory_slots)):
                screen.blit(inventory_slots[each], [32, 196+(each*64)])
            screen.blit(image.load('recource\\textures\\inventory\\vibor.png'), [32, 196+player.slot*64])
            screen.blit(money, [32, 32])
            screen.blit(text, [70, 32])
            for each in range(len(inventory)):
                if inventory[each][0] is not None:
                    screen.blit(inventory[each][0], [32, 196+(each*64)])
            i = 0
            if boss != None:
                bosshps = boss.hp
                if not boss.died:
                    if boss.hp != 0:
                        if boss.hp < 11:
                            for k in range(10):
                                if bosshps != 0:
                                    bosshps -= 1
                                    each = image.load('recource\\textures\\hp\\hp3.png')
                                    screen.blit(each, [700+(k*30), 32])
                        else:
                            for i in range(2):
                                for v in range(10):
                                    if bosshps != 0:
                                        bosshps -= 1
                                        each = image.load('recource\\textures\\hp\\hp3.png')
                                        screen.blit(each, [700+(v*30), 32+(i*30)])
            for each in hps:
                i += 1
                screen.blit(each, [hpx+(35*i), hpy])
            if banan is not None:
                screen.blit(banan, [banx, 32])
                screen.blit(banantext, [bantextx, 32])
            if player.hp == 0:
                player.smert = True
            sprites_speedplatforms_money = player.updata(left, right, up, shift, platforms, speedPlatforms, badPlatforms, door, sprites, moneys, banans, regens)
            speedPlatforms = sprites_speedplatforms_money[1]
            sprites = sprites_speedplatforms_money[0]
            moneys = sprites_speedplatforms_money[2]
            banans = sprites_speedplatforms_money[3]
            regens = sprites_speedplatforms_money[4]
            levels[lvl][2] = player.hp
            levels[lvl][3] = player.score
            levels[lvl][4] = player.bananas
            if player.smert:
                if not uminshilos:
                    player.score -= 5
                    if player.score < 0:
                        player.score = 0
                    potracheno = font2.render('Потрачено!', True, green)
                    uminshilos = True
                screen.blit(potracheno, [360, 340])
                player.umirat = True
                times += 1

            if times > 100:
                player.smert = False
                player.umirat = False
                player.bananas = player.savepoint[4]
                player.hp = 5
                player.rect.y = checkp[0]
                player.rect.x = checkp[1]
                player.faseDie = 0
                uminshilos = False
                print(player.rect.y)
                print(player.rect.x)
                times = 0

            player.savepoint[0] = player.hp
            player.savepoint[1] = player.score
            player.savepoint[2] = player.bananas
            pygame.display.update()
        lvl += 1
            #добавить анимацию


if __name__ == '__main__':
    main()
