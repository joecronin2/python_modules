def validate_ingredients(ingredients: str) -> str:
    valid = {"fire", "water", "earth", "air"}
    items = ingredients.split(" ")
    return (
        f"{ingredients} - "
        f"{'VALID' if all(item in valid for item in items) else 'INVALID'}"
    )
