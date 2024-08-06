import turtle
import math

# Функція для малювання гілки дерева
def draw_branch(t, branch_length, angle, level):
    if level == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)

    # Малюємо ліву гілку
    t.left(angle)
    draw_branch(t, branch_length * math.cos(math.radians(angle)), angle, level - 1)
    t.right(angle)

    # Малюємо праву гілку
    t.right(angle)
    draw_branch(t, branch_length * math.cos(math.radians(angle)), angle, level - 1)
    t.left(angle)

    # Повертаємось до попередньої гілки
    t.backward(branch_length)

# Функція для ініціалізації та малювання дерева
def draw_tree(level):
    t = turtle.Turtle()
    t.speed('fastest')  # Встановлюємо максимальну швидкість малювання

    # Встановлюємо початкову позицію
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)  # Повертаємо черепаху вгору

    # Малюємо дерево
    draw_branch(t, 100, 45, level)

    turtle.done()

# Запитуємо у користувача рівень рекурсії
level = int(input("Введіть рівень рекурсії: "))
draw_tree(level)
