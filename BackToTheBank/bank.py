
def main():
    inputmsg=input("Greeting: ")
    ret=value(inputmsg)
    print(f"${ret}")
    


def value(inputmsg):
    if inputmsg.lstrip().startswith("hello") or inputmsg.lstrip().startswith("Hello"):
        return 0
    elif inputmsg.lstrip().startswith("H") or inputmsg.lstrip().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()