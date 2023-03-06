from standard import is_standard, standardize
from table_display import print_matrix

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


# TO COMPLETE AN AUTOMATON
def complete(alphabet, states, initial, final, transitions):
    for state in states:
        letters = set()
        for transition in transitions:
            if transition[0] == state:
                actual_letter = transition[2]
                if actual_letter not in letters:
                    letters.add(actual_letter)
        print(letters)
        # for values in letters:
        for l_alphabet in alphabet:
            if l_alphabet not in letters:
                transitions.append(state + "," + l_alphabet + ",P")

    print_matrix(alphabet, states, initial, final, transitions)
    print(is_standard(states, initial, final, list_transitions))


if __name__ == '__main__':
    print('BEGIN\n\n')

    alphabet, states, initial, final, list_transitions = ouverture(
        "automata_test.txt")

    #print(alphabet, "\n", states, "\n", initial, "\n", final, "\n", list_transitions)

    print_matrix(alphabet, states, initial, final, list_transitions)
    print(is_standard(states, initial, final, list_transitions))

    # print(is_standard(alphabet, states, initial, final, list_transitions))

    #complete(alphabet, states, initial, final, list_transitions)
    standardize(alphabet, states, initial, final, list_transitions)
