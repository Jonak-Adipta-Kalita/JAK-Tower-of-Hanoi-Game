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


tower1 = Tower(["0", "1", "2"])
tower2 = Tower([])
tower3 = Tower([])

organizer = {"1": tower1, "2": tower2, "3": tower3}


def get_operation(operator):
    towers = operator.strip().split("->")
    remove_tower = organizer.get(towers[0])
    add_tower = organizer.get(towers[1])

    popped_ring = remove_tower.pop()
    add_tower.push(popped_ring)


while True:
    try:
        print(f"Tower 1: {tower1.rings}")
        print(f"Tower 2: {tower2.rings}")
        print(f"Tower 3: {tower3.rings}")

        get_operation(str(input(">> ")))
    except Exception:
        print("ばか がいじん")
