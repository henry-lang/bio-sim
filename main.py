from random import randint as rand


class Prey:
    skill: int

    def __init__(self, skill: int):
        self.skill = skill

    def __repr__(self) -> str:
        return str(self.skill)


class Predator:
    skill: int
    eaten: bool

    def __init__(self, skill: int):
        self.skill = skill
        self.eaten = False

    def __repr__(self) -> str:
        return f"{str(self.skill)} {str(self.eaten)}"


class Square:
    prey: list[Prey]
    predators: list[Predator]

    def __init__(self):
        self.prey = []
        self.predators = []

    def __repr__(self) -> str:
        return f"[Prey: {str(self.prey)}, Predators: {str(self.predators)}]"


class Simulation:
    size: int
    board: list[Square]

    def __init__(self, size, initial_count):
        self.board = [Square() for _ in range(size)]
        self.size = size
        for _ in range(initial_count):
            self.spawn_prey()
            self.spawn_predator()

    def random_square(self) -> Square:
        return self.board[rand(0, self.size - 1)]

    def spawn_prey(self):
        square = self.random_square()
        square.prey.append(Prey(5))

    def spawn_predator(self):
        square = self.random_square()
        square.predators.append(Predator(5))

    def simulate():
        pass


def main():
    sim = Simulation(5, 25)
    print(sim.board)


main()
