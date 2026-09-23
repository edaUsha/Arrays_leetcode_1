class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result=[]

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                result.append(nums[i:j+1])

        output=[sum(sub) for sub in result]
        return max(output)
            
