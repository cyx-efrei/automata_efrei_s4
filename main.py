from standard import is_standard, standardize
from deterministic import is_deterministic, is_complete, completion, determinisation
from table_display import print_matrix
from word_recognition import word_recognition
from minimization import minimization



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
    print("Please, enter your number of automaton to test :\n -> ", end="")
    file_name = -1
    while file_name < 1 or file_name > 44:
        file_name = int(input())

    return "./test/INT3-5-" + str(file_name) + ".txt"


def afficher_menu():
    print("1. TAP 1 display the table of the automate")
    print("2. TAP 2 to see if it's deterministic ")
    print("3. TAP 3 to see if it's standard")
    print("4. Word Recognation ")
    print("5. Quit")


if __name__ == '__main__':

    print("\n\n\n  ________  ________   ___   __  ____________              __  ______  __________  _   __")
    print(" /_  __/ / / / ____/  /   | / / / /_  __/ __ \            /  |/  /   |/_  __/ __ \/ | / /")
    print("  / / / /_/ / __/    / /| |/ / / / / / / / / /  ______   / /|_/ / /| | / / / / / /  |/ / ")
    print(" / / / __  / /___   / ___ / /_/ / / / / /_/ /  /_____/  / /  / / ___ |/ / / /_/ / /|  /  ")
    print("/_/ /_/ /_/_____/  /_/  |_\____/ /_/  \____/           /_/  /_/_/  |_/_/  \____/_/ |_/   \n")
    print("By Cyril Nakha, Ali Nahas , Nathan Krief , Paul Hu\n\n\n\n")

    file = choose_file()

    choice = 0
    choice_list = ["1", "2", "3", "4","5"]

    while choice != '4':
        afficher_menu()
        choice = input("Choice between 1 , 2 , 3 ,4 ,5: \n -> ")
        while choice not in choice_list:
            choice = input("Please redo: \n -> ")

        alphabet, states, initial, final, list_transitions = ouverture(file)

        if choice == "1":
            print_matrix(alphabet, states, initial, final, list_transitions)
            input("click on anything to return to the menu\n\n\n")

        elif choice == "2":
            print_matrix(alphabet, states, initial, final, list_transitions)
            print("\n\n-- TEST deterministic --")
            if is_deterministic(states, initial, list_transitions):
                print("It's deterministic\n")
                print("Let's see if it's deterministic complete\n")
                if is_complete(alphabet, states, list_transitions):
                    print("The automata is already deterministic complete\n")
                    input("\nNext step : Complementary. \nClick on anything to continue …\n")
                    print("jhbhjb")
                    complement(alphabet, states, initial, final, list_transitions)
                    input("click on anything to return to the menu\n\n\n")
                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    complement(alphabet, states, initial,
                               final, list_transitions)

                else:
                    print("It is no complete , so let's do it\n")

                    local_transitions, local_states = completion(alphabet, states, list_transitions)
                    print_matrix(alphabet, states, initial, final, list_transitions)
                    input("\nNext step : Complementary. \nClick on anything to continue …\n")
                    complement(alphabet, local_states, initial, final, local_transitions)
                    input("click on anything to return to the menu\n\n\n")
                    list_transitions, states = completion(
                        alphabet, states, list_transitions)
                    print_matrix(alphabet, states, initial,
                                 final, list_transitions)
                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    complement(alphabet, states, initial,
                               final, list_transitions)
            else:
                print("It's not deterministic \nlet's determinize it\n")

                local_transition, local_states, local_initial, local_final = determinisation(alphabet, states, initial,
                                                                                final, list_transitions)

                print_matrix(alphabet, local_states, local_initial,
                             local_final, local_transition)
                input("\nNext step : Completion. \nClick on anything to continue …\n")
                if is_complete(alphabet, local_states, local_transition):
                    print("The automata is already deterministic complete\n")
                    input("\nNext step : Complementary. \nClick on anything to continue …\n")
                    complement(alphabet, local_states, local_initial, local_final, local_transition)
                    input("click on anything to return to the menu\n\n\n")
                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    complement(alphabet, states, initial,
                               final, list_transitions)

                else:
                    print("It is no complete , so let's do it\n")

                    local_transition, local_states = completion(alphabet, local_states, local_transition)
                    print_matrix(alphabet, local_states, local_initial, local_final, local_transition)
                    input("\nNext step : Complementary. \nClick on anything to continue …\n")
                    complement(alphabet, local_states, local_initial, local_final, local_transition)
                    input("\nClick on anything to return to the menu\n\n\n")


                    list_transitions, local_states = completion(
                        alphabet, local_states, local_transition)
                    print_matrix(alphabet, local_states, initial,
                                 final, local_transition)
                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    complement(alphabet, states, initial,
                               final, list_transitions)

        elif choice == "3":
            print("\n\n-- TEST STANDARSIZATION : --")
            if is_standard(initial, list_transitions):
                print("is already standardize !\n\n\n")
                input("click on anything to return to the menu\n\n\n")
            else:
                print("let's standardize")
                standardize(alphabet, states, initial, final, list_transitions)
                input("click on anything to return to the menu\n\n\n")


        elif choice == "4":
            print("\n\n-- TEST Word Recognation  : --")

            word = "psp"
            while word != "end":
                print("\nEnter the word to recognize :\n -> ", end="")
                word = input()
                word_recognition(initial, final, list_transitions, word)
                input("click on anything to return to the menu\n\n\n")

        elif choice == "5":
            break



    print("\n\nbyeee")
