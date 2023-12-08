import os
import sys
import random
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Resolution..
WD = 1920
HT = 1080

# Colors..
black = color.rgb(0, 0, 0)
white = color.rgb(255, 255, 255)
gray = color.rgb(80, 80, 80)
snow = color.rgb(200, 200, 200)

# Main App Initiate..
app = Ursina(size=(WD, HT), borderless=True)

# Default GUI Properties..
window.fullscreen = True
window.exit_button.visible = False
mouse.locked = True
mouse.visible = True
application.development_mode = False

# Texture Files..
skyIMG = load_texture('data/img/bg/sky.jpg')

# Default Functions..
def respawn():
	player.position = (0, 0, 0)
	player.rotation = (0, 0, 0)
	player.update

# Render World Objects..
Sky(texture=skyIMG)
player = FirstPersonController(position=(0, 0, 0), rotation=(0, 0, 0), collider='box')
ground = Entity(model='plane', scale=(200, 10, 200), color=snow, texture='white_cube', texture_scale=(100, 100), collider='box')

# Snow Falling..
for i in range(0, 1500):
	exec(f"xtop = random.randrange(-200, 200)")
	exec(f"ztop = random.randrange(-200, 200)")
	exec(f"ytop = random.choice([200, 225, 250])")
	exec(f"rgrv = random.choice([5.0, 8.0, 10.0])")
	exec(f"snowflake{i} = Entity(model='sphere', scale=(0.65, 0.65, 0.65), position=({xtop}, {ytop}, {ztop}), gravity={rgrv}, color=color.rgb(250, 250, 250), collider='sphere')")

# Default Object Properties..
player.speed = 10

# Listen For Uesr Input..
def input(key):
	if key == 'escape':
		quit()
	elif key == 'left shift':
		player.speed = 20
		player.update
	elif key == 'left shift up':
		player.speed = 10
		player.update
	else:
		pass

def update():
	if player.y < -10.0:
		respawn()
	else:
		pass

	for x in range(0, 1500):
		exec(f"snowflake{x}.y -= random.choice([1.5, 3.0])")
		exec(f"""if snowflake{x}.y <= -5:
	snowflake{x}.y = int(random.choice([100, 125, 150, 200, 225, 250]))
	""")

# Rune App..
app.run()
