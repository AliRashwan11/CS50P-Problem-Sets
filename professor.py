import random


def main():
    lvl=get_level()
    score=10

    for _ in range(10):
        x=generate_integer(lvl)
        y=generate_integer(lvl)
        counter=0
        while True:
            try:
                ans=int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            if ans==(x+y):
                counter=0
                break
            else:
                counter=counter+1
                print("EEE")
            if counter==3:
                print(f"{x} + {y} = {x+y}")
                score=score-1
                break

    print("Score:", score)




def get_level():
    while True:
        try:
            lvl=int(input("Level:"))
        except ValueError:
            continue
        if lvl==1 or lvl==2 or lvl==3:
            return lvl
            break
        else:
            pass
    


def generate_integer(level):
    num=0
    if level==1:
        num=random.randint(0,9)
    elif level==2:
        num=random.randint(10,99)
    elif level==3:
        num=random.randint(100,999)
        
    return num


if __name__ == "__main__":
    main()