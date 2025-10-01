#  Input 2 numbers, show sum

number1=int(input("Enter First Number: "))
number2=int(input("Enter Second Number: "))

sum=number1+number2
print(sum)

# OR

def two_add(num1,num2):
    sum=num1+num2
    return sum
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
print(two_add(num1,num2))
