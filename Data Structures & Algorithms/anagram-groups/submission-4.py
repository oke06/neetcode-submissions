class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        while strs:
            cur_word = strs[0]    
            sub_output = [cur_word] 
            for word in strs[1:]:
                if all(word.count(letter) == cur_word.count(letter) for letter in word) and len(word) == len(cur_word):
                    sub_output.append(word)
            output.append(sub_output)
            for word in sub_output:
                strs.remove(word)
        return output