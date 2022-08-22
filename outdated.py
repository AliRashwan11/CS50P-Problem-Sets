months={

    "January" : "1",
    "February" :"2",
    "March":"3",
    "April":"4",
    "May":"5",
    "June":"6",
    "July":"7",
    "August" :"8",
    "September" :"9",
    "October" :"10",
    "November" :"11",
    "December" :"12"

}

def is_day(day):
    dayy=int(day)
    if 0<dayy<32:
        return True
    return False

def is_month(month):
    monthh=int(month)
    if 0<monthh<13:
        return True
    return False


while True:
    date=input("Date: ")
    date=date.strip()
    splt=date.split()
    if date=="":
        continue
    mnth=splt[0]
    if mnth in months:
        rest=splt[1]
        part=rest.partition(",")
        day=part[0]
        year=splt[2]
        if part[1]=="":
            continue
        if not is_day(day):
            continue
        if len(day)==1:
            day="0"+day
        if mnth=="October" or mnth=="November" or mnth=="December":
            print(f"{year}-{months[mnth]}-{day}")
        else:
            print(f"{year}-0{months[mnth]}-{day}")

        break
    elif mnth==date and (mnth[2]=="/" or mnth[1]=="/"):
        part=date.partition("/")
        dayandyear=part[2]
        part2=dayandyear.partition("/")
        mnth=part[0]
        day=part2[0]
        year=part2[2]
        if not is_day(day):
            continue
        if not is_month(mnth):
            continue
        if len(day)==1:
            day="0"+day
        if len(mnth)==1:
            mnth="0"+mnth
        print(f"{year}-{mnth}-{day}")
        break
    else:
        continue

