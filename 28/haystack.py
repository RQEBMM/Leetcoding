# 28. Find the Index of the First Occurrence in a String
# Easy
# 5.1K
# 307
# Companies

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

 

# Constraints:

#     1 <= haystack.length, needle.length <= 104
#     haystack and needle consist of only lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        needlength = len(needle)
        
        for x in range(len(haystack) - needlength + 1):
            print(x, haystack[x:x+needlength])
            if haystack[x:x+needlength] == needle:
                return x
        
        return -1
