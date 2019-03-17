import numpy as np
class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = ["" for i in range(numRows)]  # 使用列表生成式
        row,down = 0,True
        for char in s:
            result[row] += char
            if row == 0:
                down = True
            if row == numRows-1:
                down = False
            if down:
                row += 1
            if not down:
                row -= 1
        str = ''
        for row in result:
            str += row
        return str


sol = Solution()
a = 'LEETCODEISHIRING'
print(sol.convert(a,4))

