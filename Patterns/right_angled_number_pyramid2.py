num=int(input("Enter Number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


#Outer loop i=1
# Innerloop j=1
# print=1

#Outer loop i=2
# Innerloop j=1,2
# print=2 2

#Outer loop i=3
# Innerloop j=1,2,3
# print=3 3 3

#Outer loop i=n
# Innerloop j=1,2,3,....,n
# print=n n n n