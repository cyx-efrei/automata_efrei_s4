
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


if __name__ == '__main__':
    print('BEGIN\n\n')

    alphabet, states, initial, final = ouverture("automata_test.txt")


def is_deterministic(states, start_states, accept_states):
 # Vérification des états initiaux
    if len(start_states) != 1:
        return False
    if start_states[0] not in states:
        return False

    # Vérification des états d'acceptation
    for accept_state in accept_states:
        if accept_state not in states:
            return False

    return True
