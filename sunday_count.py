def count_sunday(start_day, days):
    # Days of the weeks in a list
    week_dayas = ["Monday", "Tuesday", "Wednesday", "Thrusday",
                  "Friday", "Saturday", "Sunday"]
    start_index = week_dayas.index(start_day)
    # Count for sunday
    sunday_count = 0
    for i in range(days):
        if (start_index + i) % 7 == 6:
            sunday_count += 1
    return sunday_count
start_day = "Tuesday"
days = 13
result = count_sunday(start_day, days)
print(f"The no.of sunday is: {result}")

