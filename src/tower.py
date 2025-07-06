from src.constants import RING_HIERARCHY


class Tower:
    def __init__(self, rings: list):
        self.rings = rings
        self.top = None if rings == [] else rings[len(rings) - 1]

    def __repr__(self):
        return str([
            RING_HIERARCHY[i]["title"] for i in self.rings
        ]) + f" -> {self.top}"

    def push(self, ring: str):
        self.rings.append(ring)
        self.top = ring

    def pop(self) -> str:
        if self.top is None:
            raise Exception()

        self.top = None if len(
            self.rings) == 1 else self.rings[len(self.rings) - 2]

        return self.rings.pop()


class TowerOrganizer:
    def __init__(self, **towers):
        self.towers = towers

    def get(self, tower_id: str):
        return self.towers[f"tower{tower_id}"]
