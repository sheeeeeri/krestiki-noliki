board = list(range(1, 10))


wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    # Оформление
    print('-------------------')
    for i in range(3):
        print('| ', board[0+i*3], ' | ',
              board[1+i*3], ' | ', board[2+i*3], ' |')
    print('-------------------')


# player_token - символ что хочет поставить пользователь в ту или иную позицию
def take_input(player_token): # Принятие входных данных
    while True:
        value = input('Куда поставить: ' + player_token + ' ?\n')
        if not (value in '123456789'):
            print('Error, please try again')
            continue
        value = int(value)
        if str(board[value-1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        board[value - 1] = player_token
        break


def check_win(): # Проверка на выигрыш
    for each in wins_coord:
        if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
            return board[each[1]-1]
    else:
        return False


def main(): # Запуск, база
    counter = 0
    print('\nИтак, чтобы начать играть, вводите номер позиции 1-9, как здесь показано')
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, ' выиграл')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья')
            break


main()
