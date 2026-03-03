if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    filename: str = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")
    try:
        with open(filename, "r") as f:
            print("Connection established...")
            print("RECOVERED DATA:")
            print(f.read())
            print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
