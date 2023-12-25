# 383. Ransom Note
# Easy
# 4.7K
# 476
# Companies

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

 

# Constraints:

#     1 <= ransomNote.length, magazine.length <= 105
#     ransomNote and magazine consist of lowercase English letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = {}

        for letter in magazine:
            magazine_map[letter] = magazine_map.get(letter, 0) + 1
        
        for letter in ransomNote:
            try:
                letter_count = magazine_map[letter]
                if letter_count > 0:
                    magazine_map[letter] = letter_count - 1
                else:
                    return False
            except KeyError as e:
                return False
        
        return True

