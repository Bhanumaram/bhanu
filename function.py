#Write a Python function that accepts a string and counts the number of upper and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12

def count_upper_lower_case_characters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return f"No. of Upper case characters: {upper_count}\nNo. of Lower case Characters: {lower_count}"

# Sample string
sample_string = 'The quick Brow Fox'
result = count_upper_lower_case_characters(sample_string)
print(result) 



#.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def get_unique_elements(input_list):
    # Use set to remove duplicates, then convert it back to a list
    unique_list = list(set(input_list))
    return unique_list

# Sample list
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
result = get_unique_elements(sample_list)
print("Unique List:", result)


#3.Write a Python function to check whether a string is a pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog".

def is_pangram(s):
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()
    
    # Create a set to store the unique letters in the string
    seen_letters = set()

    # Iterate through each character in the string
    for char in s:
        if char.isalpha():
            seen_letters.add(char)
    
    # Check if all 26 letters have been seen
    return len(seen_letters) == 26

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
if is_pangram(sentence):
    print("It's a pangram!")
else:
    print("It's not a pangram.")

#Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).

def generate_square_list():
    square_list = [x**2 for x in range(1, 11)]
    return square_list

squares = generate_square_list()

for square in squares:
    print(square)

#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = [8, 2, 3, 0, 7]
result = sum_list(sample_list)
print("Expected Output:", result)

#write a function to find sum of given values, pass values has variable number of arguments to function.
def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total

result = sum_values(8, 2, 3, 0, 7)
print("Sum:", result)
