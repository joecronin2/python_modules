def print_days(day: int):
    if day > 0:
        print_days(day - 1)
        print("Day", day)


print_days(int(input("Days until harvest: ")))
print("Harvest time!")
