from random import randint as rand
from typing import Optional


class Predator:
    skill: int
    eaten: bool

    def __init__(self, skill: int):
        self.skill = skill
        self.eaten = True

    def get_children(self) -> list["Predator"]:
        return [Predator(self.skill + 1), Predator(self.skill - 1)]

    def __repr__(self) -> str:
        return f"{str(self.skill)} {str(self.eaten)}"


class Prey:
    skill: int

    def __init__(self, skill: int):
        self.skill = skill

    def get_children(self) -> list["Prey"]:
        return [Prey(self.skill + 1), Prey(self.skill - 1)]

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
            self.predators += best_predator.get_children()
            self.prey.remove(best_prey)
            self.predators.remove(best_predator)

        self.prey = [prey.get_children() for prey in self.prey]
        self.prey = [item for sublist in self.prey for item in sublist]

    def __repr__(self) -> str:
        return f"[Predators: {str(self.predators)}, Prey: {str(self.prey)}]"


class Simulation:
    size: int
    round: int
    board: list[Square]
    distribution: list[tuple[int, int]]

    def __init__(self, size: int, distribution: list[tuple[int, int]]):
        self.board = [Square() for _ in range(size)]
        self.size = size
        self.round = 0
        self.distribution = distribution

        self.populate()

    def random_square(self) -> Square:
        return self.board[rand(0, self.size - 1)]

    def populate(self):
        for skill, amount in self.distribution:
            for _ in range(amount):
                self.random_square().predators.append(Predator(skill))
                self.random_square().prey.append(Prey(skill))

    def shuffle(self):
        all_predators: list[Predator] = []
        all_prey: list[Prey] = []

        for square in self.board:
            all_predators += square.predators
            all_prey += square.prey
            square.predators = []
            square.prey = []

        for predator in all_predators:
            self.random_square().predators.append(predator)
        for prey in all_prey:
            self.random_square().prey.append(prey)

    def get_stats(self) -> str:
        predator_count = 0
        prey_count = 0
        for square in self.board:
            predator_count += len(square.predators)
            prey_count += len(square.prey)
        return f"Predators: {str(predator_count)} | Prey: {str(prey_count)}"

    def simulate(self):
        print(f"Before round {self.round}: {self.get_stats()}")
        for square in self.board:
            square.simulate()
        print(f"After round {self.round}: {self.get_stats()}")
        self.shuffle()
        self.round += 1

    def __repr__(self) -> str:
        return str(self.board)


def main():
    distribution = [(2, 1), (3, 2), (4, 3), (5, 4), (6, 3), (7, 2), (8, 1)]
    sim = Simulation(25, distribution)
    for _ in range(100):
        sim.simulate()


main()
