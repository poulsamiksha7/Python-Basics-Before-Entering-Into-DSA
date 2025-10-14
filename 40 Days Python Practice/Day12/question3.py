#  vowel counter
def vowelCounter(t):
    vowel="aeiou"
    count=0
    for i in t.lower():
        if i in vowel:
            count+=1
    return count
t=input("Enter Text: ")
print(vowelCounter(t))
