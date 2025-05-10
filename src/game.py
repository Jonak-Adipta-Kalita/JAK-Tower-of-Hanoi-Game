from src.tower import Tower, TowerOrganizer


class Game:
    def __init__(self):
        self.towers = [
            Tower([0, 1, 2]), Tower([]), Tower([])
        ]
        self.moves = 0
        self.organizer = TowerOrganizer(
            tower1=self.towers[0],
            tower2=self.towers[1],
            tower3=self.towers[2]
        )

    def perform_operation(self, operation: str):
        towers = operation.strip().split("->")

        remove_tower = self.organizer.get(towers[0])
        add_tower = self.organizer.get(towers[1])

        if remove_tower == add_tower:
            raise Exception()

        if add_tower.top is not None and add_tower.top > remove_tower.top:
            raise Exception()

        self.moves += 1
        popped_ring = remove_tower.pop()
        add_tower.push(popped_ring)

    def print_status(self):
        print(f"Tower 1: {self.towers[0]}")
        print(f"Tower 2: {self.towers[1]}")
        print(f"Tower 3: {self.towers[2]}")

    def did_win(self) -> bool:
        return bool(self.towers[2].rings == [0, 1, 2])
