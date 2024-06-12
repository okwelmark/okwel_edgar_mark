"""
-dictionaries
-creating and using dictionaries
-dictionary methods and operations
..................................
dictionaries are collection of keys and values;-
    they can be unordered
                mutable
                indexed by keys
"""

#Example 1: creating a dictionary
#create a dictionary for a student persuing software engineering,
#the key must be your name, age, technology interest, and year of study. 
#put your own details

student_dict = {
    'name': 'Okwel Edgar Mark',
    'age': '23',
    'technology': 'Djong',
    'course': 'BSSE',
    'year': 'year 3'
}
print(student_dict['name'])

# Exercise 1: Modifying the year and age
student_dict['year'] = 'year 4'
student_dict['age'] = '24'
print(student_dict)


#Example2 adding keys and values
student_dict['email'] = 'mcedgars190@gmail.com'

print(student_dict)
# exercise 2: remove the email
del student_dict['email']
print(student_dict)

"""
get() returns the value 
update()
pop()

"""
print('................................')
print('................................')

#Example 3: Use the get method to get the value
# we can use it in the terminal
print(student_dict.get('technology'))

#Exercise 3: use the updat()to change value in age
print('................................')
print('................................')
student_dict.update({'age': '24'})
print(student_dict['age'])

print('................................')
print('................................')

#Exercise 4: use if to check if the key 'age' is present in the dictionary
if 'age' in student_dict:
    print("The key 'age' is present in the dictionary.")
    print("Age:", student_dict['age'])
else:
    print("The key 'age' is not present in the dictionary.")

    
    #keys(), values(), and the item() methods
 
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())
    
    
"""
keys(): return a view of objects that displays a list of all keys
values(): returns a view of objects that displays the list of all values
items(): returns a view of objects that displays a list of dictionary keys and values


"""
#exercise 5: use the update method to change the course and add a new key 'whatsApp_number' to the dictionary
student_dict.update({'course': 'BSSE', 'whatsApp_number': '0755106013'})
print(student_dict)