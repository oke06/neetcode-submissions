class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for i in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                j = stack.pop()
                output[j] = i - j
            stack.append(i)
        return output