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

    # Инициализация класса, обязательными входными параметрами являются матрица задач и метод распределения, среди которых есть два метода распределения, метод all_permutation или метод Венгрии.
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
        p=task_matrix.copy()
        row_ind, col_ind = linear_sum_assignment(p)
        max_cost = p[row_ind,col_ind].sum()
        best_solution = col_ind
        return max_cost,best_solution
    
    def Hungary_max(self, task_matrix):
        p=task_matrix.copy()
        row_ind, col_ind = linear_sum_assignment(-p)
        max_cost = p[row_ind,col_ind].sum()
        best_solution = col_ind
        return max_cost,best_solution
    
    def Greedy(self, task_matrix):
        p = task_matrix.copy()
        res=[]
        total=0
        for i in range (p[0].size):
            ind_i,ind_j = np.unravel_index(np.argmax(p), p.shape)
            max=np.max(p)
            p[ind_i]=0
            p[:,ind_j]=0
            total+=max
            res.append(ind_j)
        return total, res
    
    def Thrifty(self,task_matrix):
        p = task_matrix.copy()
        res=[]
        total=0
        for i in range (p[0].size):
            ind_i,ind_j = np.unravel_index(np.argmin(p), p.shape)
            min=np.min(p)
            p[ind_i]=np.inf
            p[:,ind_j]=np.inf
            total+=min
            res.append(ind_j)
        return total, res
    
    def Greedy_Thrifty(self,task_matrix,v):
        p=task_matrix.copy()
        ind=[]
        res=[]
        total=0
        for i in range (v):
            ind_i,ind_j = np.unravel_index(np.argmax(p), p.shape)
            ind.append((ind_i,ind_j))
            max=np.max(p)
            p[ind_i]=0
            p[:,ind_j]=0
            total+=max
            res.append(ind_j)
        for i in ind:
            p[i[0]]=np.inf
            p[:,i[1]]=np.inf
        for i in range (v,p[0].size):
            ind_i,ind_j = np.unravel_index(np.argmin(p), p.shape)
            min=np.min(p)
            p[ind_i]=np.inf
            p[:,ind_j]=np.inf
            total+=min
            res.append(ind_j)
        return total,res
    
    def Thrifty_Greedy(self,task_matrix,v):
        p=task_matrix.copy()
        ind=[]
        res=[]
        total=0
        for i in range (v):
            ind_i,ind_j = np.unravel_index(np.argmin(p), p.shape)
            ind.append((ind_i,ind_j))
            min=np.min(p)
            p[ind_i]=np.inf
            p[:,ind_j]=np.inf
            total+=min
            res.append(ind_j)
        for i in ind:
            p[i[0]]=0
            p[:,i[1]]=0
        for i in range (v,p[0].size):
            ind_i,ind_j = np.unravel_index(np.argmax(p), p.shape)
            max=np.max(p)
            p[ind_i]=0
            p[:,ind_j]=0
            total+=max
            res.append(ind_j)
        return total,res
        


    

    

