import time


def print_progressively(word):
    time.sleep(0.2)
    for i in word:
        time.sleep(0.2)
        # J'UTILISE FLUSH ICI POUR QUE ÇA AFFICHE PAR CHAR ET A
        print(i, end="", flush=True)
    time.sleep(0.2)
    print("\n")


#  FROM THERE, WE CONTROL ALL THE TIME SLEEP
def await_time():
    time.sleep(0.5)
