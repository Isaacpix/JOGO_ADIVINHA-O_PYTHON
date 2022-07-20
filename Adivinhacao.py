print ("**************************************")
print ("Seja bem-vindo ao jogo de adivinhação!")
print ("**************************************")

numero_secreto = 6

tentativa = input ("Digite o seu número: ")      # INPUT, é o que é mostrado na tela. É o interativo. 

print ("Você digitou ", tentativa)

tentativa = int(tentativa)                       # TRANSFORMAÇÃO do type 'str', para o type 'int', fazendo essa atribuição para 'tentativa.

if (numero_secreto == tentativa):                # if = se        else = senão      !!! usar ' : ', para validação.          
    print ("Parabéns, você acertou!!!")                                 
else:                                            
    print ("Que pena... você errou :(")

print ("*************")
print (" FIM DO JOGO!")
print ("*************")