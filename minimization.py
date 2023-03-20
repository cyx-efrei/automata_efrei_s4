def minimization(alphabet, states, initial, final, transitions):
    final_transitions = []
    Term_letter = {}
    NTerm_letter = {}
    NT = []
    T = []
    # LIST OF ALL NT STATES
    for letter in states:
        if letter not in final:
            NT.append(letter)
        else:
            T.append(letter)
    print("Nterm : ", NT)

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

    end_transition = recursive_minimize_v2(recursive_prep)
    for trans in final_transitions:
        end_transition.append(trans)


def recursive_minimize_v2(Dict):
    print("Start or Restart the recursive : ", dict)
    end = []
    for cle, valeur in Dict.items():
        print("---------", cle, valeur)
        exist_items = []
        exist_items_id = []
        for key, valeur in valeur.items():
            print("---------", key, valeur)
            if valeur not in exist_items:
                exist_items.append(valeur)
                exist_items_id.append(key)
            else:
                j = 0
                while j < len(exist_items):
                    if exist_items[j] == valeur:
                        new_state = exist_items_id[j]
                        new_state += str(key)
                        exist_items_id[j] = new_state
                        break
                        j += 1
        print("--- RESULT ---")
        print(exist_items)
        print(exist_items_id)
        for new_id in exist_items_id:
            end.append(new_id)
    return (end)


def recursive_minimize(Dict):
    print("\n\n\nh")
    end_matrix = []
    new_matrix = []
    for cle, valeur in Dict.items():
        print("---------", cle, valeur)
        if isinstance(valeur, dict):
            print("C'EST LA FIN : ", valeur, dict)
            return end_matrix.append(recursive_minimize(valeur))
        else:

            # WE SEE IF WE HAVE TWO SAME THINGS
            if valeur not in new_matrix:
                new_matrix.append(cle)
                new_matrix.append(valeur)
            else:
                # WE ARE LOOKING FOR THE INDEX OF THE SAME 'VALEUR'
                index = new_matrix.index(valeur)
                print(index, 'index')
                # WE MODIFIE THE FUTUR KEY TO CONBINE BOTH OF THEM
                new_matrix[index-1] = new_matrix[index-1] + str(cle)

    print("\nFinal Part")
    for key, value in Dict.items():
        print(key, value)
    print(new_matrix, 'nmm',
          len(new_matrix)//2, len(Dict.items()))
    print(Dict, "\n\n")

    if len(new_matrix)//2 == len(Dict.items()):
        print("return 2")
        print("Perfect !", Dict)
        return Dict
    else:

        # ICI, C'EST QUAND ON A EU UN CHANGEMENT DONC ON DOIT RECREER UN TABLEAU AVEC LES TRANSITIONS
        new_dict = dict(zip(new_matrix[::2], new_matrix[1::2]))
        print(new_dict)

        letter_transition = []
        print("##########")
        for key, value in new_dict.items():
            print("key", key)
        print("return 1")
        return recursive_minimize(new_dict)

    # for i in Dict.items():
    #     print(i)
    #     for cle, valeur in Dict[i].items():
    #         print(cle, valeur)


# THIS IS TO KNOW IN WHICH TABLE IS THE A STATE
def found_item(state, Dict):
    for cle, valeur in Dict.items():
        if isinstance(valeur, dict):
            if found_item(state, valeur):
                return cle
        else:
            if cle == state:
                return 1
