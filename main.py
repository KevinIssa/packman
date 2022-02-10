from turtle import fd, up, down, goto, Turtle
# on peut modifier le fichier directement sur Github en mode trkl
#menfou test 
# lol > dota 2
game_space = Turtle()


def read_matrices(files):  # mooc project (lire matrices) @linsfa
    """
    going to read the file with the matrices
    """
    matrices_conversion = []
    for row in open(files, encoding='utf-8'):
        matrices_conversion.append([int(i) for i in row if i.isalnum()])
    return matrices_conversion


