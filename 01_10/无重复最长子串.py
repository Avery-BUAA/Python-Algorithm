"""

定义一个set()
1.遍历字符串，count+1
2.如果s[i]在字符串中：left+1,count-1，set里面remove
3.如果不在set里面增加
4.随时记录max的值

"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        lookup = set()
        left = 0
        count = 0
        max = 0
        res = []
        for i in range(len(s)):
            count += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                count -= 1
            if count > max:
                max = count
                a = s[left:left + max]

            lookup.add(s[i])
        print(a)

        return max
