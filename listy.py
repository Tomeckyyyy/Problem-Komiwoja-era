import random
import copy

lista = [1,2,3,4,5,6,7]
k = lista.copy()
random.shuffle(k)
print(k)
print(lista)
for _ in range(1,30):
    print(random.randint(0,1))


list_index_points = [_ for _ in range(0, 6)]
print(list_index_points)

if 2:
    print("1")
elif True:
    print("2")
else:
    print("l")