class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        before_array = [1]
        for i in range(1, len(nums)):
            sub_array = nums[:i]
            stub = 1
            for num in sub_array:
                stub *= num
            before_array.append(stub)

        after_array = []
        for i in range(len(nums)-1):
            sub_array = nums[i+1:]
            stub = 1
            for num in sub_array:
                stub *= num
            after_array.append(stub)

        after_array.append(1)

        final_array = []
        for i in range(len(nums)):
            val = before_array[i] * after_array[i]
            final_array.append(val)

        return final_array
        