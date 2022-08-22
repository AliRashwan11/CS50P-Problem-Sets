import validators

inputEmail=input("Email :")

isTrue=validators.email(inputEmail)

if isTrue:
    print("Valid")
else:
    print("Invalid")