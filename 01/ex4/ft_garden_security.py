class SecurePlant:
    name: str
    height_cm: int
    age_days: int

    def __init__(self, name: str, height_cm: int=0, age_days: int=0):
        self.name = name
        self.set_height(height_cm)
        self.set_age(age_days)

    def set_height(self, height_cm: int):
        if height_cm < 0:
            raise ValueError(f"Invalid height of {height_cm}. Height must be non-negative")
        self.height_cm = height_cm

    def set_age(self, age_days: int):
        if age_days < 0:
            raise ValueError(f"Invalid age of {age_days}. Age must be non-negative")
        self.age_days = age_days
    
    def get_height(self) -> int:
        return self.height_cm

    def get_age(self) -> int:
        return self.age_days

    def grow(self, days: int=1, growth_rate: int=1):
        self.height_cm += days * growth_rate

    def __str__(self) -> str:
        return f"{self.name} ({self.height_cm}cm, {self.age_days} days)"
    

if __name__ == "__main__":
    SecurePlant("Rose", 25, 30)
    SecurePlant("InvalidRose", -5, 30)
    SecurePlant("InvalidRose2", 25, -30)