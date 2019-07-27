#leetcode : https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/
class Solution(object):
    def findDuplicates(self, nums=list):
        res = []
        for i in nums:
            if nums[abs(i)-1]>0:
                nums[abs(i)-1] *= -1
            else:
                res.append(abs(i))
        return res