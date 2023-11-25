from config import *
from pico2d import *

from mods import play_mode


def print_info(self, i, j):
    x = WIDTH / 2 + 460
    y = self.window_y + 220
    y2 = self.window_y + 170
    y3 = self.window_y + 140
    y4 = self.window_y + 110
    y5 = self.window_y + 50
    y6 = self.window_y + 20
    y7 = self.window_y - 10
    y8 = self.window_y - 40

    x2 = WIDTH / 2 + 470
    x3 = WIDTH / 2 + 490
    cost = self.window_y - 70

    color = (255, 255, 255)
    color2 = (0, 255, 0)
    color3 = (255, 0, 0)
    color4 = (255, 255, 0)
    color5 = (0, 255, 255)

    buy = True

    if self.select_mode == 0:
        if self.page == 1:
            if not play_mode.weapon.buy_list_gun[i][j]:  # 구입하지 않은 총기는 가격을 표기한다
                self.coin_icon.draw(x2, cost, 30, 30)
                buy = False

            match(i, j):
                case (0, 0):
                    self.info.draw(x, y, 'M-1911', color)
                    self.info.draw(x, y2, '대미지: 25', color)
                    self.info.draw(x, y3, '장탄수: 7', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                case (1, 0):
                    self.info.draw(x, y, 'M-92', color)
                    self.info.draw(x, y2, '대미지: 23', color)
                    self.info.draw(x, y3, '장탄수: 15', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '300', color4)
                case (2, 0):
                    self.info.draw(x, y, 'Desert Eagle', color)
                    self.info.draw(x, y2, '대미지: 35', color)
                    self.info.draw(x, y3, '장탄수: 8', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '600', color4)
                case (3, 0):
                    self.info.draw(x, y, 'M-500', color)
                    self.info.draw(x, y2, '대미지: 40', color)
                    self.info.draw(x, y3, '장탄수: 6', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '800', color4)
                case (4, 0):
                    self.info.draw(x, y, 'QUICK HAND', color)
                    self.info.draw(x, y2, '대미지: 20', color)
                    self.info.draw(x, y3, '장탄수: 12', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '1500', color4)
                case (0, 1):
                    self.info.draw(x, y, 'AKS-74U', color)
                    self.info.draw(x, y2, '대미지: 12', color)
                    self.info.draw(x, y3, '장탄수: 30', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '2000', color4)
                case (1, 1):
                    self.info.draw(x, y, 'UMP-45', color)
                    self.info.draw(x, y2, '대미지: 15', color)
                    self.info.draw(x, y3, '장탄수: 25', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '2500', color4)
                case (2, 1):
                    self.info.draw(x, y, 'VECTOR', color)
                    self.info.draw(x, y2, '대미지: 12', color)
                    self.info.draw(x, y3, '장탄수: 25', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '3000', color4)
                case (3, 1):
                    self.info.draw(x, y, 'THOMPSON', color)
                    self.info.draw(x, y2, '대미지: 18', color)
                    self.info.draw(x, y3, '장탄수: 30', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '3500', color4)
                case (4, 1):
                    self.info.draw(x, y, 'P90', color)
                    self.info.draw(x, y2, '대미지: 15', color)
                    self.info.draw(x, y3, '장탄수: 50', color)
                    self.info.draw(x, y4, '사용 탄약: 권총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '4000', color4)
                case (0, 2):
                    self.info.draw(x, y, 'SCAR-H', color)
                    self.info.draw(x, y2, '대미지: 20', color)
                    self.info.draw(x, y3, '장탄수: 25', color)
                    self.info.draw(x, y4, '사용 탄약: 소총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '5000', color4)
                case (1, 2):
                    self.info.draw(x, y, 'M16', color)
                    self.info.draw(x, y2, '대미지: 18', color)
                    self.info.draw(x, y3, '장탄수: 30', color)
                    self.info.draw(x, y4, '사용 탄약: 소총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '6000', color4)
                case (2, 2):
                    self.info.draw(x, y, 'MP-44', color)
                    self.info.draw(x, y2, '대미지: 30', color)
                    self.info.draw(x, y3, '장탄수: 20', color)
                    self.info.draw(x, y4, '사용 탄약: 소총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '7000', color4)
                case (3, 2):
                    self.info.draw(x, y, 'AUG', color)
                    self.info.draw(x, y2, '대미지: 23', color)
                    self.info.draw(x, y3, '장탄수: 30', color)
                    self.info.draw(x, y4, '사용 탄약: 소총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '8000', color4)
                case (4, 2):
                    self.info.draw(x, y, 'OTS-14', color)
                    self.info.draw(x, y2, '대미지: 21', color)
                    self.info.draw(x, y3, '장탄수: 40', color)
                    self.info.draw(x, y4, '사용 탄약: 소총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '9000', color4)
                case (0, 3):
                    self.info.draw(x, y, 'M1 GARAND', color)
                    self.info.draw(x, y2, '대미지: 70', color)
                    self.info.draw(x, y3, '장탄수: 8', color)
                    self.info.draw(x, y4, '사용 탄약: 대구경 소총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '11000', color4)
                case (1, 3):
                    self.info.draw(x, y, 'MODEL-1866', color)
                    self.info.draw(x, y2, '대미지: 100', color)
                    self.info.draw(x, y3, '장탄수: 10', color)
                    self.info.draw(x, y4, '사용 탄약: 대구경 소총탄', color)
                    self.info.draw(x, y5, '관형 탄창', color4)
                    if not buy:
                        self.info.draw(x3, cost, '13000', color4)
                case (2, 3):
                    self.info.draw(x, y, 'MINI-14', color)
                    self.info.draw(x, y2, '대미지: 50', color)
                    self.info.draw(x, y3, '장탄수: 30', color)
                    self.info.draw(x, y4, '사용 탄약: 소총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '15000', color4)
                case (3, 3):
                    self.info.draw(x, y, 'FAL', color)
                    self.info.draw(x, y2, '대미지: 70', color)
                    self.info.draw(x, y3, '장탄수: 20', color)
                    self.info.draw(x, y4, '사용 탄약: 대구경 소총탄', color)
                    if not buy:
                        self.info.draw(x3, cost, '17000', color4)
                case (4, 3):
                    self.info.draw(x, y, 'M14 EBR', color)
                    self.info.draw(x, y2, '대미지: 40', color)
                    self.info.draw(x, y3, '장탄수: 20', color)
                    self.info.draw(x, y4, '사용 탄약: 대구경 소총탄', color)
                    self.info.draw(x, y5, '2점사 사격', color4)
                    if not buy:
                        self.info.draw(x3, cost, '19000', color4)

        elif self.page == 2:
            if not play_mode.weapon.buy_list_gun2[i][j]:
                self.coin_icon.draw(x2, cost, 30, 30)
                buy = False

            match(i, j):
                case (0, 0):
                    self.info.draw(x, y, 'M1903', color)
                    self.info.draw(x, y2, '대미지: 150', color)
                    self.info.draw(x, y3, '장탄수: 5', color)
                    self.info.draw(x, y4, '사용 탄약: 저격 소총탄', color)
                    self.info.draw(x, y5, '최대 관통 횟수: 2', color4)
                    self.info.draw(x, y6, '관통 시 대미지 감소: 50', color4)
                    self.info.draw(x, y7, '마우스 우클릭으로 정조준',  color5)
                    self.info.draw(x, y8, '격발 전 정조준 필요', color3)
                    if not buy:
                        self.info.draw(x3, cost, '23000', color4)
                case (1, 0):
                    self.info.draw(x, y, 'KAR98K', color)
                    self.info.draw(x, y2, '대미지: 170', color)
                    self.info.draw(x, y3, '장탄수: 5', color)
                    self.info.draw(x, y4, '사용 탄약: 저격 소총탄', color)
                    self.info.draw(x, y5, '최대 관통 횟수: 3', color4)
                    self.info.draw(x, y6, '관통 시 대미지 감소: 40', color4)
                    self.info.draw(x, y7, '마우스 우클릭으로 정조준', color5)
                    self.info.draw(x, y8, '격발 전 정조준 필요', color3)
                    if not buy:
                        self.info.draw(x3, cost, '28000', color4)
                case (2, 0):
                    self.info.draw(x, y, 'M24', color)
                    self.info.draw(x, y2, '대미지: 200', color)
                    self.info.draw(x, y3, '장탄수: 5', color)
                    self.info.draw(x, y4, '사용 탄약: 저격 소총탄', color)
                    self.info.draw(x, y5, '최대 관통 횟수: 4', color4)
                    self.info.draw(x, y6, '관통 시 대미지 감소: 40', color4)
                    self.info.draw(x, y7, '마우스 우클릭으로 정조준', color5)
                    self.info.draw(x, y8, '격발 전 정조준 필요', color3)
                    if not buy:
                        self.info.draw(x3, cost, '33000', color4)
                case (3, 0):
                    self.info.draw(x, y, 'AWP', color)
                    self.info.draw(x, y2, '대미지: 220', color)
                    self.info.draw(x, y3, '장탄수: 5', color)
                    self.info.draw(x, y4, '사용 탄약: 저격 소총탄', color)
                    self.info.draw(x, y5, '최대 관통 횟수: 6', color4)
                    self.info.draw(x, y6, '관통 시 대미지 감소: 30', color4)
                    self.info.draw(x, y7, '마우스 우클릭으로 정조준', color5)
                    self.info.draw(x, y8, '격발 전 정조준 필요', color3)
                    if not buy:
                        self.info.draw(x3, cost, '38000', color4)
                case (4, 0):
                    self.info.draw(x, y, 'CHEYTAC M-200', color)
                    self.info.draw(x, y2, '대미지: 250', color)
                    self.info.draw(x, y3, '장탄수: 5', color)
                    self.info.draw(x, y4, '사용 탄약: 저격 소총탄', color)
                    self.info.draw(x, y5, '최대 관통 횟수: 8', color4)
                    self.info.draw(x, y6, '관통 시 대미지 감소: 30', color4)
                    self.info.draw(x, y7, '마우스 우클릭으로 정조준', color5)
                    self.info.draw(x, y8, '격발 전 정조준 필요', color3)
                    if not buy:
                        self.info.draw(x3, cost, '43000', color4)