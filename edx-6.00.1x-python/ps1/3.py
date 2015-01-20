"""
Write a program that prints the longest substring of s in which the
letters occur in alphabetical order
"""

s = 'axuvkgrfnnhchqtwxyk' 
count = 1
index = 0
length = 1
for i,l in enumerate(s[1:]):
    if l >= s[i]:
        if count == 0:
            count += 1
        count += 1
    if l < s[i] or i == len(s)-2:
        if count > length:
            length = count
            index = i - length+1
            index += 1 if i==len(s)-2 and l>=s[i] else 0
        count = 0
print('Longest substring in alphabetical order is: ' + s[index:index+length])
