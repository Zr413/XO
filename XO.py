ARRAY = [[' ' for j in range(3)] for i in range(3)]     # Генерация списка координат

x = None
y = None

VICTORI = [[0, 1, 2],                                   # Выигрышные координаты
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]


def hi():  # Приветствие и вывод игрового поля

    print('      .!77~.    P&              ?@.              ')
    print('    .B&P7!!?Y^  &&   ~P7   .J5^ G@. ?P^   .5Y.       Приветствую тебя игрок!                             ')
    print('    &#.     .#! #&   .5@&!?&B^  P@. ^B@B~P@5.        Это игра в крестики нолики                          ')
    print('   .@^       G# #&     :@@@P    5@.   !@@@!          уверен ты знаешь как играть и всеже подскажу!       ')
    print('    7G.    .Y@7 #&    7&&7G@#^  P@. .Y@B7&@P.                                                            ')
    print('     .?JJYP#G^  ##   !G?   ^GY  P@  JG~   ?B7        Для выбора поля есть 2 координаты                   ')
    print('    .^~!?J?!~^~~&&^^^^:::::::.:.B@:......            вертикальные координаты вводятся первыми.           ')
    print('   :~777777?????@&????J5PPYJJY5Y&@PPPPGGBBBGJ!:      Формат ввода: 1 1                                   ')
    print('                &B  .Y#G5JJ?^   B&  :^     ^~.   ')
    print('                @G .@#:    .Y5  #&  Y@&! ^#&7    ')
    print('               .@G ?@        @~ &&   .5@@@Y      ')
    print('               .@P .&^      J@^ &#   :B@#@#^     ')
    print('               .@5  .Y?~^~J#&~  @B  ?&G. :#@?    ')
    print('    :^!!!!~~~~~7@G^~^^7YPGP?^::^@#.:^:... ....   ')
    print('   :~!!!77777775@B7??77?????JYYP@&5PPPGBBBBGY!.  ')
    print('     JG^   :PY ^@7   ~PGPY?~   .@P  :YGGP5J^     ')
    print('     :G@#!G&Y. !@7 .&&!.  .~P~ :@5 J@P:.  .J5    ')
    print('       !@@@!   ?@~ 5@       .@.^@J.@?       GP   ')
    print('     .P@G~#@B: Y@^ ~&       !@:~@? &7       &B   ')
    print('    .J5^   !P! 5@:  !P~:.:~G@J 7@! .5?^..^J&#.   ')
    print('               G&.   .~J5PP?.  J@:   :7YPG5~     ')

    print('      0   1   2')
    for i, row in enumerate(ARRAY):
        pole = f"  {i} | {' | '.join(row)} | "
        print(pole)


def matr(m, n):                                         # Заполнение игроваого поля O и X
    ARRAY[m][n] = play
    print('      0   1   2')
    for i, row in enumerate(ARRAY):
        pole = f"  {i} | {' | '.join(row)} | "
        print(pole)


def winer():                                            # Проверка на выигрыш
    win = []
    for ind_ar in ARRAY:
        win += ind_ar

        count_1 = set([i for i, _ in enumerate(win) if _ == 'X'])
        for v in VICTORI:
            if len(count_1.intersection(set(v))) == 3:
                return True

        count_2 = set([i for i, _ in enumerate(win) if _ == 'O'])
        for v in VICTORI:
            if len(count_2.intersection(set(v))) == 3:
                return True


def start():                                            # Старт
    h = 1
    global play
    while True:

        if h % 2 != 0:
            play = 'X'
        else:
            play = 'O'

        x, y = input(f'Игрок {play} введите координаты:\n').split()

        try:                                            # Проверка на ввод не цифрового значения координат поля
            x = int(x)
            y = int(y)
        except ValueError:
            print('Введите цыфровые значения')
            continue

        if ARRAY[x][y] == 'X' or ARRAY[x][y] == 'O':     # Проверка на не пустоту
            print('Клетка занята')
            continue

        matr(x, y)

        if winer():                                       # Проверка на выигрыш
            print(f'{play} выиграл')
            break

        h += 1


hi()
start()

