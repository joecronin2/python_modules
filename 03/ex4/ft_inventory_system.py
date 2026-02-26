import sys


class ParseError(Exception):
    pass


def parse_items(items: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for entry in items:
        parts = entry.split(":")
        if len(parts) != 2:
            raise ParseError("only one delimiter expected")
        name, quantity_str = parts
        if not name:
            raise ParseError("name cannot be empty")
        try:
            quantity = int(quantity_str)
        except ValueError as e:
            raise ParseError(f"error parsing quantity: {e}")
        if quantity < 1:
            raise ParseError("quantity must be greater than 0")
        result[name] = quantity
    return result


def print_inventory(items: dict[str, int]) -> None:
    print("=== Current Inventory ===")
    total_items: int = sum(items.values())
    if total_items == 0:
        print("Inventory is empty")
        return
    for key, val in items.items():
        percentage = (val / total_items) * 100
        print(f"{key}: {val} units ({percentage:.2f}%)")

    print("\n=== Inventory statistics ===")
    most_abundant = max(items.items(), key=lambda x: x[1])
    print(f"Most abundant: {most_abundant[0]} ({most_abundant[1]} units)")
    least_abundant = min(items.items(), key=lambda x: x[1])
    print(f"Least abundant: {least_abundant[0]} ({least_abundant[1]} units)")

    print("\n=== Item Categories ===")
    categorized_items: dict[str, dict[str, int]] = {
        "moderate": {},
        "scarce": {}
    }
    for name, qty in items.items():
        if qty > 4:
            categorized_items["moderate"][name] = qty
        else:
            categorized_items["scarce"][name] = qty
    print("Moderate items:", categorized_items["moderate"])
    print("Scarce items:", categorized_items["scarce"])

    print("\n=== Management Suggestions ===")
    restock_needed = [name for name, qty in items.items() if qty < 2]
    if restock_needed:
        print("Restock needed: ", ", ".join(restock_needed))
    else:
        print("Restock needed: None")

    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys:", ", ".join(inventory.keys()))
    print("Dictionary values:", ", ".join(str(v) for v in inventory.values()))
    print("Sample lookup - 'sword' in inventory:", "sword" in inventory)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("expected arguments. Example: 'sword:1 potion:5'")
    else:
        try:
            inventory: dict[str, int] = parse_items(sys.argv[1::])
            print_inventory(inventory)
        except Exception as e:
            print(f"error parsing argument: {e}")
    pass
