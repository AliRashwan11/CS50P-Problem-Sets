from pyfiglet import Figlet
import sys
import random



figlet=Figlet()

fonts=figlet.getFonts()

## print(fonts)

if len(sys.argv)==3:
    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        if sys.argv[2] in fonts:
            inp=input("Input:")
            tofont=sys.argv[2]
            figlet.setFont(font=tofont)
            print(figlet.renderText(inp))
            sys.exit()
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
elif len(sys.argv)==1:

    inp=input("Input:")
    tofont=random.choice(fonts)
    figlet.setFont(font=tofont)
    print(figlet.renderText(inp))

else:
    sys.exit("Invalid usage")


