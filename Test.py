import random
N, M = (5, 10) #размер игрового поля


def getTotalMines(PM, i, j):
    n = 0
    for k in range(-1, 2):
        for l in  range(-1, 2):
            x = i +k
            y = j + l
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if PM [x * N + y] < 0:
                n += 1
    return n

def createGame(PM):
    rng = random.Random()
    n = M
    while n > 0:
        i = rng.randrange(N)
        j = rng.randrange(N)
        if PM[i * N + j] != 0:
            continue
        PM[i * N *j] = -1
        n -= 1
    for i in range(N):
        for j in range(N):
            if PM[i * N * j] ==0:
                PM[i * N * j] = getTotalMines(PM, i, j)





def show (pole):
    for i in range(N):
        for j in range(N):
            print( str(pole[i * N +j]).rjust(3), end ="")
        print()


def goPlayer():

    fiLoopInput = True
    while fiLoopInput:
        x,y =input("Введите координату через пробел").split()
        if not x.isdigit() or not y.isdigit():
            print("Координаты введены не верно")
            continue

        x = int(x) - 1
        y = int(y) - 1
        if x < 0 or x >= N or y < 0 or y >= N:
            print("Координаты выходят за пределы поля")
            continue
        fiLoopInput = False
    return (x, y)




def isFinish():
    pass


def startGame():
    P = [-2] * N * N
    PM = [0] * N * N

    createGame(PM)
    show(PM)
    goPlayer()

while isFinish():
    show()
    goPlayer()

