square = [x**2 for x in range(1,6)]
print(square)

# [expression for item in iterable if condition]
ev = [x for x in range(1,11) if x%2==0]
print(ev)

odd = [x for x in range(1,11) if x%2!=0]
print(odd)

words = ['hello', 'world', 'python', 'list', 'comprehension']
filtered_words = [word for word in words if 'o' in word]
print(filtered_words)
# Output: ['hello', 'world', 'python']
