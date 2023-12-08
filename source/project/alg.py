#alg.py

import numpy as np
from numpy import random
from scipy.optimize import linear_sum_assignment

# Функция для создания и вывода таблицы результатов
def print_table(data):
    # Вывод заголовка таблицы
    header = ["Алгоритм", "Среднее значение S", "Относительная погрешность"]
    print(f"{header[0]:<20} {header[1]:<20} {header[2]:<20}")

    # Вывод данных таблицы
    for row in data:
        print(f"{row[0]:<20} {row[1]:<20} {row[2]:<20}")

class TaskAssignment:

    # Инициализация класса, обязательными входными параметрами являются матрица задач и метод распределения, среди которых есть два метода распределения, метод all_permutation или Венгерский метод.
    def __init__(self, task_matrix, mode,v):
        self.task_matrix = task_matrix
        self.mode = mode
        if mode == 'Hungary_min':
            self.min_cost, self.best_solution = self.Hungary_min(task_matrix)
        if mode == 'Hungary_max':
            self.max_cost, self.best_solution = self.Hungary_max(task_matrix)
        if mode == 'greedy':
            self.max_cost, self.best_solution = self.Greedy(task_matrix)
        if mode == 'Thrifty':
            self.max_cost,self.best_solution = self.Thrifty(task_matrix)
        if mode == 'Greedy_Thrifty':
            self.max_cost,self.best_solution = self.Greedy_Thrifty(task_matrix,v)
        if mode == 'Thrifty_Greedy':
            self.max_cost,self.best_solution = self.Thrifty_Greedy(task_matrix,v)
    
    def Hungary_min(self, task_matrix):
        # Создаем копию матрицы задач
        p = task_matrix.copy()
        # Выполняем венгерский алгоритм для минимизации
        row_ind, col_ind = linear_sum_assignment(p)
        # Считаем суммарный вес и получаем решение
        max_cost = p[row_ind, col_ind].sum()
        best_solution = col_ind
        return max_cost, best_solution


    def Hungary_max(self, task_matrix):
        # Создаем копию матрицы задач
        p = task_matrix.copy()
        # Выполняем венгерский алгоритм для максимизации (умножаем на -1)
        row_ind, col_ind = linear_sum_assignment(-p)
        # Считаем суммарный вес и получаем решение
        max_cost = p[row_ind, col_ind].sum()
        best_solution = col_ind
        return max_cost, best_solution
    
    
    def Greedy(self, task_matrix):
        # Создаем копию матрицы задач
        p = task_matrix.copy()
        # Инициализируем пустые списки для решения и отслеживания выбранных строк
        best_solution = []
        max_cost = 0
        selected_rows = []
    
        # Проходим по всем строкам
        for i in range(p.shape[0]):
            # Инициализируем переменные для максимального значения и его индексов
            max_in_row = -np.inf
            ind_i, ind_j = None, None
    
            # Находим максимальное значение в строке, исключая уже выбранные строки
            for row in range(p.shape[0]):
                if row not in selected_rows:
                    max_in_row_current = np.max(p[row])
                    # Обновляем максимальное значение и его индексы, если нашли более большое
                    if max_in_row_current > max_in_row:
                        max_in_row = max_in_row_current
                        ind_i, ind_j = row, np.argmax(p[row])
    
            # Помечаем выбранную строку
            selected_rows.append(ind_i)
    
            # Зануляем выбранную строку и столбец
            p[ind_i] = 0
            p[:, ind_j] = 0
    
            # Добавляем максимальное значение к общему суммарному весу
            max_cost += max_in_row
    
            # Добавляем выбранный столбец к решению
            best_solution.append(ind_j)
    
        # Возвращаем общий вес и решение
        return max_cost, best_solution


    
    def Thrifty(self, task_matrix):
        # Создаем копию матрицы задач
        p = task_matrix.copy()
        # Инициализируем пустые списки для решения и отслеживания выбранных строк
        best_solution = []
        max_cost = 0
        selected_rows = []
    
        # Проходим по всем строкам
        for i in range(p.shape[0]):
            # Инициализируем переменные для минимального значения и его индексов
            min_row = np.inf
            ind_i, ind_j = None, None
    
            # Находим минимальное значение в строке, исключая уже выбранные строки
            for row in range(p.shape[0]):
                if row not in selected_rows:
                    min_in_row = np.min(p[row])
                    # Обновляем минимальное значение и его индексы, если нашли более маленькое
                    if min_in_row < min_row:
                        min_row = min_in_row
                        ind_i, ind_j = row, np.argmin(p[row])
    
            # Помечаем выбранную строку
            selected_rows.append(ind_i)
    
            # Зануляем выбранную строку и столбец
            p[ind_i] = np.inf
            p[:, ind_j] = np.inf
    
            # Добавляем минимальное значение к общему суммарному весу
            max_cost += min_row
    
            # Добавляем выбранный столбец к решению
            best_solution.append(ind_j)
    
        # Возвращаем общий вес и решение
        return max_cost, best_solution

    
    def Greedy_Thrifty(self, task_matrix, v):
        # Создаем копию матрицы задач
        p = task_matrix.copy()
        ind = []
        best_solution = []
        max_cost = 0
        selected_rows = []
    
        # Жадный этап
        for i in range(v):
            # Инициализируем переменные для максимального значения и его индексов
            max_in_row = -np.inf
            ind_i, ind_j = None, None
    
            # Находим максимальное значение в строке, исключая уже выбранные строки
            for row in range(p.shape[0]):
                if row not in selected_rows:
                    max_in_row_current = np.max(p[row])
                    # Обновляем максимальное значение и его индексы, если нашли более большое
                    if max_in_row_current > max_in_row:
                        max_in_row = max_in_row_current
                        ind_i, ind_j = row, np.argmax(p[row])
    
            # Помечаем выбранную строку
            selected_rows.append(ind_i)
    
            ind.append((ind_i, ind_j))
            max_val = np.max(p)
            p[ind_i] = 0
            p[:, ind_j] = 0
            max_cost += max_val
            best_solution.append(ind_j)
    
        # Бережливый этап
        for i in ind:
            p[i[0]] = np.inf
            p[:, i[1]] = np.inf
    
        # Дополнительный этап выбора оставшихся v строк
        for i in range(v, p.shape[0]):
            # Инициализируем переменные для минимального значения и его индексов
            min_row = np.inf
            ind_i, ind_j = None, None
    
            # Находим минимальное значение, исключая уже выбранные строки
            for row in range(p.shape[0]):
                if row not in selected_rows:
                    min_in_row = np.min(p[row])
                    # Обновляем минимальное значение и его индексы, если нашли более маленькое
                    if min_in_row < min_row:
                        min_row = min_in_row
                        ind_i, ind_j = row, np.argmin(p[row])
    
            # Помечаем выбранную строку
            selected_rows.append(ind_i)
    
            p[ind_i] = np.inf
            p[:, ind_j] = np.inf
            max_cost += min_row
            best_solution.append(ind_j)
    
        # Возвращаем общий вес и решение
        return max_cost, best_solution


    def Thrifty_Greedy(self, task_matrix, v):
        # Создаем копию матрицы задач
        p = task_matrix.copy()
        ind = []
        best_solution = []
        max_cost = 0
        selected_rows_min = []  # Список для отслеживания выбранных строк для минимумов
        selected_rows_max = []  # Список для отслеживания выбранных строк для максимумов
        
        #Бережливый этап
        for i in range(v):
            # Выбор минимума
            ind_i_min, ind_j_min = np.unravel_index(np.argmin(p), p.shape)
            ind.append((ind_i_min, ind_j_min))
            min_val = np.min(p)
            p[ind_i_min] = np.inf
            p[:, ind_j_min] = np.inf
            max_cost += min_val
            best_solution.append(ind_j_min)
    
            # Помечаем выбранную строку для минимума
            selected_rows_min.append(ind_i_min)
    
        #Жадный этап
        for i in ind:
            p[i[0]] = 0
            p[:, i[1]] = 0
    
        for i in range(v, p.shape[0]):
            # Инициализируем переменные для максимального значения и его индексов
            max_in_row = -np.inf
            ind_i_max, ind_j_max = None, None
    
            for row in range(p.shape[0]):
                if row not in selected_rows_min:
                    max_in_row_current = np.max(p[row])
                    # Обновляем максимальное значение и его индексы, если нашли более большое
                    if max_in_row_current > max_in_row:
                        max_in_row = max_in_row_current
                        ind_i_max, ind_j_max = row, np.argmax(p[row])
    
            # Помечаем выбранную строку для максимума
            selected_rows_max.append(ind_i_max)
    
            p[ind_i_max] = 0
            p[:, ind_j_max] = 0
            max_cost += max_in_row
            best_solution.append(ind_j_max)
    
        # Возвращаем общий вес и решение
        return max_cost, best_solution
   

