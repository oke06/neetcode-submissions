class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lists = [[] for i in range(len(nums) + 1)]     
        total = {}   
        for num in nums:
            total[num] = 1 + total.get(num, 0)

        for num, count in total.items():
            lists[count].append(num)

        output = []
        for i in range(len(lists) - 1, 0, -1):
            for num in lists[i]:
                output.append(num)
                if len(output) == k:
                    return output
        return []