class Plant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
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


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants = [
        Plant('Rose', 25, 30),
        Plant('Sunflower', 80, 45),
        Plant('Rose', 15, 120),
    ]
    days = 7
    for day in range(days):
        print(f"=== Day {day+1} ===")
        for plant in plants:
            print(plant)
            plant.grow()
            plant.age()

    print(f"\nGrowth this week: +{days - 1}cm")

    print("=== End of Program ===")
