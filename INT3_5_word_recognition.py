from INT3_5_deterministic import is_deterministic


def word_recognition(initial, final, transitions, word):
    print()

    order_states = []
    for i in range(0, len(word)):
        found = 0

        # TO FIND THE FIRST LETTER OF THE WORD
        if i == 0:
            for transition in transitions:
                if transition[0] in initial and transition[2] == word[0]:
                    order_states.append(transition[0])
                    order_states.append(transition[-1])
                    found = 1
                    break

            # CHECK IF THE FIRST LETTER HAS BEEN FOUND
            if found == 0:
                print("The first character", word[i],
                      "has not been found\nSorry, the word \"", word, "\"is not recognize by this automaton")
                return
                # RETURN WHEN THE NEXT LETTER IS NOT FINDABLE

        # TO FIND A LETTER OF THE WORD
        else:
            for transition in transitions:
                if transition[0] == order_states[-1] and transition[2] == word[i]:
                    print("- A transition with the character", word[i],
                          "has been found from", transition[0], "to", transition[-1])
                    order_states.append(transition[-1])
                    found = 1
                    break

            # CHECK IF THE LETTER HAS BEEN FOUND
            if found == 0:
                print("\nNo transition with the character", word[i],
                      "has not been found\nSorry, the word \"", word, "\"is not recognize by this automaton")
                return
                # RETURN WHEN THE NEXT LETTER IS NOT FINDABLE

        # TO CHECK IF THE LAST LETTER OF THE WORD IS A TERMINAL
        if i == len(word)-1:
            if order_states[-1] in final:
                print("\nThe word", word, "is succefully recognize")
            else:
                print("\nThe last state to complete the word \"", word,
                      "\" isn't a terminal so it's not recognize ! (Last state :", order_states[-1] + ")")
                return
