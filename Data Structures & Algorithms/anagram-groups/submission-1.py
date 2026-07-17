class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        index = 0 
        output = []
        while strs:
            sub = []
            hashmap = {
                'a':0,
                'b':0,
                'c':0,
                'd':0,
                'e':0,
                'f':0,
                'g':0,
                'h':0,
                'i':0,
                'j':0,
                'k':0,
                'l':0,
                'm':0,
                'n':0,
                'o':0,
                'p':0,
                'q':0,
                'r':0,
                's':0,
                't':0,
                'u':0,
                'v':0,
                'w':0,
                'x':0,
                'y':0,
                'z':0
            }
            for letter in strs[index]:
                if letter not in hashmap:
                    hashmap[letter] = 1
                else:
                    hashmap[letter] += 1
            for word in strs:
                if all(word.count(letter) == hashmap[letter] for letter in word) and len(word) == len(strs[0]):
                    sub.append(word)
            if len(sub) == 1:
                strs.pop(0)
            else:
                for word in sub:
                    strs.remove(word)
            output.append(sub)
        return(output)

                        
