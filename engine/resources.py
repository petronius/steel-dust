import pyglet

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


# IMAGES
# backgrounds
title = pyglet.resource.image("title.png")

# wizards
wizard0 = pyglet.resource.animation("wizard0.gif")
wizard0.anchor_x = wizard0.get_max_width() // 2  # this appears ineffective at the moment
wizard0.anchor_y = wizard0.get_max_height() // 2

purp_wiz_stand = [pyglet.resource.image('wiz_idle_1.png'),]
purp_wiz_walk = [pyglet.resource.image('wiz_idle_1.png'),
                   pyglet.resource.image('wiz_walk_1_1.png'),]
purp_wiz_cast_1 = [pyglet.resource.image('wiz_cast_1_1.png'),
                   pyglet.resource.image('wiz_cast_1_2.png'),
                   pyglet.resource.image('wiz_cast_1_3.png'),
                   pyglet.resource.image('wiz_cast_1_4.png'),
                   pyglet.resource.image('wiz_cast_1_5.png'),]
purp_wiz_cast_2 = [pyglet.resource.image('wiz_cast_2_1.png'),
                   pyglet.resource.image('wiz_cast_2_2.png'),
                   pyglet.resource.image('wiz_cast_2_3.png'),
                   pyglet.resource.image('wiz_cast_2_4.png'),]
anim_purp_wiz_stand = pyglet.image.Animation.from_image_sequence(purp_wiz_stand, duration=0.1, loop=True)
anim_purp_wiz_cast_1 = pyglet.image.Animation.from_image_sequence(purp_wiz_cast_1, duration=0.2, loop = False)
anim_purp_wiz_cast_2 = pyglet.image.Animation.from_image_sequence(purp_wiz_cast_2, duration=0.2, loop = False)
anim_purp_wiz_walk = pyglet.image.Animation.from_image_sequence(purp_wiz_cast_1, duration=0.2, loop = True)