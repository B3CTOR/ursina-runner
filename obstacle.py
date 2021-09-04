from ursina import *
from random import randint


class Obstacle(Entity):
	def __init__(self, position, scale, model, texture):
		super().__init__(
			model = model,
			position = position,
			scale = scale,
			collider = 'box',
			texture = texture,
			)
		self.run = False
		self.hit_info = self.intersects()
		self.spawned = False

	def update(self):

		self.hit_info = self.intersects()
		if self.hit_info.hit:
			self.run = True

		if self.run:
			self.z -= 35 * time.dt

	spawn = False
	spawned = False