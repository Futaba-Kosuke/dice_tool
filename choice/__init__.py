import re
import random
from typing import List

from mojimoji import zen_to_han

def choice(command: str) -> str:
    if not command[:6] in ['choice', 'CHOICE']:
        raise Exception('this is not "choice".')

    elements = [_.strip().strip('[]') for _ in command[6:].split(',')]

    return random.choice(elements)

def main():
    command = input('command >> ')
    result = choice(command)
    print(result)

if __name__ == '__main__':
    main()
