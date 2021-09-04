from ursina import *

class SpawnBarrier(Entity):
	def __init__(self, position):
		super().__init__(
			model = 'cube',
			visible = False,
			position = position,
			scale = (2,40,.1),
			collider = 'box'
			)