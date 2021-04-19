from choice import choice
from dice import roll_dices

def exec_command (command: str) -> str:

    if command[:6] in ['choice', 'CHOICE']:
        result = choice(command)

    else:
        result = roll_dices(command)

    return result
 
def main () -> None:

    command = input()
    
    result = exec_command(command=command)

    print(result)

    return

if __name__ == '__main__':

    main()
