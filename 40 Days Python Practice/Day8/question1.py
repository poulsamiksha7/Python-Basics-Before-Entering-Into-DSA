# - Palindrome check

text=input("Enter text:")

if text==text[::-1]:
    print("String is palindrome")
else:
    print("String is not a Palindrome")