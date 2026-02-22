def print_days(day: int):
    if day > 0:
        print_days(day - 1)
        print("Day", day)


def ft_count_harvest_recursive():
    print_days(int(input("Days until harvest: ")))
    print("Harvest time!")
