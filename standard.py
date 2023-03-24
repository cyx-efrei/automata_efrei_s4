from table_display import print_matrix
from supp_main import print_progressively


def is_standard(initial, transitions):

    # Vérifier s'il y a un seul état initial
    if len(initial) != 1:
        print_progressively("NO !")
        print("\nExplanation : Your automaton has more than 1 entry")
        return False

    for transition in transitions:
        if transition[4] == initial[0]:
            print_progressively("NO !")
            print(
                "\nExplanation : There is a transition to the initial state so the automaton is not standard !")
            return False

    # Si toutes les conditions sont satisfaites, l'automate est standard
    return True


# to standardize an automaton
def standardize(alphabet, states, initials, final, transitions):
    if len(initials) >= 1:
        new_initials = []
        for initial in initials:
            for transition in transitions:
                if transition[0] == initial:
                    if "i" + transition[1:] not in transitions:
                        transitions.append("i" + transition[1:])
                    if (transition[-1] in final and "i" not in final):
                        final.append("i")
    initials = "i"
    states.append("i")
    print_matrix(alphabet, states, initials, final, transitions)
    # print(is_standard(initials, transitions))
