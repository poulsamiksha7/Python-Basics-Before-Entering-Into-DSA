# Print 1 to 10 using for & while
n=1
while n<=10:
    print(n)
    n+=1

# Using for loop
for i in range(1,11):
    print(i)

# - Sum 1 to 50
sum=0
for i in range(1,51):
    sum=i+sum
    print(sum)

# - Table of user input
n=int(input("Enter your number: "))
mul=0
for i in range(1,11):
    mul=n*i
    print(f"{n}x{i}={mul}")

