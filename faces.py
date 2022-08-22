def convert(msg):
    msg=msg.replace(":)","🙂")
    msg=msg.replace(":(" , "🙁")
    return msg

def main():
    inputmsg=input("input text: ")
    inputmsg=convert(inputmsg)
    print(inputmsg)



main()


