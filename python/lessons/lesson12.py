def is_even(nums):
    return nums % 2 == 0

def my_odds(n):
    res = []
    for _ in n:
        if not is_even(_):
            res.append(_)
    return res

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odds = my_odds(my_list)

print(odds)