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

    def grow(self, days: int=1, growth_rate: int=1):
        self.height_cm += days * growth_rate

    def __str__(self) -> str:
        return f"{self.name} ({self.height_cm}cm, {self.age_days} days)"
    
class PlantFactory:
    plants: list[Plant]

    def __init__(self):
        self.plants = []

    def add_plants(self, plants: list[Plant]):
        [print("Created:", plant) for plant in plants]
        self.plants.extend(plants)
        print(f"\nTotal plants created: {len(plants)}")

    def __str__(self):
        return "Plant Factory:\n" + "\n".join(str(p) for p in self.plants)


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    PlantFactory().add_plants([
        Plant('Khat', 25, 30),
        Plant('Poppy', 80, 45),
        Plant('Ephedra', 15, 120),
        Plant('Salvia', 35, 30),
        Plant('Datura', 5, 15),
    ])

    print("=== End of Program ===")
