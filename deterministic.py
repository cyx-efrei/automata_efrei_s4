from table_display import print_matrix


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
            if transition[0] == state:
                actual_letter = transition[2]
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


def deter_automaton(alphabet, states, initial_states, final_states, transitions):
    # Read input file
    with open("automata_test.txt", 'r') as file:
        lines = file.readlines()

    # Parse input file
    alphabet = lines[0].strip().split(', ')
    states = lines[1].strip().split(', ')
    initial_states = lines[2].strip().split(', ')
    final_states = lines[3].strip().split(', ')
    transitions = {}
    for line in lines[4:]:
        q1, symbol, q2 = line.strip().split(',')
        if (q1, symbol) not in transitions:
            transitions[(q1, symbol)] = [q2]
        else:
            transitions[(q1, symbol)].append(q2)

    # Initialize variables for determinization
    new_states = []
    new_transitions = {}
    new_final_states = set()
    unmarked_states = []
    marked_states = {}

    # Create new initial state as sorted list of original initial states
    new_initial_state = ','.join(sorted(initial_states))
    new_states.append(new_initial_state)
    unmarked_states.append(new_initial_state)

    # Loop until all states are marked
    while unmarked_states:
        q = unmarked_states.pop()
        marked_states[q] = True

        # Compute transitions for new state
        for symbol in alphabet:
            next_states = set()
            for q_i in q.split(','):
                if (q_i, symbol) in transitions:
                    next_states = next_states.union(transitions[(q_i, symbol)])
            if next_states:
                next_state = ','.join(sorted(list(next_states)))
                if next_state not in new_states:
                    new_states.append(next_state)
                    unmarked_states.append(next_state)
                if (q, symbol) not in new_transitions:
                    new_transitions[(q, symbol)] = [next_state]
                else:
                    new_transitions[(q, symbol)].append(next_state)

    # Compute new final states
    for q in new_states:
        for q_i in q.split(','):
            if q_i in final_states:
                new_final_states.add(q)
                break

    n_transitions = []
    for q1, symbol in new_transitions:
        q2 = new_transitions[(q1, symbol)][0]
        n_transitions.append('{},{},{}'.format(q1, symbol, q2))

    print_matrix(alphabet, new_states, new_initial_state,
                 new_final_states, n_transitions)
