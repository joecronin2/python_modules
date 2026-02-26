import time
import random
from typing import Dict, Generator, List


def game_event_stream(n: int) -> Generator[Dict[str, object], None, None]:
    players: List[str] = ["alice", "bob", "charlie"]
    actions: List[str] = ["killed monster", "found treasure", "leveled up"]
    for i in range(1, n + 1):
        player: str = random.choice(players)
        level: int = random.randint(1, 20)
        action: str = random.choice(actions)
        yield {
            "event_id": i,
            "player": player,
            "level": level,
            "action": action,
        }


def process_stream(n: int) -> None:
    high_level_players: int = 0
    treasure_events: int = 0
    level_up_events: int = 0
    print("=== Game Data Stream Processor ===")
    print(f"Processing {n} game events...")
    start_time: float = time.time()
    for event in game_event_stream(n):
        player_level: int = int(str(event["level"]))
        if player_level >= 10:
            high_level_players += 1
        if "treasure" in str(event["action"]):
            treasure_events += 1
        if "leveled up" in str(event["action"]):
            level_up_events += 1
        print(
            f"Event {event['event_id']}: Player "
            f"{event['player']} (level {event['level']}) "
            f"{event['action']}"
        )
    processing_time: float = time.time() - start_time
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {n}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {processing_time:.3f} seconds")


def fibonacci(n: int) -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i: int = 2
    while i <= int(n ** 0.5):
        if n % i == 0:
            return False
        i += 1
    return True


def prime_generator(limit: int) -> Generator[int, None, None]:
    num: int = 2
    count: int = 0
    while count < limit:
        if is_prime(num):
            yield num
            count += 1
        num += 1


if __name__ == "__main__":
    process_stream(1000)
    print("\n=== Generator Demonstration ===")
    print("Fibonacci sequence (first 10):")
    print(", ".join(map(str, fibonacci(10))))
    print("Prime numbers (first 5):")
    print(", ".join(map(str, prime_generator(5))))
