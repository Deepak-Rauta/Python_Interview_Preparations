def OderFill(order, k):
    # first sort the order in ascending order
    order.sort()
    fullfilled = 0
    for o in order:
        if k >= o:
            k -= o
            fullfilled += 1
        else:
            break
    return fullfilled
orders = [10, 30]
k = 40
result = OderFill(orders, k)
print(result)
