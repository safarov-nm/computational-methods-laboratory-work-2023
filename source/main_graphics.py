# main_add.py

# Импорт необходимых библиотек и модулей
import time
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
    print("Венгерский алгоритм max для P1:")
    print(f"Найденное в теоретической части: {p1_Hun_max_theor}")
    print(f"Найденное в компьютерной части: {p1_Hun_max.max_cost}\n")
    
    print("Венгерский алгоритм min для P1:")
    print(f"Найденное в теоретической части: {p1_Hun_min_theor}")
    print(f"Найденное в компьютерной части: {p1_Hun_min.min_cost}\n")
    
    print("Жадный алгоритм для P1:")
    print(f"Найденное в теоретической части: {p1_greedy_theor}")
    print(f"Найденное в компьютерной части: {p1_greedy.max_cost}\n")
    
    #P2
    print("Венгерский алгоритм max для P2:")
    print(f"Найденное в теоретической части: {p2_Hun_max_theor}")
    print(f"Найденное в компьютерной части: {p2_Hun_max.max_cost}\n")
    
    print("Венгерский алгоритм min для P2:")
    print(f"Найденное в теоретической части: {p2_Hun_min_theor}")
    print(f"Найденное в компьютерной части: {p2_Hun_min.min_cost}\n")
    
    print("Жадный алгоритм для P2:")
    print(f"Найденное в теоретической части: {p2_greedy_theor}")
    print(f"Найденное в компьютерной части: {p2_greedy.max_cost}\n")
    
    #P3
    print("Венгерский алгоритм max для P3:")
    print(f"Найденное в теоретической части: {p3_Hun_max_theor}")
    print(f"Найденное в компьютерной части: {p3_Hun_max.max_cost}\n")
    
    print("Венгерский алгоритм min для P3:")
    #print(f"Найденное в теоретической части: {p3_Hun_min_theor}")
    print(f"Найденное в компьютерной части: {p3_Hun_min.min_cost}\n")
    
    print("Жадный алгоритм для P3:")
    #print(f"Найденное в теоретической части: {p3_greedy_theor}")
    print(f"Найденное в компьютерной части: {p3_greedy.max_cost}\n")
    
    #P4
    print("Венгерский алгоритм max для P4:")
    print(f"Найденное в теоретической части: {p4_Hun_max_theor}")
    print(f"Найденное в компьютерной части: {p4_Hun_max.max_cost}\n")
    
    print("Венгерский алгоритм min для P4:")
    #print(f"Найденное в теоретической части: {p4_Hun_min_theor}")
    print(f"Найденное в компьютерной части: {p4_Hun_min.min_cost}\n")
    
    print("Жадный алгоритм для P4:")
    #print(f"Найденное в теоретической части: {p4_greedy_theor}")
    print(f"Найденное в компьютерной части: {p4_greedy.max_cost}\n")

# Функция для генерации и построения экспериментальных результатов
def Graphic_Sn():
    # Задание диапазонов параметров для экспериментов
    a_min = 1
    a_max = 1.5
    bd_min = 1.1
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
    for n in range(1, 21):
        s = 0
        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0
        s5 = 0
        x.append(n)

        # Проведение экспериментов для каждого размера матрицы
        for i in range(1, 101):
            # Генерация случайных матриц на основе указанных параметров
            a = np.random.default_rng().uniform(a_min, a_max, size=n)
            b = np.zeros((n, n-1))
            v = n//2
            
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
            ass_by_Hun_max = h.TaskAssignment(task_matrix, 'Hungary_max', v)
            ass_by_Hun_min = h.TaskAssignment(task_matrix, 'Hungary_min', v)
            ass_by_greedy = h.TaskAssignment(task_matrix, 'greedy', v)
            ass_by_t = h.TaskAssignment(task_matrix, 'Thrifty', v)
            ass_by_gt = h.TaskAssignment(task_matrix, 'Greedy_Thrifty', v)
            ass_by_tg = h.TaskAssignment(task_matrix, 'Thrifty_Greedy', v)

            # Аккумуляция результатов для каждого алгоритма
            s += ass_by_Hun_max.max_cost
            s1 += ass_by_Hun_min.min_cost
            s2 += ass_by_greedy.max_cost
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
    ax.plot(x, y, label='венгерский макс')
    ax.plot(x, y1, label='венгерский мин')
    ax.plot(x, y2, label='жадный')
    ax.plot(x, y3, label='бережливый')
    ax.plot(x, y4, label='жадный-бережный')
    ax.plot(x, y5, label='бережливый-жадный')
    ax.set_title('График')
    ax.set_xlabel('n, размерность матрицы')
    ax.set_ylabel('S, среднее значение решения')
    ax.legend()
    ax.grid(linewidth=0.2)
    plt.show()
    
# Функция для генерации и построения экспериментальных результатов
def Graphic_Time():
    # Задание диапазонов параметров для экспериментов
    a_min = 1
    a_max = 1.5
    bd_min = 1.1
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
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []

    # Итерация по различным размерам матриц
    for n in range(1, 11):
        s = 0
        s1 = 0
        s2 = 0
        s3 = 0
        s4 = 0
        s5 = 0
        
        stime = 0
        stime1 = 0
        stime2 = 0
        stime3 = 0
        stime4 = 0
        stime5 = 0
        

        # Проведение экспериментов для каждого размера матрицы
        for i in range(1, 11):
            # Генерация случайных матриц на основе указанных параметров
            a = np.random.default_rng().uniform(a_min, a_max, size=n)
            b = np.zeros((n, n-1))
            v = n//2
            
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
            start_time = time.time()
            ass_by_Hun_max = h.TaskAssignment(task_matrix, 'Hungary_max', v)
            end_time = time.time()
            x_time = end_time-start_time
            
            start_time = time.time()
            ass_by_Hun_min = h.TaskAssignment(task_matrix, 'Hungary_min', v)
            end_time = time.time()
            x1_time = end_time-start_time
            
            start_time = time.time()
            ass_by_greedy = h.TaskAssignment(task_matrix, 'greedy', v)
            end_time = time.time()
            x2_time = end_time-start_time
            
            start_time = time.time()
            ass_by_t = h.TaskAssignment(task_matrix, 'Thrifty', v)
            end_time = time.time()
            x3_time = end_time-start_time
            
            start_time = time.time()
            ass_by_gt = h.TaskAssignment(task_matrix, 'Greedy_Thrifty', v)
            end_time = time.time()
            x4_time = end_time-start_time
            
            start_time = time.time()
            ass_by_tg = h.TaskAssignment(task_matrix, 'Thrifty_Greedy', v)
            end_time = time.time()
            x5_time = end_time-start_time

            # Аккумуляция результатов для каждого алгоритма
            s += ass_by_Hun_max.max_cost
            s1 += ass_by_Hun_min.min_cost
            s2 += ass_by_greedy.max_cost
            s3 += ass_by_t.max_cost
            s4 += ass_by_gt.max_cost
            s5 += ass_by_tg.max_cost
            
            stime += x_time
            stime1 += x1_time
            stime2 += x2_time
            stime3 += x3_time
            stime4 += x4_time
            stime5 += x5_time
            
            

        # Расчет средних значений результатов
        
        y.append(s/10)
        y1.append(s1/10)
        y2.append(s2/10)
        y3.append(s3/10)
        y4.append(s4/10)
        y5.append(s5/10)
        
        x.append(stime/10)
        x1.append(stime1/10)
        x2.append(stime2/10)
        x3.append(stime3/10)
        x4.append(stime4/10)
        x5.append(stime5/10)
    
    # Преобразование списков в numpy массивы
    
    x = np.array(x)
    y = np.array(y)
    x1 = np.array(x1)
    y1 = np.array(y1)
    x2 = np.array(x2)
    y2 = np.array(y2)
    x3 = np.array(x3)
    y3 = np.array(y3)
    x4 = np.array(x4)
    y4 = np.array(y4)
    x5 = np.array(x5)
    y5 = np.array(y5)

    # Сортировка значений по возрастанию x
    sort_indices = np.argsort(x)
    x = x[sort_indices]
    y = y[sort_indices]

    sort_indices = np.argsort(x1)
    x1 = x1[sort_indices]
    y1 = y1[sort_indices]

    sort_indices = np.argsort(x2)
    x2 = x2[sort_indices]
    y2 = y2[sort_indices]

    sort_indices = np.argsort(x3)
    x3 = x3[sort_indices]
    y3 = y3[sort_indices]

    sort_indices = np.argsort(x4)
    x4 = x4[sort_indices]
    y4 = y4[sort_indices]

    sort_indices = np.argsort(x5)
    x5 = x5[sort_indices]
    y5 = y5[sort_indices]
    
    

    # Построение графика
    fig, ax = plt.subplots()
    ax.plot(x, y, label='венгерский макс')
    ax.plot(x1, y1, label='венгерский мин')
    ax.plot(x2, y2, label='жадный')
    ax.plot(x3, y3, label='бережливый')
    ax.plot(x4, y4, label='жадный-бережный')
    ax.plot(x5, y5, label='бережливый-жадный')
    ax.set_title('График')
    ax.set_xlabel('t, время выполнения')
    ax.set_ylabel('S, среднее значение решения')
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
        v = (n // 2) + 1
        b[:, :v] = np.random.default_rng().uniform(bd_min, bd_max, size=(n, v))
        b[:, v:] = np.random.default_rng().uniform(b_min, b_max, size=(n, n-1-v))
        P = np.zeros((n, n))
        for i in range(n):
            P[i, 0] = a[i]
            for j in range(1, n):
                P[i, j] = P[i, j-1] * b[i, j-1]

        # Выполнение задачи назначения для различных алгоритмов
        task_matrix = P
        ass_by_Hun_max = h.TaskAssignment(task_matrix, 'Hungary_max', v)
        ass_by_Hun_min = h.TaskAssignment(task_matrix, 'Hungary_min', v)
        ass_by_greedy = h.TaskAssignment(task_matrix, 'greedy', v)
        ass_by_t = h.TaskAssignment(task_matrix, 'Thrifty', v)
        ass_by_gt = h.TaskAssignment(task_matrix, 'Greedy_Thrifty', v)
        ass_by_tg = h.TaskAssignment(task_matrix, 'Thrifty_Greedy', v)

        # Суммирование результатов
        s += ass_by_Hun_max.max_cost
        s1 += ass_by_Hun_min.min_cost
        s2 += ass_by_greedy.max_cost
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
        ["Венгерский max", s, abs(s-s)/s],
        ["Венгерский min", s1, abs(s-s1)/s],
        ["Жадный", s2, abs(s-s2)/s],
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
        Graphic_Sn()
        Graphic_Time()
        Table(n, e)

        # Запрос пользователя о продолжении или завершении программы
        flag = int(input("Продолжить? (0 - нет, 1 - да): "))
        

# Запуск главной функции при запуске скрипта
if __name__ == "__main__":
    main()

