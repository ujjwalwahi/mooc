"""
Write a program that prints the number of times the string 'bob' occurs in s
"""

s = 'azcbobobegghaklbob'
count = 0
i = s.find('bob')
while i != -1:
    count += 1
    s = s[i+1:]
    i = s.find('bob')
print("Number of times bob occur is: " + str(count))
