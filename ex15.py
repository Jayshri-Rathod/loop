i=1
while i<=6:
    space=1
    while space<=6-i:
        print(" ",end="")
        space+=1
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1
    