num=int(input("enter number"))
print("factor of number",num)
i=1
while i<=num:
    if num%i==0:
        print(i)
    i+=1