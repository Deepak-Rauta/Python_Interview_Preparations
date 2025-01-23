def binary_gap(n):
    # convert integer to binary and remove the '0b' perfix
    binary_representation = bin(n)[2:]
    # split the binary string by '1' to find the sequence of 0's
    gaps = binary_representation.strip('0').split('1')
    # find the length of longest subsequence oif 0's
    max_gap = max(len(gaps) for gap in gaps)
    return max_gap
number = 529
result = binary_gap(number)
print(result)

