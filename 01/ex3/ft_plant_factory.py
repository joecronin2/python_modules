class Plant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int, age_days: int):
        self._starting_height = height_cm
        self._starting_age = age_days
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, by_cm: int = 1) -> None:
        self.height_cm += by_cm

    def age(self, days: int = 1) -> None:
        self.age_days += days

    def get_info(self) -> None:
        print(str(self))

    def __str__(self) -> str:
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


class PlantFactory:
    plants: list[Plant]

    def __init__(self):
        self.plants = []

    def add_plants(self, plants: list[Plant]):
        for plant in plants:
            print("Created:", plant)
        self.plants.extend(plants)
        print(f"\nTotal plants created: {len(plants)}")

    def __str__(self):
        return "Plant Factory:\n" + "\n".join(str(p) for p in self.plants)


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    PlantFactory().add_plants([
        Plant('Tomato', 25, 30),
        Plant('Basil', 15, 45),
        Plant('Sunflower', 80, 60),
        Plant('Lavender', 35, 90),
        Plant('Rosemary', 20, 120),
    ])
    print("=== End of Program ===")
