class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # piles = [3,6,7,11], h = 8
        i = 1
        j = max(piles)

        while i <= j:
            mid = (i + j)//2

            hrs_mid = 0
            total_hrs = 0
            for pile in piles:
                hrs_mid = math.ceil(pile/mid)
                total_hrs = total_hrs + hrs_mid

            # print(f'for {mid} the {total_hrs}')

            if total_hrs <= h:
                j = mid - 1

            else:
                i = mid + 1

        return i
