#Lesson 8 - PIL Image analysis and editing

#In this lesson I'll show you how to read data from image file and how to draw on a picture in Python

from PIL import Image, ImageDraw #Let's import this stuff (you might have to install the module)
#If you use Thonny click on top left corner Tools -> Manage packages then search for Pillow and install it.

picdata = Image.open("rainbow.jpg") #let's load rainbow.jpg
pic = picdata.load()
#now let's get RGB values from some pixels
r, g, b = pic[1,1] #get color of pixel 1x 1y, save Red Green and Blue values.

#As you probably already know, color of pixels on computer is saved with 3 values.
#These are Red, Green and Blue, each is a value from 0 to 255.
#In PNG there is also fourth value for transparency.

print("X=1, Y=1, Red: "+str(r)+" Green: "+str(g)+" Blue: "+str(b)) #Display color info
#This returns "X=1, Y=1, Red: 254 Green: 0 Blue: 0" in your Shell window. That pixel is red after all.

r, g, b = pic[590,585] #now let's read the same but for a pixel in green part
print("X=590, Y=585, Red: "+str(r)+" Green: "+str(g)+" Blue: "+str(b))
#It returns "X=590, Y=585, Red: 1 Green: 253 Blue: 8"

r, g, b = pic[1328,507] #now let's take a pixel which is between dark blue and pink
print("X=1328, Y=507, Red: "+str(r)+" Green: "+str(g)+" Blue: "+str(b))
#"X=1328, Y=507, Red: 185 Green: 0 Blue: 254"

#Now let's draw something on copy of this image and save it

draw = ImageDraw.Draw(picdata) #Let's call image editor
draw.line((0,0,500,300),  fill=(0,0,0), width=10) #let's draw a black line from pixel x0 y0 to x500 y300, 10 pixels wide
draw.rectangle((800, 500, 1000, 970), fill=(255,255,0), outline=None) #draw yellow rectangle
draw.polygon(((1000, 1000), (1100, 1000), (1300, 900)),fill=(255, 255, 255),outline=None) #draw white polygon
draw.ellipse((1300, 200, 1500, 300), fill=(128, 128, 128), outline=(0,0,0)) #gray ellipse
draw.text((1500, 500), "This is a text", (0,0,0))

picdata.save('MyImage.jpg') #save result image to file
picdata.show() #shows you the result image

canvas = Image.new("RGB", (500,250), (255, 255, 255)) #you can also create canvas from scratch instead of loading a file
newdraw = ImageDraw.Draw(canvas)
newdraw.text((10, 10), "Hello, I'm a pink text rendered on picture. There's a square under me.", (255,2,255))
newdraw.rectangle((100, 100, 200, 200), fill=(0,0,0), outline=(255,1,0)) #
canvas.save('My2ndImage.png')
canvas.show()
#Pillow has lot of other functions like resizing image etc. Everything is in module's documentation which can be found online.