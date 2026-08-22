
# it sums all the numbers in the tuple!


def sum_numbers(*args):
    total = 0
    for i in args:
        total += i
    return total


print(sum_numbers(32, 43, 5))