#  Age category: Child, Teen, Adult

age=int(input("Enter your age: "))

if age>=40:
    print("Adult")
elif age<=30:
    print("Teen")
else:
    print("Child")

# OR

def ageCategory(age):
    if age>=40:
        print("Adult")
    elif age<=30:
        print("Teen")
    else:
        print("Child")
age=int(input("Enter a number: "))
ageCategory(age)