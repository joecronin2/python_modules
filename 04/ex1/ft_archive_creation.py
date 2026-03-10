if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    filename: str = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")
    entries: list[str] = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    try:
        with open(filename, "x") as f:
            print("Storage unit created successfully...")
            print("Inscribing preservation data...")
            for entry in entries:
                f.write(entry + "\n")
                print(entry)
            print("Data inscription complete. Storage unit sealed.")
            print(f"Archive '{filename}' ready for long-term preservation.")
    except FileExistsError:
        print("ERROR: Storage unit already exists. Creation aborted.")
