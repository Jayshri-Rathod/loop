n=int(input("enter number"))
num=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if num==sum:
    print("Amstrong number")
else:
    print("Amstrong number nahi hai")
