from ursina import *

class Player(Entity):
	def __init__(self):
		super().__init__(
			model = 'cube',
			scale = Vec3(1,2,1),
			collider = 'box',
			position = (0,0,0)
			)
		self.in_air = False
		self.landing = False
		self.landing2 = False
		self.jleft = False
		self.jright = False
		self.in_air_direction = False
		self.jumping = False

	def jump(self):
		self.in_air = True

	def jump_left(self):
		if round(self.x, 1) != -4.0:
			self.jumping = True
			self.jleft = True

	def jump_right(self):
		if round(self.x, 1) != 4.0:
			self.jumping = True
			self.jright = True

	def update(self):

		if self.in_air:
			if round(self.y,1) <= 2.5 and self.landing == False:
				self.y += .14
			if round(self.y,1) >= 2.5 and self.landing == False:
				self.landing = True
			if self.landing:
				self.y -= .1
			if round(self.y,1) == 0.0 or round(self.y,1) == -0.0:
				self.in_air = False
				self.landing = False

		
		if self.jumping:
			if round(self.y, 1) != 2.0:
				self.y += .2 # setting
			if self.jleft and round(self.x, 1) > -2.2:
				self.x -= .2 # setting
			if self.jright and round(self.x, 1) < 2.2:
				self.x += .2 # setting

		if self.jumping and round(self.y, 1) == 2.0:
			self.jumping = False
			self.landing2 = True

		if self.landing2:
			if round(self.y, 1) > 0.0:
				self.y -= .2 # setting
			if self.jleft and round(self.x, 1) > -4.0:
				self.x -= .2 # setting
			if self.jright and round(self.x, 1) < 4.0:
				self.x += .2 # setting

		if self.landing2 and round(self.y, 1) == 0.0:
			self.landing2 = False
			self.jleft = False
			self.jright = False