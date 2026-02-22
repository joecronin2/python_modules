class Plant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int, age_days: int):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self, days: int = 1, growth_rate: int = 1):
        self.height_cm += days * growth_rate

    def __str__(self) -> str:
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants = [
        Plant('Rose', 25, 30),
        Plant('Sunflower', 80, 45),
        Plant('Rose', 15, 120),
    ]
    for day in range(7):
        print(f"=== Day {day+1} ===")
        for plant in plants:
            plant.grow(days=7)
            print(plant)
    print("\nGrowth this week: +6cm")

    print("=== End of Program ===")
