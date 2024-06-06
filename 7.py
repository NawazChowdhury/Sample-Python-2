x=True

a=int(input("Enter Marks: "))
grade=""
if(a>=90):
    grade="A+"
    x=True
elif(a>=70):
    grade="A"
    x=True

if(a<=0):
    x=False


if(x):
    print("Pass with",grade)
else:
    print("Fail")