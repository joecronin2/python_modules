class Plant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int, age_days: int):
        self.starting_height = height_cm
        self.starting_age = age_days
        self.height_cm = height_cm
        self.age_days = age_days

        self.name = name

    def grow(self, days: int = 1, growth_rate: int = 1):
        self.height_cm += days * growth_rate

    def __str__(self) -> str:
        return f"{self.name} ({self.height_cm}cm, {self.age_days} days)"


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


class FloweringPlant(Plant):
    color: str

    def __init__(self, name: str, height_cm: int, age_days: int, color: str):
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self) -> None:
        print(self.name, "is blooming beautifully!")

    def __str__(self):
        return f"{super().__str__()}, {self.color} color"


class PrizeFlower(FloweringPlant):
    prize_points: int

    def __init__(self, name: str, height_cm: int, age_days: int,
                 color: str, prize_points: int):
        super().__init__(name, height_cm, age_days, color)
        self.prize_points = prize_points

    def __str__(self):
        return f"{super().__str__()}, Prize points: {self.prize_points}"


class Garden():
    plants: list[Plant]
    owner: str

    def __init__(self, owner: str):
        self.plants = []
        self.owner = owner

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)

    def grow_plants(self):
        for p in self.plants:
            p.grow()

    def water_plants(self):
        for p in self.plants:
            p.grow()


class GardenManager():
    gardens: list[Garden]

    def __init__(self):
        self.gardens = []
        pass

    def add_garden(self, garden: Garden):
        self.gardens.append(garden)

    def get_garden(self, owner: str) -> Garden:
        return next(g for g in self.gardens if g.owner == owner)

    def add_plant_to_garden(self, owner: str, plant: Plant):
        print(f"Added {plant} to {owner}'s garden")

    def water_plants(self, owner: str):
        self.get_garden(owner).water_plants()

        
if __name__ == "__main__":
    gm: GardenManager = GardenManager()
    gm.add_garden(Garden("Alice"))
