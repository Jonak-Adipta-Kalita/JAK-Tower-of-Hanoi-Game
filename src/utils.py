organizer = {"1": tower1, "2": tower2, "3": tower3}


def get_operation(operator):
    towers = operator.strip().split("->")
    remove_tower = organizer.get(towers[0])
    add_tower = organizer.get(towers[1])

    popped_ring = remove_tower.pop()
    add_tower.push(popped_ring)
