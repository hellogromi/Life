import os
import time
import copy
import random

# Создание пустого поля
def fields(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

# Вывод поля на экран
def print_f(f):
    for row in f:
        print(' '.join(['*' if cell else ' ' for cell in row]))

# Подсчет количества живых соседей для клетки
def count_neighbors(f, x, y):
    rows, cols = len(f), len(f[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < rows and 0 <= y + j < cols:
                count += f[x + i][y + j]
    return count

# Вычисление следующего поколения
def next_generation(f):
    rows, cols = len(f), len(f[0])
    new_f = copy.deepcopy(f)
    for i in range(rows):
        for j in range(cols):
            neighbors = count_neighbors(f, i, j)
            if f[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_f[i][j] = 0
            else:
                if neighbors == 3:
                    new_f[i][j] = 1
    return new_f

# Задаем размер поля
rows, cols = 20, 40

# Создаем начальное поле
f = create_f(rows, cols)

# Наполняем поле случайными значениями (живые клетки)
# Для примера заполним поле случайным образом

for i in range(rows):
    for j in range(cols):
        f[i][j] = random.choice([0, 1])

# Основной цикл игры
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_f(f)
    f = next_generation(f)
    time.sleep(0.4)