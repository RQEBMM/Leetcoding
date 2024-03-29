# 69. Sqrt(x)
# Easy
# 7.7K
# 4.4K
# Companies

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

#     For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

 

# Constraints:

#     0 <= x <= 231 - 1

# The Easy Way:
class Solution:
    def mySqrt(self, x: int, n: int) -> int:
      return x**n

# The Hard Way:
class Solution:
    def mySqrt(self, x: int, n: int) -> int:
        n = 0
        while True:
            nsq = (n+1)*(n+1)
            if nsq < x:
                n += 1
            elif nsq == x:
                return n+1
            elif nsq > x:
                return n
