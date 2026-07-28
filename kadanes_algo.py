"""Visual Example
nums = [4, -6, 2, 3]

Start

current = 4

best = 4

Visit

-6

Continue

4-6=-2

Restart

-6

Which is larger?

-2

Keep

-2

Best remains

4

Next

2

Continue

-2+2

=

0

Restart

2

Choose

2

because

2>0

So

current=2

Next

3

Continue

2+3=5

Restart

3

Choose

5

Best becomes

5

Finished."""

def maxSubArray(nums):

    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = [4, -6, 2, 3]
result = maxSubArray(nums)
print(result)