from random import randint


def get_pin_code(length: int) -> str:
    return ''.join((str(randint(0, 9)) for x in range(length)))


if __name__ == '__main__':
    print(get_pin_code(8))
