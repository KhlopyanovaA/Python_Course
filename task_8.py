#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек #отломить k долек, 
#если разрешается сделать один разлом по прямой между #дольками (то есть разломить шоколадку на два прямоугольника).


print("enter length, width and number of slices")

m = int(input())
n = int(input())
k = int(input())
if n == 1 and m == 1:
    print("no")
elif k % n == 0 or k % m == 0:
    print("yes")
else:
    print("no")
