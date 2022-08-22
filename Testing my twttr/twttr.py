def main():
    str=input("Input a string : ")
    shorten(str)


def shorten(str):
    temp=""

    for letter in str:
        if letter== "A" or letter=="a" or letter=="E" or letter=="e" or letter=="i" or letter=="I" or letter=="O" or letter=="o" or letter=="U" or letter=="u":
            continue
        else:
            temp=temp+letter


    return temp




if __name__ == "__main__":
    main()