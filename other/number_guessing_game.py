'''
数当てゲーム
'''

import random

print('''
数当てゲーム
ランダムで決められる１〜１００までの数字を当ててください。
０を入力すると終了します。''')

right_number = random.randint(1,100)

while True:
    input_number = int(input("数字を入力："))
    if input_number == 0:
        print("終了")
        break
    elif input_number == right_number:
        print("正解！")
        break
    elif input_number < right_number:
        print("%sより大きい" %input_number)
    else:
        print("%sより小さい" %input_number)
