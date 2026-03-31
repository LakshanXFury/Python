"""
Count Odd Numbers in an Interval Range
"""




def count_odd(low: int, high: int) -> int:
    return (high+1)//2 - low // 2


print(count_odd(1, 100))
print(count_odd(3, 7))


"""
(high + 1)//2 → total odds till high  (n+1)/2
low // 2 → total odds before low
"""