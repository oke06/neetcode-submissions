class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = [[] for i in range(len(nums) + 1)]
        count = {}

        for v in nums:
            count[v] = 1 + count.get(v, 0)

        for i, v in count.items():
            output[v].append(i)
        
        final = []
        for i in range(len(output) - 1, 0, -1):
            for n in output[i]:
                final.append(n)
                if len(final) == k:
                    return final
        return []
         
        