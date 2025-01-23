def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # Help us track if any elements were swapped during this phase 
        # This assumes that no elements will need to be swapped during the current pass.

        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Here the elements were swapped and we need to ste it True
                swapped = True
        # If no elements were swapped during the inner loop swapped remain False
        if not swapped:
            break
    return arr
    
array = [64, 34, 25, 12, 22, 11, 40]
result = BubbleSort(array)
print(result)








