# Check if the automaton is complete
def is_complete(automaton):
    for state in automaton["states"]:
        for symbol in automaton["alphabet"]:
            if symbol not in automaton["transitions"][state]:
                return False
    return True


# Check if the automaton is deterministic
def is_deterministic(automaton):
    transitions = automaton["transitions"]
    for state, state_transitions in transitions.items():
        if len(state_transitions.keys()) != len(set(state_transitions.values())):
            return False
    return True


# Determinize and complete the automaton
def determinization_and_completion(automaton):
    # Determine the set of all states in the new automaton
    all_states = set()
    for state in automaton["states"]:
        for symbol in automaton["alphabet"]:
            all_states.add(tuple(sorted([state, automaton["transitions"][state][symbol]])))

    # Create the new automaton
    new_automaton = {
        "alphabet": automaton["alphabet"],
        "states": [],
        "initials": [tuple(sorted(automaton["initials"]))],
        "finals": [],
        "transitions": {}
    }
    for state in all_states:
        new_automaton["states"].append(state)
        new_automaton["transitions"][state] = {}
        for symbol in automaton["alphabet"]:
            new_state = tuple(
                sorted([automaton["transitions"][state[0]][symbol], automaton["transitions"][state[1]][symbol]]))
            new_automaton["transitions"][state][symbol] = new_state
        if state[0] in automaton["finals"] or state[1] in automaton["finals"]:
            new_automaton["finals"].append(state)
    return new_automaton


# Complete the automaton
def completion(automaton):
    new_automaton = automaton.copy()
    new_state = "Sink"
    while new_state in new_automaton["states"]:
        new_state += "'"
    new_automaton["states"].append(new_state)
    for state in new_automaton["states"]:
        for symbol in new_automaton["alphabet"]:
            if symbol not in new_automaton["transitions"][state]:
                new_automaton["transitions"][state][symbol] = new_state
    return new_automaton



"""
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

# To Determinize an automaton
def determinize(alphabet, states, initials, final, transitions):
    if len(initials) > 1:
        new_initials = []
        for initial in initials :
            for transitions in transitions :
"""