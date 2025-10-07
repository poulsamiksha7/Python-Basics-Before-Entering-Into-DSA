n=int(input("Enter Number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Outer loop i=1
# j=1
# print: 1

#Outer loop i=2
# j=1,2
# print: 1 2 

#Outer loop i=3
# j=1,2,3
# print: 1 2 3

#Outer loop i=n
# j=1,2,3,4....,n
# print: 1 2 3 4 5 .... n