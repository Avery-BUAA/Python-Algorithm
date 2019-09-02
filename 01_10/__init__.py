class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        max =1
        for i in range(len(nums)-1):
            tep=0
            if nums[i+1]>nums[i]:
                max +=1
                print(max,"max")
                if i==len(nums)-2:
                    if tep<max:
                        print(max)
                        tep = max
                        max = 0

            else:
                if tep < max:
                    tep = max
                    max =0
                    print(max)
        print(tep,"tep1")

S=Solution()
S.findLengthOfLCIS([1,3,5,4,7])