#Question no:5
'''Check if a String is Pangram
You are designing a chatbot for an e-commerce platform. The chatbot is expected to understand
and respond to user queries efficiently. To ensure that it can handle diverse inputs, you need to
verify that its internal processing covers all possible alphabetical characters. A pangram is a
sentence that contains every letter of the English alphabet at least once.
Write a Python function that takes a string as input and checks whether the string is a pangram
(contains every letter of the alphabet at least once).
'''

import string

def is_pangram(s):
    alphabet_set = set(string.ascii_lowercase)  
    s = s.lower()  
    return alphabet_set.issubset(set(s))  


text = "The quick brown fox jumps over the lazy dog"


print(is_pangram(text))  


https://github.com/david39crown/Assesment-15-03