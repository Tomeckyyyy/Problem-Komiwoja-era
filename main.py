import matplotlib.pyplot as plt
import generation

# POCZĄTKOWE DANE

# how_many_points = input("Ile ma być punktów")
# population_size = input("Jaka ma być wielkość populacji?")
# how_many_we_choose_the_best = input("Ilu najlepszych przekazujemy do tworzenia następnej generacji?")
# mutation_probability = input("Jakie prawdopodobieństwo mutacji? (w procentach)")
# number_of_generations = input("Jaka ma być maksymalna liczba generacji?")
how_many_points = 13
population_size = 100
how_many_we_choose_the_best = 30
mutation_probability = 3
number_of_generations = 10

# Generowanie losowej listy punktów
list_points = generation.generate_points_list(how_many_points)
FIRST_POINT = list_points[0]
LAST_POINT = list_points[len(list_points)-1]
variables_in_the_list_points = list_points[1:len(list_points)]

# Generowanie pierwszej generacji
listX = []
listY = []
first_generation = generation.FirstGeneration(variables_in_the_list_points, population_size).get_the_best_children()
for single_first_generation in first_generation:
    for i in single_first_generation:
        listX.append(i.get_x())
        listY.append(i.get_y())
    plt.plot(listX, listY, 'ro', listX, listY, "b")
    plt.show()
    listX.clear()
    listY.clear()
for _ in range(0, number_of_generations):
    for single_next_generation in first_generation:
        next_generation = generation.Generation(first_generation).get_the_best_children()
        for i in single_next_generation:
            listX.append(i.get_x())
            listY.append(i.get_y())
        plt.plot(listX, listY, 'ro', listX, listY, "b")
        plt.show()
        listX.clear()
        listY.clear()
