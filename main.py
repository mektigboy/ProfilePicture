from PIL import Image, ImageFont, ImageDraw

width, height = 300, 300
img = Image.new("RGBA", (width, height), "#000000")
string = "mektigboy"
font = ImageFont.truetype("whiterabbit.ttf", 50)
w, h = font.getsize(string)
draw = ImageDraw.Draw(img)

draw.text(((width - w) / 2, (height - h) / 2), string, font = font, fill = "#00ff00")

img.show()
