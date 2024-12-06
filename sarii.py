a=float(input("enter a number!"))
b=float(input("enter a number!"))
def add():
    sum=a+b
    return sum
def subtraction():
    diff=a-b
    return diff
def product():
    product=a*b
    return product
def division():
    div=a/b
    return div
for i in range (5):
    print("the operation are 1.addition/n2.subtraction/n3.multiplication/n4.division/n5.exit")
    operation=int(input("enter the number:"))
    if operation==1:
        c=add()
        print(c)
    elif operation==2:
         c=subtraction()
         print(c)
    elif operation==3:
           print(c)
    elif operation==4:
        if b!=0:
            c=division
            print()
         else:
            print("division by zero is not possible")
    elif operation==5:
        print("exit")
        break
    else:
        print ("invalid choice")






    