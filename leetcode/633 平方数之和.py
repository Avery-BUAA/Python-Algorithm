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
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = c//2
        ls = list(range(x+1))
        i , j = 1 , len(ls)-1
        while i < j :
            temp = ls[i]**2 + ls[j]**2
            if temp > c:
                j -= 1
            elif temp <c:
                i +=1
            else:
                return True
        return False
s = Solution()

print(s.judgeSquareSum(5))
