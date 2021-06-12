import numpy as np


if __name__ == '__main__':
    # pc options
    win_options = {'piedra': 'tijera', 'papel': 'piedra', 'tijera': 'papel'}
    quantity = {'piedra': 1, 'papel': 1, 'tijera': 1, 'total': 3}
    probability = {'piedra': 1/3, 'papel': 1/3, 'tijera': 1/3}
    entrar = True
    prompt = '\nEnter "start" to continue or "quit" to finiIsh'
    prompt += '\nUser input : '

    while (entrar):
        inicio = input(prompt).lower()
        acumPlayer = 0
        acumPc = 0
        if (inicio == "quit"):
            print("closing program.")
            entrar = False

        # Game settings
        elif(inicio == "start"):
            while (True):

                select_pc = np.random.choice(list(win_options), 1,
                                             p=list(probability.values()))
                print(select_pc)
                player_select = input("Enter one option : ")
                if player_select in win_options:
                    # Player win
                    if win_options[player_select] == select_pc[0]:
                        print("player win.")
                        quantity[win_options[select_pc[0]]] += 1
                        quantity['total'] += 1
                        acumPlayer += 5

                    # Pc win
                    elif win_options[select_pc[0]] == player_select:
                        quantity[select_pc[0]] += 1
                        quantity['total'] += 1
                        print("pc win.")
                        acumPc += 5

                    else:
                        print("draw.")
                    if acumPlayer == 10 or acumPc == 10:
                        print(f' end game, player:{acumPlayer}, pc:{acumPc}')
                        break
                    for k in probability:
                        probability[k] = quantity[k] / quantity['total']
                    print(probability)
                else:
                    print("invalid input.")
        # Starting block
        else:
            print("invalid input.")
