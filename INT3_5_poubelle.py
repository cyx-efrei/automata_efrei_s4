# Pour obtenir les valeurs sous la forme d'un tableaud

def split_values_in_table(entries):
    print("\n\n-- RECUPERATION --")
    for i in entries:
        print(i, " ligne 1")
        splitEntries = [line.split(" ") for line in entries]
    print("End\n")

    return splitEntries


# Def pour print une matrice

def temporary_print_matrix(matrix):
    print("-- MATRIX --")
    for line in matrix:
        print("[", end="")
        for i in line:
            print(i, end=" ")
        print("]")


def recup_infos(matrix):
    alphabet = ""
    states = ""
    initial = ""
    final = ""
    for letter in splitEntries:
        # To get the alphabet
        if letter[0] == 'A':
            for i in letter:
                if (i > 'a' and i < 'z'):
                    alphabet += i

        # To get the states
        if letter[0] == 'Q':
            for i in letter:
                if (i >= '0' and i <= '9'):
                    states += str(i)

        # To get the initial states
        if letter[0] == 'I':
            for i in letter:
                if (i >= '0' and i <= '9'):
                    initial += str(i)

        # To get the final states
        if letter[0] == 'T':
            for i in letter:
                if (i >= '0' and i <= '9'):
                    final += str(i)

    alphabet = alphabet.split(",")
    print("alphabet :", alphabet)
    states = states.split(",")
    print("states :", states)
    initial = initial.split(",")
    print("initial :", initial)
    final = final.split(",")
    print("final :", final)
    return alphabet, states, initial, final
