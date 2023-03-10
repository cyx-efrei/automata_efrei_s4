from table_display import print_matrix


def is_standard(states, initial, final, transitions):
    """
    Vérifie si un automate est standard ou non.
    Un automate est standard si:
    - il a un seul état initial
    - tous les états finaux sont distincts
    - il n'y a pas de transitions avec epsilon comme symbole d'entrée ??????
    - chaque transition a un seul symbole d'entrée
    """
    # Vérifier s'il y a un seul état initial
    if len(initial) != 1:
        return False

    ''' INUTILE !!!!
    # Vérifier que tous les états finaux sont distincts
    if len(set(final)) != len(final):
        print("2")
        return False
        '''

    for transition in transitions:
        if transition[4] == initial[0]:
            print(transition[4])
            return False

    ''' PAS AU BON ENDROIT
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
    '''

    # Si toutes les conditions sont satisfaites, l'automate est standard
    print("Automate standard")
    return True


# to standardize an automaton
def standardize(alphabet, states, initials, final, transitions):
    if len(initials) >= 1:
        new_initials = []
        for initial in initials:
            for transition in transitions:
                if transition[0] == initial:
                    #print("i" + transition[1:])
                    if "i" + transition[1:] not in transitions:
                        transitions.append("i" + transition[1:])
    initials = "i"
    states.append("i")
    print_matrix(alphabet, states, initials, final, transitions)
    print(is_standard(states, initials, final, transitions))
