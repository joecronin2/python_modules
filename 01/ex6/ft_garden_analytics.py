class Plant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int, age_days: int):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days
        self.starting_height = height_cm
        self.starting_age = age_days

    def grow(self, days: int = 1, growth_rate: int = 1) -> None:
        self.height_cm += days * growth_rate

    def __str__(self) -> str:
        return f"{self.name}: {self.height_cm}cm"


class FloweringPlant(Plant):
    color: str
    is_blooming: bool

    def __init__(self, name: str, height_cm: int, age_days: int, color: str):
        super().__init__(name, height_cm, age_days)
        self.color = color
        self.is_blooming = True

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"{self.name} is blooming beautifully!")

    def __str__(self) -> str:
        status = "blooming" if self.is_blooming else "dormant"
        return f"{self.name}: {self.height_cm}cm, {self.color}" \
            f"flowers ({status})"


class PrizeFlower(FloweringPlant):
    prize_points: int

    def __init__(self, name: str, height_cm: int, age_days: int,
                 color: str, prize_points: int):
        super().__init__(name, height_cm, age_days, color)
        self.prize_points = prize_points

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}, Prize points: {self.prize_points}"


class Garden:
    plants: list[Plant]
    owner: str

    def __init__(self, owner: str):
        self.owner = owner
        self.plants: list[Plant] = []
        self._growth_events: int = 0

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)

    def grow_plants(self) -> None:
        for p in self.plants:
            print(f"{p.name} grew 1cm")
            p.grow()
        self._growth_events += 1

    def water_plants(self) -> None:
        self.grow_plants()

    def report(self, stats: "GardenManager.GardenStats") -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            print(f"  - {p}")
        summary = stats.summarise(self)
        print(
            f"Plants added: {summary['total']}, "
            f"Total growth: {summary['total_growth']}cm"
        )
        print(
            f"Plant types: {summary['regular']} regular, "
            f"{summary['flowering']} flowering, "
            f"{summary['prize']} prize flowers"
        )


class GardenManager:
    gardens: list[Garden]

    class GardenStats:
        def summarise(self, garden: "Garden") -> dict:
            regular = flowering = prize = 0
            total_growth = 0
            for p in garden.plants:
                growth = p.height_cm - p.starting_height
                total_growth += growth
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return {
                "total": len(garden.plants),
                "regular": regular,
                "flowering": flowering,
                "prize": prize,
                "total_growth": total_growth,
            }

        def score(self, garden: "Garden") -> int:
            total = 0
            for p in garden.plants:
                if isinstance(p, PrizeFlower):
                    total += p.height_cm * 3
                elif isinstance(p, FloweringPlant):
                    total += p.height_cm * 2
                else:
                    total += p.height_cm
            return total

    def __init__(self):
        self.gardens: list[Garden] = []
        self.stats = GardenManager.GardenStats()

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    def get_garden(self, owner: str) -> Garden:
        return next(g for g in self.gardens if g.owner == owner)

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        garden = self.get_garden(owner)
        garden.add_plant(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def water_all(self, owner: str) -> None:
        print(f"{owner} is helping all plants grow...")
        self.get_garden(owner).grow_plants()

    def garden_score(self, owner: str) -> int:
        return self.stats.score(self.get_garden(owner))

    def garden_report(self, owner: str) -> None:
        self.get_garden(owner).report(self.stats)

    @classmethod
    def create_garden_network(cls, owner_names: list[str]) -> "GardenManager":
        manager = cls()
        for name in owner_names:
            manager.add_garden(Garden(name))
        return manager

    @staticmethod
    def validate_height(height_cm: int, min_cm: int = 0,
                        max_cm: int = 1000) -> bool:
        return min_cm <= height_cm <= max_cm

    @staticmethod
    def season_advice(season: str) -> str:
        return {
            "spring": "Great time for flowering plants!",
            "summer": "Water frequently and watch for pests.",
            "autumn": "Prepare beds for winter.",
            "winter": "Focus on indoor seedlings.",
        }.get(season.lower(), "No specific advice available.")

    def total_gardens(self) -> int:
        return len(self.gardens)


def optimal_planting_depth(plant_type: str) -> str:
    return {
        "seed": "1-2 cm",
        "bulb": "10-15 cm",
        "sapling": "30-50 cm",
        "shrub": "40-60 cm",
    }.get(plant_type.lower(), "Unknown depth")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    gm = GardenManager.create_garden_network(["Alice", "Bob"])

    oak = Plant("Oak Tree", 100, 3650)
    rose = FloweringPlant("Rose", 25, 365, "red")
    sunfl = PrizeFlower("Sunflower", 50, 180, "yellow", 10)

    gm.add_plant_to_garden("Alice", oak)
    gm.add_plant_to_garden("Alice", rose)
    gm.add_plant_to_garden("Alice", sunfl)

    gm.water_all("Alice")

    gm.garden_report("Alice")

    tulip = FloweringPlant("Tulip", 20, 90, "purple")
    shrub = Plant("Boxwood Shrub", 60, 730)
    gm.add_plant_to_garden("Bob", tulip)
    gm.add_plant_to_garden("Bob", shrub)

    print(f"Height validation test: {GardenManager.validate_height(150)}")

    alice_score = gm.garden_score("Alice")
    bob_score = gm.garden_score("Bob")
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    print(f"Total gardens managed: {gm.total_gardens()}")
