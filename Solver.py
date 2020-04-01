from InformedSearch import InformedSearch
from Maze import Maze


def read_matrix(file_n):
    f = open(file_n)
    n = f.readline()
    num_lines = str(n)
    list_chars = []
    l = f.readline()
    for c in l:
        list_chars.append(c)
    return num_lines, list_chars


if __name__ == "__main__":

    for i in range(31):
        file_name = "Mazes/Maze" + str(i) + ".txt"
        num, list_of_chars = read_matrix(file_name)
        n = int(num)
        write_file = "Mazes/Maze" + str(i) + "results.csv"
        with open(write_file, 'w') as file:
            file.write("Search Type, Solution Length, Visited Cells, Path, Total Time\n")
            searches = [InformedSearch.greedy(Maze(n, list_of_chars), 'm'), InformedSearch.greedy(Maze(n, list_of_chars), 'e'), InformedSearch.a_star(Maze(n, list_of_chars), 'm'),
                        InformedSearch.a_star(Maze(n, list_of_chars), 'e'), InformedSearch.gradient_descent(Maze(n, list_of_chars), 'm'), InformedSearch.gradient_descent(Maze(n, list_of_chars), 'e')]
            for s in searches:
                description = s
                file.write(description + "\n")
