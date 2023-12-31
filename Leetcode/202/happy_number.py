# 202. Happy Number
# Easy
# 9.8K
# 1.3K
# Companies

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

#     Starting with any positive integer, replace the number by the sum of the squares of its digits.
#     Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#     Those numbers for which this process ends in 1 are happy.

# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:

# Input: n = 2
# Output: false

 

# Constraints:

#     1 <= n <= 231 - 1

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def foo(n: int):
            l = [int(x)**2 for x in str(n)]
            return sum(l)
        
        seen = {n}
        while n != 1:
            new_n = foo(n)
            
            if new_n in seen:
                return False
            
            seen.add(new_n)
            n = new_n
        return True


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:  
                return True
            n = sum([int(x)**2 for x in str(n)])   
            if n in seen:
                return False         
            seen.add(n)
