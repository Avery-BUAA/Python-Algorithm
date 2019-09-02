# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"
# 示例 2:
#
# 输入: "leetcode"
# 输出: "leotcede"
# 说明:
# 元音字母不包含字母"y"。
"""
    使用双指针，遍历到了就进行翻转

"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        left,right = 0 , len(s)-1
        nums = ["a","e","i","o","u","A","E","I","O","U"]
        s = list(s)
        while left < right:
            if s[left] in nums and s[right] in nums:
                s[left],s[right] = s[right] , s[left]
                right -=1
                left +=1
            elif s[left] in nums and s[right] not in nums:
                right -=1
            elif s[left] not in nums and s[right] not in nums:
                right -=1
                left += 1
            else:
                left +=1
        return "".join(s)
s = Solution()
print(s.reverseVowels("hello"))




