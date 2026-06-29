class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in list(count.keys()):
                count[num] = 1
            else:
                count[num] = count[num] + 1

        array = []
        for num, count in count.items():
            array.append([count, num])

        array.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(array[i][1])

        return result
