# Pour obtenir les valeurs sous la forme d'un tableaud

def split_values_in_table(entries):
    print("\n\n-- RECUPERATION --")
    for i in entries:
        print(i, " ligne 1")
        splitEntries = [line.split(" ") for line in entries]
    print("End\n")

    return splitEntries


# Def pour print une matrice

def temporary_print_matrix(matrix):
    print("-- MATRIX --")
    for line in matrix:
        print("[", end="")
        for i in line:
            print(i, end=" ")
        print("]")


def recup_infos(matrix):
    alphabet = ""
    states = ""
    initial = ""
    final = ""
    for letter in splitEntries:
        # To get the alphabet
        if letter[0] == 'A':
            for i in letter:
                if (i > 'a' and i < 'z'):
                    alphabet += i

        # To get the states
        if letter[0] == 'Q':
            for i in letter:
                if (i >= '0' and i <= '9'):
                    states += str(i)

        # To get the initial states
        if letter[0] == 'I':
            for i in letter:
                if (i >= '0' and i <= '9'):
                    initial += str(i)

        # To get the final states
        if letter[0] == 'T':
            for i in letter:
                if (i >= '0' and i <= '9'):
                    final += str(i)

    alphabet = alphabet.split(",")
    print("alphabet :", alphabet)
    states = states.split(",")
    print("states :", states)
    initial = initial.split(",")
    print("initial :", initial)
    final = final.split(",")
    print("final :", final)
    return alphabet, states, initial, final






def standardiser(alphabet, states, initial, final, list_transitions):
    """
    Standardise un automate qui ne l'est pas.
    """
    # Vérifier si l'automate est standard
    if est_standard(alphabet, states, initial, final, list_transitions):
        return alphabet, states, initial, final, list_transitions

    # Si l'automate n'est pas standard, demander à l'utilisateur s'il veut standardiser
    reponse = input("L'automate n'est pas standard. Voulez-vous le standardiser ? (oui/non) ")

    if reponse.upper() == 'oui':
        # Créer un nouvel état initial et ajouter une transition epsilon vers l'ancien état initial
        new_initial_state = 'q0'
        list_transitions.append((new_initial_state, '', initial[0]))
        initial = [new_initial_state]

        # Si un état final est également l'état initial, créer un nouvel état final et ajouter une transition epsilon
        # depuis l'ancien état final vers le nouvel état final
        new_final_state = 'qf'
        if initial[0] in final:
            list_transitions.append((final[0], '', new_final_state))
            final = [new_final_state]

        # Renommer les états pour qu'ils soient de la forme 'qi' où i est un entier
        states = [f'q{i}' for i in range(len(states))]

        # Pour chaque transition avec un symbole d'entrée, créer un nouvel état intermédiaire et ajouter deux
        # transitions : une de l'état de départ vers le nouvel état avec le symbole d'entrée, et une du nouvel état
        # vers l'état d'arrivée avec une transition epsilon
        new_transitions = []
        for transition in list_transitions:
            if transition[2] != '':
                new_state = f'q{len(states)}'
                new_transitions.append((transition[0], transition[2], new_state))
                new_transitions.append((new_state, '', transition[4]))
                states.append(new_state)
            else:
                new_transitions.append(transition)

        transitions = new_transitions

        # Vérifier que l'automate est maintenant standard
        if est_standard(alphabet, states, initial, final, list_transitions):
            return alphabet, states, initial, final, list_transitions
        else:
            print("Erreur lors de la standardisation de l'automate.")
            return None
    else:
        return None

def verifier_standardisation(alphabet, states, initial, final, list_transitions):
    """
    Vérifie si un automate est standard, et si ce n'est pas le cas,
    demande à l'utilisateur s'il souhaite le standardiser.
    """
    if not est_standard(alphabet, states, initial, final, list_transitions):
        reponse = input("L'automate n'est pas standard. Souhaitez-vous le standardiser ? (oui/non) ")
        if reponse.lower() == "oui":
            alphabet, states, initial, final, list_transitions = standardiser(alphabet, states, initial, final, list_transitions)
        else:
            print("Ok, l'automate ne sera pas standardisé.")
    return alphabet, states, initial, final, list_transitions