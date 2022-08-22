expression=input("Expression: ")
elements=expression.split()
sum=float(0)

if elements[1]=="+":
    sum=float(elements[0])+float(elements[2])
elif elements[1]=="-":
    sum=float(elements[0])-float(elements[2])
elif elements[1]=="*":
    sum=float(elements[0])*float(elements[2])
else :
    sum=float(elements[0])/float(elements[2])

print(sum)


