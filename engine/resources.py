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
wizard0 = pyglet.resource.animation("wizard0.gif")
wizard0.anchor_x = wizard0.get_max_width() // 2
wizard0.anchor_y = wizard0.get_max_height() // 2
