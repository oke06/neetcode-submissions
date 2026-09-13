class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            res = str(len(word)) + '#' + word
            output.append(res)
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        i, res = 0, []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        return res