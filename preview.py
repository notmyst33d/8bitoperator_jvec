from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (2100, 820), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("fonts/8bitoperator_jvec.ttf", 16 * 8)

draw.text((64, 32), "8bitoperator JVEC", font=font, fill=(0, 0, 0))
draw.text((64, 32 * 6), "QWERTYUIOPASDFGHJKLZXCVBNM", font=font, fill=(0, 0, 0))
draw.text((64, 32 * 10), "qwertyuiopasdfghjklzxcvbnm", font=font, fill=(0, 0, 0))
draw.text((64, 32 * 16), "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ", font=font, fill=(0, 0, 0))
draw.text((64, 32 * 20), "йцукенгшщзхъфывапролджэячсмитьбю", font=font, fill=(0, 0, 0))

image.save("res/jvec.png")
