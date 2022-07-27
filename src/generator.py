from random import randint


def get_pin_code(length: int = 4) -> str:
    pin = []
    for i in range(length):
        pin.append(str(randint(0, 9)))
    return ''.join(pin)


if __name__ == '__main__':
    print(get_pin_code())
    print(get_pin_code(6))
