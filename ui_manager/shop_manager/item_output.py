def draw_items(self):
    if self.select_mode == 0:
        if self.page == 1:
            self.image_m1911.draw(self.button_x[0] - 40, self.button_y[0], 400, 200)
            self.image_m92.draw(self.button_x[1] - 50, self.button_y[0], 400, 200)
            self.image_degle.draw(self.button_x[2] - 50, self.button_y[0], 400, 200)
            self.image_m500.draw(self.button_x[3] - 63, self.button_y[0], 400, 200)
            self.image_qhand.draw(self.button_x[4] - 70, self.button_y[0], 300, 150)

            self.image_aks74.draw(self.button_x[0] - 35, self.button_y[1], 240, 120)
            self.image_ump.draw(self.button_x[1] - 30, self.button_y[1], 240, 120)
            self.image_vector.draw(self.button_x[2] - 30, self.button_y[1], 240, 120)
            self.image_thompson.draw(self.button_x[3] - 35, self.button_y[1], 250, 120)
            self.image_p90.draw(self.button_x[4] - 30, self.button_y[1], 240, 120)

            self.image_scar.draw(self.button_x[0] - 40, self.button_y[2], 240, 120)
            self.image_m16.draw(self.button_x[1] - 40, self.button_y[2], 240, 120)
            self.image_mp44.draw(self.button_x[2] - 40, self.button_y[2], 240, 120)
            self.image_aug.draw(self.button_x[3] - 35, self.button_y[2], 240, 120)
            self.image_groza.draw(self.button_x[4] - 30, self.button_y[2], 240, 120)

            self.image_m1.draw(self.button_x[0] - 45, self.button_y[3], 250, 100)
            self.image_win.draw(self.button_x[1] - 52, self.button_y[3], 250, 75)
            self.image_mini14.draw(self.button_x[2] - 35, self.button_y[3], 200, 100)
            self.image_fal.draw(self.button_x[3] - 47, self.button_y[3], 250, 100)
            self.image_lvoas.draw(self.button_x[4] - 47, self.button_y[3], 230, 90)

        elif self.page == 2:
            self.image_spring.draw(self.button_x[0] - 50, self.button_y[0], 240, 95)
            self.image_kar98.draw(self.button_x[1] - 50, self.button_y[0], 240, 95)
            self.image_m24.draw(self.button_x[2] - 50, self.button_y[0], 240, 90)
            self.image_awp.draw(self.button_x[3] - 50, self.button_y[0], 250, 80)
            self.image_cheytac.draw(self.button_x[4] - 55, self.button_y[0], 250, 80)

    if self.select_mode == 1:
        self.image_knife.draw(self.button_x[0], self.button_y[0], 150, 100)
        self.image_bat.rotate_draw(-45, self.button_x[1] - 43, self.button_y[0] - 30, 35, 325)
        self.image_rapier.rotate_draw(0.5, self.button_x[2] - 50, self.button_y[0] - 25, 300, 75)
        self.image_katana.rotate_draw(-45, self.button_x[3] - 45, self.button_y[0] - 33, 35, 260)
        self.image_axe.rotate_draw(-45, self.button_x[4] - 28, self.button_y[0] - 15, 128, 256)
