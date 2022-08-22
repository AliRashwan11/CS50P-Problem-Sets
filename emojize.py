
from emoji import emojize
import sys

inp=input("Enter message :")
alias=False

if inp=="":
    sys.exit()

splt=inp.split()
print(splt)

newinp=""

for word in splt:
    for letter in word:
        if letter==":":
            newword=emojize(word,language="alias")
            newinp=newinp+newword+" "
            break
        else:
            newinp=newinp+letter
    newinp=newinp+" "


print(newinp)