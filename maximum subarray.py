class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result=[]

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                result.append(nums[i:j+1])

        output=[sum(sub) for sub in result]
        return max(output)

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum=x[0]
        max_sum=x[0]
        for i in range (len(x)):
            current_sum += x[i]
        
            if x[i]> current_sum:
                current_sum = x[i]
            if current_sum>max_sum:
                max_sum=current_sum
            
        print(max_sum)
