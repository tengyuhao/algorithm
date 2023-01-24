
def move(source, target):  #?
    pass


def hanoi(n, source, target, auxiliary):
    if n == 1:
        move(source, target)
        return
    hanoi(n-1, source, auxiliary, target)
    move(source, target)
    hanoi(n-1, auxiliary, target, source)
