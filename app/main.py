from typing import List


class Animal:
    alive: List["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False,
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )

    @classmethod
    def alive_repr(cls) -> str:
        return "[" + ", ".join(repr(animal) for animal in cls.alive) + "]"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, herbi: Herbivore) -> None:
        if not isinstance(herbi, Herbivore) or herbi.hidden:
            return
        herbi.health = max(herbi.health - 50, 0)
        if herbi.health == 0:
            if herbi in Animal.alive:
                Animal.alive.remove(herbi)
