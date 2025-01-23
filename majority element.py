# Majority elements meaning in the array if the element doesn't repeat then it gives value -1 if the repeat then it gives the value corresponding number
def find_majority_element(nums):
    # Initialize variables to store the candidate and its count
    candidate = None
    count = 0
    
    # Find the candidate for the majority element
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # Verify if the candidate is the majority element
    count = 0
    for num in nums:
        if num == candidate:
            count += 1
    
    if count > len(nums) // 2:
        return candidate
    else:
        return None

# Example usage:
input_array = [3, 3, 4, 2, 4, 4, 2, 4, 4]
majority_element = find_majority_element(input_array)

if majority_element is not None:
    print(f"The majority element in the array is: {majority_element}")
else:
    print("There is no majority element in the array.")



                 


