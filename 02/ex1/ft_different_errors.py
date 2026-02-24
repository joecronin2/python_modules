def garden_operations():

    print("Testing ValueError...")
    try:
        int("abc")  
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing ZeroDivisionError...")
    try:
        water_amount = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing FileNotFoundError...")
    try:
        with open("missing.txt", "r") as f:
            f.read()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing KeyError...")
    try:
        plants = {"rose": 5, "tulip": 10}
        print(plants["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    # 5. Multiple errors in one except block
    print("Testing multiple errors together...")
    try:
        value = int("xyz")   # Could raise ValueError
        result = 10 / value  # Could raise ZeroDivisionError
    except (ValueError, ZeroDivisionError) as e:
        print("Caught an error, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()