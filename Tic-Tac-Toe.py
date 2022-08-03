user = '         '
print('---------')
print(f'| {user[0]} {user[1]} {user[2]} |')
print(f'| {user[3]} {user[4]} {user[5]} |')
print(f'| {user[6]} {user[7]} {user[8]} |')
print('---------')
win_x = 0
win_o = 0
available_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
x_moves = [0, 2, 4, 6, 8]
o_moves = [1, 3, 5, 7, 9]
counter_ = 9
move = 0
while move < 10:
    if win_x != 1 and win_o != 1 and counter_ != 0:
        coordinates = input('Enter the coordinates:')
        if len(coordinates) == 3:
            if coordinates[0] and coordinates[2] in available_inputs:
                if coordinates[0] != '4' and coordinates[2] != '4':
                    x = int(coordinates[0])
                    y = int(coordinates[2])
                    user = list(user)
                    index = (((x - 1) * 3) + (y + 2)) - 3
                    if user[index] == ' ':
                        if move in x_moves:
                            user[index] = 'X'
                        elif move in o_moves:
                            user[index] = 'O'
                        user = ''.join(user)
                        print('---------')
                        print(f'| {user[0]} {user[1]} {user[2]} |')
                        print(f'| {user[3]} {user[4]} {user[5]} |')
                        print(f'| {user[6]} {user[7]} {user[8]} |')
                        print('---------')
                        rows = [user[0:3], user[3:6], user[6:9]]
                        columns = [user[0] + user[3] + user[6], user[1] + user[4] + user[7], user[2] + user[5] + user[8]]
                        diagonals = [user[0] + user[4] + user[8], user[2] + user[4] + user[6]]
                        matrix = [rows, columns, diagonals]
                        for m in matrix:
                            for i in m:
                                if i == 'XXX':
                                    win_x += 1
                                elif i == 'OOO':
                                    win_o += 1
                        move += 1
                        counter_ -= 1
                    elif user[index] == 'X' or 'O':
                        print('This cell is occupied! Choose another one!')
                else:
                    print('Coordinates should be from 1 to 3!')
            else:
                print('You should enter numbers!')
        else:
            print('You should enter numbers!')
    else:
        if win_x == 1 and win_o == 0:
            print('X wins')
            break
        elif win_x == 0 and win_o == 1:
            print('O wins')
            break
        elif win_x == 0 and win_x == 0:
            if counter_ == 0:
                print('Draw')
                break
