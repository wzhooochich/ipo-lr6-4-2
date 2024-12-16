'''
Написать программу, которая:
- Создает двумерную матрицу случайного размера от 4 до 8 во высоте и ширине,
  заполненную значениями из списка **[-15, -4, -2, -7, 0, 3, 5, 12, 9]**
- Выводит данную матрицу в форматированном виде. 
- Выводит сумму всех элементов , не кратных 3.

'''
# импорт библиотеки для рандома
import random

# инициализация строк и столбцов массива
lines=random.randint(4,8)
cols=random.randint(4,8)

list=[-15, -4, -2, -7, 0, 3, 5, 12, 9] # список
not_three=[] # список для проверки
sum=0 # переменная для суммы чисел

# создание матрицы из lines и cols
matrix=[[random.choice(list) for i in range(cols)]for s in range(lines)]

# вывод матрицы
for i in range(lines):
    for j in range(cols):
     print(matrix[i][j], end=' ')
    print()

# проверка на кратность трём
for p in matrix:
    for a in p:
        if a %3 !=0 :
            not_three.append(a)
print(f"список чисел , не кратных трем : {not_three}")

# перебор значений не равных трем для нахождения их суммы
for o in not_three:
    sum+=o
print('Сумма равна :',sum)
