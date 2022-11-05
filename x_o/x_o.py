import emoji

def fill_square(matrix):
    for i in range (0, len(matrix), 3):
        print(f" {matrix[i]} {matrix[i+1]} {matrix[i+2]} ")


def emoji_change(string):
    if string == "X":
        string = emoji.emojize(":lemon:")
    elif string == "O":
        string = emoji.emojize(":tomato:")
    return string

def change_players(player):
    if player == emoji.emojize(":lemon:"):
        player = emoji.emojize(":tomato:")
    else:
        player = emoji.emojize(":lemon:")
    return player


def move(player, field):
    point = input(f"В поле с каким номером ставишь {player}? ")
    if point.isdigit():
        if 0 < int(point) < 10:
            point = int(point) - 1
            if field[point] != emoji.emojize(":tomato:") and field[point] != emoji.emojize(":hollow_red_circle:"):
                return point
            else:
                print("Указанное поле занаято.")
                return move(player, field)
        else:
            print("Такого поля не существует")
            move(player, field)
    else:
        print("Введите поле цифрой от 1 до 9")
        move(player, field)


def x_o_game():
    field = []
    for i in range (0,9):
        field.append(i+1)

    player = emoji.emojize(":lemon:")
    fill_square(field)
    win = False
    for i in range(9):
        point = move(player, field)
        field[int(point)] = player
        fill_square(field)
        player = change_players(player)


x_o_game()
