class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arranged = []
        stack = []
        for i in range(len(speed)):
            arranged.append([position[i], speed[i]])
        arranged.sort()
        arranged = arranged[::-1]
        for i, s in enumerate(arranged):
            if stack and stack[-1] >= ((target - s[0])/s[1]):
                continue
            else:
                stack.append((target - s[0])/s[1])

        return len(stack)