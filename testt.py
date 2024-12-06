a=int(input("enter the number="))
b=int(input("enter the number="))
lst=['add','sub','mul','div','exist']
print("1-addition  2-subtraction  3-multiplication  4-division  5-exist")
i=1
for i in lst:
    i=int(input("select the operation to be performed-"))
    if i==1:
        print("addition")
        c=a+b
        print(c)
    if i==2:
        print("subtraction")
        c=a-b
        print(c)
    if i==3:
        print("multiplication")
        c=a*b
        print(c)
    if i==4:
        if a==0 or b==0:
            print("operation cannot be performed")
        else:
            print("division")
            c=a/b
            print(c)
    if i==5:
        print("stopped")                       