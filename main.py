from ursina import *
from menu import MenuButton
from player import Player
from obstacle import Obstacle
from field import Field
from spawn_barrier import SpawnBarrier
from physics3d import *
from random import randint
from coin import Coin

count = 0
running = False
obstacles = []
coins = []
colliders = []
positions = ((-4,5,80),
			(0,5,80),
			(4,5,80))

def update():
	global obstacles
	global coins
	global running
	global count

	if getattr(Obstacle, 'spawn'):
		count += 1
		print("SPAWN{}".format(count))
		try:
			print(obstacles[-2].spawned)
		except:
			print()
		obstacle_type = randint(1,3)

		if obstacle_type >= 2:
			random_pos = randint(1,3)
	
			if random_pos == 1:
				rand = randint(0,2)
				pos = (positions[rand],)
			if random_pos == 2:
				ran1 = randint(0,2)
				if ran1 == 0:
					ran2 = randint(1,2)
				if ran1 == 1:
					ran2 = randint(-1,0)
				if ran1 == 2:
					ran2 = randint(0,1)
				pos = (positions[ran1],positions[ran2])
			if random_pos >= 3:
				pos = (positions[0],positions[1],positions[2])
	
			for position in pos:
				obstacles.append(Obstacle(position, (.7,.7,.7), 'obstacle', 'obstacle'))
				colliders.append(MeshCollider(world, obstacles[-1], mass=1))
				colliders[-1].scale = (1,1,1)
				coins.append(Coin(position))
				coins[-1].z += 2
				coins[-1].y -= 3
				setattr(Obstacle, 'spawn', False)
				obstacles[-1].run == False
				obstacles[-2].spawned = True

		if obstacle_type == 1:
			random_pos = randint(0,1)
			if random_pos == 0:
				pos = (positions[randint(0,2)],)
			if random_pos == 1:
				ran1 = randint(0,2)
				if ran1 == 0:
					ran2 = randint(1,2)
				if ran1 == 1:
					ran2 = randint(-1,0)
				if ran1 == 2:
					ran2 = randint(0,1)
				pos = (positions[ran1],positions[ran2])
			for position in pos:
				obstacles.append(Obstacle(position, (1.1,1,.7), 'cube', 'grass'))
				colliders.append(MeshCollider(world, obstacles[-1], mass=1.5))
				colliders[-1].scale = (1.4,3,1)
				setattr(Obstacle, 'spawn', False)
				obstacles[-1].run == False
				obstacles[-2].spawned = True

	for obstacle in obstacles:
		if obstacle.z <= -100:
			obstacle.disable()
				

		for spawn_barrier in spawn_barriers:
			if obstacle.hit_info.hit and obstacle.hit_info.entity == player:
				print('dead')
			if obstacle.hit_info.hit and obstacle.hit_info.entity == spawn_barrier and obstacle.spawned == False:
				setattr(Obstacle, 'spawn', True)

		for coin in coins:
			if obstacle.run:
				coin.run = True
			if coin.z <= -100:
				coin.enabled = False


	dt = time.dt
	world.doPhysics(dt)

def input(key):
	if key == 'a':
		if round(player.x,1) <= 4.0 and player.in_air == False and player.landing == False:
			if round(player.x,1) == 1.4 or round(player.x,1) == 0.0 or round(player.x,1) == -1.4 or round(player.x,1) == -4.0 or round(player.x) == 4.0:
				player.jump_left()

	if key == 'd':
		if round(player.x,1) < 4.0 and player.in_air == False and player.landing == False:
			if round(player.x,1) == 1.4 or round(player.x,1) == 0.0 or round(player.x,1) == -1.4 or round(player.x,1) == -4.0:
				player.jump_right()

	if key == 'space' and player.in_air == False and player.landing == False and player.landing2 == False and player.jumping == False:
		player.jump()

	if key == 'y':
		EditorCamera()

app = Ursina(title = 'Runner', borderless = False)

field_texture = load_texture('assets/field.png')

spawn_barriers = [
	SpawnBarrier((0,-10,79)),
	SpawnBarrier((4,-10,79)),
	SpawnBarrier((-4,-10,79)),
]

camera.y = 6
camera.rotation = Vec3(10,0,0)

pos = (0, 5, 80)
obs = Obstacle(pos, (.7,.7,.7), 'obstacle', load_texture('assets/obstacle.png'))
obstacles.append(obs)


fields = [
	Field((0,-1,45), field_texture),
	Field((4,-1,45), field_texture),
	Field((-4,-1,45), field_texture)
]

world = BulletWorld()
world.setGravity(Vec3(0, -9.81, 0))

colliders.append(MeshCollider(world, obs, mass=1))


for i in fields:
	BoxCollider(world, i, scale = i.scale/2)

Debugger(world, wireframe=True)
player = Player()
app.run()