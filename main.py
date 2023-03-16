from standard import is_standard, standardize
from deterministic import is_deterministic, is_complete, determinization_and_completion, completion
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


if __name__ == '__main__':
    print('BEGIN\n\n')

    alphabet, states, initial, final, list_transitions = ouverture(
        "automata_test.txt")

    #print(alphabet, "\n", states, "\n", initial, "\n", final, "\n", list_transitions)

    print_matrix(alphabet, states, initial, final, list_transitions)
    #print(is_standard(states, initial, final, list_transitions))
    #print(is_deterministic(states, initial, list_transitions))

    print("NEW \n\n\n")
    print_matrix(alphabet, states, initial, final, list_transitions)

    # print(is_standard(alphabet, states, initial, final, list_transitions))

    #complete(alphabet, states, initial, final, list_transitions)
    #standardize(alphabet, states, initial, final, list_transitions)


    # Adding all the information about the automaton in a dictionary for easy use
    automaton = {
        "alphabet": alphabet,
        "states": states,
        "initials": initial,
        "finals": final,
        "transitions": list_transitions
    }

    if is_deterministic(automaton) and is_complete(automaton):
        CDFA = automaton # Complete Deterministic Finite Automaton
    else:
        NFA = automaton # Non Finite Automaton
        DFA = determinization_and_completion(NFA) # Definite Finite Automaton
        CDFA = DFA if is_complete(DFA) else completion(DFA) # Complete Deterministic Finite Automaton

    print_matrix(CDFA)

''' ----------- MENU FOR COMPLETION
    if (is_complete(alphabet, states, list_transitions)) == False:
        r = "0"
        print("\nDo you want us to make the completion ? (y/n)\n ->", end="")
        r = input()
        while (r != 'y' or r != 'n'):
            print("\nPlease enter y for yes or n for no\n ->", end="")
            r = input()
        if r == "y":
            list_transitions = completion(alphabet, states, list_transitions)
'''
