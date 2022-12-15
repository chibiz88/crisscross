import random
class pc: #Создаю класс для игры против ПК с рандомными ходами
    random_list = list(range(1, 10))
    def __init__(self):
        self.name = "Fedor"
        self.symbol = "X"
    def move(self):
        self.pc_move = random.choice(pc.random_list) #PC делает ход от 1 до 9
        player.move_list.append(self.pc_move) #Добавляю его ход в список всех ходов, чтобы в дальнейшем проверять был такой ход или нет
        pc.random_list.remove(self.pc_move) #Удаляю ход ПК из рандомного листа, чтобы ПК не повторял свои ходы
        pole.board[int(self.pc_move) - 1] = self.symbol #Заменяю элемент в поле на Х по индексу
        print(f"{self.name} сделал ход на клетку {self.pc_move}")
        self.win_control() #проверяю победил ли игрок после своего хода
        pole()
    def win_control(self):
        for i, k, j in pole.winlist:
            if (pole.board[i], pole.board[k], pole.board[j]) == (self.symbol, self.symbol, self.symbol):
                game.win += 1
class player: #Класс игрока-человека
    move_list = []
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.player_move = ""

    def win_control(self): #Проверка победы после хода
        for i, k, j in pole.winlist:
            if (pole.board[i], pole.board[k], pole.board[j]) == (self.symbol, self.symbol, self.symbol):
                game.win += 1

    def move_control(self): #Проверка что введено число от 1 до 9 и такого хода еще не было
        while self.player_move.isalpha() or len(self.player_move) > 1 or self.player_move in player.move_list:
            if self.player_move.isalpha() or len(self.player_move) > 1:
                self.player_move = input("Введи число от 1 до 9: ")
            elif self.player_move in player.move_list:
                self.player_move = input("Такой ход уже был, давай другой: ")
        return self.player_move

    def move(self): #Ход игрока-человека
        self.player_move = input(f"Твой ход {self.name}: ")
        self.move_control() #Проверка ввода
        player.move_list.append(self.player_move) #Добавляю его ход в список всех ходов, чтобы в дальнейшем проверять был такой ход или нет
        pc.random_list.remove(int(self.player_move)) #Удаляю ход из списка ходов ПК, чтобы он не повторял ходы другого игрока
        pole.board[int(self.player_move) - 1] = self.symbol #Заменяю элемент в поле на символ, соответствующий ходу игрока
        self.win_control() #Проверка победы
        pole() #Вывод поля после хода
class pole:
    winlist = [(0, 1, 2), (3, 4, 5), (6, 7, 8), #Победные комбинации
               (0, 3, 4), (1, 4, 7), (2, 5, 8),
               (0, 4, 8), (2, 4, 6)]
    board = list(range(1, 10)) #Поле
    def __init__(self):
        print(*pole.board[0:3])
        print(*pole.board[3:6])
        print(*pole.board[6:])
class game:
    count = 1
    win = 0
    draw = 0
    vs = ""
    def __init__(self):
        game.vs = input("Player1 vs Player2 (1) PC vs Player2 (2)   " )
        if game.vs == "2":
            pl_1 = pc()
            pl_2 = player(input("Введите имя 2-го игрока: "), "O")
        else:
            pl_1 = player(input("Введите имя 1-го игрока: "), "X")
            pl_2 = player(input("Введите имя 2-го игрока: "), "O")

        while game.count <= 9 and game.win < 1:
            if game.count != 1 and game.count % 2 == 0:
                pl_2.move()
                game.count += 1
                if game.win == 1:
                    print(f"Победил {pl_2.name}")
            else:
                pl_1.move()
                game.count += 1
                if game.win == 1:
                    print(f"Победил {pl_1.name}")
        if game.win == 0:
            print("Ничья!")

game()
