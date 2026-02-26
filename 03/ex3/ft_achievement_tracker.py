if __name__ == "__main__":
    alice_achievements: set[str] = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
    }

    bob_achievements: set[str] = {
        "first_kill",
        "level_10",
        "boss_slayer",
        "collector",
    }

    charlie_achievements: set[str] = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }

    all_achievements: set[str] = (
        alice_achievements | bob_achievements | charlie_achievements
    )
    common_achievements: set[str] = (
        alice_achievements & bob_achievements & charlie_achievements
    )
    rare_achievements = (
        all_achievements
        - (
            (alice_achievements & bob_achievements)
            | (alice_achievements & charlie_achievements)
            | (bob_achievements & charlie_achievements)
        )
    )

    alice_unique = alice_achievements - (
        bob_achievements | charlie_achievements
    )
    bob_unique = bob_achievements - (
        alice_achievements | charlie_achievements
    )
    charlie_unique = charlie_achievements - (
        alice_achievements | bob_achievements
    )

    print(f"Player alice achievements: {alice_achievements}")
    print(f"Player bob achievements: {bob_achievements}")
    print(f"Player charlie achievements: {charlie_achievements}")
    print(f"All unique achievements: {all_achievements}")
    print(f"Common to all players: {common_achievements}")
    print(f"Rare achievements (1 player): {rare_achievements}")
    print(f"Alice vs Bob common: {alice_achievements & bob_achievements}")
    print(f"Alice unique: {alice_unique if alice_unique else "{}"}")
    print(f"Bob unique: {bob_unique}")
    print(f"Charlie unique: {charlie_unique}")
