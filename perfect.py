num=int(input("enter number")) 
i=1
a=0
while i<num:
    if num%i==0:
        a=a+i
        print(a)
    i+=1
if a==num:
    print("perfect number")
else:
    print("not perfect number")
