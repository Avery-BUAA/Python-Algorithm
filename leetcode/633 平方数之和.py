# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
#
# 示例1:
#
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
#  
#
# 示例2:
#
# 输入: 3
# 输出: False
import math

"""
使用双指针一个从两端开始，一个增加，一个减少
"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j=int(math.sqrt(c))
        i =0
        while i <= j :
            if i**2 + j**2 > c:
                j -=1
            elif i**2 + j**2 < c:
                i +=1
            else:
                return True
        return False


s = Solution()

print(s.judgeSquareSum(5))
