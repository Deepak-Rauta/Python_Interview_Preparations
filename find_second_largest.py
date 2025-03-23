def Second_Largest(nums):
    nums = list(set(nums))
    if len(nums) < 2:
        return "No second largest elements in the list"
    nums.sort(reverse=True) # sort in descending order
    return nums[1] # extract the second lasrgets 
print(Second_Largest([10, 4, 5, 7, 9, 8, 1]))
print(Second_Largest([5, 5, 5, 5, 5]))