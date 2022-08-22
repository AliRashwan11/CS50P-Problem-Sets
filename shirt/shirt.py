from ctypes import sizeof
import sys
from PIL import Image
import PIL
from PIL import ImageOps


if not len(sys.argv) == 3:
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")
else:
    if not "." in sys.argv[1]:
        sys.exit("Invalid input")
    splt=sys.argv[1].split(".")
    splt2=sys.argv[2].split(".")
    if not splt[1]=="jpeg" and not splt[1]=="jpg" and not splt[1]=="png":
        sys.exit("Invalid input")
    if not splt[1]==splt2[1]:
        sys.exit("Input and output have different extensions")
    try:
        inputfile=open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    inputimage=Image.open(sys.argv[1])
    shirtimage=Image.open("shirt.png")

    sizeofshirt=shirtimage.size

    outputimage=PIL.ImageOps.fit(inputimage,sizeofshirt)
    outputimage.paste(shirtimage,shirtimage)
    outputimage.save(sys.argv[2])
    sys.exit()
