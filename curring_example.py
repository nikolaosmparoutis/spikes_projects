def change(b, c):
    return b(c(x))

def b(time):
    """ Function that converts days to hours. """
    return 'as'


def c(time):
    """ Function that converts minutes to seconds. """
    return 'b'


if __name__ == '__main__':
    transform = change(minutestoseconds, daystohour)
    e = transform(10)
    print(e)