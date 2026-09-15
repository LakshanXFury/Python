"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas
from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas
during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.


Imp : Ceil division divides two numbers and rounds the result up to the next largest whole number
"""

piles_1 = [3,6,7,11]
piles_2 = [30,11,23,4,20]


def getHours(piles, mid):
    ans = 0

    for pile in piles:
        ans += (pile + mid - 1) // mid  # Ceil division

    return ans

def minEatingSpeed(piles:list[int], h: int) -> int:
    l = 1
    r = max(piles)

    k = r

    while l <= r:
        mid = (l + r) // 2

        if getHours(piles, mid) > h:
            l = mid + 1
        else:
            k = mid
            r = mid - 1

    return k


print(minEatingSpeed(piles_1, 8))
print(minEatingSpeed(piles_2, 6))


