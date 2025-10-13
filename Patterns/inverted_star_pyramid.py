n=int(input("Enter Number: "))
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for k in range(2*n-(2*i+1)):
        print("*",end="")
    print()

# Outer loop i=0
# Second Inner Loop k=2*n-(2*i+1)=5 -(0,4)
# print *****

# Outer loop i=1
# Inner Loop j=0,1 This will print spaces
# Second Inner Loop k=2*n-(2*i+1)=3 -(0,2) This will print Stars
# print ***

# Outer loop i=0
# Inner Loop j=0,1,2 This will print spaces
# Second Inner Loop k=2*n-(2*i+1)=1 -(0)This will print stars
# print **