class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            box = [0] * 26
            for letter in word:
                box[ord(letter) - ord('a')] += 1
            anagrams[tuple(box)].append(word)
        return list(anagrams.values())
        