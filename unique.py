# With out using any Data structures like list, set, dict
def is_unique(s):
    n = len(s)
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                return False
    return True
my_string = "abbcde"
result = is_unique(my_string)
print(result)