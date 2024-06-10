# Exercise1 (Lists)
# 1.	Create a list with 5 items (names of people) and write a python program to output the 2nd item.
#............................

# people = ['Edgar', 'Martha', 'Lewis', 'Alonzo', 'Mark']
# print(people[1])

#............................
# 2.	Write a python program to change the value of the first item to a new value

# people = ['Edgar', 'Martha', 'Lewis', 'Alonzo', 'Mark']
# people[1] = 'Aluto'
# print(people[1])

# 3.	Write a python program to add a sixth item to the list
#.............................

# people = ['Edgar', 'Martha', 'Lewis', 'Alonzo', 'Mark']
# people.append('Okwel')

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
