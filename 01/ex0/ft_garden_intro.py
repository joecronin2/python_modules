class Plant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int, age_days: int) -> None:
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def __str__(self) -> str:
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days old"


if __name__ == "__main__":
    print("=== Welcome to My Garden ===")
    print(Plant("Rose", 25, 30))
    print(Plant("Sunflower", 39, 29))
    print("=== End of Program ===")
