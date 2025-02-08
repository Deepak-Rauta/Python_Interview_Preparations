def rotate_array(arr, positions, direction):
    n = len(arr)
    positions %= n
    if direction == 'left':
        rotate_arr = arr[positions:] + arr[:positions]
    elif direction == 'right':
        rotate_arr = arr[-positions:] + arr[:-positions]
    else:
        "Pls enter a valid directions"
    return rotate_arr
# Example usages
arr = [1,2,3,4,5,6]
positions = 2

left_result = rotate_array(arr, positions, 'left')
print(f"The left rotation is: {left_result}")


right_result = rotate_array(arr, positions, 'right')
print(f"The right rotation is: {right_result}")



# Explanations:
# 📌 Example Case:
# If positions = 2 and n = 6, then:
# positions = 2 % 6
# Step-by-Step Calculation:
# 2 divided by 6 gives a quotient of 0 (since 2 is smaller than 6).
# Remainder is 2.
# So, positions = 2.

# ✅ Final Result:
# positions remains 2 because 2 % 6 = 2.