def Find_Greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(Find_Greatest(10, 20, 5))
print(Find_Greatest(10, -20, 5))
print(Find_Greatest(-10, 8, 5))