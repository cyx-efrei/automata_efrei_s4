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

    # INITIALISATION OF THE TABLE
    x = PrettyTable()

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

    # WE WILL LOOK FOR ALL TRANSITIONS FOR EACH LETTER
    for letter in alphabet:
        list_transitions = []

        # WE WILL LOOK FOR EACH STATES
        for i in states:
            transition_string = ""

            # WE WILL LOOK FOR EACH TRANSITIONS FOR EACH STATES
            for transition in transitions:
                if transition[0] == i and transition[2] == letter:
                    transition_string += transition[4] + ","

            # SI ON NE TROUVE AUCUNE TRANSITION
            if transition_string == '':
                transition_string += "-"

            # WE ADD FOR THE LIST THAT WILL BE ADDED TO THE FINAL TABLE AND WE DELETE THE LAST CHAR WHICH IS A ","
            list_transitions.append(transition_string.strip(","))

        # WE ADD THE NEW COLUMN TO THE TABLE FOR EACH TRANSITION
        x.add_column("Transition " + letter, list_transitions)

    x.align = "c"
    print(x)


if __name__ == '__main__':
    print('BEGIN\n\n')

    alphabet, states, initial, final, list_transitions = ouverture(
        "automata_test.txt")
    print(alphabet, "lk")
    print_matrix(alphabet, states, initial, final, list_transitions)
