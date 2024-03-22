"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""
import random
from random import randrange
from turtle import *

from freegames import square, vector

COLORS = ['blue', 'green', 'purple', 'yellow', 'orange']

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

snake_color = random.choice(COLORS)
food_color = random.choice(COLORS)

while snake_color == food_color:
    food_color = random.choice(COLORS)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def move_food():
    """Move food randomly one step at a time."""
    global food

    # Generar un vector de movimiento aleatorio para la comida
    movement = vector(randrange(-1, 2) * 10, randrange(-1, 2) * 10)

    # Calcular la nueva posición propuesta para la comida
    new_food_position = food + movement

    # Verificar si la nueva posición está dentro de los límites
    if -200 < new_food_position.x < 190 and -200 < new_food_position.y < 190:
        food = new_food_position

    # Actualizar la comida en la ventana
    clear()
    square(food.x, food.y, 9, food_color)
    for body in snake:
        square(body.x, body.y, 9, snake_color)
    update()

    # Llamar recursivamente a esta función después de un tiempo
    ontimer(move_food, 1000)  # Cambia el valor para ajustar la velocidad de movimiento de la comida

# Iniciar el movimiento aleatorio de la comida
move_food()



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
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
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
move_food()
done()
