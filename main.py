from standard import is_standard, standardize
from deterministic import is_deterministic, is_complete, completion, determinisation
from table_display import print_matrix
from word_recognition import word_recognition
from minimization import minimization

from supp_main import *


# Fonction pour filtrer les données d'une ligne


def filtrer_list(list_name, num_line, first_char, separator):
    return list_name[num_line][first_char:].split(separator)

# Fonction pour ouvrir un fichier txt + lire + trier


def complement(alphabet, states, initial, final, transitions):

    new_array = []
    for s in states:
        if s not in final:
            new_array.append(s)
    final = new_array
    print_matrix(alphabet, states, initial, final, transitions)


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
    print("Please, enter your number of automaton to test :\n", end="")
    file_name = -1
    while file_name < 1 or file_name > 44:
        file_name = int(input("-> "))
        if (file_name < 1 or file_name > 44):
            print("\nPlease redo :")

    return "./test/INT3-5-" + str(file_name) + ".txt"


def afficher_menu():
    print("\n\n\n\n==================== MAIN MENU ====================\n")
    print("1. TAP 1 - Display the table of the automate")
    print("2. TAP 2 - See if it's deterministic    --    Determinise it if not")
    print("3. TAP 3 - See if it's standard         --    Standardize it if not")
    print("4. TAP 4 - Word Recognation")
    print("5. TAP 5 - Change your automaton")
    print("6. TAP 6 - Quit")


if __name__ == '__main__':

    # alphabet, states, initial, final, list_transitions = ouverture(
    #     "./test/INT3-5-6.txt")

    # minimization(alphabet, states, initial, final, list_transitions)

    print("\n\n\n  ________  ________   ___   __  ____________              __  ______  __________  _   __")
    print(" /_  __/ / / / ____/  /   | / / / /_  __/ __ \            /  |/  /   |/_  __/ __ \/ | / /")
    print("  / / / /_/ / __/    / /| |/ / / / / / / / / /  ______   / /|_/ / /| | / / / / / /  |/ / ")
    print(" / / / __  / /___   / ___ / /_/ / / / / /_/ /  /_____/  / /  / / ___ |/ / / /_/ / /|  /  ")
    print("/_/ /_/ /_/_____/  /_/  |_\____/ /_/  \____/           /_/  /_/_/  |_/_/  \____/_/ |_/   \n")
    print("By Cyril Nakha, Ali Nahas , Nathan Krief , Paul Hu\n\n\n\n")

    # WE FIRST CHOSE THE AUTOMATON AND THEN TAKE EVERYTHING
    file = choose_file()
    alphabet, states, initial, final, list_transitions = ouverture(file)

    choice = 0
    choice_list = ["1", "2", "3", "4", "5", "6"]

    while choice != '6':
        afficher_menu()
        choice = input("\nYour choice : \n -> ")
        while choice not in choice_list:
            choice = input("\nPlease redo: \n -> ")

        if choice == "1":
            print("\n\n\n\n==================== DISPLAY AUTOMATON ====================\n")
            print_matrix(alphabet, states, initial, final, list_transitions)
            input("\nClick on anything to return to the menu\n")

        elif choice == "2":
            print("\n\n\n\n==================== DETERMINISTIC ====================\n")
            print("     - There is your default automaton : \n\n")
            print_matrix(alphabet, states, initial, final, list_transitions)
            # input("\nClick on anything to continue\n")
            print("\nIs your automaton determinized ? \n -> ", end="")

            # IF THE AUTOMATON IS DETERMINIZED
            if is_deterministic(states, initial, list_transitions):
                print_progressively("yes !")
                input("\nNext step : Completion !\nClick on anything to continue\n")
                # await_time()
                print(
                    "\n==================== COMPLETION PART ====================")
                print("\nIs your automaton complete ? \n -> ", end="")

                # IF IT'S COMPLETE
                if is_complete(alphabet, states, list_transitions):
                    print_progressively("yes !")
                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    print(
                        "\n==================== COMPLEMENT PART ====================\n")
                    complement(alphabet, states, initial,
                               final, list_transitions)

                    input(
                        "\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

                # IF IT'S NOT COMPLETE

                else:
                    print(
                        "\n==================== COMPLETION PART ====================\n")
                    local_transitions, local_states = completion(
                        alphabet, states, list_transitions)

                    print("There is your complete deterministic automaton : \n")
                    print_matrix(alphabet, states, initial,
                                 final, list_transitions)

                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    print(
                        "\n==================== COMPLEMENT PART ====================\n")
                    print("There is the complement automaton : \n")

                    complement(alphabet, local_states, initial,
                               final, local_transitions)

                    input(
                        "\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

            # IF THE AUTOMATON IS NOT DETERMINIZED
            else:
                print_progressively("NO !")
                print("\n======== DETERMINIZATION")

                local_transition, local_states, local_initial, local_final = determinisation(alphabet, states, initial,
                                                                                             final, list_transitions)
                print("There is the deterministic automaton : \n")
                print_matrix(alphabet, local_states, local_initial,
                             local_final, local_transition)
                input("\nNext step : Completion !\nClick on anything to continue\n")

                print(
                    "\n==================== COMPLETION PART ====================")
                print("\nIs your automaton complete ? \n -> ", end="")

                # COMPLETION
                if is_complete(alphabet, local_states, local_transition):
                    print_progressively("yes !")
                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    print(
                        "\n==================== COMPLEMENT PART ====================\n")
                    complement(alphabet, local_states, local_initial,
                               local_final, local_transition)

                    input(
                        "\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

                # IF IT'S NOT COMPLETE
                else:
                    print(
                        "\n==================== COMPLETION PART ====================\n")

                    local_transition, local_states = completion(
                        alphabet, local_states, local_transition)

                    print("There is your complete deterministic automaton : \n")
                    print_matrix(alphabet, local_states,
                                 local_initial, local_final, local_transition)

                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    print(
                        "\n==================== COMPLEMENT PART ====================\n")
                    print("There is the complement automaton : \n")

                    complement(alphabet, local_states, local_initial,
                               local_final, local_transition)

                    input(
                        "\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

        # IS STANDARD ?
        elif choice == "3":
            print("\n\n\n\n==================== STANDARDIZATION ====================\n")

            print("\nIs your automaton standardize ? \n -> ", end="")

            # IF IT IS STANDARD
            if is_standard(initial, list_transitions):
                print_progressively("yes !")
                input("\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

            # IF IT IS NOT STANDARD
            else:
                input("\nNext step : Standardization !\nClick on anything to continue\n")
                print("\nThere is the standardize automaton\n")
                standardize(alphabet, states, initial, final, list_transitions)
                input("\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

        elif choice == "4":
            print("\n\n\n\n==================== Word Recognation ====================\n")

            word = "psp"
            while word != "end":
                print("\nEnter the word to recognize :\n -> ", end="")
                word = input()
                word_recognition(initial, final, list_transitions, word)
            input("\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

        elif choice == "5":
            print("\n\n")
            print("==================== CHANGE AUTOMATON ====================\n")
            file = choose_file()
            alphabet, states, initial, final, list_transitions = ouverture(
                file)

        # TO LEAVE
        elif choice == "6":
            break

    print("\n\nI finished my work for today ! Bye !")
