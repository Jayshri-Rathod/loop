num1=int(input("enter  starting number"))
num2=int(input("enter ending number"))
i=num1
while i<=num2:
    j=1
    while j<=10:
        print(i,"*",j,"=",i*j)
        j+=1
    i+=1
    print()
