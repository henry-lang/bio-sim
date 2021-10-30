from random import randint as rand
from typing import Optional


class Predator:
    skill: int
    eaten: bool

    def __init__(self, skill: int):
        self.skill = skill
        self.eaten = True

    def __repr__(self) -> str:
        return f"{str(self.skill)} {str(self.eaten)}"


class Prey:
    skill: int

    def __init__(self, skill: int):
        self.skill = skill

    def __repr__(self) -> str:
        return str(self.skill)


class Square:
    predators: list[Predator]
    prey: list[Prey]

    def __init__(self):
        self.predators = []
        self.prey = []

    def find_best_predator(self) -> Optional[Predator]:
        best_predator: Optional[Predator] = None

        for predator in self.predators:
            if not best_predator or predator.skill > best_predator.skill:
                best_predator = predator

        return best_predator

    def find_best_prey(self, predator: Predator) -> Optional[Prey]:
        best_prey: Optional[Prey] = None

        for prey in self.prey:
            if not best_prey or prey.skill < best_prey.skill:
                best_prey = prey

        if not best_prey:
            return None

        if best_prey.skill < predator.skill:
            return best_prey
        elif best_prey.skill == predator.skill:
            return best_prey if rand(0, 1) == 1 else None

        return None

    def simulate(self):
        while (best_predator := self.find_best_predator()) and (best_prey := self.find_best_prey(best_predator)):
            print(f"{best_predator} eats {best_predator}")
            self.predators.append(Predator(best_predator.skill - 1))
            self.predators.append(Predator(best_predator.skill + 1))
            self.prey.remove(best_prey)
            self.predators.remove(best_predator)

    def __repr__(self) -> str:
        return f"[Predators: {str(self.predators)}, Prey: {str(self.prey)}]"


class Simulation:
    size: int
    board: list[Square]
    distribution: list[tuple[int, int]]

    def __init__(self, size: int, distribution: list[tuple[int, int]]):
        self.board = [Square() for _ in range(size)]
        self.size = size
        self.distribution = distribution

        self.populate()

    def random_square(self) -> Square:
        return self.board[rand(0, self.size - 1)]

    def populate(self):
        for skill, amount in self.distribution:
            for _ in range(amount):
                self.random_square().predators.append(Predator(skill))
                self.random_square().prey.append(Prey(skill))

    def simulate(self):
        for square in self.board:
            square.simulate()

    def __repr__(self) -> str:
        return str(self.board)


def main():
    distribution = [(2, 1), (3, 2), (4, 3), (5, 4), (6, 3), (7, 2), (8, 1)]
    sim = Simulation(25, distribution)
    print(sim)
    sim.simulate()
    print(sim)


main()
