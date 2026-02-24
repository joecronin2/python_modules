def water_plant(plant: str) -> None:
    if not plant:
        raise ValueError("Cannot water None or empty plant name!")


def water_plants(plant_list: list[str]):
    print("Opening watering system")
    try:
        for plant in plant_list:
            water_plant(plant)
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("Testing watering system...")
    water_plants([
        "Tomato",
        "Basil",
        "Sunflower",
        "Lavender",
        "Rosemary",
    ])

    print("\nTesting watering system with error...")
    water_plants([
        "Tomato",
        "Basil",
        "Sunflower",
        "",
        "Lavender",
        "Rosemary",
    ])
