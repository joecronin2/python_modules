import sys


def print_scores(scores: list[int]) -> None:
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("No scores provided.")
        print(f"Usage: python {sys.argv[0]} <score1> <score2>")
    else:
        scores = []
        i = 1
        while i < len(sys.argv):
            try:
                scores.append(int(sys.argv[i]))
                i += 1
            except Exception as e:
                print(f"error converting '{sys.argv[i]}' to an integer: {e}")

        print_scores(scores)
