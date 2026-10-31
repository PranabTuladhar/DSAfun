# class Hashy():
#     def __init__(self,value):
#         self.value = value

#     def hash_function(value):
#         sum_of_chars = 0
#         for char in value:
#             sum_of_chars += ord(char)

#         return sum_of_chars % 10

#     print("'Bob' has hash code",hash_function('Bob') )


# Question 1 – Build a hash function
# Create a function called hash_function(value) that:

# Takes a string as input.

# Loops through every character.

# Converts each character into its Unicode number using ord().

# Adds all the numbers together.

# Uses modulo (% 10) to return an index between 0 and 9.

# class Hashy():

#     def __init__(self,value):
#         self.value = value

#     def hash_function(value):
#         sum_of_chars = 0
#         for char in value:
#             sum_of_chars += ord(char)

#         return sum_of_chars % 10

#     print("'Bob' has hash code",hash_function('Bob'))
#     print("'Amy' has hash code", hash_function('Amy'))
#     print("'John' has hash code", hash_function('John'))


# Question 2 – Implement insertion
# Create a hash table with 10 empty buckets.

# Implement an add(name) function that:

# Accepts a first name.

# Uses your hash function to calculate its index.

# Stores the name at the correct index.

# Prevents duplicate names from being inserted.

# my_list = [None,None,None,None,None,None,None,None,None,None]

# def hash_function(value):
#     sum_of_char = 0
#     for char in value:
#         sum_of_char += ord(char)
#     return sum_of_char % 10

# # def add(name):
# #     index = hash_function(name)
# #     my_list[index] = name

# # add('AnthonyBatman')
# # add('Pete')
# # add('Jones')
# # add('Lisabel')
# # add('Siricuis')
# # add('SeraJammies')
# # print(my_list)

# # handling collision

# def add(name):

#     index = hash_function(name)

#     while my_list[index] is not None:
#         index = (index +1) %len(my_list)

#     my_list[index] = name

# add('AnthonyBatman')
# add('Pete')
# add('Jones')
# add('Lisabel')
# add('Siricuis')
# add('SeraJammies')
# add('Sera')
# add('Jammies')
# add('Andy')
# add('James')
# print(my_list)


# Question 3 – Build the complete hash set
# Challenge
# Now combine everything into one working hash table.

# Implement these three functions:

# add(name) – Inserts a unique name into the hash table.

# contains(name) – Returns True if the name exists, otherwise False.

# remove(name) – Removes a name if it exists.
# my_list = [None,None,None,None,None,None,None,None,None,None]
# def hash_function(value):
#     sum_of_char = 0
#     for char in value:
#         sum_of_char += ord(char)
#     return sum_of_char %len(my_list)

# def add(name):
#     index = hash_function(name)

#     while my_list[index] is not None:
#         index = (index + 1) % len(my_list)

#     my_list[index] = name


# def remove(name):
#     index = hash_function(name)

#     # while my_list[index]:
#     #     index = (index + 1) % len(my_list)

#     my_list.remove(name)

# def contains(name):
#     index = hash_function(name)

#     if my_list.__contains__(name):
#         return True
#     else:
#         return False


# add('Bob')
# add('Boby')
# add('Cob')
# add('Coby')
# add('Dob')
# add('Doby')
# add('Fob')
# add('Foby')
# print(my_list)
# remove('Bob')
# remove('Boby')
# print(my_list)

# print(contains('Cob'))
# print(contains('Robert'))