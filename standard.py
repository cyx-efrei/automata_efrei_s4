from table_display import print_matrix


def is_standard(initial, transitions):

    # Vérifier s'il y a un seul état initial
    if len(initial) != 1:
        return False

    for transition in transitions:
        if transition[4] == initial[0]:
            print(
                "There is a transition to the initial state so the automaton is not standard !")
            return False

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
    print(is_standard(initials, transitions))
