def check_temperature(temp_str: str):
    try:
        n = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid integer")
        return None
    if not 0 <= n <= 40:
        print("Error: Temperature must be between 0°C and 40°C")
        return None
    return n


def test_temperature_input():
    print(f"Should be 25: {check_temperature("25")}")
    print(f"Should be None: {check_temperature("abc")}")
    print(f"Should be None: {check_temperature("100")}")
    print(f"Should be None: {check_temperature("-50")}")


if __name__ == "__main__":
    test_temperature_input()
