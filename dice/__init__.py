import re
import random
from typing import List

from mojimoji import zen_to_han

# コマンドを分割
def command_splitter (string: str) -> List[str]:
    return re.split('(\w+)', string)[1:-1]

# ダイスを振る
def roll_dice (dice: str) -> List[int]:
    articles, faces = re.split('[d]', dice)

    if articles == '0' or faces == '0':
        return [0]
    
    result = [0] * int(articles)
    for i in range(int(articles)):
        result[i] = random.randint(1, int(faces))

    return result

# コマンド実行
def roll_dices (command: str) -> str:

    elements = command_splitter(zen_to_han(command))

    result = ''
    formula = ''
    for elem in elements:

        if 'd' in elem:
            rolled = roll_dice(elem)

            if rolled == [0]:
                result += '0'
                continue

            result += f'{sum(rolled)}[{", ".join(map(str, rolled))}]'
            formula += f'{sum(rolled)}'

        else:
            result += elem
            formula += elem

    result = re.split('>=|>|<=|<|==', result)[0]
    total = eval(re.split('>=|>|<=|<|==', formula)[0])

    if not len(re.findall('>=|>|<=|<|==', formula)):
        judge = ''

    elif eval(formula):
        judge = ' ＞ 成功'

    else:
        judge = ' ＞ 失敗'
    
    result = f'({command}) ＞ {result} ＞ {str(total)}{judge}'

    return result

def main():
    command = input('command >> ').split()[0]
    result = roll_dices(command)
    print(result)

if __name__ == '__main__':
    mai()
