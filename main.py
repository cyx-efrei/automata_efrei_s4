from prettytable import PrettyTable

# Fonction pour filtrer les données d'une ligne


def filtrer_list(list_name, num_line, first_char, separator):
    return list_name[num_line][first_char:].split(separator)

# Fonction pour ouvrir un fichier txt + lire + trier


def ouverture(url):
    with open(url, 'r') as f:
        lines = f.read().splitlines()

        alphabet = filtrer_list(lines, 0, 4, ', ')

        states = filtrer_list(lines, 1, 4, ',')

        initial_state = filtrer_list(lines, 2, 4, ',')

        final_state = filtrer_list(lines, 3, 4, ',')

        list_transitions = []
        for line in lines[4:]:
            list_transitions.append(line)

    return alphabet, states, initial_state, final_state, list_transitions


# PRINT MATRIX
def get_arrow(i, initial, final):
    if i in initial and i in final:
        return ("<-->")
    else:
        if i in initial:
            return ("-->")
        else:
            if i in final:
                return ("<--")
            else:
                return ("")


# TO PRINT THE MATRIX, WE USE THE LIBRARY PRETTYTABLE
def print_matrix(alphabet, states, initial, final, transitions):
    x = PrettyTable()
    #x.field_names = [" ", "0"] + alphabet

    list_initial = []
    list_states = []
    for i in states:
        # FOR ARROW / FIRST COLUMN
        list_initial.append(get_arrow(i, initial, final))
        # FOR LIST OF STATES / SCD COLUMN
        list_states.append(i)

    # ON ADD LES LISTES AU TABLEAU
    x.add_column("", list_initial)
    x.add_column("STATES", list_states)

    # FOR TRANSITIONS
    for letter in alphabet:
        list_transitions = []
        for i in states:
            for transition in transitions:
                found = 0
                if transition[0] == i and transition[2] == letter:
                    found = 1
                    list_transitions.append(transition[4])
                    break
            if found == 0:
                list_transitions.append("--")
        x.add_column("Transition " + letter, list_transitions)

        print(list_transitions)

    print(x)


if __name__ == '__main__':
    print('BEGIN\n\n')

    alphabet, states, initial, final, list_transitions = ouverture(
        "automata_test.txt")
    print(alphabet, "lk")
    print_matrix(alphabet, states, initial, final, list_transitions)
