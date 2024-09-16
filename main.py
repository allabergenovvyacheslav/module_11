from PIL import Image
from PIL import ImageFont, ImageDraw


class PostMaker:
    def __init__(self, new_foto):
        self.image = Image.open(new_foto)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 1, self.h // 1))

    def paste(self, name_foto):
        paste_image = Image.open(name_foto)
        paste_image = paste_image.resize((paste_image.size[0] // 3, paste_image.size[1] // 3))
        self.image.paste(paste_image, (0, 0))

    def upgrade(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("ofont.ru_AV Fontimer.ttf", 30)
        draw.text((5, 220), 'Привет пупсик', font=font, fill='yellow')
        self.image.show()


image = (PostMaker('cat.jpg'))
image.paste('sun.jpg')
image.upgrade('Привет пупсик')
