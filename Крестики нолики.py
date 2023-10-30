print('Добро пожаловать в игру крестики - нолики! ')
boart_size = 3
# Длина игрового поля
board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    print((5 * '_')*3)
    for i in range(boart_size):
        print((' ' * 3 + '|' )*3)
        print('',board[i *3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
        print(('_' * 3 + '|') * 3)
    pass

def game_step(index, char):
    if (int(index) >9 or int(index) <1 or board[int(index) - 1] in ('X', 'O')):
        return False

    board[int(index) -1] = char
    return True


def check_win():
    win = False

    win_combination = (
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    )
    for pos in win_combination:
        if(board[pos[0]] ==  board[pos[1]]and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def start_game():

    current_player = 'X'

    step = 1
    draw_board()
    while (step<10) and (check_win() == False):
        index = input(' Ходит игрока '+ current_player + ' введите номер поля, (Введите 0, если хотите закончить игру.)')

        if (index == '0'):
            print('Играй Закончена')
            break

        if (game_step(index,current_player)):
            print('Ход выполнен')

            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'

            draw_board()
            step += 1

        else:
            print('Ход не выполнен,  выберите другой номер поля ')

            print('Победу одержал ' + check_win())


start_game()
