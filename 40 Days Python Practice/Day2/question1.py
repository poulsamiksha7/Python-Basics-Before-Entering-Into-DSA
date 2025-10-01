# - Check odd/even

num=int(input("Enter a Number: "))

if num%2==0:
    print("Number is even ")
else:
    print("Number is odd ")

# OR
def oddEven(num1):
    if num1%2==0:
        print("Number is even")
    else:
        print("Number is odd")
num1=int(input("Enter a Number: "))
oddEven(num1)