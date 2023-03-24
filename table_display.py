# TO PRINT THE MATRIX, WE USE THE LIBRARY PRETTYTABLE
from prettytable import PrettyTable


# PRINT MATRIX
def get_arrow(i, initial, final):
    if i in initial and i in final:             # Fonction to return an arrow according to the type (if in initial or in final or in both)
        return ("<-->")
    else:
        if i in initial:
            return ("-->")
        else:
            if i in final:
                return ("<--")
            else:
                return ("")


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
                decomposed_transition = transition.split(",")
                if decomposed_transition[0] == i and decomposed_transition[1] == letter:
                    transition_string += decomposed_transition[2] + ","

            # SI ON NE TROUVE AUCUNE TRANSITION
            if transition_string == '':
                transition_string += "---"

            # WE ADD FOR THE LIST THAT WILL BE ADDED TO THE FINAL TABLE AND WE DELETE THE LAST CHAR WHICH IS A ","
            list_transitions.append(transition_string.strip(","))

        # WE ADD THE NEW COLUMN TO THE TABLE FOR EACH TRANSITION
        x.add_column("Transition " + letter, list_transitions)

    x.align = "c"
    print(x)
