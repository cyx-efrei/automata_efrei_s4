# Fonction pour ouvrir un fichier txt + lire + lecture

def ouverture(url):
    with open(url, 'r') as f:
        entries = [line.strip() for line in f]
    print(entries, "iuhuhbj")
    return entries

# Pour obtenir uniquement les valeurs


def split_values_in_table(entries):
    print("\n\n-- RECUPERATION --")
    for i in entries:
        print(i, " ligne 1")
        splitEntries = [line.split(" ") for line in entries]
    print("End\n\n")

    return splitEntries

# Def pour print une matrice


def temporary_print_matrix(matrix):
    print("-- MATRIX --")
    for line in matrix:
        print("[", end="")
        for i in line:
            print(i, end=" ")
        print("]")


if __name__ == '__main__':
    print('BEGINNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN')
    entries = ouverture("automata_test.txt")
    splitEntries = split_values_in_table(entries)
    print(splitEntries, " ligne 2")
    temporary_print_matrix(splitEntries)
