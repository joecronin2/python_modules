from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda t, p: (spell1(t, p), spell2(t, p))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda t, p: base_spell(t, p * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda t, p: spell(t, p) if condition(t, p) else "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    return lambda t, p: [spell(t, p) for spell in spells]


if __name__ == "__main__":

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 50)
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    boosted_fireball = power_amplifier(fireball, 3)
    print("Original: 10, Amplified: "
          f"{boosted_fireball('Slime', 10).split()[-2]}")

    print("\nTesting conditional caster...")

    def is_strong(target, power):
        return power > 20
    guarded_spell = conditional_caster(is_strong, fireball)
    print(f"Power 25: {guarded_spell('Wolf', 25)}")
    print(f"Power 15: {guarded_spell('Wolf', 15)}")

    print("\nTesting spell sequence...")
    spell_list = [fireball, heal, fireball]
    sequence_caster = spell_sequence(spell_list)

    results = sequence_caster("Goblin", 15)
    for i, res in enumerate(results, 1):
        print(f"Spell {i}: {res}")
