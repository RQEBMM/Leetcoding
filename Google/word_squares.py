# A “word square” is an ordered sequence of K different words of length K that, when written one word per line, reads the same horizontally and vertically. For example:

# BALL AREA LEAD LADY

# AREA

# LEAD

# LADY

# In this exercise you're going to create a way to find word squares.

# First, design a way to return true if a given sequence of words is a word square.

# Second, given an arbitrary list of words, return all the possible word squares it contains. Reordering is allowed.

# For example, the input list

# [AREA, BALL, DEAR, LADY, LEAD, YARD]

# should output

# [(BALL, AREA, LEAD, LADY), (LADY, AREA, DEAR, YARD)]

# Finishing the first task should help you accomplish the second task. Learning objectives

# This problem gives practice with algorithms, recursion, arrays, progressively optimizing from an initial solution, and testing.

class TestCase:
    def __init__(self, case, exp_result):
        self.case = case
        self.exp_result = exp_result

test_cases = {
    TestCase(['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD'], False),
    TestCase(['BALL', 'AREA', 'LEAD', 'LADY'], True),
    TestCase(['BALL', 'AREA', 'LADS', 'LADY'], False),
#    TestCase(['LADY', 'AREA', 'DEAR', 'YARD'], True),
}

import pandas as pd

def is_word_square(list_of_words):
    if len(list_of_words) == 0:
        return False

    example_word = list_of_words[0]

    # assure all words match in len
    for word in list_of_words:
        if len(word) != len(example_word):
            return False
    
    h = list(list_of_words)
    v = [''] * len(example_word)
    
    for idx in range(len(example_word)): # 0, 1, 2, 3
        new_word = ''
        for word in list_of_words: # B, A, L, L;
            new_word = f"{new_word}{word[idx]}" # 'BALL'
        v[idx] = new_word
    result = h == v
    # print(h, v, result)
    return result

import itertools

list_of_words = ['AREA', 'BALL', 'DEAR', 'LADY', 'LEAD', 'YARD']
def get_word_squares(list_of_words):
    wordspace = list(itertools.permutations(list_of_words))
    print(wordspace)
    

for case in test_cases:
    print(case.case, case.exp_result)
    result = is_word_square(case.case)
    print("result: ", result)
    if result == case.exp_result:
        print("GOOD GOOD GOOD!")
    else:
        print("!BAD !BAD !BAD!")
