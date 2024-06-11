# Exercise 1 (Lists)

# 1. Create a list with 5 items (names of people) and write a python program to output the 2nd item.
names = ["Alice", "Bob", "Charlie", "David", "Emma"]
print("The 2nd item is:", names[1])

# 2. To change the value of the first item to a new value
names[0] = "Eva"
print("List after changing the first item:", names)

# 3. Write a python program to add a sixth item to the list
names.append("Frank")
print("List after adding a sixth item:", names)

# 4. Write a python program to add “Bathel” as the 3rd item in your list
names.insert(2, "Bathel")
print("List after adding 'Bathel' as the 3rd item:", names)

# 5. Write a python program to remove the 4th item from the list
removed_item = names.pop(3)
print("List after removing the 4th item:", names)
print("Removed item:", removed_item)

# 6. Use negative indexing to print the last item in your list
print("The last item is:", names[-1])

# 7. Create a new list with 7 items and use a range of indexes to print the 3rd, 4th, and 5th items.
new_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print("3rd, 4th, and 5th items:", new_list[2:5])

# 8. Write a list of countries and make a copy of it.
countries = ["USA", "UK", "Canada", "Australia", "India"]
countries_copy = countries.copy()
print("Copy of countries list:", countries_copy)

# 9. Write a python program to loop through the list of countries
print("Looping through the list of countries:")
for country in countries:
    print(country)

# 10. Write a list of animal names and sort them in both descending and ascending order.
animal_names = ["lion", "elephant", "zebra", "giraffe", "monkey"]
ascending_order = sorted(animal_names)
descending_order = sorted(animal_names, reverse=True)
print("Animal names in ascending order:", ascending_order)
print("Animal names in descending order:", descending_order)

# 11. Using the list above, write a python program to output only animal names with the letter ‘a’ in them
names_with_a = [name for name in animal_names if 'a' in name]
print("Animal names with the letter 'a':", names_with_a)

# 12. Write two lists, one containing your first names and the other your second names. Join the two lists.
first_names = ["John", "Jane", "Alice"]
second_names = ["Doe", "Smith", "Johnson"]
full_names = list(zip(first_names, second_names))
print("Joined list of full names:", full_names)

"""

Explanation:

1. Output the 2nd item from the list of names:
   - Access the second item in the list `names` using index `1` and print it.

2. Changing the value of the first item:
   - Modify the first item in the list `names` by assigning a new value to it.

3. Adding a sixth item to the list:
   - Use the `append()` method to add a new item to the end of the list `names`.

4. Adding “Bathel” as the 3rd item:
   - Use the `insert()` method to insert "Bathel" at index `2` (3rd position) in the list `names`.

5. Removing the 4th item from the list:
   - Use the `pop()` method to remove and return the item at index `3` (4th position) from the list `names`.

6. Printing the last item using negative indexing:
   - Access the last item in the list `names` using negative index `-1`.

7. Printing the 3rd, 4th, and 5th items from a new list:
   - Create a new list `new_list` and use slicing to print a range of items from index `2` to `4` (3rd to 5th positions).

8. Making a copy of a list:
   - Create a copy of the list `countries` using the `copy()` method.

9. Looping through the list of countries:
   - Use a `for` loop to iterate over each item in the list `countries` and print it.

10. Sorting animal names in ascending and descending order:
    - Use the `sorted()` function to sort the list `animal_names` in both ascending and descending order.

11. Outputting only animal names with the letter ‘a’:
    - Use a list comprehension to filter out names from the list `animal_names` that contain the letter 'a'.

12. Joining two lists of first and second names:
    - Use the `zip()` function to join the lists `first_names` and `second_names` element-wise into a 
    list of tuples containing full names.
"""