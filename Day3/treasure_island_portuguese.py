print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Bem-vindo à Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.")
print("Ao digitar sua resposta, escreva apenas a palavra entre os asteriscos (*)")

intersection_choice = input(
    "\n Você começa a caminhar por uma trilha de areia até se deparar com um cruzamento, está escuro e você só ouve os sons da floresta, para onde você escolhe ir? *esquerda* ou *direita?* "
)

if intersection_choice.lower() == "esquerda":
    print(
        "\n *******************************************************************************"
    )
    lake_choice = input(
        "\n Você vira à esquerda e segue em frente, após alguns minutos de caminhada você se depara com um lago de cristalinas águas azuis, você decide tentar *nadar* ou *esperar* por um barco? "
    )

    if lake_choice.lower() == "esperar":
        print(
            "\n *******************************************************************************"
        )
        door_choice = input(
            "\n Depois de alguns minutos você percebe um pequeno barco de madeira vindo em sua direção, o barco, embora vazio, parece estar de alguma forma sendo conduzido ate voce. Ao entrar no barco você percebe que ele não tem nenhum tipo de remo e nem mesmo motor, mas mesmo assim ele começa a andar sobre a agua atravessando o lago e te deixa do outro lado onde você se depara com uma grande estrutura de pedra com 3 portas esculpidas, uma *vermelha*, uma *amarela* e uma *azul* qual você escolhe? "
        )

        if door_choice.lower() == "vermelha":
            print(
                "\n *******************************************************************************"
            )
            print(
                "\n Assim que você entra na sala a porta atrás de você fecha com um baque e desaparece na parede, você corre para onde a porta deveria estar quando a sala começa a esquentar, e chamas aparecem por toda parte queimando você vivo. Fim De Jogo"
            )
        elif door_choice.lower() == "amarela":
            print(
                "\n *******************************************************************************"
            )
            print(
                "\n Ao entrar pela porta, uma grande sala se ilumina revelando um grande baú de tesouro no centro da sala. \n VOCE GANHOU!!!!!"
            )
        elif door_choice.lower() == "azul":
            print(
                "\n *******************************************************************************"
            )
            print(
                "\n Você entra no quarto e sente o hálito de uma fera que não come há dias, quando você tenta voltar você percebe que já é tarde demais, pois na sala não havia apenas uma fera esperando por você, mas mais de você poderia contar. Fim De Jogo"
            )
        else:
            print(
                "\n *******************************************************************************"
            )
            print(
                "\n A montanha na qual a estrutura foi esculpida começa a desabar e você fica preso nos escombros, esmagado. Fim De Jogo"
            )

    else:
        print(
            "\n *******************************************************************************"
        )
        print(
            "\n Você entra no lago e começa a nadar para chegar ao outro lado, quando de repente você sente uma mordida na perna, ao sentir a dor você olha em volta e se vê rodeado de piranhas que te atacam até você não conseguir mais se defender, e afundar, quase morto, no fundo do lago onde permanecerá pelo resto da eternidade. Fim De Jogo"
        )

else:
    print(
        "\n *******************************************************************************"
    )
    print(
        "\n Você vira cuidadosamente para a direita, prestando atenção aos sons da floresta, ao dar alguns passos à frente voce sente a falta de chão sob seus pés e percebe que está caindo em um buraco que parece não ter fim. até você tem o seu. Fim De Jogo"
    )
