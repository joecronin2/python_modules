class GardenError(Exception):
    def __init__(self, message: str = "Garden error occurred") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self) -> None:
        super().__init__("Plant name cannot be empty")


class WaterError(GardenError):
    def __init__(self) -> None:
        super().__init__("Water level must be between 1 and 10")


class Plant:
    def __init__(self, name: str) -> None:
        if not name:
            raise PlantError()
        self.name: str = name
        self.healthy: bool = True

    def water(self, amount: int) -> None:
        if not (1 <= amount <= 10):
            raise WaterError()

        print(f"Watering {self.name} with amount {amount}")


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plant(self, plant_name: str) -> None:
        try:
            plant: Plant = Plant(plant_name)
            self.plants.append(plant)
            print(f"Added plant: {plant_name}")
        except GardenError as e:
            print(f"Failed to add plant: {e}")

    def water_plants(self, amount: int) -> None:
        print("Starting watering system...")
        try:
            for plant in self.plants:
                try:
                    plant.water(amount)
                except WaterError as e:
                    print(f"Watering error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
        self, plant_name: str, water_level: int, sunlight_hours: int
    ) -> None:
        if not plant_name:
            raise PlantError()
        if not (1 <= water_level <= 10):
            raise WaterError()
        if not (2 <= sunlight_hours <= 12):
            raise GardenError("Sunlight hours must be between 2 and 12")
        print(f"{plant_name} is healthy!")


def test_garden_management() -> None:
    print("=== Garden Management System Test ===")
    manager: GardenManager = GardenManager()
    print("\nAdding plants...")
    plant_names: list[str] = ["Tomato", "", "Basil", "Rose"]

    for name in plant_names:
        manager.add_plant(name)

    print("\nWatering plants (valid amount)...")
    try:
        manager.water_plants(5)
    except Exception as e:
        print(f"Unexpected system error: {e}")
    finally:
        print("Watering cycle completed")

    print("\nTesting plant health validation...")
    tests: list[tuple[str, int, int]] = [
        ("Tomato", 5, 6),
        ("", 5, 6),
        ("Basil", 20, 6),
        ("Rose", 5, 20),
    ]

    for plant_name, water, sun in tests:
        try:
            manager.check_plant_health(plant_name, water, sun)
        except GardenError as e:
            print(f"Health check failed: {e}")

    print("\nSystem continues working after errors.")


if __name__ == "__main__":
    test_garden_management()
