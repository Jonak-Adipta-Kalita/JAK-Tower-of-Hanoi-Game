import math


def section_formula(A, B, m, n):
    return (m * B + n * A) / (m + n)


def distance_formula(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])
