#using for loop with equal logic
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False


#sorting the array
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
                
        return False


#using set function
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set={}
        for i in nums:
            if i in set:
                return True
            else:
                set[i]=1
        return False


