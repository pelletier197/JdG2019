import sys

sys.setrecursionlimit(100000)
etages = []
nb_etage_courant = 0
etage_courant = []

split = lambda A, n: [A[i:i + n] for i in range(0, len(A), n)]
with open('mountain.txt') as file:
    [height, width, nb_etages] = file.readline().split(" ")
    height = int(height)
    width = int(width)
    nb_etages = int(nb_etages)

    print('width', width, 'height', height, 'nb etages', nb_etages)
    for i in range(nb_etages):
        line = file.readline().replace("\n", "").replace("\r", "").split(" ")
        etages.append(split(line, width))


def find(value):
    for i in range(height):
        for j in range(width):
            for k in range(nb_etages):
                if etages[k][i][j] == value:
                    return i, j, k


start_x, start_y, etage_debut = find('100')
end_x, end_y, etage_fin = find("101")

for i in etages[0]:
    print(i)
print('-' * 20)
for i in etages[1]:
    print(i)
print('-' * 20)
for i in etages[2]:
    print(i)


def can_walk(i, j, k):
    return etages[k][i][j] == '0' or etages[k][i][j] == '12' or etages[k][i][j] == '11' or etages[k][i][j] == '10' or \
           etages[k][i][j] == '101'


def solve(current_x, current_y, etage_courant, visited, movements):
    visited[etage_courant][current_x][current_y] = True
    print(visited)
    print(current_x, current_y, etage_courant)
    if current_x == end_x and current_y == end_y and etage_courant == etage_fin:
        return True, movements

    # A droite
    if current_y < width - 1 and can_walk(current_x, current_y + 1, etage_courant) and not \
            visited[etage_courant][current_x][current_y + 1]:
        new_mvm = movements[:]
        new_mvm.append(4)
        solved, new_mvm = solve(current_x, current_y + 1, etage_courant, visited, new_mvm)
        if solved:
            return solved, new_mvm

    # En bas
    if current_x < height - 1 and can_walk(current_x + 1, current_y, etage_courant) and not \
            visited[etage_courant][current_x + 1][current_y]:
        new_mvm = movements[:]
        new_mvm.append(3)
        solved, new_mvm = solve(current_x + 1, current_y, etage_courant, visited, new_mvm)
        if solved:
            return solved, new_mvm

    # A gauche
    if current_y > 0 and can_walk(current_x, current_y - 1, etage_courant) and not \
            visited[etage_courant][current_x][current_y - 1]:
        new_mvm = movements[:]
        new_mvm.append(2)
        solved, new_mvm = solve(current_x, current_y - 1, etage_courant, visited, new_mvm)
        if solved:
            return solved, new_mvm

    # En haut
    if current_x > 0 and can_walk(current_x - 1, current_y, etage_courant) and not \
            visited[etage_courant][current_x - 1][current_y]:
        new_mvm = movements[:]
        new_mvm.append(1)
        solved, new_mvm = solve(current_x - 1, current_y, etage_courant, visited, new_mvm)
        if solved:
            return solved, new_mvm

    # Monter
    if (etages[etage_courant][current_x][current_y] == '10' or etages[etage_courant][current_x][
        current_y] == '12') and not \
            visited[etage_courant + 1][current_x][current_y]:
        new_mvm = movements[:]
        new_mvm.append(5)
        solved, new_mvm = solve(current_x, current_y, etage_courant + 1, visited, new_mvm)
        if solved:
            return solved, new_mvm

    # Descendre
    if (etages[etage_courant][current_x][current_y] == '11' or etages[etage_courant][current_x][
        current_y] == '12') and not \
            visited[etage_courant - 1][current_x][current_y]:
        new_mvm = movements[:]
        new_mvm.append(5)
        solved, new_mvm = solve(current_x, current_y, etage_courant - 1, visited, new_mvm)
        if solved:
            return solved, new_mvm

    return False, []


visited = [[[False for j in range(width)] for i in range(height)] for i in range(nb_etages)]
print(visited)

print(solve(start_x, start_y, etage_debut, visited, []))
