# Q1.
# Write a program to take a number and print "Positive", "Negative", or "Zero".
num=int(input("Enter Number: "))
if num<0:
    print("Negative")
elif num>0:
    print("Positive")
elif num==0:
    print("Zero")
else:
    print("Invalid Input")
# Q2.

# Input 3 numbers and print the largest without using max().
numbers=input("Enter Numbers seperated by spaces: ")
num= list(map(int, numbers.split()))
max_num=num[0]
for i in num:
    if i>max_num:
        max_num=i
print(max_num)

# Q3.

# Print the sum of all even numbers from 1 to 100 using a loop.
sum=0
for i in range(1,101):
    sum+=i
print(sum)
# Q5.

# Take a number from user and print its multiplication table (1 to 10).
n=int(input("Enter Number: "))
for i in range(1,11):
    mult=i*n
    print(f"{n}*{i}={mult}")

# Q10.

# Print this pattern:

# *
# **
# ***
# ****

n=int(input("Enter num: "))
for i in range(0,n):
    for j in range(i+1):
        print("*",end="")
    print()
# Q11.

# Write a function is_prime(n) that returns True if number is prime, else False.

        
def is_Prime(num):
    if num==0 or num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return True
        else:
            return False
num=int(input("Enter Number : "))
print(is_Prime(num))
# Q12.

# Write a function factorial(n) without recursion.

def fact(n):
    if n==0 or n==1:
        return 1
    for i in range(0,n):
        factorial=n*fact(n-1)
    return factorial
n=int(input("Enter Number: "))
print(fact(n))
# Q13.

# Write a function that returns the first non-repeating character in a string.
# Example: "aabbcde" → 'c'

def non_Repeat(string):
    n=len(string)
    dict={}
    count=0
    for i in range(0,n):
        if i in dict:
            dict[i]=dict.get(0,i)+1
            count+=1
        else:
            dict[i]=1
            count=1
        if count==1:
            return dict[i]
string=input("Enter Text: ")
print(non_Repeat(string))


    

                  