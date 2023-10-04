#.Write a Python program to unpack a tuple into several variables.
my_tuple=(10,20,30,40)
var1 ,var2 ,var3 ,var4 = my_tuple
print ("var1:",var1)
print ("var2:" ,var2)
print ("var3:", var3)
print ("var4:", var4)


#Write a Python program to add an item to a tuple.
tuple = (1, 2, 3, 4, 5)
new_item = 6
new_tuple = tuple + (new_item,)
print("tuple:", tuple)
print("New Tuple:", new_tuple)


#Write a Python program to convert a tuple to a string.
# Ex:tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
result_str = ''.join(tuple)
print(result_str)


#Write a Python program to get the specified element from the last element of a tuple.

my_tuple = (10, 20, 30, 40, 50)
index = 4
if abs(index) <= len(my_tuple):
    element = my_tuple[index]
    print(f"The element at index {index} from the end is: {element}")
else:
    print("Invalid index")

#.Write a Python program to add member(s) to a set.
my_set = set()
my_set.add(10)
print("Set after adding a single element:", my_set)
fruits = {"apple", "banana", "cherry"}
fruits.update(["orange", "grape"])
print("Set after adding multiple elements:", fruits)

#Write a Python program to create an intersection of sets.
# Create two sets
x = {1, 2, 3, 4, 5}
y = {3, 4, 5, 6, 7}
print(x.intersection(y))


#Write a Python program to create a union of sets.
x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}
print(x.union(y))


#Write a Python program to create set difference.
x = {1, 2, 3, 4, 5}
y = {3, 4, 5, 6, 7}
print (x.difference(y))


#Write a Python program to create a symmetric difference.
x = {1, 2, 3, 4, 5}
y = {3, 4, 5, 6, 7}
print(x.symmetric_difference(y))

#Write a Python program to find the maximum and minimum values in a set.
# Create a set
b = {3, 7, 1, 9, 4, 6, 2, 8, 5}
print(max(b))
print(min(b))



