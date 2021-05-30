#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
         0   1   2
        ['', '', '']
        ['P', '', '']
        ['P', 'A', '']
        ['P', 'A', 'Y']
        ['P', 'AP', 'Y']
        ['PA', 'AP', 'Y']
        ['PA', 'APL', 'Y']
        ['PA', 'APL', 'YI']
        ['PA', 'APLS', 'YI']
        ['PAH', 'APLS', 'YI']
        ['PAH', 'APLSI', 'YI']
        ['PAH', 'APLSI', 'YIR']
        ['PAH', 'APLSII', 'YIR']
        ['PAHN', 'APLSII', 'YIR']

        """
        if numRows == 1:
            return s

        result = ["" for _ in range(numRows)]

        for i in range(len(s)):
            # find the row using the modulo since we are ciruclating over the
            # row from top to bottom.
            # In below example, we are considering following charters.
            # P   A   H   N
            # A P L S I I G
            # Y   I   R
            # P->0, A -> 1, Y-> 2, P ->3
            row = i % (2*numRows - 2)
            if row < numRows:
                result[row] += s[i]
            else:
                result[numRows-row-2] += s[i]

        return ''.join(result)


print(Solution().convert('PAYPALISHIRING', 3))
print(Solution().convert('PAYPALISHIRING', 4))
# @lc code=end
