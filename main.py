
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

    return alphabet, states, initial_state, final_state

def is_deterministic(states, initial_state, accept_states, list_transition):

 # Vérification des états initiaux
    if len(initial_state) != 1:
        return False
    if initial_state[0] not in states:
        return False
# Vérification des états d'acceptation
    for i in accept_states:
        if i not in states:
            return False

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

    alphabet, states, initial, final = ouverture("automata_test.txt")



