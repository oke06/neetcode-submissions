class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        for s in strs:
            array = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                array[index] += 1
            output[tuple(array)].append(s)
        return list(output.values())
