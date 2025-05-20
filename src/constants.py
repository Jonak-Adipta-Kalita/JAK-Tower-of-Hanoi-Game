DIMENSIONS = (960, 540)

GRAY_COLOR = (32, 32, 32)
PURPLE_COLOR = (221, 160, 221)
BLUE_COLOR = (100, 149, 237)
PINK_COLOR = (255, 182, 193)
ORANGE_COLOR = (255, 200, 160)

RING_HIERARCHY = {
    0: {
        "tile": "Big",
        "height": DIMENSIONS[1]/10.8,
        "color": ORANGE_COLOR,
        "ring_length": DIMENSIONS[0] / 9.6
    },
    1: {
        "title": "Medium",
        "height": DIMENSIONS[1]/13.5,
        "color": PURPLE_COLOR,
        "ring_length": DIMENSIONS[0] / 12
    },
    2: {
        "title": "Small",
        "height": DIMENSIONS[1]/18,
        "color": BLUE_COLOR,
        "ring_length": DIMENSIONS[0] / 16
    },
    3: {
        "title": "Very Small",
        "height": DIMENSIONS[1]/27,
        "color": PINK_COLOR,
        "ring_length": DIMENSIONS[0] / 24
    }
}
