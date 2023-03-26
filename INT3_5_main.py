from INT3_5_standard import *
from INT3_5_deterministic import *
from INT3_5_table_display import *
from INT3_5_word_recognition import *
from INT3_5_minimization import minimization
from INT3_5_complementary import *
from INT3_5_supp_main import *


if __name__ == '__main__':

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
            if is_deterministic(alphabet, states, initial, list_transitions):
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
                               final, list_transitions, 0)

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
                               final, local_transitions, 0)

                    input(
                        "\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

            # IF THE AUTOMATON IS NOT DETERMINIZED
            else:
                print_progressively("NO !")
                print("\n======== DETERMINIZATION")

                local_alphabet, local_transition, local_states, local_initial, local_final = determinisation(alphabet, states, initial,
                                                                                             final, list_transitions)
                print("There is the deterministic automaton : \n")
                print_matrix(local_alphabet, local_states, local_initial,
                             local_final, local_transition)
                input("\nNext step : Completion !\nClick on anything to continue\n")

                print(
                    "\n==================== COMPLETION PART ====================")
                print("\nIs your automaton complete ? \n -> ", end="")

                # COMPLETION
                if is_complete(local_alphabet, local_states, local_transition):
                    print_progressively("yes !")
                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    print(
                        "\n==================== COMPLEMENT PART ====================\n")
                    complement(local_alphabet, local_states, local_initial,
                               local_final, local_transition, 0)

                    input(
                        "\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

                # IF IT'S NOT COMPLETE
                else:
                    print(
                        "\n==================== COMPLETION PART ====================\n")

                    local_transition, local_states = completion(
                        local_alphabet, local_states, local_transition)

                    print("There is your complete deterministic automaton : \n")
                    print_matrix(local_alphabet, local_states,
                                 local_initial, local_final, local_transition)

                    input(
                        "\nNext step : Complementary. \nClick on anything to continue …\n")
                    print(
                        "\n==================== COMPLEMENT PART ====================\n")
                    print("There is the complement automaton : \n")

                    complement(local_alphabet, local_states, local_initial,
                               local_final, local_transition, 0)

                    input(
                        "\nReturn to the MAIN MENU. \nClick on anything to continue …\n")

        # IS STANDARD ?
        elif choice == "3":

            # On reinitialise au cas ou
            alphabet, states, initial, final, list_transitions = ouverture(file)

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

            choice = '3'
            print("Do you want to recognize a word on the automate or its complementary ?\n 1. This automate\n 2. The complementary")
            while choice <'1' or choice>'2' :
                choice = input("\n -> ")
            if choice == '2':
                local_final = final
                final = complement(local_alphabet, local_states, local_initial, local_final, local_transition, 1)
            word = "psp"
            while word != "end":
                print("\nEnter \"end\" to stop the loop.\nEnter the word to recognize :\n -> ", end="")
                word = input()
                word_recognition(alphabet, states, initial, final, list_transitions, word)
            input("\nReturn to the MAIN MENU. \nClick on anything to continue …\n")
            if choice == '2':
                final = local_final

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
