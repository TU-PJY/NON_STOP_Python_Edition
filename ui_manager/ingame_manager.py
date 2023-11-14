from pico2d import *
from config import *
from game_work import game_framework
from mods import play_mode


def load_resource(self):
	self.font = load_font(font_directory, 40)
	pass


def render_ammo_ind(self):
	cur = self.weapon.cur_ammo

	if self.weapon.gun_type == 'pistol' or self.weapon.gun_type == 'smg':
		num = self.weapon.num_ammo_small
	elif self.weapon.gun_type == 'ar':
		num = self.weapon.num_ammo_middle
	elif self.weapon.gun_type == 'rifle' or self.weapon.gun_type == 'sr':
		num = self.weapon.num_ammo_big

	self.font.draw(20, 120, '%d | %d' %(cur, num), (self.r, self.g, self.b))
	pass


def update_ammo_ind(self):
	if self.weapon.reload_need:  # 총알을 모두 소모하면 인디케이터가 붉은색으로 표시된다
		self.g, self.b = 0, 0
	else:
		self.r, self.g, self.b = 255, 255, 255
	pass