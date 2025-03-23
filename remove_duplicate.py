def RemoveDuplicate(nums):
    unique_lst = list(dict.fromkeys(nums))
    return unique_lst
print(RemoveDuplicate([10, 3, 3, 4, 6, 4, 2, 1, 2]))