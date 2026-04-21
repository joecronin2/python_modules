from ex0.factories import FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from typing import List, Tuple


def run_tournament(opponents: List[Tuple[object, object]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i, (fac_i, strat_i) in enumerate(opponents):
        for j, (fac_j, strat_j) in enumerate(opponents):
            if i >= j:
                continue
            print("* Battle *")
            c1 = fac_i.create_base()
            c2 = fac_j.create_base()
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            try:
                # act with first creature's strategy
                for msg in strat_i.act(c1):
                    print(msg)

                # act with second creature's strategy
                for msg in strat_j.act(c2):
                    print(msg)
            except Exception as exc:
                print(f"Battle error, aborting tournament: {exc}")
                return


if __name__ == "__main__":
    # Tournament 0 (basic)
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    print("*** Tournament ***")
    run_tournament([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    # Tournament 1 (error)
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    print("*** Tournament ***")
    run_tournament([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])

    # Tournament 2 (multiple)
    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    print("*** Tournament ***")
    run_tournament([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])
