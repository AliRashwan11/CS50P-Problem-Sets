def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")





def is_valid(str):
    counter=0
    numpassed=0
    for letter in str:
        counter=counter+1

        if not letter.isalnum():
            return False

        if counter==1 or counter==2:
            if not letter.isalpha():
                return False

        if numpassed==0 and letter=='0':
            return False
        if letter.isnumeric():
            numpassed=1
        if letter.isalpha() and numpassed==1:
            return False






    if counter>6 or counter <2:
        return False

    return True







main()