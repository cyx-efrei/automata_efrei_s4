# from table_display import print_matrix


def is_deterministic(states, initial, transitions):
 # Vérification des états initiaux
    if len(initial) != 1:
        return False

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

    return True


# TO COMPLETE AN AUTOMATON
def is_complete(alphabet, states, transitions):
    missed_transition = []
    for state in states:
        letters = []
        for transition in transitions:
            decomposed_transition = transition.split(",")
            if decomposed_transition[0] == state:
                actual_letter = decomposed_transition[1]
                if actual_letter not in letters:
                    letters.append(actual_letter)
                # letter contient toutes les lettres qui ont une transition à partir du state

        list_differences = []
        if len(letters) != len(alphabet):
            for a in alphabet:
                if a not in letters:
                    list_differences.append(a)
            missed_transition.append(state)
            missed_transition.append(list_differences)

    if len(missed_transition) != 0:
        print("This automaton is not complete because : ")
        i = 0
        while i < len(missed_transition):
            if i % 2:
                for j in missed_transition[i]:
                    print("-    Transition of", j)

            else:
                print("\nThe state",
                      missed_transition[i], "doesn't have : ")
            i += 1

        return False
    else:
        print("This automaton is already complete !")
        return True


def completion(alphabet, states, transitions):
    for state in states:
        letters = set()
        for transition in transitions:
            decomposed_transition = transition.split(",")
            if decomposed_transition[0] == state:
                actual_letter = decomposed_transition[1]
                if actual_letter not in letters:
                    letters.add(actual_letter)

        # for values in letters:

        for l_alphabet in alphabet:
            if ("P," + l_alphabet + ",P") not in transitions:
                transitions.append("P," + l_alphabet + ",P")
            if l_alphabet not in letters:
                transitions.append(state + "," + l_alphabet + ",P")

    states.append("P")

    return transitions, states


def determinisation(alphabet, states, initial, final, transitions):

    etats_initiaux_string = ""
    for etat in initial:
        etats_initiaux_string += str(etat)

    new_transitions = []
    # Ici on garde les noms des nvx transitions pour ne pas se répéter
    new_transitions_base = []

    for lettre in alphabet:
        resultat_transition = ""
        for transition in transitions:
            if lettre == transition[2] and transition[0] in initial:
                if transition[4] not in resultat_transition:
                    resultat_transition += transition[4]
        if resultat_transition != "":
            new_transitions_base.append(resultat_transition)
            new_transitions.append(etats_initiaux_string + "," +
                                   lettre + "," + resultat_transition)

    # on balaye les nouveaux states ( 013 puis 02 )
    for new_states in new_transitions_base:
        for lettre in alphabet:
            resultat_transition = ""               # on balaye les lettres
            for state in new_states:
                for transition in transitions:
                    if lettre == transition[2] and transition[0] == state:
                        if transition[4] not in resultat_transition:
                            resultat_transition += transition[4]
            if resultat_transition not in new_transitions_base and resultat_transition != "":
                new_transitions_base.append(resultat_transition)

            if resultat_transition != "":
                new_transitions.append(
                    new_states + "," + lettre + "," + resultat_transition)

            new_states_off = []
            for transition in new_transitions:
                new_transition = transition.split(",")
                if new_transition[0] not in new_states_off:
                    new_states_off.append(new_transition[0])

    # RESULTAT DES NOUVELLES TRANSITIONS
    return (new_transitions, new_states_off, new_states_off[0])
