class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

class Solution:
    def twoSum(self,nums,target):
        mapping = {}
        for index,value in enumerate(nums):
            diff = target - value
            if diff in mapping:
                return [index,mapping[diff]]
            else:
                mapping[value] = index

nums = [2, 7, 11, 15]
target = 9

sol = Solution()
a = sol.twoSum(nums, target)
print(a)
