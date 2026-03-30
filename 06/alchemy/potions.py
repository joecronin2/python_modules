from alchemy.elements import (
    create_earth,
    create_water,
    create_fire,
    create_air,
)


def healing_potion() -> str:
    return "Healing potion brewed with " + " and ".join(
        [
            create_fire(),
            create_water(),
        ]
    )


def strength_potion() -> str:
    return "Strength potion brewed with " + " and ".join(
        [
            create_earth(),
            create_earth(),
        ]
    )


def invisibility_potion() -> str:
    return "Invisibility potion brewed with " + " and ".join(
        [
            create_air(),
            create_water(),
        ]
    )


def wisdom_potion() -> str:
    return "Wisdom potion brewed with all elements: " + " and ".join(
        [
            create_air(),
            create_fire(),
            create_water(),
            create_earth(),
        ]
    )


__all__ = [
    "healing_potion",
    "strength_potion",
    "invisibility_potion",
    "wisdom_potion",
]
