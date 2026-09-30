class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            container = [0] * 26
            for letter in word:
                container[ord(letter) - ord('a')] += 1
            output[tuple(container)].append(word)
        return list(output.values())