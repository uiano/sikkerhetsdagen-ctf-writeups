from PIL import Image, ImageFont, ImageDraw
from hashlib import md5
FLAG = 'UIACTF{Usikre direkte objektreferanser}'
for i, c in enumerate(FLAG):
    filename = md5(str(i).encode()).hexdigest() + '.jpg'
    img = Image.new(mode="RGB", size=(150, 200), color=(242, 243, 245))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf", 100)
    draw.text((0, 0),c,(200, 16, 46),font=font)
    img.save(filename)
    print(i, c, filename)


