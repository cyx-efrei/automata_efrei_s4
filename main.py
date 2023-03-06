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
                transition_string += "---"

            # WE ADD FOR THE LIST THAT WILL BE ADDED TO THE FINAL TABLE AND WE DELETE THE LAST CHAR WHICH IS A ","
            list_transitions.append(transition_string.strip(","))

        # WE ADD THE NEW COLUMN TO THE TABLE FOR EACH TRANSITION
        x.add_column("Transition " + letter, list_transitions)

    x.align = "c"
    print(x)

def est_standard(alphabet, states, initial, final, transitions):
    """
    Vérifie si un automate est standard ou non.
    Un automate est standard si:
    - il a un seul état initial
    - tous les états finaux sont distincts
    - il n'y a pas de transitions avec epsilon comme symbole d'entrée
    - chaque transition a un seul symbole d'entrée
    """
    # Vérifier s'il y a un seul état initial
    if len(initial) != 1:
        return False
    # Vérifier que tous les états finaux sont distincts
    if len(set(final)) != len(final):
        return False
    # Vérifier s'il y a des transitions avec epsilon comme symbole d'entrée
    for transition in transitions:
        if transition[2] == 'epsilon':
            return False
    # Vérifier que chaque transition a un seul symbole d'entrée
    for state in states:
        symbols = set()
        for transition in transitions:
            if transition[0] == state:
                symbol = transition[2]
                if symbol in symbols:
                    return False
                symbols.add(symbol)
    # Si toutes les conditions sont satisfaites, l'automate est standard
    print("Automate standard")
    return True

def est_deterministe(alphabet, states, initial, final, transitions):
    """
    Vérifie si un automate est déterministe ou non.
    Un automate est déterministe si chaque état a exactement une transition
    sortante pour chaque symbole d'entrée de l'alphabet.
    """
    # Créer un dictionnaire de transitions pour chaque état et symbole d'entrée
    trans_dict = {}
    for state in states:
        trans_dict[state] = {}
        for sym in alphabet:
            trans_dict[state][sym] = []

    for transition in transitions:
        source_state = transition[0]
        input_sym = transition[2]
        dest_state = transition[4]

        # Vérifier que l'état source, le symbole d'entrée et l'état de destination sont valides
        if source_state not in states:
            print(f"Erreur: l'état source {source_state} n'est pas valide.")
            return
        if input_sym not in alphabet:
            print(f"Erreur: le symbole d'entrée {input_sym} n'est pas valide.")
            return
        if dest_state not in states:
            print(f"Erreur: l'état de destination {dest_state} n'est pas valide.")
            return

        # Ajouter la transition au dictionnaire de transitions
        trans_dict[source_state][input_sym].append(dest_state)

    # Vérifier que chaque état a exactement une transition sortante pour chaque symbole d'entrée
    for state in states:
        for sym in alphabet:
            if len(trans_dict[state][sym]) > 1:
                print(f"L'état {state} a plusieurs transitions sortantes pour le symbole d'entrée {sym}.")
                print("N'est pas déterministe")
                return
            elif len(trans_dict[state][sym]) == 0:
                print(f"L'état {state} n'a pas de transition sortante pour le symbole d'entrée {sym}.")
                print("N'est pas déterministe")
                return

    # Si toutes les conditions sont satisfaites, l'automate est déterministe
    print("Est déterministe")



if __name__ == '__main__':
    print('BEGIN\n\n')

    alphabet, states, initial, final, list_transitions = ouverture(
        "automata_test.txt")
    est_deterministe(alphabet, states, initial, final, list_transitions)
    print_matrix(alphabet, states, initial, final, list_transitions)

