inputmsg=input("Greeting: ")
if inputmsg.lstrip().startswith("hello") or inputmsg.lstrip().startswith("Hello"):
    print("$0")
elif inputmsg.lstrip().startswith("H") or inputmsg.lstrip().startswith("h"):
    print("$20")
else:
    print("$100")


