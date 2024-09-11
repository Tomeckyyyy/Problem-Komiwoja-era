import random
import math


# Zamiana miejscami elementów przy użyciu tymczasowej zmiennej
def swap_position(lista, indeks1, indeks2):
    lista[indeks1], lista[indeks2] = lista[indeks2], lista[indeks1]


# Klasa reprezentuje pojedynczy punkt
class Point:
    def __init__(self):
        self.x = random.randint(1, 20)
        self.y = random.randint(1, 20)

    # Funkcja, która oblicza odległość od punktu
    def distance_to_next_point(self, next_x, next_y):
        distance = math.sqrt(pow((self.x - next_x), 2) + pow((self.y - next_y), 2))
        return distance

    # Zwraca X
    def get_x(self):
        return self.x

    # Zwraca Y
    def get_y(self):
        return self.y


# Klasa, która reprezentuje pojedynczą próbę rozwiązania
class SolutionExample:
    # Tworzenie instancji następuje przez stworzenie dziecka dwóch rodziców.
    def __init__(self, variables_in_the_list_points: list, parent1: list, parent2: list, mutation_probability: int,
                 first_point, last_point):
        self.child: list = [_ for _ in range(0, len(variables_in_the_list_points))]
        list_index_points = [_ for _ in range(0, len(variables_in_the_list_points))]
        random.shuffle(list_index_points)
        self.copy_variables_in_the_list_points: list = variables_in_the_list_points.copy()
        # Wymieszanie skopiowanej listy, żeby na pewno nie było powtarzalności
        random.shuffle(self.copy_variables_in_the_list_points)
        for index in list_index_points:
            # Jeśli nastąpi, mutacja wybierze jedną z kopii zmiennych punktów i w podanym indeksie wstawi ją i usunie z
            # kopii zmiennych punktów
            if mutation_probability >= random.randint(0, 100):
                x = random.randint(0, len(self.copy_variables_in_the_list_points) - 1)
                self.child[index] = self.copy_variables_in_the_list_points[x]
                self.copy_variables_in_the_list_points.remove(x)
            else:
                parent_part1 = self.check_parent(parent1)
                parent_part2 = self.check_parent(parent2)
                if parent_part1 and parent_part2:
                    if 1 == random.randint(1, 2):
                        self.child[index] = parent_part1
                        self.copy_variables_in_the_list_points.remove(parent_part1)
                    else:
                        self.child[index] = parent_part2
                        self.copy_variables_in_the_list_points.remove(parent_part2)
                elif parent_part1:
                    self.child[index] = parent_part1
                    self.copy_variables_in_the_list_points.remove(parent_part1)
                elif parent_part2:
                    self.child[index] = parent_part2
                    self.copy_variables_in_the_list_points.remove(parent_part2)
                else:
                    x = random.randint(0, len(self.copy_variables_in_the_list_points) - 1)
                    self.child[index] = self.copy_variables_in_the_list_points[x]
                    self.copy_variables_in_the_list_points.remove(x)
        self.child.insert(0, first_point)
        self.child.append(last_point)

    # Sprawdza, czy rodzic ma dozwolony ruch dla tego dziecka
    def check_parent(self, parent):
        for single_point_list_point in self.copy_variables_in_the_list_points:
            for single_point_parent in parent:
                if single_point_list_point == single_point_parent:
                    return single_point_parent
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

    # Funkcja zwraca nową listę, nową próbę rozwiązania, dziecko tych rodziców
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
def generate_points_list(how_many_points):
    list_points = []
    for _ in range(0, how_many_points):
        point = Point()
        list_points.append(point)
        print(point.get_x(), point.get_y())
    return list_points


# TODO: w pierwszej generacji nie zawsze zaczyna od tych głównych punktów
# TODO: wybieranie najlepszych dzieci, trzeba zrobić we wszystkich klasach generacji
