from standard import is_standard, standardize
from deterministic import is_deterministic, is_complete, completion, determinisation
from table_display import print_matrix
from word_recognition import word_recognition
from minimization import minimization

import time

# def pour le time sleep


def sleep():
    time.sleep(0.2)

# Fonction pour filtrer les données d'une ligne


def filtrer_list(list_name, num_line, first_char, separator):
    return list_name[num_line][first_char:].split(separator)

# Fonction pour ouvrir un fichier txt + lire + trier


def complement(alphabet, states, initial, final, transitions):
    if is_complete(alphabet, states, transitions) != True:
        print("It is not complete")
        return False
    if is_deterministic(states, initial, transitions) != True:
        print("the automaton is not deterministic !")
        return False
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


def choose_file():
    print("Please, enter your number of automaton to test :\n -> ", end="")
    file_name = -1
    while file_name < 1 or file_name > 44:
        file_name = int(input())

    return "./test/INT3-5-" + str(file_name) + ".txt"


def afficher_menu():
    print("1. TAP 1 display the table of the automate")
    print("2. TAP 2 to see if it's deterministic ")
    print("3. TAP 3 to see if it's standard")
    print("4. Quitter")


if __name__ == '__main__':

    print("\n\n\n  ________  ________   ___   __  ____________              __  ______  __________  _   __")
    print(" /_  __/ / / / ____/  /   | / / / /_  __/ __ \            /  |/  /   |/_  __/ __ \/ | / /")
    print("  / / / /_/ / __/    / /| |/ / / / / / / / / /  ______   / /|_/ / /| | / / / / / /  |/ / ")
    print(" / / / __  / /___   / ___ / /_/ / / / / /_/ /  /_____/  / /  / / ___ |/ / / /_/ / /|  /  ")
    print("/_/ /_/ /_/_____/  /_/  |_\____/ /_/  \____/           /_/  /_/_/  |_/_/  \____/_/ |_/   \n\n")

    file = choose_file()

    choice = 0
    choice_list = ["1", "2", "3", "4"]

    while choice != '4':
        afficher_menu()
        choice = input("Choice between 1 , 2 , 3 or 4: \n -> ")
        while choice not in choice_list:
            choice = input("Please redo: \n -> ")

        alphabet, states, initial, final, list_transitions = ouverture(file)

        if choice == "1":
            print_matrix(alphabet, states, initial, final, list_transitions)

        elif choice == "2":
            print_matrix(alphabet, states, initial, final, list_transitions)
            print("\n\n-- TEST deterministic --")
            if is_deterministic(states, initial, list_transitions):
                print("It's deterministic ")
                print("Let's see if it's deterministic complete ")
                if is_complete(alphabet, states, list_transitions):
                    print("The automata is already deterministic complete")
                else:
                    print("It is no complete , so let's do it")

                    list_transitions, states = completion(
                        alphabet, states, list_transitions)

                    print_matrix(alphabet, states, initial,
                                 final, list_transitions)
            else:
                deter_automaton(alphabet, states, initial,
                                final, list_transitions)

        elif choice == "3":
            print("\n\n-- TEST STANDARSIZATION : --")
            if is_standard(initial, list_transitions):
                print("is already standardize !\n\n\n")
            else:
                print("let's standardize")
                standardize(alphabet, states, initial, final, list_transitions)

    print("\n\nbyeee")

    # MENU CYRIL

    # file = "./test/INT3-5-39.txt"

    # print('BEGIN =================== \n', file)

    # alphabet, states, initial, final, list_transitions = ouverture(
    #     file)

    # #print(alphabet, "\n", states, "\n", initial, "\n", final, "\n", list_transitions)

    # print_matrix(alphabet, states, initial, final, list_transitions)

    # #complement(alphabet, states, initial, final, list_transitions)

    # print("\n\n-- TEST MINIMIZATION --")

    # minimization(alphabet, states, initial, final, list_transitions)

    # # END

    # print("\n\n-- TEST STANDARSIZATION : --")

    # if is_standard(initial, list_transitions):
    #     print("is already standardize !")
    # else:
    #     print("let's standardize")
    #     standardize(alphabet, states, initial, final, list_transitions)

    # # END

    # print("\n\n-- TEST deterministic --")
    # print(is_deterministic(states, initial, list_transitions))

    # # END

    # print("\n\n-- TEST COMPLETE : --")

    # if is_complete(alphabet, states, list_transitions):
    #     print("already complete")
    # else:
    #     print("let's complete")

    #     list_transitions, states = completion(
    #         alphabet, states, list_transitions)

    #     print_matrix(alphabet, states, initial, final, list_transitions)

    # # END

    # print("\n\n-- TEST WORD RECOGNITION : --")

    # word = "psp"
    # while word != "pp":
    #     print("Enter the word to recognize :\n ->", end="")
    #     word = input()
    #     word_recognition(initial, final, list_transitions, word)

    # # END
    # print("\n\n-- TEST COMPLEMENT : --")

    # complement(alphabet, states, initial, final, list_transitions)


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
