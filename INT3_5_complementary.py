from INT3_5_table_display import print_matrix


def complement(alphabet, states, initial, final, transitions, n):

    new_array = []                                              # We just put as final all states that weren't
    for s in states:
        if s not in final:
            new_array.append(s)
    final = new_array

    if n == 1 :
        return final
    print_matrix(alphabet, states, initial, final, transitions)
