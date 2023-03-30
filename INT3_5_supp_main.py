import time


# Fonction of the main menu

def afficher_menu():
    print("\n\n\n\n==================== MAIN MENU ====================\n")
    print("1. TAP 1 - Display the table of the automate")
    print("2. TAP 2 - See if it's deterministic    --    Determinise it if not")
    print("3. TAP 3 - See if it's standard         --    Standardize it if not")
    print("4. TAP 4 - Word Recognation")
    print("5. TAP 5 - Change your automaton")
    print("6. TAP 6 - Quit")


# Fonction pour choisir l'automate

def choose_file():
    print("Please, enter your number of automaton to test :\n", end="")
    file_name = str(input("-> "))
    while file_name.isalpha():
        print("\nPlease redo :")
        file_name = str(input("-> "))
        if (file_name.isalpha()):
            continue
        else:
            break
    file_name = int(file_name)
    while file_name < 1 or file_name > 44:
        print("\nPlease redo :")
        file_name = int(input("-> "))
        if (file_name < 1 or file_name > 44):
            continue

    return "./INT3_5_automate/INT3_5_" + str(file_name) + ".txt"


# Fonction pour filtrer les données d'une ligne

def filtrer_list(list_name, num_line, first_char, separator):
    return list_name[num_line][first_char:].split(separator)


# Fonction pour ouvrir un fichier txt + lire + trier

def ouverture(url):
    with open(url, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

        alphabet = filtrer_list(lines, 0, 4, ',')

        states = filtrer_list(lines, 1, 4, ',')

        initial_state = filtrer_list(lines, 2, 4, ',')

        final_state = filtrer_list(lines, 3, 4, ',')

        list_transitions = []
        for line in lines[4:]:
            list_transitions.append(line)

        if len(alphabet) == 1 and alphabet[0] == "":
            alphabet = []

    return alphabet, states, initial_state, final_state, list_transitions


# Fonction pour afficher progressivement un mot

def print_progressively(word):
    time.sleep(0.2)
    for i in word:
        time.sleep(0.2)
        # J'UTILISE FLUSH ICI POUR QUE ÇA AFFICHE PAR CHAR ET A
        print(i, end="", flush=True)
    time.sleep(0.2)
    print("\n")


#  FROM THERE, WE CONTROL ALL THE TIME SLEEP

def await_time():
    time.sleep(0.5)
