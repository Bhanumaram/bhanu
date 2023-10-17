#recurssive function:-
#Factorial
def function(n):
    if n == 1:
        return 1
    else:
        return n * function(n-1)
print(function(6))
 

#adding of elements
def add(n):
    print(n)
    if n==1:
        return(1)
    return (n+add(n-1))
add(5)    
    

#lambda function:-
#adding the elements
sum=lambda a,b:a+b
print(sum(10,20))


#dividing the elements
div=lambda x,y:x%y
print(div(45,45))


#finding square in element
square = lambda x: x ** 2
print(square(5))  


#finding even number
is_even = lambda x: x % 2 == 0
print(is_even(6)) 


#filter function:-
#filtering even values
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_values = list(filter(lambda x: x % 2 == 0, values))
print(even_values) 


#filtering positive numbers
numbers = [-2, -1, 0, 1, 2, 3, 4]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers) 


#filtering prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 20))
prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers) 


#map functions:-
#calculate the squares of each element in the list
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares) 


#finding the lenght of words in the list
words = ["apple", "banana", "cherry"]
word_lengths = list(map(len, words))
print(word_lengths)


#convert the list of strings to uppercase
words = ["apple", "banana", "cherry"]
uppercase_words = list(map(lambda word: word.upper(), words))
print(uppercase_words)  


#reduce function:-
#finding factorial of number
from functools import reduce
num = 5
factorial = reduce(lambda x, y: x * y, range(1, num + 1), 1)
print(factorial)  


#finding the maximum value in the list
from functools import reduce
numbers = [4, 7, 2, 8, 5]
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)  


#joining a list of words in seperate
from functools import reduce
words = ["apple", "banana", "cherry"]
joined = reduce(lambda x, y: x + ", " + y, words)
print(joined)  


#nested functios:-
def outer_function(x):
    def inner_function(y):
        return y * 2
    return x + inner_function(x)

result = outer_function(3)
print(result)  

#nested function with non local variable
def outer_function(x):
    def inner_function(y):
        nonlocal x
        x += 10
        return x + y
    return inner_function

inner = outer_function(5)
result = inner(7)
print(result)  


