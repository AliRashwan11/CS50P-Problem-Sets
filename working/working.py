import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(str):
    if re.search("^[0-9]+:[0-9]{2} (AM|PM) to [0-9]+:[0-9]{2} (AM|PM)$",str) or re.search("^[0-9]+ (AM|PM) to [0-9]+ (AM|PM)$",str):
        if ":" in str:
            splt=str.split(":")
            hour1=int(splt[0])
            str1=splt[1]
            min1=0
            
            if "AM" in str1:
                splt2=str1.split("AM")
                str2=splt2[0]
                min1=int(str2)
                time1=0
                if hour1==12:
                    time1=-12
            elif "PM" in str1:
                splt2=str1.split("PM")
                str2=splt2[0]
                min1=int(str2)
                time1=12
                if hour1==12:
                    time=0
            if -1<hour1<13 and -1<min1<60:
                True
            else:
                raise ValueError

            splt3=str.split("to")
            str3=splt3[1].strip()
            hour2=str3.split(":")
            min2=hour2[1]
            min2=(min2.split(" "))[0]
            min2=int(min2)
            hour2=int(hour2[0])


            if -1<hour2<13 and -1<min2<60:
                True
            else:
                raise ValueError

            if "AM" in str3:
                time2=0
                if hour2==12:
                    time2=-12
            else:
                time2=12
                if hour2==12:
                    time2=0

            hour1+=time1
            hour2+=time2

            strToReturn=""
            if hour1<10:
                strToReturn+="0"
            strToReturn+=f"{hour1}:"
            if min1<9:
                strToReturn+="0"
            strToReturn+=f"{min1} to "
            if hour2<10:
                strToReturn+="0"
            strToReturn+=f"{hour2}:"
            if min2<9:
                strToReturn+="0"
            strToReturn+=f"{min2}"

            return strToReturn

        else:
            spltn=str.split("to")
            fromv=spltn[0]
            to=spltn[1].strip()
           

            if "AM" in fromv:
                time1=0
                fromv=(fromv.split("AM"))[0]
                fromv=fromv.strip()
                if fromv=="12":
                    time1=-12
            else:
                time1=12
                fromv=(fromv.split("PM"))[0]
                fromv=fromv.strip()
                if fromv=="12":
                    time1=0

            if "AM" in to:
                time2=0
                to=(to.split("AM"))[0]
                to=to.strip()
                if to=="12":
                    time2=-12
            else:
                time2=12
                to=(to.split("PM"))[0]
                to=to.strip()
                if to=="12":
                    time2=0
            fromv=int(fromv)
            to=int(to)

            if -1<fromv<13 and -1<to<13:
                True
            else:
                raise ValueError

            fromv+=time1
            to+=time2

            strToReturn=""
            if fromv<10:
                strToReturn+="0"
            strToReturn+=f"{fromv}:00 to "
            if to<10:
                strToReturn+="0"
            strToReturn+=f"{to}:00"

            return strToReturn
    else:
        raise ValueError






if __name__ == "__main__":
    main()