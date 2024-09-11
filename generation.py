import random
import math
import main


# Zamiana miejscami elementów przy użyciu tymczasowej zmiennej
def swap_position(lista, indeks1, indeks2):
    lista[indeks1], lista[indeks2] = lista[indeks2], lista[indeks1]


class Point:
    def __init__(self):
        self.x = random.randint(1, 20)
        self.y = random.randint(1, 20)

    # Funkcja, która oblicza odległość od punktu
    def distance_to_next_point(self, next_x, next_y):
        distance = math.sqrt(pow((self.x - next_x), 2) + pow((self.y - next_y), 2))
        return distance

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class SolutionExample:
    def __init__(self, variables_in_the_list_points: list, parent1: list, parent2: list, mutation_probability: int):
        self.child: list = [_ for _ in range(0, len(variables_in_the_list_points))]
        list_index_points = [_ for _ in range(0, len(variables_in_the_list_points))]
        random.shuffle(list_index_points)
        self.copy_variables_in_the_list_points: list = variables_in_the_list_points.copy()
        for index in list_index_points:
            # Jeśli nastąpi, mutacja wybierze jedną z kopii zmiennych punktów i w podanym indeksie wstawi ją i usunie z
            # kopii zmiennych punktów
            if mutation_probability >= random.randint(0, 100):
                x = random.randint(0, len(self.copy_variables_in_the_list_points) - 1)
                self.child[index] = self.copy_variables_in_the_list_points[x]
                self.copy_variables_in_the_list_points.remove(x)
            else:
                if self.check_parent(parent1) and self.check_parent(parent2):
                    continue
                elif self.check_parent(parent1):
                    continue
                elif self.check_parent(parent2):
                    continue
                else:
                    continue
        self.child.insert(0, main.FIRST_POINT)
        self.child.append(main.LAST_POINT)

    # Sprawdza, czy rodzic ma dozwolony ruch dla tego dziecka
    def check_parent(self, parent):
        for single_point_list_point in self.copy_variables_in_the_list_points:
            for single_point_parent in parent:
                if single_point_list_point == single_point_parent:
                    return True
        return False

    # Funkcja, która oblicza długość całej drogi
    def evaluation_child(self):
        all_distance = 0
        for i in range(0, len(self.child)):
            if i == len(self.child) - 1:
                distance = self.child[i].distance_to_next_point(self.child[1].get_x(), self.child[1].get_y())
            else:
                distance = self.child[i].distance_to_next_point(self.child[i + 1].get_x(),
                                                                self.child[i + 1].get_y())
            print(distance)
            all_distance += distance
        return all_distance

    def get_child(self):
        return self.child


# Tutaj są, generowane kolejne generacje
class Generation:
    def __init__(self, list_the_best_older_generation):
        self.list_the_best_children = []
        for _ in list_the_best_older_generation:
            continue

    def get_the_best_children(self):
        return self.list_the_best_children


# Tutaj jest, generowana cała pierwsza generacja
class FirstGeneration:
    def __init__(self, variables_in_the_list_points, population):
        self.list_first_generation = []
        for _ in range(0, population):
            new_shuffled_list = variables_in_the_list_points.copy()
            random.shuffle(new_shuffled_list)
            self.list_first_generation.append(new_shuffled_list)

    def get_the_best_children(self):
        return self.list_first_generation


# Generuje początkowy problem
def generate_points_list():
    list_points = []
    for _ in range(0, main.how_many_points):
        point = Point()
        list_points.append(point)
        print(point.get_x(), point.get_y())
    return list_points
