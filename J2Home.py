import random
import time

def cards_init():
    source_cards = [ ['3',4],['4',4],['5',4],['6',4],['7',4],['8',4],['9',4],['10',4],['J',4],['Q',4],['K',4],['A',4],['2',4]] #除去大小王的扑克牌
    player_1 = []   #抓牌前玩家palyer_1手牌
    player_2 = []   #抓牌前玩家palyer_2手牌
    indexs = [ i for i in range(52) ]   #对52张牌进行索引
    index_player_1 = []  #玩家palyer_1手牌索引
    index_player_2 = []  #玩家palyer_1手牌索引
    for i in range(26):
        index = random.choice(indexs)   #为玩家player_1随机分配扑克牌
        index_player_1.append( index )  #为玩家player_1随机分配扑克牌
        indexs.remove(index)            #牌已经被抓走，则在底牌中删除这张牌

        index = random.choice(indexs)
        index_player_2.append(index)
        indexs.remove(index)

    for i in index_player_1:   #将分配到的牌放到手里
        player_1.append( source_cards[ i//4 ][0] )

    for i in index_player_2:
        player_2.append( source_cards[ i//4 ][0] )

    return player_1, player_2

player_1, player_2 = cards_init()  #游戏的初始化
print(player_1)
print(player_2)
lover = input('希望谁为获胜者？player1 or player2 or impartial: ')    #加了一个玩赖的设置
if lover=='player1':
    while 'J' in player_2:
        player_2.remove('J')

if lover=='player2':
    while 'J' in player_1:
        player_1.remove('J')
print(player_1)
print(player_2)

land_cards = []    #打出的扑克牌
is_end = False     #游戏是否结束的标志




'''
push_card(players)是游戏的逻辑设置，使用了递归。如果玩家的底牌数量为零，则游戏结束；如果出的牌在底牌中不存在并且不是J，则下一个玩家出牌；如果出的牌在底牌中存在，
则将出的牌和相同的牌之间的所有牌归为自己，再重新出牌；如果出的牌为J,则将所有的底牌都归为自己。
'''
def push_card(players):
    if len(players)<5:  #检测玩家是否还有底牌
        print('game over')
        is_end=True      #将游戏的结束标志设置为True
        return -1

    temp_card = players[0]    #获得玩家的出牌信息

    if temp_card not in land_cards and temp_card != 'J':    #出的牌再底牌中不存在，并且不是J
        print('玩家手牌为：', players)
        print('底牌为：', land_cards)
        print('出牌为：', temp_card)
        print('不能收牌')
        print()
        time.sleep(1)
        land_cards.append(temp_card)    #将玩家的出牌追加到底牌的末尾
        del players[0]    #在玩家手牌中删除已经出过的牌
        return -2
    elif temp_card in land_cards:    #出的牌在底牌中存在
        print('玩家手牌为：', players)
        print('底牌为：', land_cards)
        print('出牌为：', temp_card)
        print('收牌')
        time.sleep(1)
        cut = land_cards[land_cards.index(temp_card):]    #截取底牌中与玩家出牌相同的纸牌之间的所有纸牌
        for i in range( land_cards.index(temp_card), len(land_cards) ):    #将截取后的牌在底牌中删除
            del land_cards[-1]
        players.extend(cut)    #将截取到的纸牌追加到玩家手牌的末尾
        players.append(temp_card)  #将玩家打出的纸牌收归到末尾
        del players[0]    #删除刚刚出手的纸牌
        print('收牌后为：',players)
        print()
        push_card(players)    #递归调用
    elif temp_card=='J':    #如果玩家的出牌为J
        print('玩家手牌为：', players)
        print('J来家')
        print('底牌为：', land_cards)
        print('出牌为：', temp_card)
        time.sleep(1)
        players.extend(land_cards)    #将所有底牌收回来
        players.append(temp_card)
        for i in range(len(land_cards)):    #将底牌列表中的所有牌删除
            del land_cards[-1]
        del players[0]
        print('收牌后为：', players)
        print()
        push_card(players)

while not is_end:    #游戏循环
    push_card(player_1)
    push_card(player_2)
























