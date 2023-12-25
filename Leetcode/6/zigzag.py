6. Zigzag Conversion
Medium
7K
13.7K
Companies

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

# Constraints:

#     1 <= s.length <= 1000
#     s consists of English letters (lower-case and upper-case), ',' and '.'.
#     1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        offset = max(0, numRows - 2)
        k = numRows + offset
        header = ''.join([s[x] for x in range(0, len(s), k)])
        rows = []

        for row_idx in range(1,numRows-1):
            offset_row_idx = k - row_idx
            row_indices = range(row_idx, len(s), k)
            offset_idxs = range(offset_row_idx, len(s), k)
            for i, v in enumerate(row_indices):
                rows.append(v)
                try:
                    offset_v = offset_idxs[i]
                    rows.append(offset_v)
                except IndexError:
                    pass
        
        rows = ''.join([s[x] for x in rows])
        footer = ''.join([s[x] for x in range(numRows-1, len(s), k)])
        return header + rows + footer
