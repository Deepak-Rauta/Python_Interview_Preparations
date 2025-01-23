def find_frequencies(arr):
    frequencies = {}

    for element in arr:
        if element in frequencies:
            frequencies[element] += 1
        else:
            frequencies[element] = 1

    return frequencies

# Example usage:
arr = [2, 3, 2, 4, 5, 3, 5, 5, 4, 2]

result = find_frequencies(arr)

for key, value in result.items():
    print(f"Element {key} occurs {value} times.")
    