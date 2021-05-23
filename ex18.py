i=1
while i<=100:
    j=2
    num=0
    while j<i-1:
        if i%j==0:
            num+=1
        j+=1
    if  i!=1 and num==0:
        print(i,"prime number")
    else:
        print(i,"not a prime number")
    i+=1
    
# n=int(input("enter number"))
# num1=str(n)
# i=1
# while i<=len(num1):
#     if len(num1)==1:
#         print(n)
#         break
#     a=n%10
#     n=n//10
#     i+=2
#     print(n*10,"+",a*1)


# n=int(input("enter the number"))
# x=n%10
# y=(n//10)%10
# z=((n//10)//10)%10
# b=((n//10)//10)//10
# a=x*1000+y*100+z*10+b
# if a<100000:
#     print(a)
# else:
#     print("input is wrong")

# num=int(input("enter number"))
# num1=str(num)
# i=1
# while i<=len(num1):
#     n=int(num1)
#     j=1
#     while j<=i:
#         n=n//100
#         print(n*10**len(num1),"+",end=" ")
#         j+=1
#     len(num1)-1



# year1=int(input("enter year"))
# year2=int(input("enter year"))
# i=year1
# while i<=year2:
#     if i%4==0 and i%100!=0 or i%400==0:
#         print(i,"leap year")
#     else:
#         print(i,"is not a leap year")
#     i+=1



# a=int(input("enter number"))
# b=int(input("enter number"))
# c=int(input("enter number"))
# i=0
# while i<1:
#     if (a>b)*a+(b>a)*b+(c>a)*c+(c>b)*c==a:
#         print(a)
#     elif (a>b)*a+(b>a)*b+(c>a)*c+(c>b)*c==b:
#         print(b)
#     elif (a>b)*a+(b>a)*b+(c>a)*c+(c>b)*c==c:
#         print(c)
#     else:
#         print("all are equal")
#     i+=1