def count_sub_str(str, sub_str):
    count = 0
    sub_len = len(sub_str)
    for i in range(len(str) - sub_len + 1):
        if str[i:i + sub_len] == sub_str:
            count += 1
    return count
string = 'abcabcd'
sub_string = 'bcd'
result = count_sub_str(string, sub_string)
print(result)


