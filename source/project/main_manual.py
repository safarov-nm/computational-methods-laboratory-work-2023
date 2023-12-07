# main_manual.py

# Импорт необходимых библиотек и модулей
import numpy as np  # Импорт библиотеки NumPy для работы с массивами и матрицами
import alg as alg  # Импорт созданного модуля alg.py
import matplotlib.pyplot as plt  # Импорт библиотеки для построения графиков

# Функция для расчета теоретических решений
def theor_solution():
    # Задание матриц P1, P2, P3, P4
    p1 = alg.np.array([7, 6, 5.1, 4, 6, 5.1, 4, 2, 5, 4, 2, 1, 4, 2, 1, 0.5]).reshape(4, 4)
    p2 = alg.np.array([7, 6, 5.5, 4, 6, 5.1, 4, 2, 5, 4, 2, 1, 4, 2, 1, 0.5]).reshape(4, 4)
    p3 = alg.np.array([4, 2, 2/3, 1/6, 15, 7.5, 2.5, 5/8, 6, 3, 1, 1/4, 12, 6, 2, 1/2]).reshape(4, 4)
    p4 = alg.np.array([16, 32/3, 64/9, 128/27, 16, 4, 1, 1/4, 16, 8, 4, 2, 16, 16/3, 16/9, 16/27]).reshape(4, 4)
    
    # Инициализация экземпляров TaskAssignment для каждой матрицы с использованием разных алгоритмов
    p1_Hun_max = alg.TaskAssignment(p1, 'Hungary_max', 0)
    p1_Hun_min = alg.TaskAssignment(p1, 'Hungary_min', 0)
    p1_greedy = alg.TaskAssignment(p1, 'greedy', 0)
    
    p2_Hun_max = alg.TaskAssignment(p2, 'Hungary_max', 0)
    p2_Hun_min = alg.TaskAssignment(p2, 'Hungary_min', 0)
    p2_greedy = alg.TaskAssignment(p2, 'greedy', 0)
    
    p3_Hun_max = alg.TaskAssignment(p3, 'Hungary_max', 0)
    p3_Hun_min = alg.TaskAssignment(p3, 'Hungary_min', 0)
    p3_greedy = alg.TaskAssignment(p3, 'greedy', 0)
    
    p4_Hun_max = alg.TaskAssignment(p4, 'Hungary_max', 0)
    p4_Hun_min = alg.TaskAssignment(p4, 'Hungary_min', 0)
    p4_greedy = alg.TaskAssignment(p4, 'greedy', 0)

    # Определение теоретических значений решений
    p1_Hun_max_theor = 16
    p1_Hun_min_theor = 13
    p1_greedy_theor = 14.6
    p2_Hun_max_theor = 16.1
    p2_Hun_min_theor = 13
    p2_greedy_theor = 14.6
    p3_Hun_max_theor = 22 + 1/6
    p3_Hun_min_theor = 9.625
    p3_greedy_theor = 22.166666666666668
    p4_Hun_max_theor = 31 + 19/27
    p4_Hun_min_theor = 23.77777777777778
    p4_greedy_theor = 26.02777777777778

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
    print(f"Найденное в теоретической части: {p3_Hun_min_theor}")
    print(f"Найденное в компьютерной части: {p3_Hun_min.min_cost}\n")
    
    print("Жадный алгоритм для P3:")
    print(f"Найденное в теоретической части: {p3_greedy_theor}")
    print(f"Найденное в компьютерной части: {p3_greedy.max_cost}\n")
    
    #P4
    print("Венгерский алгоритм max для P4:")
    print(f"Найденное в теоретической части: {p4_Hun_max_theor}")
    print(f"Найденное в компьютерной части: {p4_Hun_max.max_cost}\n")
    
    print("Венгерский алгоритм min для P4:")
    print(f"Найденное в теоретической части: {p4_Hun_min_theor}")
    print(f"Найденное в компьютерной части: {p4_Hun_min.min_cost}\n")
    
    print("Жадный алгоритм для P4:")
    print(f"Найденное в теоретической части: {p4_greedy_theor}")
    print(f"Найденное в компьютерной части: {p4_greedy.max_cost}\n")
    
# Функция для генерации и построения экспериментальных результатов
def Graphic(n, e, a_min, a_max, bd_min, bd_max, b_min, b_max):
    # Инициализация пустых списков для хранения результатов
    y = []
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    x = []
    
    s = 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    
    mas = [0] * n
    mas1 = [0] * n
    mas2 = [0] * n
    mas3 = [0] * n
    mas4 = [0] * n
    mas5 = [0] * n
    for i in range(1, e+1):
        
        #Создаем случайную матрицу
        a = np.random.uniform(a_min, a_max, size=n)
            
        b = np.zeros((n, n-1))
        v = n//2
                
        b[:, :v] = np.random.uniform(bd_min, bd_max, size=(n, v))
        b[:, v:] = np.random.uniform(b_min, b_max, size=(n, n-1-v))
            
        # Создание матрицы P на основе сгенерированных значений
        P = np.zeros((n, n))
        for m in range(n):
            P[m, 0] = a[m]
            for k in range(1, n):
                P[m, k] = P[m, k-1] * b[m, k-1]
    
        task_matrix = P
        
        # Выполнение задачи назначения для различных алгоритмов, ищем индексы значений
        ass_by_Hun_max = alg.TaskAssignment(task_matrix, 'Hungary_max', v)
        ass_by_Hun_min = alg.TaskAssignment(task_matrix, 'Hungary_min', v)
        ass_by_greedy = alg.TaskAssignment(task_matrix, 'greedy', v)
        ass_by_t = alg.TaskAssignment(task_matrix, 'Thrifty', v)
        ass_by_gt = alg.TaskAssignment(task_matrix, 'Greedy_Thrifty', v)
        ass_by_tg = alg.TaskAssignment(task_matrix, 'Thrifty_Greedy', v)
                
        Hun_max = ass_by_Hun_max.best_solution
        Hun_min = ass_by_Hun_min.best_solution
        Greedy = ass_by_greedy.best_solution
        Thrifty = ass_by_t.best_solution
        Greedy_Thrifty = ass_by_gt.best_solution
        Thrifty_Greedy = ass_by_tg.best_solution
            
        
        for j in range(n):
            mas[j] += task_matrix[Hun_max[j], j]
            mas1[j] += task_matrix[Hun_min[j], j]
            mas2[j] += task_matrix[Greedy[j], j]
            mas3[j] += task_matrix[Thrifty[j], j]
            mas4[j] += task_matrix[Greedy_Thrifty[j], j]
            mas5[j] += task_matrix[Thrifty_Greedy[j], j]
            
    for k in range(n):        
        mas[k] = mas[k] / e
        mas1[k] = mas1[k] /e
        mas2[k] = mas2[k] /e
        mas3[k] = mas3[k] /e
        mas4[k] = mas4[k] /e
        mas5[k] = mas5[k] /e
        
    for i in range(0,n):
        # Добавление средних значений результатов
        s += mas[i]
        s1 += mas1[i]
        s2 += mas2[i]
        s3 += mas3[i]
        s4 += mas4[i]
        s5 += mas5[i]
        
        x.append(i+1)
        y.append(s)
        y1.append(s1)
        y2.append(s2)
        y3.append(s3)
        y4.append(s4)
        y5.append(s5)
       
            
    # Построение графика
    show(x, y, y1, y2, y3, y4, y5)
        
    
# Построение графика
def show(x, y, y1, y2, y3, y4, y5):
        
        plt.plot(x, y, label='венгерский макс')
        plt.plot(x, y1, label='венгерский мин')
        plt.plot(x, y2, '--', label='жадный')
        plt.plot(x, y3, '-.', label='бережливый')
        plt.plot(x, y4, 'o--',label='жадный-бережный', markersize=2)
        plt.plot(x, y5, ':',label='бережливый-жадный')
        plt.title('График')
        plt.xlabel('Время')
        plt.ylabel('S')
        plt.legend()
        plt.grid(linewidth=0.2)
        plt.show()
    


def Table(n, e, a_min, a_max, bd_min, bd_max, b_min, b_max):
    
    s = 0
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0

    # Проведение экспериментов для указанного числа раз (e)
    for i in range(1, e+1):
        # Генерация случайных матриц на основе указанных параметров
        a = np.random.default_rng().uniform(a_min, a_max, size=n)
        b = np.zeros((n, n-1))
        v = n // 2 + 1
        b[:, :v] = np.random.default_rng().uniform(bd_min, bd_max, size=(n, v))
        b[:, v:] = np.random.default_rng().uniform(b_min, b_max, size=(n, n-1-v))

        # Построение матрицы P
        P = np.zeros((n, n))
        for i in range(n):
            P[i, 0] = a[i]
            for j in range(1, n):
                P[i, j] = P[i, j-1] * b[i, j-1]

        # Выполнение задачи назначения для различных алгоритмов
        task_matrix = P
        ass_by_Hun_min = alg.TaskAssignment(task_matrix, 'Hungary_min', v)
        ass_by_Hun_max = alg.TaskAssignment(task_matrix, 'Hungary_max', v)
        ass_by_greedy = alg.TaskAssignment(task_matrix, 'greedy', v)
        ass_by_t = alg.TaskAssignment(task_matrix, 'Thrifty', v)
        ass_by_gt = alg.TaskAssignment(task_matrix, 'Greedy_Thrifty', v)
        ass_by_tg = alg.TaskAssignment(task_matrix, 'Thrifty_Greedy', v)

        # Суммирование результатов
        s += ass_by_Hun_max.max_cost
        s1 += ass_by_greedy.max_cost
        s2 += ass_by_Hun_min.min_cost
        s3 += ass_by_t.max_cost
        s4 += ass_by_gt.max_cost
        s5 += ass_by_tg.max_cost

    # Расчет средних значений результатов
    s = s / e
    s1 = s1 / e
    s2 = s2 / e
    s3 = s3 / e
    s4 = s4 / e
    s5 = s5 / e

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
    alg.print_table(table_data)

    # Запись таблицы в файл и вывод на экран
    with open('data.txt', 'w') as file:
        file.write(str(table_data))

def main():
    # Вызов функции для вывода теоретических результатов
    theor_solution()

    flag = 1
    while flag:
        # Ввод параметров для эксперимента
        print("Введите число этапов:", end=" ")
        n = int(input())
        print("Введите число эксприментов:", end=" ")
        e = int(input())
        print("Введите a минимальное:", end=" ")
        a_min = float(input())
        print("Введите a максимальное:", end=" ")
        a_max = float(input())
        print("Введите b дозревания минимальное (b > 1):", end=" ")
        bd_min = float(input())
        print("Введите b дозревания максимальное (b > 1):", end=" ")
        bd_max = float(input())
        print("Введите b увядания минимальное (b < 1):", end=" ")
        b_min = float(input())
        print("Введите b увядания максимальное (b < 1):", end=" ")
        b_max = float(input())

        # Вызов функций для построения графика и создания таблицы
        Graphic(n, e, a_min, a_max, bd_min, bd_max, b_min, b_max)
        Table(n, e, a_min, a_max, bd_min, bd_max, b_min, b_max)

        # Проверка на продолжение экспериментов
        print("Продолжить? (0 - нет, 1 - да): ")
        flag = int(input())

if __name__ == "__main__":
    main()
