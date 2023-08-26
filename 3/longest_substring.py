# Given a string s, find the length of the longest
# substring
# without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

# Constraints:

#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        for x in reversed(range(1, len(set(s)) + 1)):
            remaining_indices = len(s) - x
            remaining_searches = remaining_indices + 1
            
            for start in range(0, remaining_searches):
                end = start + x
                sub = s[start:end]
                if len(sub) == len(set(sub)):
                    return len(sub)
        return len(s)
