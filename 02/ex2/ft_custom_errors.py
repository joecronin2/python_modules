class GardenError(Exception):
    def __init__(self, message="garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self):
        super().__init__("The tomato plant is wilting!")


class WaterError(GardenError):
    def __init__(self):
        super().__init__("Not enough water in the tank!")


if __name__ == "__main__":
    print("Testing PlantError...")
    try:
        raise PlantError
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing PlantError as GardenError...")
    try:
        raise PlantError
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("Testing WaterError...")
    try:
        raise WaterError
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing WaterError as GardenError...")
    try:
        raise WaterError
    except GardenError as e:
        print(f"Caught GardenError: {e}")
