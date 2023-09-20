#Write a python program to remove a given  character from string.
string=input('enter a string : ')
sub_string=input('enter a character to remove from string: ')
new_string=string.replace(sub_string,'')
print(new_string)

print()
print()

#Write a program to check String is Palindrome or not.
string=input('enter a string : ')
if string == (string[::-1]):
    print('palindrome ')
else:
   print('not palindrome')

print()
print()

#Write a python program to check given character is vowel or consonant.
sub_string=input('enter a character to check: ')
if sub_string in 'aeiouAEIOU':
    print('Given character is vowel')
else:
    print('Given Character is consonant')

print()
print()

#Write a python program to replace string space with given character in Python.
string=input('enter a string: ')
sub_string=input('enter character to replace: ')
new_string=string.replace(' ',sub_string)
print(new_string)

print()
print()

#Write a python program to count alphabets, digits, and special characters in the string.
string=input('enter a string: ')
alphabets=0
digits=0
special_characters=0
for MB in string:
    if MB.isalpha():
        alphabets+=1
    elif MB.isdigit():
       digits+=1
    else:
       special_characters+=1
print(f'alphabet count = {alphabets}')
print(f'special_characters count = {special_characters}')

print()
print()

#Write a python program to remove all the blank spaces in a given string.
string=input('enter a string: ')
new_string=string.replace(' ','')
print(new_string)

print()
print()

#Write a python program to find sum of integers in the string.
string=input('enter a string: ')
sum=0
for MB in string:
    if MB.isdigit():  
        sum+=int(MB)
print(sum)

print()
print()

#Write a python program to Remove Repeated Character from String.
string=input('enter a string: ')
new_string=''
for MB in string:
   if MB not in new_string:
       new_string+=MB
print(new_string)

print()
print()

#Write a python program to count occurrence of given character in string. 
string=input('enter a string: ')
sub_string=input('enter a character: ')
print(string.count(sub_string))

print()
print()

#Write a python program to check string is anagrams or not in Python.
string=input('enter a string1: ')
string2=input('enter a string2: ')
if len(string)==len(string2):
    for MB in string:
        if MB not in string2:
            print('not anagram')
            break
    else:
        print('anagram')
else:
    print('not anagram')