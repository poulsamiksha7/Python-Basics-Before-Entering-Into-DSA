# - Triangle pattern
n=int(input("Enter your number: "))
for i in range(0,n):
    for j in range(i+1):
        print("*",end=" ")
    print()