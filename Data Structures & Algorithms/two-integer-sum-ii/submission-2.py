class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        pointer_1 = 0

        while pointer_1 < len(numbers)-1:
            pointer_2 = pointer_1 + 1
            while pointer_2 <= len(numbers)-1:
                num = numbers[pointer_2]
                if num == target - numbers[pointer_1]:
                    return [pointer_1 + 1, pointer_2 + 1]
                else:
                    pointer_2 += 1
            pointer_1 += 1
                 
        return [pointer_1 + 1, pointer_2 + 1]


        