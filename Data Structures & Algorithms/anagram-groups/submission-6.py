class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = collections.defaultdict(list)
        for s in strs:
            index = [0] * 26
            for c in s:
                enc = ord(c) - ord('a')
                index[enc] += 1

            output[tuple(index)].append(s)
        return list(output.values())
        