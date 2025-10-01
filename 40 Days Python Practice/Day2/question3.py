#  Divisible by 3 and 5?

num=int(input("Enter your Number: "))

if num%3 ==0 and num%5==0:
    print("Number is divisible by 5 and 3")
elif num%3==0:
    print("Number is divisible by 3")
elif num%5==0:
    print("Number is divisible by 5")
else:
    print("Invalid Number")

# OR

def divisibility(num1):
    
    if num1%3 ==0 and num1%5==0:
        print("Number is divisible by 5 and 3")
    elif num1%3==0:
        print("Number is divisible by 3")
    elif num1%5==0:
        print("Number is divisible by 5")
    else:
        print("Invalid Number")
num1=int(input("Enter your number: "))
divisibility(num1)