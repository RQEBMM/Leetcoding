# 125. Valid Palindrome
# Easy
# 8.5K
# 8K
# Companies

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

 

# Constraints:

#     1 <= s.length <= 2 * 105
#     s consists only of printable ASCII characters.

# The Easy Way:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(lambda x: x.isalnum(), s)).lower()
        return s == ''.join(reversed(s))

# The Hard Way:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def clean_str(s):
            cleaning_map = {
                'A': 'a',
                'B': 'b',
                'C': 'c',
                'D': 'd',
                'E': 'e',
                'F': 'f',
                'G': 'g',
                'H': 'h',
                'I': 'i',
                'J': 'j',
                'K': 'k',
                'L': 'l',
                'M': 'm',
                'N': 'n',
                'O': 'o',
                'P': 'p',
                'Q': 'q',
                'R': 'r',
                'S': 's',
                'T': 't',
                'U': 'u',
                'V': 'v',
                'W': 'w',
                'X': 'x',
                'Y': 'y',
                'Z': 'z',

                '0': '0',
                '1': '1',
                '2': '2',
                '3': '3',
                '4': '4',
                '5': '5',
                '6': '6',
                '7': '7',
                '8': '8',
                '9': '9',
                '`': '',
                '~': '',
                '!': '',
                '@': '',
                '#': '',
                '$': '',
                '%': '',
                '^': '',
                '&': '',
                '*': '',
                '(': '',
                ')': '',
                '-': '',
                '_': '',
                '=': '',
                '+': '',
                '[': '',
                ']': '',
                '{': '',
                '}': '',
                '\\': '',
                '|': '',
                ';': '',
                ':': '',
                "'": '',
                '"': '',
                ',': '',
                '.': '',
                '/': '',
                '<': '',
                '>': '',
                '?': '',
                ' ': '',
            }
            new_s = ''
            for char in s:
                new_s += cleaning_map.get(char, char)
            return new_s
        
        s = clean_str(s)
        
        if len(s) < 2:
            return True

        def is_even(num):
            return int(num % 2 == 0)
        
        def is_odd(num):
            return int(num % 2 != 0)
        
        p1 = len(s) // 2
        p2 = len(s) // 2 - is_even(len(s))
        
        for i in range(p1 + is_odd(len(s))):
            char1 = s[p1+i]
            char2 = s[p2-i]
            if char1 != char2:
                return False

        return True
