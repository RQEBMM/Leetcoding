# 49. Group Anagrams
# Medium
# 17.9K
# 536
# Companies

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

 

# Constraints:

#     1 <= strs.length <= 104
#     0 <= strs[i].length <= 100
#     strs[i] consists of lowercase English letters.

# Hard way: not good enough
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def get_word_map(s):
            s_map = {}
            for c in s:
                s_map[c] = s_map.get(c, 0) + 1
            return s_map
        
        def isAnagram(s, t):
            if len(s) != len(t):
                return False
            
            return s == t
        
        buckets = []
        str_map = {}
        for string in strs:
            str_map[strs] = get_word_map(string)
        
        for i in range(len(strs)):
            word = strs.pop(0)
            fit = False
            for bucket in buckets:
                if isAnagram(str_map[word], bucket[0]):
                    bucket.append(word)
                    fit = True
            
            if fit == False: 
                buckets.append([word])
        
        return buckets

            
