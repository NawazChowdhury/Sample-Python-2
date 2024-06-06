a=int(input("Enter Num 1: "))
b=int(input("Enter Num 2: "))
c=int(input("Enter Num 3: "))

if(a==b and b==c):
    res=(a+b+c)*3
elif(a==b or b==c or a==c):
    res=(a+b+c)*2
else:
    res=a+b+c


print(res)