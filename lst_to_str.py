words = ["Python", "is", "fum"]
result = " ".join(words)
print(result)

# join a list of integer
number = [1,2,3,4,5]
result = ",".join(map(str, number))
print(result)

# Reverse list and join
words = ["hello", "world", "python"]
result = " ".join(words[::-1])
print(result)

# or
words = ["hello", "world", "python"]
result = " ".join(reversed(words))
print(result)

# Concatenate Characters
chars = ["a", "b", "c", "d"]
result = "".join(chars)
print(result)

# Add Prefix While Joining
fruits = ["apple", "banana", "cherry"]
result = ";".join(f"fruit:{fruit}" for fruit in fruits)
print(result)  # Output: "fruit:apple;fruit:banana;fruit:cherry"

# join nested list
nested_list = [[1,2], [3,4], [5,6]]
flattened = [str(num) for sublist in nested_list for num in sublist]
result = "-".join(flattened)
print(result)

nested_list = [[1,2], [3,4], [5,6]]
flattende = [str(num) for sublist in nested_list for num in sublist]
result = "-".join(flattened)
print(result)

# capitalize and join
words = ["python", "is", "awesome"]
result = ",".join(word.capitalize() for word in words)
print(result)

# Extract Initials and Join
names = ["John Doe", "Jane Smith", "Sam Brown"]
result = ".".join(name[0] for name in names)
print(result)

# conditional join
words = ["apple", "banana", "cherry", "date"]
result = " ".join(word for word in words if len(word) > 5)
print(result)
