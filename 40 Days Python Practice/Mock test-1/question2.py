# Question 2: Conditional Statements (15 points)

# Write a program that takes a number as input and:
# - If divisible by both 3 and 5: print 'FizzBuzz'
# - If divisible by 3 only: print 'Fizz'
# - If divisible by 5 only: print 'Buzz'
# - Otherwise: print the number itself

# **Test with:** 15, 9, 10, 7  
# **Expected:** FizzBuzz, Fizz, Buzz, 7

num=int(input("Enter Number: "))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print(num)