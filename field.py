from ursina import *

class Field(Entity):
	def __init__(self, position, texture):
		super().__init__(
			model = 'cube',
			scale = Vec3(2,.1,100),
			position = position,
			texture = 'brick',
			collider = 'box',
			)