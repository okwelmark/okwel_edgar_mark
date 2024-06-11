# Exercise1 (Lists)
# 1.	Create a list with 5 items (names of people) and write a python program to output the 2nd item.
#............................

people = ['Edgar', 'Martha', 'Lewis', 'Alonzo', 'Mark']
print(people[1])

#............................
# 2.	Write a python program to change the value of the first item to a new value

people = ['Edgar', 'Martha', 'Lewis', 'Alonzo', 'Mark']
people[1] = 'Aluto'
print(people[1])

# 3.	Write a python program to add a sixth item to the list
#.............................

people = ['Edgar', 'Martha', 'Lewis', 'Alonzo', 'Mark']
people.append('Okwel')

# print(people[5])

# 4.	Write a python program to add “Bathel” as the 3rd item in your list
#........................................
people = ['Edgar', 'Martha', 'Lewis', 'Alonzo', 'Mark']
people.insert(2, 'Bethal')
print(people[2])
print(people[1])
print(people[3])
print(" ")


# 5.	Write a python program to remove the 4th item from the list
#....................................................
#people = ['Edgar', 'Martha', 'Lewis', 'Alonzo', 'Mark']
people.remove('Alonzo')
for person in people:
    print(person)
# 6.	Use negative indexing to print the last item in your list
# 7.	Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
# 8.	Write a list of countries and make a copy of it.
# 9.	Write a python program to loop through the list of countries
# 10.	Write a list of animal names and sort them in both descending and ascending order.
# 11.	Using the list above, write a python program to output only animal names with the letter ‘a’ in them
# 12.	Write two lists, one containing your first names and the other your second names. Join the two lists.



# 1.
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(names[1])

# 2.
names[0] = "Alex"
print(names)

# 3.
names.append("Frank")
print(names)

# 4.
names.insert(2, "Bathel")
print(names)

# 5.
del names[3]
print(names)

# 6.
print(names[-1])

# 7.
new_list = ["a", "b", "c", "d", "e", "f", "g"]
print(new_list[2:5])

# 8.
countries = ["USA", "UK", "Canada"]
countries_copy = countries.copy()
print(countries_copy)

# 9.
for country in countries:
    print(country)

# 10.
animal_names = ["lion", "tiger", "elephant", "zebra"]
animal_names.sort()
print("Ascending order:", animal_names)
animal_names.sort(reverse=True)
print("Descending order:", animal_names)

# 11.
for animal in animal_names:
    if 'a' in animal:
        print(animal)

# 12.
first_names = ["John", "Jane", "Michael"]
last_names = ["Doe", "Smith", "Johnson"]
full_names = list(zip(first_names, last_names))
print(full_names)





# Sure, here's an explanation of the provided Python code for Exercise 1:

# 1. *Create a list and output the 2nd item:*  
#    - We create a list called names containing five names: "Alice", "Bob", "Charlie", "David", and "Eve". 
#    - Then, we use indexing (names[1]) to print the second item in the list, which is "Bob".

# 2. *Change the value of the first item:*  
#    - We change the value of the first item in the names list from "Alice" to "Alex" using indexing (names[0] = "Alex").

# 3. *Add a sixth item to the list:*  
#    - We append the name "Frank" to the names list using the append() method (names.append("Frank")).

# 4. *Add “Bathel” as the 3rd item:*  
#    - We insert the name "Bathel" at the 3rd position (index 2) in the names list using the insert() method (names.insert(2, "Bathel")).

# 5. *Remove the 4th item from the list:*  
#    - We remove the item at index 3 from the names list using the del statement (del names[3]).

# 6. *Print the last item using negative indexing:*  
#    - We print the last item in the names list using negative indexing (names[-1]).

# 7. *Print a range of items from a new list:*  
#    - We create a new list called new_list with seven items ("a" to "g").
#    - Then, we use a range of indexes (2:5) to print the 3rd, 4th, and 5th items from new_list.

# 8. *Make a copy of a list:*  
#    - We create a list called countries with three country names.
#    - Then, we make a copy of the countries list using the copy() method and store it in countries_copy.

# 9. *Loop through a list:*  
#    - We iterate over each item in the countries list using a for loop and print each country.

# 10. *Sort a list in ascending and descending order:*  
#     - We create a list called animal_names containing names of animals.
#     - First, we sort the list in ascending order using the sort() method.
#     - Then, we print the list.
#     - Next, we sort the list in descending order using the sort(reverse=True) method.
#     - Finally, we print the list again.

# 11. *Output items containing the letter ‘a’:*  
#     - We iterate over each animal name in the animal_names list using a for loop.
#     - If an animal name contains the letter 'a', we print it.

# 12. *Join two lists:*  
#     - We create two lists, first_names and last_names, containing first names and last names, respectively.
#     - Then, we use the zip() function to combine the two lists element-wise into a list of tuples representing full names.