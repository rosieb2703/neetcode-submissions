class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        nums.extend(nums)

        # or

        # length = len(nums)
        # capacity = 2 * length
        # ans = capacity * [0]

        # for i in range(length):
        #     ans[i] = nums[i]
        #     ans[i+length] = nums[i]

        return nums

