class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0 for i in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            if stack:
                while stack and temp > stack[-1][1]:
                    output[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append([i, temp])
            else:
                stack.append([i, temp])
        return output
