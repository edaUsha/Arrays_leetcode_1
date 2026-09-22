class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

#Using hash table
#time complexity reduces
numToIndex = {}
for i in range(len(nums)):
    diff= target - nums[i]
    if diff in numToIndex:
        print([i,numToIndex[diff]])
    numToIndex[nums[i]] = i


    
        
