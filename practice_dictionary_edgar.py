
# Exercise 5 (Dictionaries)

# 1. Print the value of the shoe size:
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

print("The shoe size is:", Shoes["size"])

# 2. Change the value “Nick” to “Adidas”:
Shoes["brand"] = "Adidas"
print("Dictionary after changing brand to 'Adidas':", Shoes)

# 3. Add a key/value pair "type": "sneakers" to the dictionary:
Shoes["type"] = "sneakers"
print("Dictionary after adding 'type' key:", Shoes)

# 4. Return a list of all the keys in the dictionary:
keys_list = list(Shoes.keys())
print("List of keys:", keys_list)

# 5. Return a list of all the values in the dictionary:
values_list = list(Shoes.values())
print("List of values:", values_list)

# 6. Check if the key “size” exists in the dictionary:
key_exists = "size" in Shoes
print("Does 'size' key exist in the dictionary?", key_exists)

# 7. Loop through the dictionary:
print("Looping through the dictionary:")
for key, value in Shoes.items():
    print(key, ":", value)

# 8. Remove “color” from the dictionary:
Shoes.pop("color")
print("Dictionary after removing 'color':", Shoes)

# 9. Empty the dictionary:
Shoes.clear()
print("Empty dictionary:", Shoes)

# 10. Make a copy of a dictionary:
original_dict = {"key1": "value1", "key2": "value2"}
copied_dict = original_dict.copy()
print("Copied dictionary:", copied_dict)

# 11. Show nested dictionaries:
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}
print("Nested dictionary:", nested_dict)

"""

Explanation:

1. Accessing values by keys and printing them.
2. Modifying values in the dictionary by assigning new values to existing keys.
3. Adding new key-value pairs to the dictionary.
4. Retrieving all keys from the dictionary using the `keys()` method and converting them to a list.
5. Retrieving all values from the dictionary using the `values()` method and converting them to a list.
6. Checking if a specific key exists in the dictionary using the `in` operator.
7. Looping through the dictionary using a `for` loop and accessing both keys and values.
8. Removing a key-value pair from the dictionary using the `pop()` method.
9. Emptying the dictionary using the `clear()` method.
10. Making a copy of a dictionary using the `copy()` method.
11. Creating nested dictionaries, where each value in the dictionary is another dictionary.

"""