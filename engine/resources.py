import pyglet
import engine.wizard.animationmanager

pyglet.resource.path = ["resources"]
pyglet.resource.reindex()


# image tools
def center_image(image):
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2
    return image


def uncenter_image(image):
    image.anchor_x = 0
    image.anchor_y = 0
    return image    
    
# A Model is just a bundle of animations; animations are defined from images in the resources folder.
class Model:
    def __init__(self, animations):
    # self.animations should be a dict of string:animation i.e., "walk":anim_purple_wiz_walk
    # as found in engine.resources
        self.animations = animations
        
    def get_anim(self, animation_name):
        if animation_name in self.animations:
            return (self.animations[animation_name], self.animations[animation_name].get_duration())
        else:
            return None, 0


# IMAGES
# backgrounds
title = pyglet.resource.image("title.png")
stone_floor = pyglet.resource.image("gray_stone.png")

# Base wizard spritesheet
# ImageGrid coordinates are from bottom left, NOT top left
wizard_spritesheet = pyglet.resource.image("wizards_spritesheet.png")
image_grid = pyglet.image.ImageGrid(wizard_spritesheet, 16, 16)

# default duration of each frame in animations
DEFAULT_ANIMATION_DURATION = 0.2
DEFAULT_DEATH_ANIM_DURATION = 0.2
DEFAULT_BIRTH_ANIM_DURATION = 0.2


# Animation and model definitions
# Purple wizard
purple_wiz_idle = (
    image_grid[(15,0)],
    image_grid[(15,1)],
    image_grid[(15,2)],
    image_grid[(15,3)],
   )
purple_wiz_cast_1 = (
    image_grid[(15,4)],
    image_grid[(15,5)],
    image_grid[(15,6)],
    image_grid[(15,7)],
    image_grid[(15,8)],
    image_grid[(15,9)],
    image_grid[(15,10)])
purple_wiz_cast_2 = (
    image_grid[(15,11)],
    image_grid[(15,12)],
    image_grid[(15,13)],
    image_grid[(15,14)],
    image_grid[(15,14)])
purple_wiz_walk = (
    image_grid[(14,0)],
    image_grid[(14,1)])
purple_wiz_hit = (
    image_grid[(14,2)],
    image_grid[(15,0)])
purple_wiz_cast_3 = (
    image_grid[(14,3)],
    image_grid[(14,4)],
    image_grid[(14,5)],
    image_grid[(14,6)])
purple_wiz_birth = (
    image_grid[(14,7)],
    image_grid[(14,8)],
    image_grid[(14,9)],
    image_grid[(14,10)],
    image_grid[(14,11)],
    image_grid[(14,12)],
    image_grid[(14,13)],
    image_grid[(14,14)],
    image_grid[(14,15)],
    image_grid[(13,0)])
purple_wiz_death = (
    image_grid[(13,1)],
    image_grid[(13,2)],
    image_grid[(13,3)],
    image_grid[(13,4)],
    image_grid[(13,5)],
    image_grid[(13,6)],
    image_grid[(13,7)],
    image_grid[(13,8)],
    image_grid[(13,9)],
    image_grid[(13,10)],
    image_grid[(13,11)],
    image_grid[(13,12)],
    image_grid[(13,13)],
    image_grid[(13,14)],
    image_grid[(13,15)])

anim_purple_wiz_idle = pyglet.image.Animation.from_image_sequence(
    purple_wiz_idle, duration=DEFAULT_ANIMATION_DURATION, loop=True)
anim_purple_wiz_cast_1 = pyglet.image.Animation.from_image_sequence(
    purple_wiz_cast_1, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_purple_wiz_cast_2 = pyglet.image.Animation.from_image_sequence(
    purple_wiz_cast_2, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_purple_wiz_cast_3 = pyglet.image.Animation.from_image_sequence(
    purple_wiz_cast_3, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_purple_wiz_walk = pyglet.image.Animation.from_image_sequence(
    purple_wiz_walk, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_purple_wiz_hit = pyglet.image.Animation.from_image_sequence(
    purple_wiz_hit, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_purple_wiz_birth = pyglet.image.Animation.from_image_sequence(
    purple_wiz_birth, duration=DEFAULT_BIRTH_ANIM_DURATION, loop = False)
anim_purple_wiz_death = pyglet.image.Animation.from_image_sequence(
    purple_wiz_death, duration=DEFAULT_DEATH_ANIM_DURATION, loop = False)

model_purple_wiz = Model(
    {"walk":anim_purple_wiz_walk,
    "idle":anim_purple_wiz_idle,
    "cast1":anim_purple_wiz_cast_1,
    "cast2":anim_purple_wiz_cast_2,
    "cast3":anim_purple_wiz_cast_3,
    "birth":anim_purple_wiz_birth,
    "death":anim_purple_wiz_death,
    "hit":anim_purple_wiz_hit})

#Green Wizard
green_wiz_idle = (
    image_grid[(12,0)],
    image_grid[(12,1)],
    image_grid[(12,2)],
    image_grid[(12,3)],
   )
green_wiz_cast_1 = (
    image_grid[(12,4)],
    image_grid[(12,5)],
    image_grid[(12,6)],
    image_grid[(12,7)],
    image_grid[(12,8)],
    image_grid[(12,9)],
    image_grid[(12,10)])
green_wiz_cast_2 = (
    image_grid[(12,11)],
    image_grid[(12,12)],
    image_grid[(12,13)],
    image_grid[(12,14)],
    image_grid[(12,14)])
green_wiz_walk = (
    image_grid[(11,0)],
    image_grid[(11,1)])
green_wiz_hit = (
    image_grid[(11,2)],
    image_grid[(12,0)])
green_wiz_cast_3 = (
    image_grid[(11,3)],
    image_grid[(11,4)],
    image_grid[(11,5)],
    image_grid[(11,6)],
    image_grid[11,7])
green_wiz_birth = (
    image_grid[(11,8)],
    image_grid[(11,9)],
    image_grid[(11,10)],
    image_grid[(11,11)],
    image_grid[(11,12)],
    image_grid[(11,13)],
    image_grid[(11,14)],
    image_grid[(11,15)],
    image_grid[(10,0)])
green_wiz_death = (
    image_grid[(10,1)],
    image_grid[(10,2)],
    image_grid[(10,3)],
    image_grid[(10,4)],
    image_grid[(10,5)],
    image_grid[(10,6)],
    image_grid[(10,7)],
    image_grid[(10,8)],
    image_grid[(10,9)],
    image_grid[(10,10)],
    image_grid[(10,11)],
    image_grid[(10,12)],
    image_grid[(10,13)],
    image_grid[(10,14)],
    image_grid[(10,15)])

anim_green_wiz_idle = pyglet.image.Animation.from_image_sequence(
    green_wiz_idle, duration=DEFAULT_ANIMATION_DURATION, loop=True)
anim_green_wiz_cast_1 = pyglet.image.Animation.from_image_sequence(
    green_wiz_cast_1, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_green_wiz_cast_2 = pyglet.image.Animation.from_image_sequence(
    green_wiz_cast_2, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_green_wiz_cast_3 = pyglet.image.Animation.from_image_sequence(
    green_wiz_cast_3, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_green_wiz_walk = pyglet.image.Animation.from_image_sequence(
    green_wiz_walk, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_green_wiz_hit = pyglet.image.Animation.from_image_sequence(
    green_wiz_hit, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_green_wiz_birth = pyglet.image.Animation.from_image_sequence(
    green_wiz_birth, duration=DEFAULT_BIRTH_ANIM_DURATION, loop = False)
anim_green_wiz_death = pyglet.image.Animation.from_image_sequence(
    green_wiz_death, duration=DEFAULT_DEATH_ANIM_DURATION, loop = False)

model_green_wiz = Model(
    {"walk":anim_green_wiz_walk,
    "idle":anim_green_wiz_idle,
    "cast1":anim_green_wiz_cast_1,
    "cast2":anim_green_wiz_cast_2,
    "cast3":anim_green_wiz_cast_3,
    "birth":anim_green_wiz_birth,
    "death":anim_green_wiz_death,
    "hit":anim_green_wiz_hit})

# Blue Wizard
blue_wiz_idle = (
    image_grid[(9,0)],
    image_grid[(9,1)],
    image_grid[(9,2)],
    image_grid[(9,3)],
   )
blue_wiz_cast_1 = (
    image_grid[(9,4)],
    image_grid[(9,5)],
    image_grid[(9,6)],
    image_grid[(9,7)],
    image_grid[(9,8)],
    image_grid[(9,9)],
    image_grid[(9,10)])
blue_wiz_cast_2 = (
    image_grid[(9,11)],
    image_grid[(9,12)],
    image_grid[(9,13)],
    image_grid[(9,14)],
    image_grid[(9,14)])
blue_wiz_walk = (
    image_grid[(8,0)],
    image_grid[(8,1)])
blue_wiz_hit = (
    image_grid[(8,2)],
    image_grid[(9,0)])
blue_wiz_cast_3 = (
    image_grid[(8,3)],
    image_grid[(8,4)],
    image_grid[(8,5)],
    image_grid[(8,6)])
blue_wiz_birth = (
    image_grid[8,7],
    image_grid[(8,8)],
    image_grid[(8,9)],
    image_grid[(8,10)],
    image_grid[(8,11)],
    image_grid[(8,12)],
    image_grid[(8,13)],
    image_grid[(8,14)],
    image_grid[(8,15)],
    image_grid[(7,0)])
blue_wiz_death = (
    image_grid[(7,1)],
    image_grid[(7,2)],
    image_grid[(7,3)],
    image_grid[(7,4)],
    image_grid[(7,5)],
    image_grid[(7,6)],
    image_grid[(7,7)],
    image_grid[(7,8)],
    image_grid[(7,9)],
    image_grid[(7,10)],
    image_grid[(7,11)],
    image_grid[(7,12)],
    image_grid[(7,13)],
    image_grid[(7,14)],
    image_grid[(7,15)])

anim_blue_wiz_idle = pyglet.image.Animation.from_image_sequence(
    blue_wiz_idle, duration=DEFAULT_ANIMATION_DURATION, loop=True)
anim_blue_wiz_cast_1 = pyglet.image.Animation.from_image_sequence(
    blue_wiz_cast_1, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_blue_wiz_cast_2 = pyglet.image.Animation.from_image_sequence(
    blue_wiz_cast_2, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_blue_wiz_cast_3 = pyglet.image.Animation.from_image_sequence(
    blue_wiz_cast_3, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_blue_wiz_walk = pyglet.image.Animation.from_image_sequence(
    blue_wiz_walk, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_blue_wiz_hit = pyglet.image.Animation.from_image_sequence(
    blue_wiz_hit, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_blue_wiz_birth = pyglet.image.Animation.from_image_sequence(
    blue_wiz_birth, duration=DEFAULT_BIRTH_ANIM_DURATION, loop = False)
anim_blue_wiz_death = pyglet.image.Animation.from_image_sequence(
    blue_wiz_death, duration=DEFAULT_DEATH_ANIM_DURATION, loop = False)

model_blue_wiz = Model(
    {"walk":anim_blue_wiz_walk,
    "idle":anim_blue_wiz_idle,
    "cast1":anim_blue_wiz_cast_1,
    "cast2":anim_blue_wiz_cast_2,
    "cast3":anim_blue_wiz_cast_3,
    "birth":anim_blue_wiz_birth,
    "death":anim_blue_wiz_death,
    "hit":anim_blue_wiz_hit})

# Yellow Wizard
yellow_wiz_idle = (
    image_grid[(6,0)],
    image_grid[(6,1)],
    image_grid[(6,2)],
    image_grid[(6,3)],
   )
yellow_wiz_cast_1 = (
    image_grid[(6,4)],
    image_grid[(6,5)],
    image_grid[(6,6)],
    image_grid[(6,7)],
    image_grid[(6,8)],
    image_grid[(6,9)],
    image_grid[(6,10)])
yellow_wiz_cast_2 = (
    image_grid[(6,11)],
    image_grid[(6,12)],
    image_grid[(6,13)],
    image_grid[(6,14)],
    image_grid[(6,14)])
yellow_wiz_walk = (
    image_grid[(5,0)],
    image_grid[(5,1)])
yellow_wiz_hit = (
    image_grid[(5,2)],
    image_grid[(6,0)])
yellow_wiz_cast_3 = (
    image_grid[(5,3)],
    image_grid[(5,4)],
    image_grid[(5,5)],
    image_grid[(5,6)],
    image_grid[(5,7)])
yellow_wiz_birth = (
    image_grid[(5,8)],
    image_grid[(5,9)],
    image_grid[(5,10)],
    image_grid[(5,11)],
    image_grid[(5,12)],
    image_grid[(5,13)],
    image_grid[(5,14)],
    image_grid[(5,15)],
    image_grid[(4,0)])
yellow_wiz_death = (
    image_grid[(4,1)],
    image_grid[(4,2)],
    image_grid[(4,3)],
    image_grid[(4,4)],
    image_grid[(4,5)],
    image_grid[(4,6)],
    image_grid[(4,7)],
    image_grid[(4,8)],
    image_grid[(4,9)],
    image_grid[(4,10)],
    image_grid[(4,11)],
    image_grid[(4,12)],
    image_grid[(4,13)],
    image_grid[(4,14)],
    image_grid[(4,15)])

anim_yellow_wiz_idle = pyglet.image.Animation.from_image_sequence(
    yellow_wiz_idle, duration=DEFAULT_ANIMATION_DURATION, loop=True)
anim_yellow_wiz_cast_1 = pyglet.image.Animation.from_image_sequence(
    yellow_wiz_cast_1, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_yellow_wiz_cast_2 = pyglet.image.Animation.from_image_sequence(
    yellow_wiz_cast_2, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_yellow_wiz_cast_3 = pyglet.image.Animation.from_image_sequence(
    yellow_wiz_cast_3, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_yellow_wiz_walk = pyglet.image.Animation.from_image_sequence(
    yellow_wiz_walk, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_yellow_wiz_hit = pyglet.image.Animation.from_image_sequence(
    yellow_wiz_hit, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_yellow_wiz_birth = pyglet.image.Animation.from_image_sequence(
    yellow_wiz_birth, duration=DEFAULT_BIRTH_ANIM_DURATION, loop = False)
anim_yellow_wiz_death = pyglet.image.Animation.from_image_sequence(
    yellow_wiz_death, duration=DEFAULT_DEATH_ANIM_DURATION, loop = False)

model_yellow_wiz = Model(
    {"walk":anim_yellow_wiz_walk,
    "idle":anim_yellow_wiz_idle,
    "cast1":anim_yellow_wiz_cast_1,
    "cast2":anim_yellow_wiz_cast_2,
    "cast3":anim_yellow_wiz_cast_3,
    "birth":anim_yellow_wiz_birth,
    "death":anim_yellow_wiz_death,
    "hit":anim_yellow_wiz_hit})

# Red Wizard
red_wiz_idle = (
    image_grid[(3,0)],
    image_grid[(3,1)],
    image_grid[(3,2)],
    image_grid[(3,3)],
   )
red_wiz_cast_1 = (
    image_grid[(3,4)],
    image_grid[(3,5)],
    image_grid[(3,6)],
    image_grid[(3,7)],
    image_grid[(3,8)],
    image_grid[(3,9)],
    image_grid[(3,10)])
red_wiz_cast_2 = (
    image_grid[(3,11)],
    image_grid[(3,12)],
    image_grid[(3,13)],
    image_grid[(3,14)],
    image_grid[(3,14)])
red_wiz_walk = (
    image_grid[(2,0)],
    image_grid[(2,1)])
red_wiz_hit = (
    image_grid[(2,2)],
    image_grid[(3,0)])
red_wiz_cast_3 = (
    image_grid[(2,3)],
    image_grid[(2,4)],
    image_grid[(2,5)],
    image_grid[(2,6)])
red_wiz_birth = (
    image_grid[2,7],
    image_grid[(2,8)],
    image_grid[(2,9)],
    image_grid[(2,10)],
    image_grid[(2,11)],
    image_grid[(2,12)],
    image_grid[(2,13)],
    image_grid[(2,14)],
    image_grid[(2,15)],
    image_grid[(1,0)])
red_wiz_death = (
    image_grid[(1,1)],
    image_grid[(1,2)],
    image_grid[(1,3)],
    image_grid[(1,4)],
    image_grid[(1,5)],
    image_grid[(1,6)],
    image_grid[(1,7)],
    image_grid[(1,8)],
    image_grid[(1,9)],
    image_grid[(1,10)],
    image_grid[(1,11)],
    image_grid[(1,12)],
    image_grid[(1,13)],
    image_grid[(1,14)],
    image_grid[(1,15)],
    image_grid[0,0],
    image_grid[0,1],
    image_grid[0,2],)

anim_red_wiz_idle = pyglet.image.Animation.from_image_sequence(
    red_wiz_idle, duration=DEFAULT_ANIMATION_DURATION, loop=True)
anim_red_wiz_cast_1 = pyglet.image.Animation.from_image_sequence(
    red_wiz_cast_1, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_red_wiz_cast_2 = pyglet.image.Animation.from_image_sequence(
    red_wiz_cast_2, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_red_wiz_cast_3 = pyglet.image.Animation.from_image_sequence(
    red_wiz_cast_3, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_red_wiz_walk = pyglet.image.Animation.from_image_sequence(
    red_wiz_walk, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_red_wiz_hit = pyglet.image.Animation.from_image_sequence(
    red_wiz_hit, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_red_wiz_birth = pyglet.image.Animation.from_image_sequence(
    red_wiz_birth, duration=DEFAULT_BIRTH_ANIM_DURATION, loop = False)
anim_red_wiz_death = pyglet.image.Animation.from_image_sequence(
    red_wiz_death, duration=DEFAULT_DEATH_ANIM_DURATION, loop = False)

model_red_wiz = Model(
    {"walk":anim_red_wiz_walk,
    "idle":anim_red_wiz_idle,
    "cast1":anim_red_wiz_cast_1,
    "cast2":anim_red_wiz_cast_2,
    "cast3":anim_red_wiz_cast_3,
    "birth":anim_red_wiz_birth,
    "death":anim_red_wiz_death,
    "hit":anim_red_wiz_hit})
    
# Gray Wizard

wizard_spritesheet = pyglet.resource.image("wizards_spritesheet_annex.png")
image_grid = pyglet.image.ImageGrid(wizard_spritesheet, 16, 16)

gray_wiz_idle = (
    image_grid[(15,0)],
    image_grid[(15,1)],
    image_grid[(15,2)],
    image_grid[(15,3)],
   )
gray_wiz_cast_1 = (
    image_grid[(15,4)],
    image_grid[(15,5)],
    image_grid[(15,6)],
    image_grid[(15,7)],
    image_grid[(15,8)],
    image_grid[(15,9)],
    image_grid[(15,10)])
gray_wiz_cast_2 = (
    image_grid[(15,11)],
    image_grid[(15,12)],
    image_grid[(15,13)],
    image_grid[(15,14)],
    image_grid[(15,14)])
gray_wiz_walk = (
    image_grid[(14,0)],
    image_grid[(14,1)])
gray_wiz_hit = (
    image_grid[(14,2)],
    image_grid[(15,0)])
gray_wiz_cast_3 = (
    image_grid[(14,3)],
    image_grid[(14,4)],
    image_grid[(14,5)],
    image_grid[(14,6)])
gray_wiz_birth = (
    image_grid[(14,7)],
    image_grid[(14,8)],
    image_grid[(14,9)],
    image_grid[(14,10)],
    image_grid[(14,11)],
    image_grid[(14,12)],
    image_grid[(14,13)],
    image_grid[(14,14)],
    image_grid[(14,15)],
    image_grid[(13,0)])
gray_wiz_death = (
    image_grid[(13,1)],
    image_grid[(13,2)],
    image_grid[(13,3)],
    image_grid[(13,4)],
    image_grid[(13,5)],
    image_grid[(13,6)],
    image_grid[(13,7)],
    image_grid[(13,8)],
    image_grid[(13,9)],
    image_grid[(13,10)],
    image_grid[(13,11)],
    image_grid[(13,12)],
    image_grid[(13,13)],
    image_grid[(13,14)],
    image_grid[(13,15)])

anim_gray_wiz_idle = pyglet.image.Animation.from_image_sequence(
    gray_wiz_idle, duration=DEFAULT_ANIMATION_DURATION, loop=True)
anim_gray_wiz_cast_1 = pyglet.image.Animation.from_image_sequence(
    gray_wiz_cast_1, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_gray_wiz_cast_2 = pyglet.image.Animation.from_image_sequence(
    gray_wiz_cast_2, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_gray_wiz_cast_3 = pyglet.image.Animation.from_image_sequence(
    gray_wiz_cast_3, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_gray_wiz_walk = pyglet.image.Animation.from_image_sequence(
    gray_wiz_walk, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_gray_wiz_hit = pyglet.image.Animation.from_image_sequence(
    gray_wiz_hit, duration=DEFAULT_ANIMATION_DURATION, loop = False)
anim_gray_wiz_birth = pyglet.image.Animation.from_image_sequence(
    gray_wiz_birth, duration=DEFAULT_BIRTH_ANIM_DURATION, loop = False)
anim_gray_wiz_death = pyglet.image.Animation.from_image_sequence(
    gray_wiz_death, duration=DEFAULT_DEATH_ANIM_DURATION, loop = False)

model_gray_wiz = Model(
    {"walk":anim_gray_wiz_walk,
    "idle":anim_gray_wiz_idle,
    "cast1":anim_gray_wiz_cast_1,
    "cast2":anim_gray_wiz_cast_2,
    "cast3":anim_gray_wiz_cast_3,
    "birth":anim_gray_wiz_birth,
    "death":anim_gray_wiz_death,
    "hit":anim_gray_wiz_hit})

wizard_models=(model_purple_wiz, model_green_wiz, model_blue_wiz, model_yellow_wiz, model_red_wiz, model_gray_wiz)

# old wizard art
wizard0 = pyglet.resource.animation("wizard0.gif")
wizard0.anchor_x = wizard0.get_max_width() // 2  # this appears ineffective at the moment
wizard0.anchor_y = wizard0.get_max_height() // 2