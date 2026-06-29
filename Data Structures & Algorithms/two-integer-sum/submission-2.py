class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            match = target - nums[i]

            if match in m:
                return [m[match], i]

            m[nums[i]] = i