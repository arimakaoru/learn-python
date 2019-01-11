'''
じゃんけん
'''

import random

print("--------------------じゃんけん--------------------")
hand = {'1':"グー", '2':"チョキ", '3':"パー"}
while True:
    player = input("\nグー：1, チョキ：2, パー：3, やめる：q => ")
    if player == 'q':
        judge = "終了"
        break
    elif (player in hand) == False:
        print("無効な入力です")
        continue
    else:
        cpu = random.choice(list(hand.keys()))
        if player == cpu:
            judge = "あいこでしょっ！"
        elif ((player == '1' and cpu == '2') or
              (player == '2' and cpu == '3') or
              (player == '3' and cpu == '1')):
            judge = "勝ち！"
        else:
            judge = "負け！"
        print("あなた：%s　相手：%s\n%s" %(hand[player], hand[cpu], judge))
