def main():
    inp=input("Enter a fraction")
    num=convert(inp)
    fin=gauge(num)
    print(fin)


def convert(fraction):
  
        part=fraction.partition("/")

        try:
            X=int(part[0])
            Y=int(part[2])
        except ValueError:
            raise ValueError
        else:
            try:
                 per = (X*100)/Y
            except ZeroDivisionError:
                raise ZeroDivisionError
            else:
                if per<=100 and per>=0:
                    return round(per)
                else:
                    raise ValueError


def gauge(percentage):
    if percentage==0 or percentage==1:
        return "E"
    elif percentage==100 or percentage==99:
        return "F"
    else:
        return f"{percentage}%"
    


if __name__ == "__main__":
    main()