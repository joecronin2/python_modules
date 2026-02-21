class Plant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int, age_days: int):
        self._starting_height = height_cm
        self._starting_age = age_days
        self.name = name

    def grow(self, days: int=1, growth_rate: int=1):
        self.height_cm += days * growth_rate

    def __str__(self) -> str:
        return f"{self.name} ({self.height_cm}cm, {self.age_days} days)"

class Flower(Plant):
    def bloom(self):
        pass
    
class Tree(Plant):
    def produce_shade(self):
        pass
    
class Vegetable(Plant):
    def __init__(self, name: str, height_cm: int, age_days: int):
        super(self).__init__()