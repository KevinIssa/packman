from turtle import Turtle, Screen, tracer, done

MUR = 1
PIECE = 2
TAILLE = 30
OFFSETX = 31*TAILLE/2
OFFSETY = 28*TAILLE/2


def read_matrix(files):
    matrix_conversion = []
    for row in open(files, 'r', encoding='utf-8'):
        row = row.split()
        matrix_conversion.append([int(i) for i in row])
    return matrix_conversion


def draw_square(drawer, length):
    drawer.down()
    drawer.begin_fill()
    for i in range(4):
        drawer.fd(length)
        drawer.right(90)
    drawer.end_fill()
    drawer.up()


game_window = Screen()
game_space = Turtle()
tracer(0)
game_window.bgcolor('black')

game_space.hideturtle()
game_space.up()
game_space.color('blue', 'blue')

game_terrain = read_matrix('packman_gamespace.txt')
print(game_terrain)
for line in range(len(game_terrain)):
    for column in range(len(game_terrain[line])):
        game_space.goto((column * TAILLE) - OFFSETX, (line * TAILLE) - OFFSETY)
        if game_terrain[line][column] == MUR:
            draw_square(game_space, TAILLE)
        elif game_terrain[line][column] == PIECE:
            game_space.dot(round(TAILLE/4), 'yellow')

done()
