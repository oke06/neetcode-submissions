class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        final = []
        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
        if k < 0:
            pass 
        else:
            for i in range(k):
                most_nums = 0
                num_with_most_nums = 0
                for num in num_count:
                    if num_count[num] > most_nums:
                        most_nums = num_count[num]
                        num_with_most_nums = num
                final.append(num_with_most_nums)        
                num_count.pop(num_with_most_nums)
        return final
