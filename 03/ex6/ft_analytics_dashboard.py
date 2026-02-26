if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    players: dict[str, int] = {
        "alice": 2300,
        "bob": 1800,
        "charlie": 2150,
        "diana": 2100,
    }
    achievements: dict[str, int] = {
        "alice": 5,
        "bob": 3,
        "charlie": 7,
        "diana": 2,
    }
    regions: list[str] = ["north", "east", "central", "north", "east"]

    print("=== List Comprehension Examples ===")
    high_scorers: list[str] = [
        name for name, score in players.items() if score > 2000
    ]
    scores_doubled: list[int] = [score * 2 for score in players.values()]
    active_players: list[str] = [name for name in players.keys()]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")
    print("=== Dict Comprehension Examples ===")
    player_scores: dict[str, int] = {
        name: score for name, score in players.items()
    }
    score_categories: dict[str, int] = {
        "high": sum(1 for s in players.values() if s > 2200),
        "medium": sum(1 for s in players.values() if 2000 >= s > 1900),
        "low": sum(1 for s in players.values() if s <= 1900),
    }
    achievement_counts: dict[str, int] = {
        name: count for name, count in achievements.items()
    }
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    print("=== Set Comprehension Examples ===")
    unique_players: set[str] = {name for name in players.keys()}
    unique_achievements: set[str] = {
        "first_kill",
        "level_10",
        "boss_slayer",
    }
    active_regions: set[str] = {region for region in regions}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")

    print("=== Combined Analysis ===")
    total_players: int = len(players)
    total_unique_achievements: int = len(unique_achievements)
    average_score: float = sum(players.values()) / total_players
    top_performer: tuple[str, int] = max(
        players.items(), key=lambda x: x[1]
    )
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.1f}")
    print(
        f"Top performer: {top_performer[0]} "
        f"({top_performer[1]} points, "
        f"{achievements.get(top_performer[0], 0)} achievements)"
    )
