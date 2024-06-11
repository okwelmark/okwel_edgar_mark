
# EXERCISE THREE (SETS)


# 1. Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["coffee", "tea", "juice"])
print("Beverages set:", beverages)


# 2. Use the correct method to add 2 more items to the beverages set.
beverages.add("water")
beverages.add("soda")
print("Beverages set after adding two items:", beverages)


# 3. Given the set below; Check if microwave is present in the set.
mySet = {"oven", "kettle", "microwave", "refrigerator"}
is_microwave_present = "microwave" in mySet
print("Is microwave present in mySet:", is_microwave_present)


# 4. Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print("mySet after removing 'kettle':", mySet)


# 5. Write a python program to loop through the set above.
for item in mySet:
    print(item)


# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set.
mySet2 = {"item1", "item2", "item3", "item4"}
myList = ["item5", "item6"]
mySet2.update(myList)
print("mySet2 after adding elements from myList:", mySet2)


# 7. Write two sets, one containing your ages and the other your first names. Join the two sets.
ages = {25, 30, 35}
first_names = {"Alice", "Bob", "Charlie"}
combined_set = ages.union(first_names)
print("Combined set:", combined_set)


"""
Explanation:

1. **Creating a set of favorite beverages:**
   - A set of favorite beverages is created using the `set()` constructor, which takes a list of three beverages: `["coffee", "tea", "juice"]`.

2. **Adding two more items to the beverages set:**
   - The `add()` method is used to add `"water"` and `"soda"` to the `beverages` set.

3. **Checking if "microwave" is present in `mySet`:**
   - The expression `"microwave" in mySet` checks for the presence of `"microwave"` in the set `mySet`, which contains `{"oven", "kettle", "microwave", "refrigerator"}`.

4. **Removing "kettle" from `mySet`:**
   - The `remove()` method is used to remove `"kettle"` from the set `mySet`.

5. **Looping through `mySet`:**
   - A `for` loop iterates through each item in `mySet`, printing each item.

6. **Adding elements from a list to a set:**
   - A set `mySet2` containing four items and a list `myList` containing two items are created. The `update()` method adds all elements from `myList` to `mySet2`.

7. **Joining two sets:**
   - Two sets are created: `ages` containing three age values and `first_names` containing three first names. The `union()` method combines these two sets into a new set `combined_set`.


"""