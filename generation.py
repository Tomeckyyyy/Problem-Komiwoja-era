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
    def __init__(self, variables_in_the_list_points: list, first_point: Point, last_point: Point, mutation_probability,
                 parent1=None, parent2=None, is_first_population=False, is_pmx_algorithm=True):
        if parent1 is not None and parent2 is not None:
            self.parent1 = parent1
            self.parent2 = parent2
        self.variables_in_the_list_points: list = variables_in_the_list_points.copy()
        self.len_of_variable_point = len(variables_in_the_list_points)
        # Jeśli to jest pierwsza generacja, wszystko jest totalnie losowe i po prostu algorytm miesza listę
        if is_first_population:
            self.first_population(first_point, last_point)
        # Jeśli nie jest to pierwsza generacja algorytm tworzy dzieci za pomocą jednego z algorytmów
        else:
            self.child: list = [_ for _ in range(0, self.len_of_variable_point)]
            if is_pmx_algorithm:
                self.partially_mapped_crossover()
            else:
                self.order_crossover()
            # Mutacja występuje po krzyżowaniu, metodą zamiany dwóch losowo wybranych punktów
            if mutation_probability >= random.randint(0, 100):
                # TODO: Zmienić nazwy tych zmiennych
                p = random.randint(0, len(self.child) - 1)
                l = random.randint(0, len(self.child) - 1)
                child_p = self.child[p]
                child_l = self.child[l]
                self.child[p] = child_l
                self.child[l] = child_p
            self.child.insert(0, first_point)
            self.child.append(last_point)

    def partially_mapped_crossover(self):
        while True:
            randint_1 = random.randint(0, self.len_of_variable_point - 1)
            randint_2 = random.randint(0, self.len_of_variable_point - 1)
            if randint_1 != randint_2:
                break
        # wyciąga z pierwszego lub drugiego rodzica część trasy
        index_start_of_section = min(randint_1, randint_2)
        index_end_of_section = max(randint_1, randint_2)
        section_of_parent_1 = self.parent1[index_start_of_section: index_end_of_section]
        # Pętla która kopiuje sekcje.
        # !!!!!!!!!!! tutaj tą pętle trzeba mieć na oku, może być tak, że nie dochodzi do ostatniego indeksu!!!!!!!!!!!
        for i in range(index_start_of_section, index_end_of_section):
            self.child[i] = section_of_parent_1[i - index_start_of_section]
            self.variables_in_the_list_points.remove(self.child[i])
        self.copying_the_uncompleted_points()

    def order_crossover(self):
        while True:
            randint_1 = random.randint(0, self.len_of_variable_point - 1)
            randint_2 = random.randint(0, self.len_of_variable_point - 1)
            if randint_1 != randint_2:
                break
        self.copying_the_uncompleted_points()

    # Funkcja która, kopiuje po kolei nieuzupełnione punkty z drugiego rodzica oraz kopiuje po kolei nieuzupełnione
    # punkty
    def copying_the_uncompleted_points(self):
        # Pętla która, kopiuje po kolei nieuzupełnione punkty z drugiego rodzica
        for i in range(len(self.child)):
            if isinstance(self.child[i], int):
                for point_from_variable_points in self.variables_in_the_list_points:
                    if point_from_variable_points == self.parent2[i]:
                        self.child[i] = self.parent2[i]
                        self.variables_in_the_list_points.remove(point_from_variable_points)

        # Pętla która, kopiuje po kolei nieuzupełnione punkty
        for i in range(len(self.child)):
            if isinstance(self.child[i], int):
                self.child[i] = self.variables_in_the_list_points.pop(0)

    def first_population(self, first_point, last_point):
        self.child = self.variables_in_the_list_points.copy()
        random.shuffle(self.child)
        self.child.insert(0, first_point)
        self.child.append(last_point)

    # Funkcja, która oblicza długość całej drogi
    def evaluation_child(self):
        all_distance = 0
        for i in range(0, len(self.child)):
            if i == len(self.child) - 1:
                distance = self.child[i].distance_to_next_point(self.child[1].get_x(), self.child[1].get_y())
            else:
                distance = self.child[i].distance_to_next_point(self.child[i + 1].get_x(),
                                                                self.child[i + 1].get_y())
            all_distance += distance
        return all_distance

    # Funkcja zwraca nową listę, nową próbę rozwiązania, dziecko tych rodziców
    def get_child(self):
        child_with_evaluation = (self.child, self.evaluation_child())
        return child_with_evaluation


# Tutaj jest, generowana cała pierwsza generacja
class Generation:
    def __init__(self, variables_in_the_list_points, first_point, last_point, population, how_many_we_choose_the_best,
                 is_first_generation, mutation_probability: int, the_best_older_generation=None, is_pmx_algorithm=True):
        self.list_the_best_generation = []
        list_generation = []
        if is_first_generation:
            for _ in range(0, population):
                new_solution_example: tuple = SolutionExample(variables_in_the_list_points, first_point, last_point,
                                                              mutation_probability, is_first_population=True,
                                                              is_pmx_algorithm=is_pmx_algorithm).get_child()
                list_generation.append(new_solution_example)
        else:
            for _ in range(0, population):
                parent1: list = the_best_older_generation[random.randint(0, how_many_we_choose_the_best - 1)][0].copy()
                parent2: list = the_best_older_generation[random.randint(0, how_many_we_choose_the_best - 1)][0].copy()
                del parent1[0]
                del parent1[-1]
                del parent2[0]
                del parent2[-1]
                # print("#####################")
                # print(len(parent1))
                # print("TATATAT")
                # print(len(parent2))
                # print("#####################")
                new_solution_example: tuple = SolutionExample(variables_in_the_list_points, first_point, last_point,
                                                              mutation_probability, parent1, parent2, False,
                                                              is_pmx_algorithm).get_child()
                list_generation.append(new_solution_example)
        list_generation.sort(key=lambda x: x[1])
        self.list_the_best_generation = list_generation[0:how_many_we_choose_the_best]
        list_generation.clear()

    def get_the_best_children(self):
        return self.list_the_best_generation


# Generuje początkowy problem
def generate_points_list(how_many_points):
    list_points = []
    for _ in range(0, how_many_points):
        point = Point()
        list_points.append(point)
        print(point.get_x(), point.get_y())
    return list_points
