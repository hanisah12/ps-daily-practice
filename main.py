# task - 1

sentence = "Emma-is-a-data-scientist"
domain = sentence.split('-')
for word in domain:
    print(word)

sentence = "Emma-is-a-data-scientist"
word = ""  
for char in sentence:
    if char!='-':         
        word=word+char
    else:                  
        print(word)
        word = ""

# task - 2

str1 = "Python"
reversed_str="".join(reversed(str1))
print(reversed_str)

str1="Python"
str2=""
for char in str1:
    str2=char+str2
print(str2)

# task - 3

def consonants_count(str1):
    total=0
    text=str1.lower()
    for i in text:
        if i.isalpha() and i not in ["a","e","i","o","u"]:
            total=total+1
    return total
print(consonants_count("Hello World"))

# task - 4

str1="Python is awesome"
s = str1.replace(" ", "")
print(s)   

# task - 5

password=input("Enter a password:")
if len(password)>=8 and any(char in "!@#$%^&*" for char in password):
    print("Password is Strong")
else:
    print("Password is not Strong")

