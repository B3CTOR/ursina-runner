from ursina import *

class Coin(Entity):
	def __init__(self, origin):
		super().__init__(
			model = 'cube',
			texture = 'grass',
			scale = (.6,.6,.6),
			position = origin
			)
		self.run = False

	def update(self):
		if self.run:
			self.z -= 25 * time.dt