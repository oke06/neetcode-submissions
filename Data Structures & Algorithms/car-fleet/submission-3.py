class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = sorted(zip(position, speed), reverse = True)
        for p, s in cars:
            time = (target - p) / s
            if fleets and fleets[-1] < time or not fleets:
                fleets.append(time)
        return len(fleets)