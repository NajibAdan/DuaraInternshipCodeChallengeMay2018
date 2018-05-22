'''
Duara Internship Code Challenge - 22nd May 2018

Task 4

Converting a list of t9 characters and returning a list of all words in dictionary represented in a dictionary
'''
import re

keypad = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']


def convert(number):
    possible_words = []
    number_str = str(number)
    pattern = "^"
    for x in number_str:
        pattern = pattern + "[" + keypad[int(x)] + "]"
    pattern += "$"
    file = open('words.txt', 'r')
    for word in file:
        if re.search(pattern, word.lower()):
            possible_words.append(word.strip())

    print possible_words
