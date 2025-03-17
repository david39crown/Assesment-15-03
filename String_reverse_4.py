#Question no:4
''': Reverse User Input for Data Processing
Imagine you are developing a secure system for user input validation, and part of the system
involves reversing strings (such as passwords or IDs) for a unique encryption method.
Write a Python program that accepts a string from the user and returns it in reverse order. This
could simulate part of a process where data is transformed before being stored or transmitted
securely.
Example 1:
Input:
1234abcd
Output:
dcba4321
'''

# Function to reverse a string
def reverse_string(data):
    return data[::-1]


user_input = input("Enter a string: ")


reversed_string = reverse_string(user_input)
print("Reversed Output:", reversed_string)
