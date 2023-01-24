"""
recursive function
"""


def func1(value):
    if value < 1:
        return

    func2(value - 1)

    print(f"value={value}")


def func2(value):
    func1(value)

func1(3)