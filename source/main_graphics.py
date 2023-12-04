# main_add.py

# Импорт необходимых библиотек и модулей
import numpy as np
import alg as h  # Предполагается, что "alg" - это модуль или скрипт с классом TaskAssignment
import matplotlib.pyplot as plt

# Функция для расчета теоретических решений
def theor_solution():
    # Определение матриц P1, P2, P3 и P4
    p1 = h.np.array([7, 6, 5.1, 4, 6, 5.1, 4, 2, 5, 4, 2, 1, 4, 2, 1, 0.5]).reshape(4, 4)
    p2 = h.np.array([7, 6, 5.5, 4, 6, 5.1, 4, 2, 5, 4, 2, 1, 4, 2, 1, 0.5]).reshape(4, 4)
    p3 = h.np.array([4, 2, 2/3, 1/6, 15, 7.5, 2.5, 5/8, 6, 3, 1, 1/4, 12, 6, 2, 1/2]).reshape(4, 4)
    p4 = h.np.array([16, 32/3, 64/9, 128/27, 16, 4, 1, 1/4, 16, 8, 4, 2, 16, 16/3, 16/9, 16/27]).reshape(4, 4)

    # Инициализация экземпляров TaskAssignment для каждой матрицы с использованием разных алгоритмов
    p1_Hun_max = h.TaskAssignment(p1, 'Hungary_max', 0)
    p1_Hun_min = h.TaskAssignment(p1, 'Hungary_min', 0)
    p1_greedy = h.TaskAssignment(p1, 'greedy', 0)
    
    p2_Hun_max = h.TaskAssignment(p2, 'Hungary_max', 0)
    p2_Hun_min = h.TaskAssignment(p2, 'Hungary_min', 0)
    p2_greedy = h.TaskAssignment(p2, 'greedy', 0)
    
    p3_Hun_max = h.TaskAssignment(p3, 'Hungary_max', 0)
    p3_Hun_min = h.TaskAssignment(p3, 'Hungary_min', 0)
    p3_greedy = h.TaskAssignment(p3, 'greedy', 0)
    
    p4_Hun_max = h.TaskAssignment(p4, 'Hungary_max', 0)
    p4_Hun_min = h.TaskAssignment(p4, 'Hungary_min', 0)
    p4_greedy = h.TaskAssignment(p4, 'greedy', 0)

    # Определение теоретических значений решений
    p1_Hun_max_theor = 16
    p1_Hun_min_theor = 13
    p1_greedy_theor = 14.6
    p2_Hun_max_theor = 16.1
    p2_Hun_min_theor = 13
    p2_greedy_theor = 14.6
    p3_Hun_max_theor = 22 + 1/6
    p4_Hun_max_theor = 31 + 19/27

    # Вывод результатов для каждого алгоритма и матрицы
    #P1
    print("Венгерский алгоритм max для P1:\n")
    print("Найденное в теоретической части:", p1_Hun_max_theor)
    print("Найденное в компьютерной части:", p1_Hun_max.max_cost)
    
    print("Венгерский алгоритм min для P1:\n")
    print("Найденное в теоретической части:", p1_Hun_min_theor)
    print("Найденное в компьютерной части:", p1_Hun_min.min_cost)
    
    print("Жадный алгоритм для P1:\n")
    print("Найденное в теоретической части:", p1_greedy_theor)
    print("Найденное в компьютерной части:", p1_greedy.max_cost)
    
    #P2
    print("Венгерский алгоритм max для P2:\n")
    print("Найденное в теоретической части:", p2_Hun_max_theor)
    print("Найденное в компьютерной части:", p2_Hun_max.max_cost)
    
    print("Венгерский алгоритм min для P2:\n")
    print("Найденное в теоретической части:", p2_Hun_min_theor)
    print("Найденное в компьютерной части:", p2_Hun_min.min_cost)
    
    print("Жадный алгоритм для P2:\n")
    print("Найденное в теоретической части:", p2_greedy_theor)
    print("Найденное в компьютерной части:", p2_greedy.max_cost)
    
    #P3
    print("Венгерский алгоритм max для P3:\n")
    print("Найденное в теоретической части:", p3_Hun_max_theor)
    print("Найденное в компьютерной части:", p3_Hun_max.max_cost)
    
    print("Венгерский алгоритм min для P3:\n")
    #print("Найденное в теоретической части:", p3_Hun_min_theor)
    print("Найденное в компьютерной части:", p3_Hun_min.min_cost)
    
    print("Жадный алгоритм для P3:\n")
    #print("Найденное в теоретической части:", p3_greedy_theor)
    print("Найденное в компьютерной части:", p3_greedy.max_cost)
    
    #P4
    print("Венгерский алгоритм max для P4:\n")
    print("Найденное в теоретической части:", p4_Hun_max_theor)
    print("Найденное в компьютерной части:", p4_Hun_max.max_cost)
    
    print("Венгерский алгоритм min для P4:\n")
    #print("Найденное в теоретической части:", p4_Hun_min_theor)
    print("Найденное в компьютерной части:", p4_Hun_min.min_cost)
    
    print("Жадный алгоритм для P4:\n")
    #print("Найденное в теоретической части:", p4_greedy_theor)
    print("Найденное в компьютерной части:", p4_greedy.max_cost)

# Функция для генерации и построения экспериментальных результатов
def Graphic():
    # Задание диапазонов параметров для экспериментов
    a_min = 1
    a_max = 1.5
    bd_min = 1
    bd_max = 1.2
    b_min = 0.8
    b_max = 0.9

    # Инициализация пустых списков для хранения результатов
    y = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    x = []

    # Итерация по различным размерам матриц
    for n in range(1, 9):
        s1 = 0
        s = 0
        s2 = 0
        s3 = 0
        s4 = 0
        s5 = 0
        x.append(n)

        # Проведение экспериментов для каждого размера матрицы
        for i in range(1, 100):
            # Генерация случайных матриц на основе указанных параметров
            a = np.random.default_rng().uniform(a_min, a_max, size=n)
            b = np.zeros((n, n-1))
            v = n//3
            b[:, :v] = np.random.default_rng().uniform(bd_min, bd_max, size=(n, v))
            b[:, v:] = np.random.default_rng().uniform(b_min, b_max, size=(n, n-1-v))

            # Создание матрицы P на основе сгенерированных значений
            P = np.zeros((n, n))
            for i in range(n):
                P[i, 0] = a[i]
                for j in range(1, n):
                    P[i, j] = P[i, j-1] * b[i, j-1]

            task_matrix = P

            # Выполнение задачи назначения для различных алгоритмов
            ass_by_Hun_min = h.TaskAssignment(task_matrix, 'Hungary_min', v)
            ass_by_Hun_max = h.TaskAssignment(task_matrix, 'Hungary_max', v)
            ass_by_greedy = h.TaskAssignment(task_matrix, 'greedy', v)
            ass_by_t = h.TaskAssignment(task_matrix, 'Thrifty', v)
            ass_by_gt = h.TaskAssignment(task_matrix, 'Greedy_Thrifty', v)
            ass_by_tg = h.TaskAssignment(task_matrix, 'Thrifty_Greedy', v)

            # Аккумуляция результатов для каждого алгоритма
            s += ass_by_Hun_max.max_cost
            s1 += ass_by_greedy.max_cost
            s2 += ass_by_Hun_min.min_cost
            s3 += ass_by_t.max_cost
            s4 += ass_by_gt.max_cost
            s5 += ass_by_tg.max_cost

        # Расчет средних значений результатов
        y.append(s/100)
        y1.append(s1/100)
        y2.append(s2/100)
        y3.append(s3/100)
        y4.append(s4/100)
        y5.append(s5/100)

    # Построение графика
    fig, ax = plt.subplots()
    ax.plot(x, y1, label='жадный')
    ax.plot(x, y2, label='венгерский мин')
    ax.plot(x, y3, label='бережливый')
    ax.plot(x, y, label='венгерский макс')
    ax.plot(x, y4, label='жадный-бережный')
    ax.plot(x, y5, label='бережливый-жадный')
    ax.set_title('График')
    ax.set_xlabel('n')
    ax.set_ylabel('S')
    ax.legend()
    ax.grid(linewidth=0.2)
    plt.show()

def Table(n, e):
    # Задание диапазонов параметров для экспериментов
    a_min = 1
    a_max = 1.5
    bd_min = 1
    bd_max = 1.2
    b_min = 0.8
    b_max = 0.9
    s = 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0

    # Проведение экспериментов для указанного числа раз (e)
    for i in range(1, e):
        # Генерация случайных матриц на основе указанных параметров
        a = np.random.default_rng().uniform(a_min, a_max, size=n)
        b = np.zeros((n, n-1))
        v = n//3
        b[:, :v] = np.random.default_rng().uniform(bd_min, bd_max, size=(n, v))
        b[:, v:] = np.random.default_rng().uniform(b_min, b_max, size=(n, n-1-v))
        P = np.zeros((n, n))
        for i in range(n):
            P[i, 0] = a[i]
            for j in range(1, n):
                P[i, j] = P[i, j-1] * b[i, j-1]

        # Выполнение задачи назначения для различных алгоритмов
        task_matrix = P
        ass_by_Hun_min = h.TaskAssignment(task_matrix, 'Hungary_min', v)
        ass_by_Hun_max = h.TaskAssignment(task_matrix, 'Hungary_max', v)
        ass_by_greedy = h.TaskAssignment(task_matrix, 'greedy', v)
        ass_by_t = h.TaskAssignment(task_matrix, 'Thrifty', v)
        ass_by_gt = h.TaskAssignment(task_matrix, 'Greedy_Thrifty', v)
        ass_by_tg = h.TaskAssignment(task_matrix, 'Thrifty_Greedy', v)

        # Суммирование результатов
        s += ass_by_Hun_max.max_cost
        s1 += ass_by_greedy.max_cost
        s2 += ass_by_Hun_min.min_cost
        s3 += ass_by_t.max_cost
        s4 += ass_by_gt.max_cost
        s5 += ass_by_tg.max_cost

    # Расчет средних значений результатов
    s = s/e
    s1 = s1/e
    s2 = s2/e
    s3 = s3/e
    s4 = s4/e
    s5 = s5/e

    # Создание данных для вывода в таблицу
    table_data = [
        ["Венгерский max", s, ""],
        ["Жадный", s1, abs(s-s1)/s],
        ["Венгерский min", s2, abs(s-s2)/s],
        ["Бережливый", s3, abs(s-s3)/s],
        ["Жадный-Бережливый", s4, abs(s-s4)/s],
        ["Бережливый-Жадный", s5, abs(s-s5)/s],
    ]

    # Вывод таблицы
    h.print_table(table_data)

# Главная функция программы
def main():
    # Вызов функции расчета теоретических решений
    theor_solution()

    # Инициализация флага для продолжения или завершения программы
    flag = 1
    while flag:
        # Ввод пользователем размерности матрицы и числа экспериментов
        print("Введите размерность матрицы:", end=" ")
        n = int(input())
        print("Введите число эксприментов:", end=" ")
        e = int(input())

        # Вызов функций Graphic и Table
        Graphic()
        Table(n, e)

        # Запрос пользователя о продолжении или завершении программы
        print("Продолжить? (0 - нет, 1 - да): ")
        flag = int(input())
        

# Запуск главной функции при запуске скрипта
if __name__ == "__main__":
    main()

