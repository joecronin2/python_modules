class Plant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int, age_days: int):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

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
    print(*plants, sep='\n')
    print("=== End of Program ===")
