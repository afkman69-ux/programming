
# returns the tallest building within the tuple


def skyline(*args):
    high = 0
    for i in args:
        if i > high:
            high = max(high, i)
    return high
print(skyline(1, 654, 1234, 43))