import re
import sys


def main():
    print(count(input("Text: ")))


def count(str):
    ums=len(re.findall(r"\b(um)\b",str,re.IGNORECASE))


    return ums






if __name__ == "__main__":
    main()

