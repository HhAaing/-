while True:
    distance = int(input("输入距离  "))
    fix_Size = int(input('目标战车大小修正  '))
    fix_Character = int(input('角色对战车大小修正  '))
    fix_Card = int(input('射击卡牌命中修正  '))
    def Dice():
        Dice = int(input('2d6骰值(输入‘0’可由程序生成一2d6)  '))
        if Dice == 0:
            from random import randint
            Dice1 = randint(1,6)
            Dice2 = randint(1,6)
            print(f'2d6 = {Dice1} + {Dice2} = {Dice1 + Dice2}')
            return Dice1 + Dice2
        else:
            return Dice
    def 击破判定():
        attack = int(input('战车攻击力  '))
        target_side_defend = int(input("目标战车受击侧防御  "))
        fix_character_attack = int(input('角色攻击力修正  '))
        fix_card_attack = int(input('卡牌攻击力修正  '))
        Dice_attack = Dice()
        fix_distance = 0
        if distance == 1:
            fix_distance = 2
        else:
            fix_distance = 1

        fix_attack_sum = fix_distance + fix_character_attack +fix_card_attack

        if attack + fix_attack_sum + Dice_attack> target_side_defend:
            print('目标战车被击破............')
        else:
            print('目标未被击破............')

    Dice_Get = Dice()
    if Dice_Get > distance + fix_Card + fix_Character + fix_Size:
        print('命中............')
        击破判定()

    else:
        print('未命中............')

