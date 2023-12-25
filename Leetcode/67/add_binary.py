# 67. Add Binary
# Easy
# 9K
# 909
# Companies

# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

 

# Constraints:

#     1 <= a.length, b.length <= 104
#     a and b consist only of '0' or '1' characters.
#     Each string does not contain leading zeros except for the zero itself.

#The Easy Way:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #convert to integer
        x, y = int(a, 2), int(b, 2)
        while y:
            #XOR Operation ex: 1010 ^ 1011 = 0001
            #AND Operation and Left Shift 
            #ex：1010 & 1011 = 1010, and shifting left by one gives 10100.
            x, y = x ^ y, (x & y) << 1
        #convert back to binary and slice the first 2 element for ex bin（2）0b10， got 10
        return bin(x)[2:]

# The Hard Way:
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def num_from_bstring(s):
            num = 0
            for i, place in enumerate(reversed(list(s))):
                num += int(place) * 2**i
            return num

        def bstring_from_num(n):
            last_place = 0
            while 2**last_place < n:
                last_place += 1
            # print('last place of', n, 'is 2**', last_place)
            # last_place += 1
            bstring = ['0']*(last_place + 1)
            place = last_place

            while place >= 0:
                # print(place, bstring)
                if n - 2**place >= 0:
                    bstring[place] = '1'
                    n -= 2**place               
                place -= 1
            
            return ''.join(reversed(bstring))

        num_a = num_from_bstring(a)
        num_b = num_from_bstring(b)
        # print(num_a, '+', num_b, '=', num_a + num_b)
        bstring = bstring_from_num(num_a + num_b)
        # print(a, '+', b, '=', bstring)

        return str(int(bstring))
