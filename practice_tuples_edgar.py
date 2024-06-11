# Exercise 2 (Tuples)

# 1. Consider the tuple below; Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone_brand = x[1]  # Assuming "iphone" is the favorite
print("My favorite phone brand is:", favorite_phone_brand)

# 2. Use negative indexing to print the 2nd last item in your tuple.
second_last_item = x[-2]
print("The 2nd last item is:", second_last_item)

# 3. Using the phones list above, write a python program to update “iphone” to “itel”
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("Updated tuple:", x)

# 4. Write a python program to add “Huawei” to your tuple.
x = x + ("Huawei",)
print("Tuple after adding Huawei:", x)

# 5. Write a python program to loop through the tuple above.
print("Looping through the tuple:")
for phone in x:
    print(phone)

# 6. Write a python program to remove/delete the first item in your tuple.
x_list = list(x)
del x_list[0]
x = tuple(x_list)
print("Tuple after removing the first item:", x)

# 7. Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print("Tuple of cities in Uganda:", cities)

# 8. Write a python program to unpack your tuple.
city1, city2, city3, city4, city5 = cities
print("Unpacked cities:")
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print("2nd, 3rd, and 4th cities:", cities[1:4])

# 10. Write two tuples, one containing your first names and the other your second names. Join the two tuples.
first_names = ("John", "Jane")
second_names = ("Doe", "Smith")
full_names = first_names + second_names
print("Joined tuple:", full_names)

# 11. Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "green")
colors_multiplied = colors * 3
print("Colors multiplied by 3:", colors_multiplied)

# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_eight = thistuple.count(8)
print("Number of times 8 appears:", count_eight)


"""
Explanation:

1. Output your favorite phone brand:
   - A tuple `x` is defined with phone brands. The favorite brand, `"iphone"`, 
   is accessed using the index `1` and printed.

2. Use negative indexing to print the 2nd last item in your tuple:
   - Negative indexing is used to get the second last item from the tuple. `x[-2]` gets `"tecno"`.

3. Update "iphone" to "itel":
   - Tuples are immutable, so the tuple is converted to a list. The element at index `1` is 
   changed from `"iphone"` to `"itel"`, and then it's converted back to a tuple.

4. Add "Huawei" to your tuple:
   - Tuples are immutable, so to add an item, a new tuple is created by concatenating the original
   tuple with a new tuple containing `"Huawei"`.

5. Loop through the tuple:
   - A `for` loop is used to iterate through the tuple `x`, printing each phone brand.

6. Remove/delete the first item in your tuple:
   - The tuple is converted to a list to remove the first item. The first item is deleted using `del`, 
   and then the list is converted back to a tuple.

7. Using the tuple() constructor, create a tuple of the cities in Uganda:
   - The `tuple()` constructor is used to create a tuple from a list of city names in Uganda.

8. Unpack your tuple:
   - The tuple `cities` is unpacked into five variables (`city1, city2, city3, city4, city5`), and each variable is printed.

9. Use a range of indexes to print the 2nd, 3rd, and 4th cities in your tuple:
   - Slicing is used to print the 2nd, 3rd, and 4th cities from the `cities` tuple. `cities[1:4]` gets 
   the items from index `1` to `3`.

10. Join two tuples containing your first names and second names:
    - Two tuples `first_names` and `second_names` are created and concatenated to form a new tuple `full_names`.

11. Create a tuple of colors and multiply it by 3:
    - The `colors` tuple is multiplied by `3` using the `*` operator, resulting in the tuple being repeated three times.

12. Return the number of times 8 appears in this tuple:
    - The `count()` method is used to count how many times the value `8` appears in the tuple `thistuple`.



"""