from ex0.factories import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory):
    base = factory.create_base()
    evolved = factory.create_evolved()

    for creature in (base, evolved):
        print(creature.describe())
        print(creature.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory):
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(c1.describe() + " vs. " + c2.describe())
    print()
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    print("Testing factory")
    test_factory(FlameFactory())

    print("\nTesting factory")
    test_factory(AquaFactory())

    print("\nTesting battle")
    battle(FlameFactory(), AquaFactory())
