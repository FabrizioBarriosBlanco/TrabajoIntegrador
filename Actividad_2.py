"""Snake, classic arcade game."""

from random import randrange, choice # Importa la función choice
from turtle import *
from freegames import square, vector

# Define una lista de colores diferentes (excluyendo el rojo)
colors = ['green', 'blue', 'yellow', 'orange', 'purple']

# Selecciona colores aleatorios para la serpiente y la comida
snake_color = choice([c for c in colors])
food_color = choice([c for c in colors])

if snake_color == food_color:
  food_color = choice([c for c in colors])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
      square(body.x, body.y, 9, snake_color) #En vez de seleccionar un color fijo, trae esa variable aleatoria
    square(food.x, food.y, 9, food_color) #En vez de seleccionar un color fijo, trae esa variable aleatoria
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
