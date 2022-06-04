from PIL import Image, ImageFont, ImageDraw

width = 300
height = 300
img = Image.new("RGBA", (width, height), "black")
string = ":)"
font = ImageFont.truetype("whiterabbit.ttf", 30)
w, h = font.getSize(string)
draw = ImageDraw.Draw(img)

draw.text(((width - w) / 2, (height - h) / 2), string, font = font, fill = "green")

img.show()
