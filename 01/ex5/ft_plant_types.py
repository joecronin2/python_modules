class Plant:
    def __init__(self, name: str, height_cm: int = 0,
                 age_days: int = 0) -> None:
        self.set_name(name)
        self.set_height(height_cm)
        self.set_age(age_days)

    def set_height(self, height_cm: int) -> None:
        if height_cm < 0:
            raise ValueError(f"Invalid height of {height_cm}. "
                             "Height must be non-negative")
        self.__height_cm = height_cm

    def set_age(self, age_days: int) -> None:
        if age_days < 0:
            raise ValueError(f"Invalid age of {age_days}. "
                             "Age must be non-negative")
        self.__age_days = age_days

    def set_name(self, name: str) -> None:
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string")
        self.__name = name

    def get_height(self) -> int:
        return self.__height_cm

    def get_age(self) -> int:
        return self.__age_days

    def get_name(self) -> str:
        return self.__name

    def grow(self, by_cm: int = 1) -> None:
        self.set_height(self.get_height() + by_cm)

    def age(self, days: int = 1) -> None:
        self.set_age(self.get_age() + days)

    def get_info(self) -> None:
        print(str(self))

    def __str__(self) -> str:
        return (f"{self.get_name()}: {self.get_height()}cm, "
                f"{self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height_cm: int, age_days: int,
                 color: str) -> None:
        super().__init__(name, height_cm, age_days)
        self.set_color(color)

    def bloom(self) -> None:
        print(self.get_name(), "is blooming beautifully!")

    def set_color(self, color: str) -> None:
        if not color or not isinstance(color, str):
            raise ValueError("Color must be a non-empty string")
        self.__color = color

    def get_color(self) -> str:
        return self.__color

    def get_info(self) -> None:
        print(str(self))

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.get_color()} color"


class Tree(Plant):
    def __init__(self, name: str, height_cm: int, age_days: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height_cm, age_days)
        self.set_trunk_diameter(trunk_diameter)

    def produce_shade(self) -> None:
        shade = self.get_height() / self.get_trunk_diameter()
        print(f"{self.get_name()} provides {shade:.2f} square meters of shade")

    def set_trunk_diameter(self, trunk_diameter: int) -> None:
        if trunk_diameter <= 0:
            raise ValueError(f"Invalid trunk diameter of {trunk_diameter}. "
                             "Trunk diameter must be positive")
        self.__trunk_diameter = trunk_diameter

    def get_trunk_diameter(self) -> int:
        return self.__trunk_diameter

    def get_info(self) -> None:
        print(str(self))

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.get_trunk_diameter()}cm diameter"


class Vegetable(Plant):
    def __init__(self, name: str, height_cm: int, age_days: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height_cm, age_days)
        self.set_harvest_season(harvest_season)
        self.set_nutritional_value(nutritional_value)

    def set_harvest_season(self, harvest_season: str) -> None:
        if not harvest_season or not isinstance(harvest_season, str):
            raise ValueError("Harvest season must be a non-empty string")
        self.__harvest_season = harvest_season

    def get_harvest_season(self) -> str:
        return self.__harvest_season

    def set_nutritional_value(self, nutritional_value: str) -> None:
        if not nutritional_value or not isinstance(nutritional_value, str):
            raise ValueError("Nutritional value must be a non-empty string")
        self.__nutritional_value = nutritional_value

    def get_nutritional_value(self) -> str:
        return self.__nutritional_value

    def show_nutritional_value(self) -> None:
        print(f"{self.get_name()} is rich in {self.get_nutritional_value()}")

    def get_info(self) -> None:
        print(str(self))

    def __str__(self) -> str:
        return f"{super().__str__()}, {self.get_harvest_season()} harvest"


if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    rose.get_info()
    rose.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    oak.get_info()
    oak.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.get_info()
    tomato.show_nutritional_value()

    tulip = Flower("Tulip", 30, 20, "yellow")
    tulip.get_info()
    tulip.bloom()

    pine = Tree("Pine", 1200, 3650, 80)
    pine.get_info()
    pine.produce_shade()

    carrot = Vegetable("Carrot", 25, 70, "autumn", "beta-carotene")
    carrot.get_info()
    carrot.show_nutritional_value()
