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

<<<<<<< HEAD
def is_deterministic(states, initial_state, accept_states, list_transition):

 # Vérification des états initiaux
    if len(initial_state) != 1:
        return False
    if initial_state[0] not in states:
        return False
# Vérification des états d'acceptation
    for i in accept_states:
        if i not in states:
=======

def is_deterministic(alphabet, states, initial, final, transitions):
 # Vérification des états initiaux
    if len(initial) != 1:
        return False

    '''   --------------------------------- INUTILE ???
    if initial[0] not in states:
        return False
    '''
    '''   --------------------------------- PAS CAPÉ ??
    # Vérification des états d'acceptation
    for accept_state in accept_states:
        if accept_state not in states:
>>>>>>> 4f32613d24bd44ea370cbd71afd5ab21327af288
            return False
'''
    # Vérifier que chaque transition a un seul symbole d'entrée
    for state in states:
        letter = set()
        for transition in transitions:
            if transition[0] == state:
                actual_letter = transition[2]
                if actual_letter in letter:
                    print("3")
                    return False
                letter.add(actual_letter)

    for state in states :
        list_transition = []
        for lettre in alphabet :
            for transition in list_transition:
                if lettre in transition[2] :
                    return False
                else:
                    list_transition.append(transition[2])



    #voir que chaque state envoie un fois et unique fois
    """for i in list_transition:
        if list_transition[i][2]== list_transition[i+1][2] and list_transition[i]== list_transition[i+1]:
            return False"""


# ENTRE FOR STATE ET FOR LATTER METTRE UNE CREATION DE TABLE


    return True


if __name__ == '__main__':
    print('BEGIN\n\n')

    alphabet, states, initial, final, list_transitions = ouverture(
        "automata_test.txt")

    print(alphabet, states, initial, final, list_transitions)
    print_matrix(alphabet, states, initial, final, list_transitions)

    print(is_deterministic(alphabet, states, initial, final, list_transitions))
