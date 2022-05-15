class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            number_1 = nums[i]
            number_2 = target - number_1
            for j in range(len(nums) - i):
                if nums[j] == number_2:
                    break
        return [i, j]