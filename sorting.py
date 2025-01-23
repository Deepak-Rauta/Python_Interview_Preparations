def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Track if any swapping is done in the inner loop
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, break
        if not swapped:
            break
    return arr

# Test the function
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)

# The swapped = False line is used to keep track of whether any elements were swapped during a pass. 
# If no elements were swapped, it means the list is already sorted, and we can stop the algorithm early to save time.


