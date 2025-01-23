def harmonic_sum(n):
    """
    Compute the harmonic sum of n.

    Parameters:
    - n (int): The number of terms in the harmonic sum.

    Returns:
    - float: The computed harmonic sum.
    """
    # Initialize the sum to 0
    result = 0.0

    # Iterate from 1 to n
    for i in range(1, n + 1):
        result += 1 / (2 ** i)

    return result

# Example usage:
n_terms = 5
result = harmonic_sum(n_terms)
print(f"The harmonic sum of {n_terms} terms is: {result}")
