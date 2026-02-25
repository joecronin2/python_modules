def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    if not plant_name:
        raise ValueError("plant name cannot be empty")
    if not (1 <= water_level <= 10):
        raise ValueError("water level must be between 1 and 10")
    if not (2 <= sunlight_hours <= 12):
        raise ValueError("hours of sunlight must be between 2 and 12")


if __name__ == "__main__":
    print("testing good values...")
    try:
        check_plant_health("tomato", 4, 4)
        print("tomato is healthy!")
    except ValueError as e:
        print(f"Error: {e}")

    print("\ntesting empty plant name...")
    try:
        check_plant_health("", 4, 4)
    except ValueError as e:
        print(f"Error: {e}")

    print("\ntesting bad water level...")
    try:
        check_plant_health("tomato", 40, 4)
    except ValueError as e:
        print(f"Error: {e}")

    print("\ntesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 4, 40)
    except ValueError as e:
        print(f"Error: {e}")
