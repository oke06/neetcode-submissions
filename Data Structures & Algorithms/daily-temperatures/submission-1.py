class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        for i in range(len(temperatures)):
            count = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output.append(count)
                    break
                else:
                    count += 1
            if len(output) != i + 1:
                output.append(0) 

        return output
