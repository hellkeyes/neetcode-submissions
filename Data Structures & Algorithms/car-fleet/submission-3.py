class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        hrs = []

        cars = sorted(zip(position, speed), reverse=True)

        for key, value in cars:
            x = (target - key) / value
            hrs.append(x)

        # print(hrs)


        i = 0
        j = 1
        fleet = 1
        while j < len(hrs):
            if hrs[i] >= hrs[j]:
                j += 1
            else:
                fleet += 1
                i = j
                j += 1

        return fleet