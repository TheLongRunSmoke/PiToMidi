import sys
from sys import stdout
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
sys.path.append("libs")
from utils import *

# Oversampling.
antialiasing = 3

# Minimal padding from image border.
paddingMin = 12

# Output image size.
width = 1280
height = 720 

# Symbol count in row and columns, respectively.
countX = 50
countY = 20

# Font size in pt.
fontSize = 30

padding, interval = compute_params((width, height), paddingMin, fontSize, (countX, countY), antialiasing)
img = Image.new("RGB", (width*antialiasing, height*antialiasing), (0,0,0))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", fontSize*antialiasing)
fromFile = argv_resolver(sys.argv)[0]
outputDir = argv_resolver(sys.argv)[0][0:-4]
if not(os.path.isdir(outputDir)):
  os.mkdir(outputDir)
xpos = 0
ypos = 0
num = 1
img.resize((width,height), Image.ANTIALIAS).save("/".join([outputDir, "0000.png"]))
with open(fromFile) as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if is_number(c):
        draw.text((padding[0]+xpos,padding[1]+ypos),c,(255,255,255),font=font)
        img.resize((width,height), Image.ANTIALIAS).save("/".join([outputDir, ".".join([str(num).zfill(4),"png"])]))
        xpos += interval[0]
        if xpos >= (interval[0]*countX):
            xpos = 0
            ypos += interval[1]
            if ypos >= (interval[1]*countY):
                break
        num += 1
        stdout.write("\r")
        stdout.flush()
        for i in range(0, num/20):
          stdout.write("|")
        stdout.write(bar(num%20/5))
        stdout.write(" %.1f%%" % ((num/float(1000))*100) )
        stdout.flush()
stdout.write("\nReady!")
stdout.flush()        
