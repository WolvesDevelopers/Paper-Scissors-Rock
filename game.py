import random as rd




#entry point
if __name__ == '__main__':
    #pc options 
    pc_options = ["piedra","papel","tijera"]

    acumPlayer = 0
    acumPc = 0
 
        
    entrar = True    
    prompt = '\nEnter "start" to continue or "quit" to finiIsh'
    prompt += '\nUser input : '


    while (entrar):
        inicio = input(prompt).lower()
        if (inicio == "quit"):
            print("closing program.")
            entrar = False
        
        #Game settings
        elif(inicio == "start"):
             while (True):

                select_pc = rd.choice(pc_options)
                player_select = input("Enter one option : ").lower()
        


               #Option 1 : piedra
                if(player_select == "piedra" and select_pc == "tijera"):
                    print("player win.")
                    acumPlayer +=5
                    print("player points : ", acumPlayer)
                    if(acumPlayer == 10):
                        acumPlayer = 0 
                        break


                elif(player_select == "piedra" and select_pc == "papel"):
                    print("pc win.")
                    acumPc += 5
                    print("pc points : ", acumPc)
                    if(acumPc == 10):
                        acumPc = 0
                        break

                elif(player_select == select_pc):
                    print("draw.")
                
               
               #Option 2 : papel
                if(player_select == "papel" and select_pc == "piedra"):
                    print("player win.")
                    acumPlayer+=5
                    print("player points : ", acumPlayer)
                    if(acumPlayer == 10):
                        acumPlayer = 0 
                        break

                elif(player_select == "papel" and select_pc == "tijera"):
                    print("pc win.")
                    acumPc+=5
                    print("pc points : ", acumPc)
                    if(acumPc == 10):
                        acumPc = 0
                        break

               
               #option 3 : tijera    
                if(player_select == "tijera" and select_pc == "papel"):
                    print("player win.")
                    acumPlayer+=5
                    print("player points : ", acumPlayer)
                    if(acumPlayer == 10):
                        acumPlayer = 0 
                        break

                elif(player_select == "tijera" and select_pc == "piedra"):
                    print("pc win")
                    acumPc += 5
                    print("pc points : ", acumPc)
                    if(acumPc == 10):
                        acumPc = 0
                        break
            
       #Starting block
        else:
            print("invalid input.")
       
