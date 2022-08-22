def main():
    time=input("what time is it? ")
    convertedtime=convert(time)
    if convertedtime>=7 and convertedtime<=8:
        print("breakfast time")
    elif convertedtime>=12 and convertedtime<=13:
        print("lunch time")
    elif convertedtime>=18 and convertedtime<=19:
        print("dinner time")



def convert(time):
    times=time.split(":")
    hour=int(times[0])
    min=float(times[1])
    min=(min/60)
    return hour+min


main()