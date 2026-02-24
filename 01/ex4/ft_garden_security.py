class SecurePlant:
    def __init__(self, name: str, height_cm: int = 0,
                 age_days: int = 0) -> None:
        self.__name = name
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

    def get_height(self) -> int:
        return self.__height_cm

    def get_age(self) -> int:
        return self.__age_days

    def grow(self, by_cm: int = 1) -> None:
        self.set_height(by_cm)

    def age(self, days: int = 1) -> None:
        self.set_age(days)

    def get_info(self) -> None:
        print(str(self))

    def __str__(self) -> str:
        return f"{self.__name}: {self.__height_cm}cm, {self.__age_days}" \
            " days old"


if __name__ == "__main__":
    try:
        print(SecurePlant("Rose", 25, 30))
        print(SecurePlant("InvalidRose", -5, 30))
        print(SecurePlant("InvalidRose2", 25, -30))
    except ValueError:
        print("invalid value passed")
