from INT3_5_supp_main import print_progressively


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
                    return False
                # We put all transition letter in letter to see if they are in double. If a letter is already present, it's used twice ==> NO DETERMINISTIC
                letter.add(actual_letter)

    return True


# TO SEE IF AN AUTOMATON IS COMPLETE
def is_complete(alphabet, states, transitions):
    missed_transition = []
    for state in states:
        letters = []
        for transition in transitions:
            decomposed_transition = transition.split(",")       # We divide each transition to have a list like : [state , letter , state]
            if decomposed_transition[0] == state:               # We verify if the first state of the list is the one of the loop
                actual_letter = decomposed_transition[1]        # By doing this, we check all transition of the states for all letter
                if actual_letter not in letters:                # Then we put the letter in a list. If a state doesn't have a transition of a letter, we will see it in letters because it will not be in
                    letters.append(actual_letter)
                # letter contient toutes les lettres qui ont une transition à partir du state

        list_differences = []                                   # There, we check if a transition of a letter is MISSING. If not, the number of transitions === number of letter (alphabet)
        if len(letters) != len(alphabet):
            for a in alphabet:
                if a not in letters:                            # We check if a letter is missing for transition of state
                    list_differences.append(a)
            missed_transition.append(state)                     # We save the state for which transitions of a letter are missing
            missed_transition.append(list_differences)          # We save the letter for which transitions of a letter are missing

    if len(missed_transition) != 0:                             # not empty ==> tranisitions are missing
        print_progressively("NO !")
        input("\nNext step : Explanation !\nClick on anything to continue\n")
        print("\n\n======= EXPLANATION\n\nThis automaton is not complete because : ")
        i = 0
        while i < len(missed_transition):
            if i % 2:                                           ### LES NOMBRES PAIRS CONTIENNENT LE NOM DES ÉTATS, LES IMPAIRS LES LETTRES DE TRANSISTIONS MANQUANTES
                for j in missed_transition[i]:
                    print("-    Transition of", j)

            else:
                print("\nThe state", missed_transition[i], "doesn't have : ")
            i += 1

        input("\nNext step : Completion !\nClick on anything to continue\n")
        return False
    else:
        return True


def completion(alphabet, states, transitions):
    for state in states:
        letters = set()
        for transition in transitions:
            decomposed_transition = transition.split(",")
            if decomposed_transition[0] == state:
                actual_letter = decomposed_transition[1]
                if actual_letter not in letters:                        # We put all transition letters of each state in letters
                    letters.add(actual_letter)

        # for values in letters:

        for l_alphabet in alphabet:
            if ("P," + l_alphabet + ",P") not in transitions:           # We check if the transitions OF P !!!! doesn't exist and save it
                transitions.append("P," + l_alphabet + ",P")
            if l_alphabet not in letters:
                transitions.append(state + "," + l_alphabet + ",P")     # We COMPLETE missing transitions by redirecting them to P !!

    states.append("P")                                                  # We add the nex state to all states list

    return transitions, states


def determinisation(alphabet, states, initial, final, transitions):

    etats_initiaux_string = ""
    for etat in initial:
        etats_initiaux_string += str(etat)                                      # We create the first new state with all initial states            

    new_transitions = []                                                        # Ici on garde les noms des nvx transitions pour ne pas se répéter
    new_transitions_base = []

    for lettre in alphabet:                                                     # We create the states of transitions. Like if we have transition in a to 1 and 2, we get there 12
        resultat_transition = ""
        for transition in transitions:
            if lettre == transition[2] and transition[0] in initial:
                if transition[4] not in resultat_transition:
                    resultat_transition += transition[4]                        # Here, we combine all letters
        if resultat_transition != "":
            new_transitions_base.append(resultat_transition)                    # List of all new states
            new_transitions.append(etats_initiaux_string + "," + lettre + "," + resultat_transition)          # list of all new transitions

    
    for new_states in new_transitions_base:                                     # on balaye les nouveaux states ( 013 puis 02 )
        for lettre in alphabet:
            resultat_transition = ""                                            # on balaye les lettres
            for state in new_states:
                for transition in transitions:
                    if lettre == transition[2] and transition[0] == state:
                        if transition[4] not in resultat_transition:
                            resultat_transition += transition[4]
            if resultat_transition not in new_transitions_base and resultat_transition != "":       # We check if we have a new state in the table (like the method seen in class)
                new_transitions_base.append(resultat_transition)                                    # If a new state, we add it to the loop

            if resultat_transition != "":                                                           # Creating all new transitions
                new_transitions.append(
                    new_states + "," + lettre + "," + resultat_transition)

            new_states_off = []
            for transition in new_transitions:
                new_transition = transition.split(",")
                if new_transition[0] not in new_states_off:                                         # Now, we regroup all states
                    new_states_off.append(new_transition[0])

    # RESULTAT DES NOUVELLES TRANSITIONS

    new_finals = []
    for states in new_states_off:
        for j in states:
            if j in final and states not in new_finals:                                             # We check if a new state has an old final.
                new_finals.append(states)

    # le premier state est celui qui sera inital
    return (new_transitions, new_states_off, new_states_off[0], new_finals)
