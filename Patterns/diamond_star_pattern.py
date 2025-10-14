n=int(input("Enter Number: "))
for i in range(0,n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(0,2*i+1):
        print("*",end="")
    for l in range(0,n-i-1):
        print(" ",end="")
    print()
for i in range(0,n):
    for o in range(0,i):
        print(" ",end="")
    for p in range(2*n-(2*i+1)):
        print("*",end="")
    for q in range(0,i):
        print(" ",end="")
    print()

    