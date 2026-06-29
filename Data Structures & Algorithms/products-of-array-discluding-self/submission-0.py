class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        new_list = []
        for i, num in enumerate(nums):
            multiplied_num = 1
            j = 0
            while j < len(nums):
                if j == i:
                    pass
                else:
                    multiplied_num *= nums[j]
                j +=1
            new_list.append(multiplied_num)

        return new_list

        
