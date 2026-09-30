class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        listed = [[] for i in range(len(nums) + 1)]
        output = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            listed[c].append(n)
        for i in range(len(listed) - 1, 0, -1):
            for n in listed[i]:
                output.append(n)
                if len(output) == k:
                    return output
        return []