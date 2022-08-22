import sys

msg="Adieu, adieu, to "
counter=0

while True:
    try:
        name=input("Name:")
        msg=msg+","
        counter=counter+1
    except EOFError:
        break
    msg=msg+name

toremove=0
newmsg=""

for letter in msg:
    if letter=="," and toremove==counter-2:
        newmsg=newmsg+"and"
        toremove=toremove+1
    elif letter==",":
        toremove=toremove+1
        newmsg=newmsg+","
    else:
        newmsg=newmsg+letter

print(newmsg)



