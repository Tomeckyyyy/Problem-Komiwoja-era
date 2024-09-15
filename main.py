import matplotlib.pyplot as plt
import generation

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!POCZĄTKOWE DANE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# how_many_points = input ("Ile ma być punktów")
# population_size = input ("Jaka ma być wielkość populacji?")
# how_many_we_choose_the_best = input ("Ilu najlepszych przekazujemy do tworzenia następnej generacji?")
# mutation_probability = input ("Jakie prawdopodobieństwo mutacji? (w procentach)")
# number_of_generations = input ("Jaka ma być maksymalna liczba generacji?")
how_many_points = 60
population_size = 300
how_many_we_choose_the_best = 30
mutation_probability = 3
number_of_generations = 500
is_pmx_algorithm = True

# Generowanie losowej listy punktów
list_points = generation.generate_points_list(how_many_points)
FIRST_POINT = list_points[0]
LAST_POINT = list_points[len(list_points) - 1]
variables_in_the_list_points = list_points[1:len(list_points) - 1]

# Generowanie pierwszej generacji
listX = []
listY = []
list_of_the_best_value_from_single_generation = []
generation_the_best_child = generation.Generation(variables_in_the_list_points, FIRST_POINT, LAST_POINT,
                                                  population_size, how_many_we_choose_the_best, True,
                                                  mutation_probability, is_pmx_algorithm).get_the_best_children()
for i in range(number_of_generations):
    generation_the_best_child = generation.Generation(variables_in_the_list_points, FIRST_POINT, LAST_POINT,
                                                      population_size, how_many_we_choose_the_best, False,
                                                      mutation_probability, generation_the_best_child,
                                                      is_pmx_algorithm).get_the_best_children()
    list_of_the_best_value_from_single_generation.append(generation_the_best_child[0][1])
    if i % 100 == 0:
        for point in generation_the_best_child[0][0]:
            listX.append(point.get_x())
            listY.append(point.get_y())
        plt.plot(listX, listY, 'ro', listX, listY, "b")
        plt.show()
        listX.clear()
        listY.clear()

for point in generation_the_best_child[0][0]:
    listX.append(point.get_x())
    listY.append(point.get_y())
plt.plot(listX, listY, 'ro', listX, listY, "b")
plt.show()
listX.clear()
listY.clear()

plt.plot([x for x in range(len(list_of_the_best_value_from_single_generation))],
         list_of_the_best_value_from_single_generation, "b")
plt.show()
