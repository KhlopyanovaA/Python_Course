#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*

# 5
    #1 2 3 4 5
    #3
    #-> 1

N = int(input("введите кол-во элементов в массиве: "))
A = [0] * N
for i in range(N):
    A[i] = int(input())
print(A)
x = int(input("введите число для поиска:  "))
print(A.count(x)
