import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        numbers=ip.split(".")
        if -1<int(numbers[0])<256 and -1<int(numbers[1])<256 and -1<int(numbers[2])<256 and -1<int(numbers[3])<256:
            return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()