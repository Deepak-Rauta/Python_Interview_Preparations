# The goal of this problem is to determine the amount of water that can be trapped between bars in an elevation map after it rains. 
# The bars are represented as a list of non-negative integers, where each element corresponds to the height of a bar. 
# The water is trapped in the valleys formed between the bars.
# To solve this problem, we need to identify the trapped water in each position based on the heights of the surrounding bars.

# First create two array:-
# left_max[i] = Max height from index 0 to i
# right_max[i] = max height from index n-1 to i
# left_max = [0] * n: This initializes an array of size n with all values as 0. 
# It will be used to store the maximum height encountered from the left for each position.
# right_max = [0] * n: This initializes another array to store the maximum height encountered from the right.
# trapped_water = 0: This variable will keep track of the total trapped water.
# left_max[i - 1] → Maximum height encountered so far (to the left).
# height[i] → Current bar’s height.
# We take the maximum of these two values.



def trap(height):
    if not height:
        return 0
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    trapped_water = 0

    # Fill left max
    left_max[0] = height[0]  # # The first element's max left boundary is itself.
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
