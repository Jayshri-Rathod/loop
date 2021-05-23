# i=1
# while i<11:
#     print(i)
#     i+=1

# for i in range(1,11):
#     print(i)


# i=1
# while i<21:
#     if i%2==0:
#         print(i)
#     i+=1

# for i in range(1,21):
#     if i%2==0:
#     print(i)

# i=1
# while i<21:
#     if i%2!=0:
#         print(i)
#         i+=1

# for i in range(1,21):
#     if i%2!=0:
#         print(i)


# i=21
# while i>0:
#     if i%2==0:
#         print(i)
#     i-=1

# for i in range(21,0,-1):
#     if i%2==0:
#         print(i)

# num=int(input("enter number"))
# i=1
# while i<11:
#     print(num*i)
#     i+=1


# num=int(input("enter number"))
# for i in range(1,11):
#     print(num*i)


num=int(input("enter number"))
save=num
product=1
while save!=0:
    product=product*(save%10)
    save=int(save/10)
print(product)

# num=int(input("enter number"))
# save=num
# for i in range(0):
#     i=i*(save%10)
#     save=int(save/10)
# print(i)


# num=int(input("enter number"))
# i=2
# while num>2:
#     i=i*num
#     num-=1
# print(i)


# num=int(input("enter number"))
# n=num
# i=0
# sum=0
# while i<=n:
#     a=num%10
#     sum=sum+a
#     num=num//10
#     i+=1
# print(sum)


# num=int(input("enter number"))
# i=2
# while i<=num:
#     if num%2==0:
#         print(num,"not prime number")
#         break
#     i+=1
# else:
#     print(num,"prime number")


