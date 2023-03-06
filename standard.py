def is_standard(alphabet, states, initial, final, transitions):
    """
    Vérifie si un automate est standard ou non.
    Un automate est standard si:
    - il a un seul état initial
    - tous les états finaux sont distincts
    - il n'y a pas de transitions avec epsilon comme symbole d'entrée ??????
    - chaque transition a un seul symbole d'entrée
    """
    # Vérifier s'il y a un seul état initial
    if len(initial) != 1:
        return False

    # Vérifier que tous les états finaux sont distincts
    if len(set(final)) != len(final):
        return False

    # Vérifier que chaque transition a un seul symbole d'entrée
    for state in states:
        symbols = set()
        for transition in transitions:
            if transition[0] == state:
                symbol = transition[2]
                if symbol in symbols:
                    return False
                symbols.add(symbol)

    # Si toutes les conditions sont satisfaites, l'automate est standard
    print("Automate standard")
    return True
