from standard import is_standard, standardize
from deterministic import is_deterministic, is_complete, completion
from table_display import print_matrix
from word_recognition import word_recognition
from minimization import minimization

# Fonction pour filtrer les données d'une ligne


def filtrer_list(list_name, num_line, first_char, separator):
    return list_name[num_line][first_char:].split(separator)

# Fonction pour ouvrir un fichier txt + lire + trier


def ouverture(url):
    with open(url, 'r') as f:
        lines = f.read().splitlines()

        alphabet = filtrer_list(lines, 0, 4, ',')

        states = filtrer_list(lines, 1, 4, ',')

        initial_state = filtrer_list(lines, 2, 4, ',')

        final_state = filtrer_list(lines, 3, 4, ',')

        list_transitions = []
        for line in lines[4:]:
            list_transitions.append(line)

    return alphabet, states, initial_state, final_state, list_transitions

def complement(alphabet, states, initial, final, transitions):
    if (is_complete(alphabet, states, transitions) and is_deterministic(states, initial, transitions)) != True:
        print("One of these condition is not true")
        return False
    print("the automaton is complete deterministic !")
    new_array = []
    for s in states:
        if s not in final:
            new_array.append(s)
    final = new_array
    print_matrix(alphabet, states, initial, final, list_transitions)

if __name__ == '__main__':
    print('BEGIN\n')

    alphabet, states, initial, final, list_transitions = ouverture(
        "automata_test3.txt")

    complement(alphabet, states, initial, final, list_transitions)
    print_matrix(alphabet, states, initial, final, list_transitions)