import pygame as pg
import random as rd


def draw_sea():
    """ Отрисовка моря. """
    pg.draw.rect(screen, SEA, (0, WINY - 130, WINX, WINY))
    start_triangle = 0
    for _ in range(20):
        pg.draw.polygon(screen, SEA, [(start_triangle, WINY - 130),
                                      (start_triangle + 20, WINY - 150),
                                      (start_triangle + 40, WINY - 130)])
        start_triangle += 40


def draw_sky():
    """ Отрисовка неба. """
    pg.draw.rect(screen, BLUE, (0, 0, WINX, WINY - 130))


def draw_sun():
    """ Отрисовка солнца. """
    pg.draw.circle(screen, YELLOW, (0, 0), 80)


def draw_wharf():
    """ Отрисовка пристани. """
    pg.draw.rect(screen, BROWN, (560, WINY - 200, 240, 30))
    pg.draw.rect(screen, BROWN_WATERED, (600, WINY - 170, 30, 170))
    pg.draw.rect(screen, BROWN_WATERED, (730, WINY - 170, 30, 170))


def draw_chair():
    """ Отрисовка рыбацкого стула. """
    pg.draw.rect(screen, DARK_GREEN, (630, WINY - 230, 40, 5))
    pg.draw.rect(screen, BLACK, (630, WINY - 225, 3, 25))
    pg.draw.rect(screen, BLACK, (667, WINY - 225, 3, 25))
    pg.draw.rect(screen, BLACK, (630, WINY - 203, 40, 3))
    pg.draw.rect(screen, BLACK, (667, WINY - 250, 3, 25))
    pg.draw.rect(screen, DARK_GREEN, (665, WINY - 250, 3, 15))


def draw_fisherman():
    """ Отрисовка рыбака. """
    pg.draw.rect(screen, BLACK, (640, WINY - 280, 20, 50))
    pg.draw.polygon(screen, SKIN, [(642, WINY - 230), (658, WINY - 230), (620, WINY - 202), (610, WINY - 202)])
    pg.draw.rect(screen, GREY, (607, WINY - 202, 22, 2))
    pg.draw.polygon(screen, SKIN, [(647, WINY - 265), (647, WINY - 255), (625, WINY - 240), (625, WINY - 245)])
    pg.draw.line(screen, BLACK, (625, WINY - 242), (500, WINY - 367), 3)
    pg.draw.circle(screen, GREY, (615, WINY - 252), 7)
    pg.draw.circle(screen, SKIN, (625, WINY - 242), 4)
    pg.draw.rect(screen, SKIN, (647, WINY - 281, 7, -5))
    pg.draw.circle(screen, RED, (650, WINY - 303), 12)
    pg.draw.circle(screen, SKIN, (650, WINY - 295), 12)
    pg.draw.circle(screen, WHITE, (645, WINY - 298), 4)
    pg.draw.circle(screen, BLACK, (645, WINY - 298), 2)
    pg.draw.rect(screen, BLACK, (633, WINY - 307, 28, 6))


def draw_fishing_line(end_pos_y):
    """ Отрисовка лески.

    Принимаемы параметры:

    * end_pos_y - координата Y конца лески

    """

    pg.draw.line(screen, WHITE, (500, WINY - 366), (500, WINY - end_pos_y), 2)
    pg.draw.circle(screen, GREY, (500, WINY - 366), 3)
    pg.draw.circle(screen, GREY, (500, WINY - end_pos_y), 3)
    pg.draw.line(screen, GREY, (500, WINY - end_pos_y), (500, WINY - end_pos_y + 3), 2)
    pg.draw.line(screen, GREY, (497, WINY - end_pos_y + 3), (500, WINY - end_pos_y + 3), 2)
    pg.draw.circle(screen, RED, (500, WINY - end_pos_y - 100), 6)
    pg.draw.circle(screen, RED, (500, WINY - end_pos_y - 103), 6)
    pg.draw.circle(screen, RED, (500, WINY - end_pos_y - 97), 6)


def draw_cloud(rect_start_x, width):
    """ Отрисовка облака.

    Принимаемые параметры:

    * rect_start_x - координата X начала облака
    * width - ширина облака

    """

    pg.draw.ellipse(screen, WHITE, (rect_start_x, 100, width, 60))
    pg.draw.circle(screen, WHITE, (rect_start_x + 100, 100), 25)
    pg.draw.circle(screen, WHITE, (rect_start_x + 150, 110), 40)
    pg.draw.circle(screen, WHITE, (rect_start_x + 60, 120), 30)
    pg.draw.circle(screen, WHITE, (rect_start_x + 190, 115), 25)


def draw_fish(rect_start_x, end_pos_y):
    """ Отрисовка рыбы.

    Принимаемые параметры:

    * rect_start_x - координата X начала рыбьего тела
    * end_pos_y - координата Y рыбы

    """

    pg.draw.ellipse(screen, FISH_BODY, (rect_start_x, WINY - end_pos_y, 30, 12))
    pg.draw.polygon(screen, FISH_TAIL, [(rect_start_x, WINY - end_pos_y + 6),
                                        (rect_start_x - 10, WINY - end_pos_y - 3),
                                        (rect_start_x - 10, WINY - end_pos_y + 12)])
    pg.draw.circle(screen, SEA, (rect_start_x + 27, WINY - end_pos_y + 5), 2)


def draw_accident_shark(shark_start):
    """ Отрисовка акульего плавника.

    Принимаемые параметры:

    * shark_start - координата X начала плавника

    """

    pg.draw.polygon(screen, GREY, [(shark_start, WINY - 110),
                                   (shark_start - 15, WINY - 140),
                                   (shark_start + 40, WINY - 110)])


def draw_wow_eyes(man_rad, fish_rad):
    """ Отрисовка удивленных глаз рыбы и рыбака.

    Принимаемые параметры:

    * man_rad, fish_rad - радиус зрачков человека и рыбы

    """

    pg.draw.circle(screen, WHITE, (645, WINY - 298), man_rad + 2)
    pg.draw.circle(screen, BLACK, (645, WINY - 298), man_rad)

    pg.draw.circle(screen, SEA, (513, WINY - 245), fish_rad)


""" Параметры окна. """
FPS = 90
WINX = 800
WINY = 600

"""" Цветовые константы. """
BLUE = (145, 159, 245)
WHITE = (255, 255, 255)
YELLOW = (239, 255, 0)
SEA = (51, 0, 255)
BROWN = (117, 62, 20)
BROWN_WATERED = (77, 36, 5)
BLACK = (0, 0, 0)
GREY = (119, 119, 119)
SKIN = (255, 204, 153)
RED = (255, 0, 0)
DARK_GREEN = (0, 51, 0)
FISH_BODY = (153, 255, 153)
FISH_TAIL = (0, 255, 0)

""" Инициализация окна. """
pg.init()
screen = pg.display.set_mode((WINX, WINY))
icon = pg.image.load("icon.png")
pg.display.set_icon(icon)
pg.display.set_caption("Fisherman in da hood")
clock = pg.time.Clock()


def main():
    cloud_start = rd.randint(0, WINX)
    cloud_width = 250

    fish_start = rd.randint(0, WINX)
    shark_start = rd.randint(0, WINX)

    end_pos_y = 50

    man_rad = 2
    fish_rad = 2

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return

        draw_sky()
        draw_sun()
        draw_sea()
        draw_accident_shark(shark_start)
        draw_chair()
        draw_fisherman()
        draw_fishing_line(end_pos_y)
        draw_fish(fish_start, end_pos_y)
        draw_wharf()
        draw_cloud(cloud_start, cloud_width)
        draw_wow_eyes(man_rad, fish_rad)
        pg.draw.circle(screen, BLUE, (513, WINY - 245), 2)

        cloud_start += 1
        shark_start += 1

        if fish_start != 486:
            fish_start += rd.randint(1, 4)
        else:
            if end_pos_y != 250:
                end_pos_y += 1
            else:
                if man_rad != 10:
                    draw_wow_eyes(man_rad, fish_rad)
                    man_rad += 1
                    fish_rad += 1

        if fish_start > WINX + 200:
            fish_start = -250

        if shark_start > WINX + 200:
            shark_start = -250

        if cloud_start > WINX + 200:
            cloud_start = -250

        pg.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()