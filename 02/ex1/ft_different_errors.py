def garden_operations(err: str) -> None:
    if err == "ValueError":
        int("NotAnInt")
    elif err == "ZeroDivisionError":
        print(1 / 0)
    elif err == "FileNotFoundError":
        open("NonExistentFile")
    elif err == "KeyError":
        {"key": "value"}["NonExistentKey"]
    else:
        pass


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    errors: list[str] = [
        "ValueError",
        "ZeroDivisionError",
        "FileNotFoundError",
        "KeyError",
    ]
    for err in errors:
        print(f"Triggering {err}...")
        try:
            garden_operations(err)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, KeyError) as e:
            print(f"Caught {type(e).__name__}")
            print(f"What went wrong: {e}")
        print("Program continues running.\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
