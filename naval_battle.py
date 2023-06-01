import os
import random

def auto_deck(massive):
    for a in range (11):
        for b in range (11):
            massive[a][b]="▢"

    for a in range (0, 10):
        massive[0][a+1]=a
        massive[a+1][0]=a
    return massive

def print_mas(massive):
    for i in range(11):
        for j in range (11):
          print (massive[i][j], end = " ")
        print ("\n", end = "")

def print_full(massive, massive_1, player):
    print(f"Доска {player}")
    for i in range(11):
        for j in range (11):
          print (massive[i][j], end = " ")
        print ("           ", end = " " )
        for k in range (11):
            print(massive_1[i][k], end = " " )
        print ("\n", end = "")

def shot (mas_def):
    while (True):
        a = int(input("Координата по горизонтали: "))
        b = int(input("Координата по вертикали: "))
        if mas_def[a+1][b+1]!= "■" and mas_def[a+1][b+1]!= "▣" and 0<=a<11 and 0<=b<11:
            return (a+1, b+1)
        else:
            print("Неправильные координаты. Повтор ввода. Нажмите Enter")

def shot_auto(mas_def):
    while(True):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        if mas_def[a+1][b+1]!= "■" and mas_def[a+1][b+1]!= "▣":
            return (a+1, b+1)

def paint_vertical(d1, d2, l, massive):
    for i in range(d1, d2+1):
        massive[i+1][l] = "◆"
        if 0<l+1<11:
            massive[i+1][l+1] = "▩"
        if 0<l-1<11:
            massive[i+1][l-1] = "▩"
        if 0<d2+2<11:
            for j in range (l-1, l+2):
                if 0<j<11: 
                    massive[d2+2][j] = "▩"
        if 0<d1<11:
            for j in range (l-1, l+2):
                if 0<j<11: 
                    massive[d1][j] = "▩"
    return massive

def paint_horizontal(d1, d2, l, massive):
    for i in range(d1, d2+1):
        massive[l][i+1] = "◆"
        if 0<l+1<11: 
            massive[l+1][i+1] = "▩"
        if 0<l-1<11:
            massive[l-1][i+1] = "▩"
        if 0<d2+2<11:
            for j in range (l-1, l+2):
                if 0<j<11: 
                    massive[j][d2+2] = "▩"
        if 0<d1<11:
            for j in range (l-1, l+2):
                if 0<j<11: 
                    massive[j][d1] = "▩"
    return massive

def build_4(massive):
    while(True):
        print_mas(massive)
        print("ПОСТРОЙКА ЛИНКОРА (4 КЛЕТКИ)")
        line = int(input("Введите как повёрнут будет корабль(вертикально - 1 или горизонтально - 2): "))
        diapazon1 = int(input("Введите нижнюю границу диапазона: "))
        diapazon2 = int(input("Введите верхнюю границу диапазона: "))
        l = int(input("Введите линию, на которой будет располагатся корабль: "))
        l+=1
        if 0 <= l < 11 and 0 <= diapazon1 < 10 and 0<= diapazon2 < 10 and diapazon2 - diapazon1 == 3:
            if line == 1:
                massive = paint_vertical(diapazon1, diapazon2, l, massive)
            else: 
                massive = paint_horizontal(diapazon1, diapazon2, l, massive)
            return massive
        else: 
            print("Неправильные координаты. Повтор ввода. Нажмите Enter")
            input()
            os.system('cls')

def build_4_auto(massive):
    while (True):
        line = random.randint(1, 2)
        diapazon1 = random.randint(0, 6)
        diapazon2 = diapazon1+3
        l = random.randint(0, 9)
        l+=1
        if line == 1:
            massive = paint_vertical(diapazon1, diapazon2, l, massive)
        else: 
            massive = paint_horizontal(diapazon1, diapazon2, l, massive)
        return massive
        
def build_3(massive):  
    while(True):
        os.system('cls')
        print_mas(massive)
        print("ПОСТРОЙКА КРЕЙСЕРА (3 КЛЕТКИ)")
        line = int(input("Введите как повёрнут будет корабль(вертикально - 1 или горизонтально - 2): "))
        diapazon1 = int(input("Введите нижнюю границу диапазона: "))
        diapazon2 = int(input("Введите верхнюю границу диапазона: "))
        l = int(input("Введите линию, на которой будет располагатся корабль: "))
        l+=1
        if 0 <= l < 11 and 0 <= diapazon1 < 10 and 0<= diapazon2 < 10 and diapazon2 - diapazon1 == 2:
            if line == 1:
                if massive[diapazon1+1][l]!="▩" and massive[diapazon2+1][l]!="▩" and massive[diapazon1+1][l]!="◆" and massive[diapazon2+1][l]!="◆":
                    massive = paint_vertical(diapazon1, diapazon2, l, massive)  
                    return massive
                else: 
                    print("Неправильные координаты. Повтор ввода. Нажмите Enter")
                    input()
            else: 
                if massive[l][diapazon1+1]!="▩" and massive[l][diapazon2+1]!="▩" and massive[l][diapazon1+1]!="◆" and massive[l][diapazon2+1]!="◆":
                    massive = paint_horizontal(diapazon1, diapazon2, l, massive)
                    return massive
                else:
                    print("Неправильные координаты. Повтор ввода. Нажмите Enter")
                    input()
        else: 
            print("Неправильные координаты. Повтор ввода. Нажмите Enter")
            input()

def build_3_auto(massive):  
    while(True):
        line = random.randint(1, 2)
        diapazon1 = random.randint(0, 7)
        diapazon2 = diapazon1+2
        l = random.randint(0, 9)
        l+=1
        if line == 1:
            if massive[diapazon1+1][l]!="▩" and massive[diapazon2+1][l]!="▩" and massive[diapazon1+1][l]!="◆" and massive[diapazon2+1][l]!="◆":
                massive = paint_vertical(diapazon1, diapazon2, l, massive)  
                return massive
        else: 
            if massive[l][diapazon1+1]!="▩" and massive[l][diapazon2+1]!="▩" and massive[l][diapazon1+1]!="◆" and massive[l][diapazon2+1]!="◆":
                massive = paint_horizontal(diapazon1, diapazon2, l, massive)
                return massive

def build_2(massive): 
    while(True):
        os.system('cls')
        print_mas(massive)
        print("ПОСТРОЙКА ЭСМИНЦА (2 КЛЕТКИ)")
        line = int(input("Введите как повёрнут будет корабль(вертикально - 1 или горизонтально - 2): "))
        diapazon1 = int(input("Введите нижнюю границу диапазона: "))
        diapazon2 = int(input("Введите верхнюю границу диапазона: "))
        l = int(input("Введите линию, на которой будет располагатся корабль: "))
        l+=1
        if 0 <= l < 11 and 0 <= diapazon1 < 11 and 0<= diapazon2 < 11 and diapazon2 - diapazon1 == 1:
            if line == 1:
                if massive[diapazon1+1][l]!="▩" and massive[diapazon2+1][l]!="▩" and massive[diapazon1+1][l]!="◆" and massive[diapazon2+1][l]!="◆":
                    massive = paint_vertical(diapazon1, diapazon2, l, massive)    
                    return massive
                else: 
                    print("Неправильные координаты. Повтор ввода. Нажмите Enter")
                    input()
            else: 
                if massive[l][diapazon1+1]!="▩" and massive[l][diapazon2+1]!="▩" and massive[l][diapazon1+1]!="◆" and massive[l][diapazon2+1]!="◆":
                    massive = paint_horizontal(diapazon1, diapazon2, l, massive)
                    return massive
                else:
                    print("Неправильные координаты. Повтор ввода. Нажмите Enter")
                    input()
        else: 
            print("Неправильные координаты. Повтор ввода. Нажмите Enter")
            input()

def build_2_auto(massive):  
    while(True):
        line = random.randint(1, 2)
        diapazon1 = random.randint(0, 8)
        diapazon2 = diapazon1+1
        l = random.randint(0, 9)
        l+=1
        if line == 1:
            if massive[diapazon1+1][l]!="▩" and massive[diapazon2+1][l]!="▩" and massive[diapazon1+1][l]!="◆" and massive[diapazon2+1][l]!="◆":
                massive = paint_vertical(diapazon1, diapazon2, l, massive)    
                return massive
        else: 
            if massive[l][diapazon1+1]!="▩" and massive[l][diapazon2+1]!="▩" and massive[l][diapazon1+1]!="◆" and massive[l][diapazon2+1]!="◆":
                massive = paint_horizontal(diapazon1, diapazon2, l, massive)
                return massive

def build_1(massive): 
    while(True):
        os.system('cls')
        print_mas(massive)
        print("ПОСТРОЙКА ФРЕГАТА (1 КЛЕТКА)")
        a1 = int(input("Введите координаты по горизонту: "))
        b1 = int(input("Введите координаты по вертикали: "))
        if 0<=a1<10 and 0<=b1<10 and massive[a1+1][b1+1]!="▩" and massive[a1+1][b1+1]!="◆":
            for i in range (a1, a1+3):
                for j in range(b1, b1+3):
                    if 0<i<11 and 0<j<11:
                        massive[i][j]="▩"
            massive[a1+1][b1+1]="◆"
            return massive
        else: 
            print("Неправильные координаты. Повтор ввода. Нажмите Enter")
            input()

def build_1_auto(massive): 
    while(True):
        a1 = random.randint(0, 9)
        b1 = random.randint(0, 9)
        if massive[a1+1][b1+1]!="▩" and massive[a1+1][b1+1]!="◆":
            for i in range (a1, a1+3):
                for j in range(b1, b1+3):
                    if 0<i<11 and 0<j<11:
                        massive[i][j]="▩"
            massive[a1+1][b1+1]="◆"
            return massive

def build_deck(massive):
    os.system('cls')
    print("Время строить Линкор, нажмите Enter")
    input()
    os.system('cls')
    massive = build_4(massive)
    os.system('cls')
    print("Время строить 2 Крейсера, нажмите Enter")
    print_mas(massive)
    input()
    os.system('cls')
    for i in range (2):
        massive = build_3(massive)
    os.system('cls')
    print("Время строить 3 Эсминца, нажмите Enter")
    print_mas(massive)
    input()
    os.system('cls')
    for i in range (3):
        massive = build_2(massive)
    os.system('cls')
    print("Время строить 4 Фрегата, нажмите Enter")
    print_mas(massive)
    input()
    os.system('cls')
    for i in range (4):
        massive = build_1(massive)
    return massive

def build_deck_auto(massive):
    massive = build_4_auto(massive)
    for i in range (2):
        massive = build_3_auto(massive)
    for i in range (3):
        massive = build_2_auto(massive)
    for i in range (4):
        massive = build_1_auto(massive)
    return massive

while (True):
    print("--МОРСКОЙ БОЙ МЕНЮ--")
    print ("1. PVP режим\n2. PVA режим\n3. Авторы\n0. Выход")
    choise = int(input("Выбранный пункт: "))
    if choise == 1:
        os.system('cls')
        player_1_ships = [[0 for j in range(11)] for i in range(11)]
        player_1_attempts = [[0 for j in range(11)] for i in range(11)]
        player_2_ships = [[0 for j in range(11)] for i in range(11)]
        player_2_attempts = [[0 for j in range(11)] for i in range(11)]
        hp1 = 20
        hp2 = 20
        player_1_ships = auto_deck(player_1_ships)         
        player_1_attempts = auto_deck(player_1_attempts)
        player_2_ships = auto_deck(player_2_ships)
        player_2_attempts = auto_deck(player_2_attempts)

        player_1 = input("Первый игрок введите имя: ")
        player_1_ships = build_deck(player_1_ships)
        os.system('cls')
        player_2 = input("Второй игрок введите имя:")
        player_2_ships = build_deck(player_2_ships)
        print(f"{player_1} и {player_2}, если вы готовы, нажмите Enter")
        input()
        os.system('cls')
        while(hp2 > 0 and hp1 > 0):
            print(f"Игрок {player_1}, вы готовы? Нажмите Enter")
            input()
            os.system('cls')
            while (True):
                print_full(player_1_ships, player_1_attempts, player_1)
                a, b = shot(player_2_ships)
                if player_2_ships[a][b] == "▩" or player_2_ships[a][b] == "▢":
                    player_2_ships[a][b] = "■"
                    player_1_attempts[a][b] = "■"
                    print ("Промах! Нажмите Enter что бы продолжить.")
                    input()
                    os.system('cls')
                    break
                else:
                    player_2_ships[a][b] = "▣"
                    player_1_attempts[a][b] = "▣"
                    hp2-=1
                    print ("Попадание! Нажмите Enter что бы продолжить.")
                    input()
                    os.system('cls')
                if hp2 == 0: 
                    break
            print(f"Игрок {player_2}, вы готовы? Нажмите Enter")
            input()
            os.system('cls')
            while (True):
                print_full(player_2_ships, player_2_attempts, player_2)
                a, b = shot(player_1_ships)
                if player_1_ships[a][b] == "▩" or player_1_ships[a][b] == "▢":
                    player_1_ships[a][b] = "■"
                    player_2_attempts[a][b] = "■"
                    print ("Промах! Нажмите Enter что бы продолжить.")
                    input()
                    os.system('cls')
                    break
                else:
                    player_1_ships[a][b] = "▣"
                    player_2_attempts[a][b] = "▣"
                    hp2-=1
                    print ("Попадание! Нажмите Enter что бы продолжить.")
                    input()
                    os.system('cls')
                if hp1 == 0: 
                    break
        if hp2 == 0:
            print (f"{player_1} выиграл! Нажмите Enter что бы выйти в меню.")
        else :
            print (f"{player_2} выиграл! Нажмите Enter что бы выйти в меню.")
        input()
        os.system('cls')
    if choise == 2:
        os.system('cls')
        player_1_ships = [[0 for j in range(11)] for i in range(11)]
        player_1_attempts = [[0 for j in range(11)] for i in range(11)]
        player_2_ships = [[0 for j in range(11)] for i in range(11)]
        player_2_attempts = [[0 for j in range(11)] for i in range(11)]
        hp1 = 20
        hp2 = 20
        player_1_ships = auto_deck(player_1_ships)         
        player_1_attempts = auto_deck(player_1_attempts)
        player_2_ships = auto_deck(player_2_ships)
        player_2_attempts = auto_deck(player_2_attempts)

        player_1 = input("Первый игрок введите имя: ")
        player_1_ships = build_deck(player_1_ships)
        player_2_ships = build_deck_auto(player_2_ships)
        while(hp2 > 0 and hp1 > 0):
            print(f"Игрок {player_1}, вы готовы? Нажмите Enter")
            input()
            os.system('cls')
            while (True):
                print_full(player_1_ships, player_1_attempts, player_1)
                a, b = shot(player_2_ships)
                if player_2_ships[a][b] == "▩" or player_2_ships[a][b] == "▢":
                    player_2_ships[a][b] = "■"
                    player_1_attempts[a][b] = "■"
                    print ("Промах! Нажмите Enter что бы продолжить.")
                    input()
                    os.system('cls')
                    break
                else:
                    player_2_ships[a][b] = "▣"
                    player_1_attempts[a][b] = "▣"
                    hp2-=1
                    print ("Попадание! Нажмите Enter что бы продолжить.")
                    input()
                    os.system('cls')
                if hp2 == 0: 
                    break
            while (True):
                a, b = shot_auto(player_1_ships)
                if player_1_ships[a][b] == "▩" or player_1_ships[a][b] == "▢":
                    player_1_ships[a][b] = "■"
                    player_2_attempts[a][b] = "■"
                    break
                else:
                    player_1_ships[a][b] = "▣"
                    player_2_attempts[a][b] = "▣"
                    hp2-=1
                if hp1 == 0: 
                    break
        if hp2 == 0:
            print (f"{player_1} выиграл! Нажмите Enter что бы выйти в меню.")
        else :
            print (f"Бот выиграл! Нажмите Enter что бы выйти в меню.")
        input()
        os.system('cls')
    if choise == 3:
        print ("Нашитпостил @shiden_kai для Python Bootcamp в Step Academy как финальный проект. Было спонсировано банкой пива и пачкой сухариков")
        print("Нажмите Enter")
        input()
        os.system('cls')
    if choise == 0:
        break
