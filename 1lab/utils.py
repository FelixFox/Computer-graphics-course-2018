"""
L-system sticks:

axiom = X
F -> FF
X -> F[+X]F[-X]+X
angle = 20

"""


class Position:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle


def apply_rules(chr):
    if chr == 'X':
        return 'F[+X]F[-X]+X'
    elif chr == 'F':
        return 'FF'
    else:
        return chr


def process_string(string):
    new_string = ""
    for char in string:
        new_char = apply_rules(char)
        new_string += str(new_char)
    return new_string


def create_lsystem(num_iters=2, axiom='X'):
    start_string = axiom
    end_string = ""

    for i in range(num_iters):
        end_string = process_string(start_string)
        start_string = end_string

    return end_string


if __name__ == '__main__':
    print(create_lsystem())
