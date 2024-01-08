# 50. Pow(x, n)
# Medium
# 9.2K
# 9.1K
# Companies

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

 

# Constraints:

#     -100.0 < x < 100.0
#     -231 <= n <= 231-1
#     n is an integer.
#     Either x is not zero or n > 0.
#     -104 <= xn <= 104

# The Easy Way:
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n



# The Hard Way:
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        elif n > 0:
            new_x = 1
        else:
            new_x = 1
            x     = abs(1/x)

        for _ in range(abs(n)):
            new_x *= x

        return new_x
