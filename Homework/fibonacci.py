#Almada Putra A.
#%%
#the calculator
FirstNum = input("enter your first number: ")
SecondNum = input("enter your second number: ")

def addition(num_1, num_2):
    return int(num_1) + int(num_2)
print(addition(FirstNum, SecondNum))
#%%
FirstNum = input("enter your first number: ")
SecondNum = input("enter your second number: ")

def subtraction(num_1, num_2):
    return int(num_1) - int(num_2)
print(subtraction(FirstNum, SecondNum))
#%%
FirstNum = input("enter your first number: ")
SecondNum = input("enter your second number: ")

def multiplication(num_1, num_2):
    return int(num_1) * int(num_2)
print(multiplication(FirstNum, SecondNum))
#%%
FirstNum = input("enter your first number: ")
SecondNum = input("enter your second number: ")

def division(num_1, num_2):
    return int(num_1) / int(num_2)
print(division(FirstNum, SecondNum))
#%%
#the factorial
def factorial(number):
    if (number > 1):
        print(number)
        return number * factorial(number - 1)
    else:
        return number
#%%
#the fibonacci
def fibonacci(number):
    if (number > 1):
        return fibonacci(number - 1) + fibonacci(number - 2)
    else:
        return number
#%%
#palindrome
import string
def ignore_punctuation(word):
    return "". join(letter.lower() for letter in word if letter in string.ascii_letters)
def reverse(word):
    return word[::-1]
def is_palindrome(word):
    word = ignore_punctuation(word)
    rev = reverse(word)
    if (word == rev):
        return True
    else:
        return False
word = str(input("eneter a word: "))
result = is_palindrome(word)
if result:
    print("yes, its a palindrome.")
else:
    print("no, its not a palindrome.")
#%%
#the letter counting/ASCII number
word = input("enter word here : ")
from collections import Counter
count=Counter(word)
for i in word:
    print(i,count[i])
#%%
#anagram finding
str1 = input("enter first word: ")
str2 = input("enter second word: ")
  
def isAnagram(str1, str2): 
    if (len(str1) != len(str2)): 
        return False; 
    value = 0; 
  
    for i in range(0,len(str1)): 
        value = value ^ ord(str1[i]); 
        value = value ^ ord(str2[i]); 
  
    return value == 0; 
  
if (isAnagram(str1, str2)): 
    print("The two strings are anagram of each other"); 
else: 
    print("The two strings are not anagram of each other")
#%%
#converting the roman to arabic
class rom_conversion:
    def roman_to_arabic(self, s):
        roman_val = {"I" : 1, "IV" : 4, "V" : 5, "IX" : 9, "X" : 10}
        arabic_val = 0
        for i in range(len(s)):
            if i > 0 and roman_val[s[i]] > roman_val[s[i - 1]]:
                arabic_val += roman_val[s[i]] - 2 * roman_val[s[i - 1]]
            else:
                arabic_val += roman_val[s[i]]
        return arabic_val
    
print(rom_conversion().roman_to_arabic("X"))
#%%
#converting arabic to roman
conv = [[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'],[1, 'I']]
num = 17
roman = ''
i = 0 
while num > 0:
    while conv[i][0] > num: i+=1
    roman += conv[i][1] 
    num -= conv[i][0] 
print(roman)

    
    
    
    
    
    
    
    
    
    
    
    
