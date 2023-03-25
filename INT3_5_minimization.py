from table_display import print_matrix


def minimization(alphabet, states, initial_state, final_state, list_transitions):

    def split(partition, symbol):
        split_result = {}
        for part in partition:
            split_temp = {}
            for state in part:
                for transition in list_transitions:
                    start, letter, end = transition.split(',')
                    if start == state and letter == symbol:
                        if end in split_temp:
                            split_temp[end].append(state)
                        else:
                            split_temp[end] = [state]

            for splitted in split_temp.values():
                splitted = frozenset(splitted)
                if splitted in split_result:
                    split_result[splitted] |= splitted
                else:
                    split_result[splitted] = splitted
        return set(split_result.keys())

    # Initial partition (final and non-final states)
    P = {frozenset(final_state), frozenset(
        set(states).difference(final_state))}
    W = {frozenset(final_state)}

    while W:
        A = W.pop()
        for symbol in alphabet:
            Ys = split(P, symbol)
            for Y in Ys:
                if Y.intersection(A):
                    Y_difference_A = Y.difference(A)
                    old_Y = None
                    for part in P:
                        if Y.issubset(part):
                            old_Y = part
                            break
                    if old_Y:
                        P.discard(old_Y)
                        P.update([Y.intersection(A), Y_difference_A])

                        if old_Y in W:
                            W.discard(old_Y)
                            W.update([Y.intersection(A), Y_difference_A])
                        else:
                            W.add(Y.intersection(A) if len(Y.intersection(A))
                                  <= len(Y_difference_A) else Y_difference_A)

    # Create minimized transitions
    minimized_transitions = []
    new_initial_state = None
    new_final_state = None
    for part in P:
        for state in part:
            if state == initial_state[0]:
                new_initial_state = ','.join(part)
            if state in final_state:
                new_final_state = ','.join(part)
            for transition in list_transitions:
                start, letter, end = transition.split(',')
                if start == state:
                    new_start = ','.join(part)
                    for part_end in P:
                        if end in part_end:
                            new_end = ','.join(part_end)
                            break
                    new_transition = f'{new_start},{letter},{new_end}'
                    if new_transition not in minimized_transitions:
                        minimized_transitions.append(new_transition)

    # Create new minimized states
    minimized_states = [','.join(part) for part in P]

    print("Minimized alphabet:", alphabet)
    print("Minimized states:", minimized_states)
    print("Minimized initial state:", new_initial_state)
    print("Minimized final states:", new_final_state)
    print("Minimized transitions:", minimized_transitions)

    return alphabet, minimized_states, [new_initial_state], [new_final_state], minimized_transitions


# # Test minimization
# url = "path/to/your/automaton/file.txt"
# alphabet, states, initial_state, final_state, list_transitions = ouverture(url)
# minimized_alphabet, minimized_states, minimized_initial_state, minimized_final_state, minimized_transitions = hopcroft_minimization(
#     alphabet, states, initial_state, final_state, list_transitions)


def minimization2(alphabet, states, initial, final, transitions):
    final_transitions = []
    Term_letter = {}
    NTerm_letter = {}
    NT = []
    T = []
    # LIST OF ALL NT STATES
    for state in states:
        if state not in final:
            NT.append(state)
        else:
            print("ajout", state)
            T.append(state)
    print("Nterm : ", NT)
    print("term : ", T)

    if len(NT) == 1:
        final_transitions.append(NT[0])
    else:
        for letter in NT:
            # part of the letter :
            part = []
            for transition in transitions:
                if transition[0] == letter:
                    if transition[-1] in NT:
                        part.append("NT")
                    else:
                        part.append("T")
            NTerm_letter[letter] = part

    if len(T) == 1:
        final_transitions.append(T[0])
    else:
        for letter in T:
            # part of the letter :
            part = []
            for transition in transitions:
                if transition[0] == letter:
                    if transition[-1] in NT:
                        part.append("NT")
                    else:
                        part.append("T")
            Term_letter[letter] = part

    # TO PUT EVERYTHING IN THE SAME DICTIONNARY TO PASS IT TO

    recursive_prep = {}
    recursive_prep["NT"] = NTerm_letter
    recursive_prep["T"] = Term_letter

    end_transition = recursive_minimize_v2(
        recursive_prep, transitions, alphabet)

    print(end_transition)

    # for trans in final_transitions:
    #     end_transition.append(trans)

    final_states = []
    for i in end_transition:
        res = ""
        for j in i:
            res += j
        if res != "":
            final_states.append(res)

    print("fs", final_states)

    transition_off = []
    for state in final_states:
        for letter in alphabet:
            for transition in transitions:
                print(state)
                print(state[0])
                if transition[0] == state[0] and transition[2] == letter:
                    # print(transition[0], state,
                    #       transition[2], letter, transition)
                    for transition_state in final_states:
                        if transition[-1] in transition_state and (state+","+letter+","+transition_state) not in transition_off:
                            transition_off.append(
                                state+","+letter+","+transition_state)

    # FIND TERMINALS
    term_states = []
    for i in final:
        for j in final_states:
            if i in j and j not in term_states:
                term_states.append(j)

    # FIND INITIALS
    init_states = []
    for i in initial:
        for j in final_states:
            if i in j and j not in init_states:
                init_states.append(j)

    print(transition_off, final_states, term_states, init_states)

    print_matrix(alphabet, final_states, init_states,
                 term_states, transition_off)


def recursive_minimize_v2(Dict, transitions, alphabet):
    print("Start or Restart the recursive : ", dict)
    end = []
    for cle, values in Dict.items():
        print("---------", cle, values)
        exist_items = []
        exist_items_id = []
        for key, valeur in values.items():
            print("---------", key, valeur)
            # Ici on va écrire les nouveaux noms des states
            if valeur not in exist_items:
                print("in", values)
                exist_items.append(valeur)
                exist_items_id.append(key)
                # print(valeur, "in", exist_items, "and", valeur in exist_items)
            else:
                j = 0
                while j < len(exist_items):
                    if exist_items[j] == valeur:
                        new_state = exist_items_id[j]
                        new_state += str(key)
                        exist_items_id[j] = new_state
                        break
                    j += 1
            # jusque là

        # end_loop = True
        # for new_th in exist_items_id:
        #     print(new_th, "kjbjkb", len(new_th))
        #     if len(new_th) > 1:
        #         end_loop = False
        #         print("on rentre dedans là nn ?")
        #         # sous_recursive(new_th, values, Dict)
        #         break

        # if end_loop != True:
        #     print("okk?")

        print(Dict)

        print("--- RESULT ---")
        print(exist_items)
        print(exist_items_id)
        end_temp = []
        for new_id in exist_items_id:
            end_temp.append(new_id)
        end.append(end_temp)
        print("end : ", end)

        final_dictionnary_part = {}
        print("BAH WSHHHHHHHHHHHHHHHHHHHHHHHHHH", end)
        while True:
            print("=======================", end)
            exist_items_id_off = []
            for partition in end:
                dictionnary_part = {}
                for sous_partition in partition:
                    # print(sous_partition)
                    if len(sous_partition) > 1:
                        new_partition = {}
                        res = ""
                        for state in sous_partition:
                            # print(state, "jhbjhcbjhshbcxshbcjdsbh")
                            print("return", state, "for", search_fill(
                                state, end, transitions, alphabet))
                            dictionnary_part[state] = search_fill(
                                state, end, transitions, alphabet)
                            print("may : ", dictionnary_part)

                exist_items_temp = []
                dictionnary_part_end = {}
                exist_items_id_temp = []
                print("enndd =====!!!! : ", dictionnary_part)
                for key, value in dictionnary_part.items():
                    # print("value", value)
                    if value not in exist_items_temp:
                        exist_items_temp.append(value)
                        exist_items_id_temp.append(key)
                    else:
                        for j in range(0, len(exist_items_temp)):
                            if exist_items_temp[j] == value:
                                res_temp = ""
                                res_temp = exist_items_id_temp[j] + key
                                exist_items_id_temp[j] = res_temp
                                break
                        print(key, res_temp)
                        dictionnary_part_end[res_temp] = dictionnary_part[key]
                        # dictionnary_part[key] = res_temp
                print("FINISISSUBXSDJHBCJEHDBKCJBKDJEBCKJZB",
                      dictionnary_part_end, 'and we have :', exist_items_temp, "and", exist_items_id_temp)

                exist_items_id_off.append(exist_items_id_temp)
                for key, value in dictionnary_part_end.items():
                    print("searching --- :", key, exist_items_id_temp)
                    if key in exist_items_id_temp:
                        final_dictionnary_part[key] = dictionnary_part_end[key]

                print("YES FINAL :", final_dictionnary_part, exist_items_id_off)

            if len(exist_items_id_off) == len(end):
                print("MINIMIZED !", exist_items_id_off)
                break
        # sous_recursive(end)
    return (exist_items_id_off)


def search_fill(state, end, transitions, alphabet):
    print('DEBUTTTTT', state, end)

    res = []

    for letter in alphabet:
        transition_temp = ""
        for transition in transitions:
            transition = transition.split(",")
            # print(transition, "hhhhhhhhhh")
            if transition[0] == state and transition[1] == letter:
                transition_temp = transition[2]
                break
        print("testtttttttttt", transition)
        Index_portion = 0
        for new_state_temp in end:
            for sous_new_state in new_state_temp:
                found = 0
                print("SUITEEEE ", sous_new_state, transition[2])
                if transition[2] in sous_new_state:
                    # print("FOUND :", sous_new_state, "from", state, Index_portion, "and", transition[2])
                    res.append(sous_new_state)
                    found = 1
                    Index_portion += 1
            if found == 0:
                res.append(transition[2])

    print("enddd =====", res)
    return res

# def sous_recursive(new_th, exist_items, Dict):
#     print("okjhcbduhbscjbdekskcjbdskjcbds", new_th, exist_items, Dict)


# THIS IS TO KNOW IN WHICH TABLE IS THE A STATE
def found_item(state, Dict):
    for cle, valeur in Dict.items():
        if isinstance(valeur, dict):
            if found_item(state, valeur):
                return cle
        else:
            if cle == state:
                return 1
