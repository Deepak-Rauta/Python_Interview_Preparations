# def my_product(orders, k):
#     # first sort the array
#     orders.sort()
#     # Initialize the variable
#     fullfilled = 0
    
#     for order in orders:
#         if k >= order:
#             k -= order
#             fullfilled += 1
#         else:
#             break
#     return fullfilled
# orders = [1,2,3,5,7]
# k = 10
# result = my_product(orders, k)
# print(result)
    

def FilledOrders(orders, k):
    # First sort the array 
    orders.sort()
    # Initialize the variables
    filled_orders = 0
    for order in orders:
        if k >= order:
            k -= order
            filled_orders += 1
        else:
            break
    return filled_orders
orders = [1,2,3,5,7]
k = 10
result = FilledOrders(orders, k)
print(result)
