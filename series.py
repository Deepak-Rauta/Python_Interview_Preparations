def series_pattern(n, m):  #Define a function series_pattern
    result = 1  #take a variable result which will store the cumulative product of the series
    for i in range(n, m + 1):
        result *= i
    return result

# Example usage:
n = 2
m = 5
for i in range(n, m + 1):
    print(series_pattern(n, i))

            # Q2
def alternating_series_sum(n): # define a function that take a parametr n
    result = 0 # it wll store the result
    for i in range(1, n + 1):
        result += (-1) ** (i + 1) / i
    return result

# Example usage:
n = 5
print(alternating_series_sum(n))

