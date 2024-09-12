import random
import copy

lista = [1,2,3,4,5,6,7]
k = lista.copy()
random.shuffle(k)
print(k)
print(lista)
for _ in range(1,30):
    print(random.randint(0,1))


# list_index_points = [_ for _ in range(0, 6)]
list_index_points = [0,1,2,3]
last = list_index_points[len(list_index_points)-1]
k = list_index_points[0:len(list_index_points)-1]
list_index_points.clear()
print(last, k)

if 2:
    print("1")
elif True:
    print("2")
else:
    print("l")



lista = [("Jan", 25.09), ("Anna", 22.8), ("Piotr", 30)]
# Używając sorted (zwraca nową posortowaną listę):
posortowana_lista = sorted(lista, key=lambda x: x[1])

# Używając sort (sortuje listę w miejscu):
lista.sort(key=lambda x: x[1])

print(posortowana_lista, "\n", lista)
