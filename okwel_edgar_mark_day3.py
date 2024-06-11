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



# 1. **Bitwise AND (`&`)**:
#    - Performs a bitwise AND operation.
#    - Example: `5 & 3` results in `1`
#    - Explanation: `0101 & 0011` results in `0001` (in binary)

# 2. **Bitwise OR (`|`)**:
#    - Performs a bitwise OR operation.
#    - Example: `5 | 3` results in `7`
#    - Explanation: `0101 | 0011` results in `0111` (in binary)

# 3. **Bitwise XOR (`^`)**:
#    - Performs a bitwise XOR operation.
#    - Example: `5 ^ 3` results in `6`
#    - Explanation: `0101 ^ 0011` results in `0110` (in binary)

# 4. **Bitwise NOT (`~`)**:
#    - Performs a bitwise NOT operation (inverts all bits).
#    - Example: `~5` results in `-6`
#    - Explanation: `~0101` results in `1010` (in binary, with 2's complement representation)

# 5. **Bitwise Left Shift (`<<`)**:
#    - Shifts the bits of the first operand left by the number of positions specified by the second operand.
#    - Example: `5 << 1` results in `10`
#    - Explanation: `0101 << 1` results in `1010` (in binary)

# 6. **Bitwise Right Shift (`>>`)**:
#    - Shifts the bits of the first operand right by the number of positions specified by the second operand.
#    - Example: `5 >> 1` results in `2`
#    - Explanation: `0101 >> 1` results in `0010` (in binary)









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

