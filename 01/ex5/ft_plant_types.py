class Plant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int, age_days: int):
        self._starting_height = height_cm
        self._starting_age = age_days
        self.height_cm = height_cm
        self.age_days = age_days

        self.name = name

    def grow(self, days: int = 1, growth_rate: int = 1):
        self.height_cm += days * growth_rate

    def __str__(self) -> str:
        return f"{self.name} ({self.height_cm}cm, {self.age_days} days)"


class Flower(Plant):
    color: str

    def __init__(self, name: str, height_cm: int, age_days: int, color: str):
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self) -> None:
        print(self.name, "is blooming beautifully!")

    def __str__(self):
        return f"{super().__str__()}, {self.color} color"


class Tree(Plant):
    trunk_diameter: int

    def __init__(self, name: str, height_cm: int, age_days: int,
                 trunk_diameter: int):
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.height_cm / self.trunk_diameter
        print(f"{self.name} provides {shade} square meters of shade")

    def __str__(self):
        return f"{super().__str__()}, {self.trunk_diameter}cm diameter"


class Vegetable(Plant):
    harvest_season: str
    nutritional_value: str

    def __init__(self, name: str, height_cm: int, age_days: int,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutritional_value(self):
        print(f"{self.name} is rich in {self.nutritional_value}")

    def __str__(self):
        return f"{super().__str__()}, {self.harvest_season} harvest"


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    print(rose)
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    print(oak)
    oak.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print(tomato)
    tomato.show_nutritional_value()

    tulip = Flower("Tulip", 30, 20, "yellow")
    print(tulip)
    tulip.bloom()

    pine = Tree("Pine", 1200, 3650, 80)
    print(pine)
    pine.produce_shade()

    carrot = Vegetable("Carrot", 25, 70, "autumn", "beta-carotene")
    print(carrot)
    carrot.show_nutritional_value()
