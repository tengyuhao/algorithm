"""
recursive function
"""


def func(value):
    if value < 1:
        return

    func(value - 1)

    print(f"value={value}")



func(3)