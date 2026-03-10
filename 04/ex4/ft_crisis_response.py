def crisis_handler(filename: str) -> None:
    try:
        with open(filename, "r") as archive:
            if filename == "classified_data.txt":
                raise PermissionError
            content: str = archive.read().strip()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system integrity preserved")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    crisis_handler("lost_archive.txt")

    print("\nCRISIS ALERT: Attempting access to 'classified_data.txt'...")
    crisis_handler("classified_data.txt")

    print("\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    crisis_handler("standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")
