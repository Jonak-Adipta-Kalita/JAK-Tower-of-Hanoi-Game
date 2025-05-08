class Tower:
    def __init__(self, rings: list):
        self.rings = rings
        self.top = None if rings == [] else len(rings)

    def push(self, ring: str):
        self.rings.append(ring)
        self.top = 0 if self.top is None else self.top + 1

    def pop(self) -> str:
        if self.top is None:
            raise Exception()

        self.top = None if self.top == 0 else self.top - 1

        return self.rings.pop()


class Organizer:
    def __init__(self, **towers):
        self.towers = towers

    def get(self, tower_id: str):
        return self.towers[f"tower{tower_id}"]
