def char_count_difference(s):
    # count the star count
    star_count = s.count("*")
    # count the hash count
    hash_count = s.count("#")

    difference = star_count - hash_count
    return difference

str =  "*##***##*"
result = char_count_difference(str)

if result > 0:
    print("More '*':", result)
elif result < 0:
    print("More '#':", result)
else:
    print("Equal number of '*' and '#'")

