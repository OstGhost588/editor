from PIL import Image, ImageFont
from PIL import ImageDraw
im = Image.open("img.png")
I1 = ImageDraw.Draw(im)

myFont = ImageFont.truetype('Christmas ScriptC.ttf', 65)
I1.text((28,36), "nice car", font = myFont, fill = (0,0,125))
im.show()
im.save()