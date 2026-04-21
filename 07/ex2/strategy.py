from abc import ABC, abstractmethod
from typing import Any, List


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Any) -> List[str]:
        """Return a list of messages produced by performing the strategy on the creature.
        Raise ValueError on invalid combination.
        """


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return True

    def act(self, creature: Any) -> List[str]:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{getattr(creature, 'name', repr(creature))}' for this normal strategy")
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")

    def act(self, creature: Any) -> List[str]:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{getattr(creature, 'name', repr(creature))}' for this aggressive strategy")
        msgs: List[str] = []
        msgs.append(creature.transform())
        msgs.append(creature.attack())
        msgs.append(creature.revert())
        return msgs


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature: Any) -> List[str]:
        if not self.is_valid(creature):
            raise ValueError(f"Invalid Creature '{getattr(creature, 'name', repr(creature))}' for this defensive strategy")
        msgs: List[str] = []
        msgs.append(creature.attack())
        msgs.append(creature.heal())
        return msgs
