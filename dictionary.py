#Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}
# Sample dictionary
sample_dict = {0: 10, 1: 20}
new_key = 2
new_value = 30

# Adding the new key and value to the dictionary
sample_dict[new_key] = new_value

print(sample_dict)

#Write a Python script to check whether a given key already exists in a dictionary

my_dict = {0: 10, 1: 20, 2: 30, 3: 40}

# Key to check for existence
key_to_check = 2

# Check if the key exists in the dictionary
if key_to_check in my_dict:
    print(f"The key {key_to_check} exists in the dictionary.")
else:
    print(f"The key {key_to_check} does not exist in the dictionary.")


#-----o------

#Write a Python program to iterate over dictionaries using for loops

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterating over keys
for key in my_dict:
    print(b'Key: {key}')

# Iterating over values
for value in my_dict.values():
    print(b'Value: {value}')

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(b'Key: {key}, Value: {value}')


#-----o------


#.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

square_dict = {}

# Populate the dictionary with keys and their squares
for i in range(1, 16):
    square_dict[i] = i ** 2

print(square_dict)

#-----o------

#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'marolix technology'
#Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}

sample_string = 'marolix technology'

letter_count = {}

# Iterate through each character in the string
for char in sample_string:
    # Check if the character is a letter (ignoring spaces)
    if char.isalpha():
        # Convert the character to lowercase to make it case-insensitive
        char = char.lower()
        
        # If the character is already in the dictionary, increment its count
        if char in letter_count:
            letter_count[char] += 1
        else:
            # If the character is not in the dictionary, add it with a count of 1
            letter_count[char] = 1

print(letter_count)


#-----o-----

#Write a Python program to sum all the items in a dictionary.

my_dict = {'a': 10, 'b': 20, 'c': 30}

# Initialize a variable to store the sum
total = 0

# Iterate through the values of the dictionary and add them to the total
for value in my_dict.values():
    total += value

print("The sum of all items in the dictionary is:", total)


#-----o------

#Write a Python program to combine two dictionary by adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

counter1 = Counter(d1)
counter2 = Counter(d2)
result = counter1 + counter2
combined_dict = dict(result)

print(combined_dict)


#-----o-----


#Write a Python program to access dictionary key's element by index.
#Expected Output:
#physics
#math
#chemistry

my_dict = {
    "subject1": "physics",
    "subject2": "math",
    "subject3": "chemistry"
}

order_of_keys = ["subject1", "subject2", "subject3"]

# Access dictionary values by index
for key in order_of_keys:
    print(my_dict[key])


#-----o------

#Write a Python program to remove a key from a dictionary.

my_dict = {
    "name": "bhanu",
    "age": 24,
    "city": "vijayawada"
}

# Method 1: Using the 'del' statement
key_to_remove = "age"
if key_to_remove in my_dict:
    del my_dict[key_to_remove]

# Method 2: Using the 'pop()' method
key_to_remove = "city"
value = my_dict.pop(key_to_remove, None)

# Print the modified dictionary
print("Dictionary after removing keys:")
print(my_dict)

# If you want to get the value of the removed key (Method 2)
if value is not None:
    print(f"Removed key '{key_to_remove}' with value '{value}'")
else:
    print(f"Key '{key_to_remove}' not found in the dictionary")


#------o-----

#Write a Python script to merge two Python dictionaries.d

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)

print("Merged dictionary using update:")
print(dict1)
