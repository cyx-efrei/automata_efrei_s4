from standard import is_standard, standardize
from deterministic import is_deterministic, is_complete, completion
from table_display import print_matrix
from word_recognition import word_recognition
from minimization import minimization

# Fonction pour filtrer les données d'une ligne


def filtrer_list(list_name, num_line, first_char, separator):
    return list_name[num_line][first_char:].split(separator)

# Fonction pour ouvrir un fichier txt + lire + trier


def complement(alphabet, states, initial, final, transitions):
    if is_complete(alphabet, states, transitions) and is_deterministic(states, initial, transitions) != True:
        print("One of these condition is not true")
        return False
    print("the automaton is complete deterministic !")
    new_array = []
    for s in states:
        if s not in final:
            new_array.append(s)
    final = new_array
    print_matrix(alphabet, states, initial, final, list_transitions)


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


if __name__ == '__main__':
    print('BEGIN\n')

    alphabet, states, initial, final, list_transitions = ouverture(
        "./test/INT3-5-37.txt")

    #print(alphabet, "\n", states, "\n", initial, "\n", final, "\n", list_transitions)

    print_matrix(alphabet, states, initial, final, list_transitions)

    #complement(alphabet, states, initial, final, list_transitions)

    # -- TEST MINIMIZATION

    #minimization(alphabet, states, initial, final, list_transitions)

    # END

    # -- TEST STANDARSIZATION :

    print(is_standard(initial, list_transitions))

    standardize(alphabet, states, initial, final, list_transitions)

    # END

    # -- TEST COMPLETE :

    # print(is_complete(alphabet, states, list_transitions))

    # list_transitions = completion(alphabet, states, list_transitions)

    # print_matrix(alphabet, states, initial, final, list_transitions)

    # END

    # -- TEST deterministic
    #print(is_deterministic(states, initial, list_transitions))

    # END

    # -- TEST WORD RECOGNITION :

    # print("Enter the word to recognize :\n ->", end="")
    # word = input()
    # word_recognition(initial, final, list_transitions, word)

    # END


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
