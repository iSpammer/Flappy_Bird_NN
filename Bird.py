import os

import pygame


class Bird:
    IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]

    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0  # degrees to tilt
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5  # 3shan pygame frame bybd2 mn fo2 fa 3shan atyr fo2 lzm negative
        self.tick_count = 0  # track kont banot mneen
        self.height = self.y

    def move(self):
        self.tick_count += 1  # 1 frame moved
        disp = self.vel * self.tick_count + 0.5 * 3 * self.tick_count ** 2
        # -10.5 + 1.5 >> moving upward vel of -9 we by2el kol frame l7d 0 b3d kda byzeed tane le -9
        if disp >= 16:
            disp = (disp / abs(disp)) * 16

        if disp < 0:
            disp -= 2

        self.y = self.y + disp

        if disp < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > - 90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        # rotating img
        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_img.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_img, new_rect.topleft)

    def get_mask(self):  # crashing bird bageb el edges
        return pygame.mask.from_surface(self.img)
