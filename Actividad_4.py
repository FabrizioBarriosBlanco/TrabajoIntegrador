from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
score = 0  # Contador de puntuación

def tap(x, y):
    """Responder al toque en la pantalla."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

def inside(xy):
    """Devolver True si xy está dentro de la pantalla."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Dibujar la bola y los objetivos."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    # Mostrar la puntuación en la ventana del juego
    goto(160, 160)
    color('black')
    write(f'Score: {score}', align='center', font=('Courier', 24, 'normal'))
    update()

def move():
    """Mover la bola y los objetivos."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 3  # Aumenta la velocidad de movimiento de los objetivos

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else:
            # Incrementar la puntuación cuando la bola golpea un objetivo
            global score
            score += 1

    draw()

    for target in targets:
        if not inside(target):
            target.x = 200  # Reposiciona el objetivo en el lado derecho

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
