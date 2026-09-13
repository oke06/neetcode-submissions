class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ordered = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, total in count.items():
            ordered[total].append(n)

        output = []
        for i in range(len(ordered) - 1, -1, -1):
            for n in ordered[i]:
                output.append(n)
                if len(output) == k:
                    return output
        return []