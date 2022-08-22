import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if "src" in s:
        splt=s.split("src")
        str=splt[1]
        splt2=str.split("\"")
        str2=splt2[1]
        if re.search("^http://youtube.com/embed/(.+)$",str2) or re.search("^https://youtube.com/embed/(.+)$",str2) or re.search("^https://www.youtube.com/embed/(.+)$",str2):
            splt3=str2.split("/")
            str3=splt3[4]
            return "https://youtu.be/"+str3
        else:
            return "None"
    else:
        return "None"





if __name__ == "__main__":
    main()