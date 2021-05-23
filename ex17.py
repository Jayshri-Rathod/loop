i=0
while i<7:
    j=0
    while j<7: 
        if (i+j==4)or (j-i==4) or (i+j==10)or (i-j==2):
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()
    i+=1