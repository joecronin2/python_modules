if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    try:
        with open("classified_data.txt", "r") as vault:
            print("Vault connection established with failsafe protocols")
            print("SECURE EXTRACTION:")
            for line in vault:
                print(line.strip())
    except FileNotFoundError:
        print("ERROR: Classified vault not found.")
    with open("security_protocols.txt", "w") as secure_vault:
        print("SECURE PRESERVATION:")
        secure_vault.write("[CLASSIFIED] New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security")
