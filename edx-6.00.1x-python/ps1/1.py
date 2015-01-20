"""
Write a program that counts up the number of vowels contained in the string s
"""

s = 'azcbobobegghakl'
vowels = 0
for letter in s:
    if letter in 'aeiou':
        vowels += 1
print("Number of vowels: " + str(vowels))
