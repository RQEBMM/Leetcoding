# 58. Length of Last Word
# Easy
# 4.3K
# 219
# Companies

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
# consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

 

# Constraints:

#     1 <= s.length <= 104
#     s consists of only English letters and spaces ' '.
#     There will be at least one word in s.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().rsplit(' ', maxsplit=1)
        last_word = words[-1]
        return len(last_word)

# Without python luxuries:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ctr = 0
        len_s = len(s)
        ptr = len_s - 1
        val = s[ptr]
        
        while val == ' ':
            ptr -= 1    
            val = s[ptr]
        
        while val != ' ' and ptr > -1:
            ctr +=1
            ptr -= 1
            val = s[ptr]
        
        return ctr
