def example(name):
    return name.split('.')[-1]
print(example("document.pdf"))
print(example("image.jpg"))


a=('apple','banana','cherry')
b=0
x=dict.fromkeys(a,b)
print(x)


username=input("enter the name")
if username.isalnum()and 6<=len(username)<=15:
    print("vaild username")
else:
    print("invalid username")  



a="hello world from python"
print(a[: : -1])
new={}
for i in a:
    if i.isalpha():
        new [i]=new.get (i,0)+1
print(new)
result=""
for i in a:
    if i not in result:
       result+=i
print(result)          







