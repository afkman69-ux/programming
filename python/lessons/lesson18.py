
# it returns even numbers within the tuple 


def pick_evens(*args):

    even = []

    for i in args:
        if i % 2 == 0:
            even.append(i)
    return even


print(pick_evens(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
print(pick_evens(1, 3, 5, 7))