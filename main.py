from PIL import Image, ImageDraw #


def new_foto_1(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 1, h // 1))


def new_foto_2(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))


im = new_foto_1('cat.jpg')
im2 = new_foto_2('sun.jpg')

im.paste(im2, (200, 200))
im.show()
