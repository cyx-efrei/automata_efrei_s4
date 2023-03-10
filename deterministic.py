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
            if transition[0] == state:
                actual_letter = transition[2]
                if actual_letter not in letters:
                    letters.append(actual_letter)
                # letter contient toutes les lettres qui ont une transition à partir du state

        list_differences = []
        if len(letters) != 2:
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
            if transition[0] == state:
                actual_letter = transition[2]
                if actual_letter not in letters:
                    letters.add(actual_letter)

        # for values in letters:

        for l_alphabet in alphabet:
            if l_alphabet not in letters:
                transitions.append(state + "," + l_alphabet + ",P")

    return transitions
