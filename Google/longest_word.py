# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

# Note: D can appear in any format (list, hash table, prefix tree, etc.

# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".

# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.

# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

# Learning objectives

# This question gives you the chance to practice with algorithms and data structures. It’s also a good example of why careful analysis for Big-O performance is often worthwhile, as is careful exploration of common and worst-case input conditions.

S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}
expected = "apple"

D = sorted(D, key=len, reverse=True)

def is_in_S(word, S):
    
    for i in range(len(S)):
        char = S[i]
        if word.startswith(char):
            word = word[1:]
            if len(word) == 0:
                return True

    return False
        
def get_longest(S, D):
    for word in D:
        word_in_S = is_in_S(word, S)
        if word_in_S:
            return word

longest = get_longest(S, D)
print(expected == longest)
print(longest)
