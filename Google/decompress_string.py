# In this exercise, you're going to decompress a compressed string.

# Your input is a compressed string of the format number[string] and the decompressed output form should be the string written number times. For example:

# The input

# 3[abc]4[ab]c

# Would be output as

# abcabcabcababababc
# Other rules

# Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa

# One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab

# Characters allowed as input include digits, small English letters and brackets [ ].

# Digits are only to represent amount of repetitions.

# Letters are just letters.

# Brackets are only part of syntax of writing repeated substring.

# Input is always valid, so no need to check its validity.
# Learning objectives

# This question gives you the chance to practice with strings, recursion, algorithm, compilers, automata, and loops. It’s also an opportunity to work on coding with better efficiency.

test_cases = {
    '3[abc]4[ab]c' : 'abcabcabcababababc',
    '10[a]': 'aaaaaaaaaa',
    '2[3[a]b]':'aaabaaab',
    '0[abc]': '',
    '1[]': '',
    '1[a]': 'a',
    '10[a10[b]]': 'abbbbbbbbbbabbbbbbbbbbabbbbbbbbbbabbbbbbbbbbabbbbbbbbbbabbbbbbbbbbabbbbbbbbbbabbbbbbbbbbabbbbbbbbbbabbbbbbbbbb'
}

class Chunk:
    def __init__(self, string):
        self.num = None
        self.sub = None
        
        # store num
        self.num, remainder = string.split('[', maxsplit=1)
        
        sub = ''
        idx = 0
        while idx < len(remainder):
            char = remainder[idx]
            if char.isdigit():
                chunk = Chunk(remainder[idx:])
                sub += chunk.evaluate()
                idx = idx + len(chunk.sub) + 2 + len(chunk.num)
            elif char == ']':
                self.sub = sub
                return
            else:
                sub += char
                idx += 1
            
        self.sub = sub

    # evaluate parsed string
    def evaluate(self):
        return f"{int(self.num) * self.sub}"

def solution(compressed_str) -> str:
    if compressed_str[-1] != ']':
        compressed_str = '1[' + compressed_str + ']'
    
    return Chunk(compressed_str).evaluate()

for comp, decomp in test_cases.items():
    print(comp, decomp)
    solved = solution(comp)
    print(solved)
    if solved != decomp:
        print("Bad bad bad!")
    else:
        print("Goodgoodgood!")
