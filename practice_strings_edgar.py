
# Exercise 4 (Strings)

# 1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables.
num = 10
text = " is a number"
concatenated = str(num) + text
print("Concatenated string:", concatenated)

# 2. Consider the example below; Output the string without spaces at the beginning, in the middle and at the end.
txt = "      Hello,       Uganda!       "
cleaned_txt = " ".join(txt.split())
print("String without extra spaces:", cleaned_txt)

# 3. Write a python program to convert the value of ‘txt’ to uppercase.
uppercase_txt = cleaned_txt.upper()
print("Uppercase string:", uppercase_txt)

# 4. Write a python program to replace character ‘U’ with ‘V’ in the string above.
replaced_txt = uppercase_txt.replace('U', 'V')
print("String with 'U' replaced by 'V':", replaced_txt)

# 5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position.
y = "I am proudly Ugandan"
substring = y[2:5]
print("Characters in the 2nd, 3rd, and 4th position:", substring)

# 6. The piece of code below will give an error when output; Write a python program to correct it.
x = 'All "Data Scientists" are cool!'
print("Corrected string:", x)

"""

Explanation:

1. Concatenating an integer and a string:
   - An integer `num` and a string `text` are declared. To concatenate them, the integer is converted 
   to a string using `str(num)` and then concatenated with `text` using the `+` operator.

2. Removing spaces at the beginning, in the middle, and at the end:
   - The string `txt` contains extra spaces. Using the `split()` method, the string is split into 
   words, and then `" ".join()` is used to join them back together with a single space between each
   word, effectively removing extra spaces.

3. Converting the string to uppercase:
   - The `upper()` method is used to convert all characters in the cleaned string `cleaned_txt` to uppercase.

4. Replacing character ‘U’ with ‘V’:
   - The `replace()` method is used to replace all occurrences of the character 'U' with 'V' in the 
   uppercase string `uppercase_txt`.

5. Returning a range of characters in the 2nd, 3rd, and 4th positions:
   - Using string slicing `y[2:5]`, the characters from index `2` to `4` (2nd to 4th positions) in the 
   string `y` are extracted and printed.

6. Correcting the string with quotes:
   - The string `x` contains double quotes around "Data Scientists". To fix the syntax error, single quotes 
   are used to enclose the entire string. This way, double quotes inside the string are handled correctly.

"""