# Приветствие

print('Здравствуйте, вас приветствует игра "Жизнь", ознакомьтесь с правилами игры в описании!', "Поехали?", sep="\n")

# Готовность

answer = input("Ведите да или нет: ").lower()

correctness = False
while correctness != True:
    if answer == "да" or answer == "нет":
        correctness = True
    else:
        correctness = False
        answer = input("Введите да или нет: ").lower()

while answer != "нет":

    import time
    import copy
    import random

    # Создание пустого поля
    def fields(rows, cols):
        return [[0 for _ in range(cols)] for _ in range(rows)]

    # Вывод поля на экран
    def print_f(f):
        for row in f:
            print(' '.join(['•' if cell else ' ' for cell in row]))

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
                neighb = count_neighbors(f, i, j)
                if f[i][j] == 1:
                    if neighb < 2 or neighb > 3:
                        new_f[i][j] = 0
                else:
                    if neighb == 3:
                        new_f[i][j] = 1
        return new_f

    # Задаем размер поля
    rows = int(input("Введите значение оси y до 20: "))
    correctness_1 = False
    while correctness_1 != True:
        if rows < 1 or rows > 20:
            correctness_1 = False
            rows = int(input("Введите значение оси x  до 20: "))
        else:
            correctness_1 = True

    cols = int(input("Введите значение до 20: "))
    correctness_2 = False
    while correctness_2 != True:
        if cols < 1 or cols > 20:
            correctness_2 = False
            cols = int(input("Введите значение до 20: "))
        else:
            correctness_2 = True

    # Создаем начальное поле

    f = fields(rows, cols)

    # Наполняем поле случайными значениями (живые клетки)

    # Для примера заполним поле случайным образом

    for i in range(rows):
        for j in range(cols):
            f[i][j] = random.choice([0, 1])

    # Основной цикл игры
    correctness_4 = False
    while correctness_4 != True:
        try:
            days = int(input("Введите количество дней до 100: "))
        except ValueError:
            correctness_4 = False
            print("Ввели не число!")
        else:
            correctness_4 = True

    corectness_3 = False
    while corectness_3 != True:
        if days <= 100:
            corectness_3 = True
        else:
            corectness_3 = False
            days = int(input("Введите количество дней до 100: "))

    for i in range(days):
        if  not any(any(f[j]) for j in range(len(f))):
            break
        print_f(f)
        f = next_generation(f)
        time.sleep(0.4)

    # Предлогаем повторить

    print("Не хотите повторить?")

    # Готовность повторить

    answer = input("Введите да или нет: ")

    correctness = False
    while correctness != True:
        if answer == "да" or answer == "нет":
            correctness = True
        else:
            correctness = False
            answer = input("Введите да или нет: ").lower()
