def main():
    percentage=take_fraction()
    percentage=round(percentage)
    if percentage==0 or percentage==1:
        print("E")
    elif percentage==100 or percentage==99:
        print("F")
    else:
        print(f"{percentage}%")



def take_fraction():
    while True:
        fraction=input("Enter a fraction")
        part=fraction.partition("/")

        try:
            X=int(part[0])
            Y=int(part[2])
        except ValueError:
            pass
        else:
            try:
                 per = (X*100)/Y
            except ZeroDivisionError:
                pass
            else:
                if per<=100 and per>=0:
                    return per



main()