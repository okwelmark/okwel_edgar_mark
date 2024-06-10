#python functions
#python logical operators
#name of the operator         Symbol
#
#
#Logical operator 
# 
#Membership operators
#
#bitwise operators
#













#python cases
#--------SNAKE_CASE IS MORE RECOMMENDABLE-------
#1 snake_case
#2 camelCase
#3 PascalCase
#4 UPPERCASE
# Kebab-case



#COMPREHENSIONS LISTS AND DICTIONARIES
# Comprehensions provide a consice way of creating dictionaries
#lists        use [] square brackets (stores multiple items in  a single variable)
#dictionaries use {} curly brackets (stores data with key value pairs)
#

#Example 1
#create a list of squares in range of 10
list_of_squares = [i**2 for i in range(10)]
print(list_of_squares)

#Exercise 2
#create a list of even squares in the range of 20
list_of_even_squares = [i**2 for i in range(20) if (i**2) % 2 == 0]
print(list_of_even_squares)

#Example 2: Dictionary Comprehensions
#create a dictionary comprehension for favorite cars and count thr lengths of characters
favorite_cars = ["Volgs wagon", "Mercedez", "Range rover", "Audi", "BMW"]
car_lengths = {car: len(car) for car in favorite_cars}
print(car_lengths)

#Exercise 2
#create a list of tuple where each tuple contains a number and its cube for numbers
#between 1 and 10 using dictionary comprehension
# Creating a list of tuples using dictionary comprehension

num_cubes_dict = {i: i**3 for i in range(1, 11)}
num_cubes = list(num_cubes_dict.items())
print(num_cubes)

