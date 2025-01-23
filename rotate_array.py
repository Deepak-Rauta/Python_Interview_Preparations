# def rotate_array(arr, positions, direction):
#     n = len(arr)
#     positions %= n
#     if direction == 'left':
#         rotate_arr = arr[positions:] + arr[:positions]
#     elif direction == 'right':
#         rotate_arr = arr[-positions:] + arr[:-positions]
#     else:
#         "Pls enter a valid directions"
#     return rotate_arr
# # Example usages
# arr = [1,2,3,4,5,6]
# positions = 2

# left_result = rotate_array(arr, positions, 'left')
# print(f"The left rotation is: {left_result}")


# right_result = rotate_array(arr, positions, 'right')
# print(f"The right rotation is: {right_result}")

def rotate_arr(arr, position, direction):
    n = len(arr)
    position %= n
    if direction == 'left':
        rotated_array = arr[position:] + arr[:position]
    elif direction == 'right':
        rotated_array = arr[-position:] + arr[:-position]
    else:
        "Pls enter a valid directions"

    return rotated_array
arr = [1,2,3,4,5,6]
position = 2
left_result = rotate_arr(arr, position, 'left')
print(f'left_restlt is:', {left_result})

right_result = rotate_arr(arr, position, 'right')
print(f'left_restlt is:', {right_result})
