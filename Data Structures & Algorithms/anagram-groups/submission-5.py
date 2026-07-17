class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for letter in word:
                index = ord(letter) - ord("a")
                count[index] += 1

            output[tuple(count)].append(word)
        return list(output.values())
        