import random

def jogar():
    palavras = ["KENNEDY", "ESCOLA", "PYTHON", "JAVASCRIPT", "POMBO"]
    palavra = random.choice(palavras)

    letras_acertadas = []
    for letra in palavra:
        letras_acertadas.append("_")

    acertou = False
    enforcou = False
    limite_tentativas = len(palavra) + 6
    tentativa = 1

    def mostrar_letras_acertadas():
        for letra in letras_acertadas:
            print(letra, end=" ")

    print("Tente adivinhar a palavra secreta: ")
    while(not acertou and not enforcou):
        # mostrar as letras acertadas
        mostrar_letras_acertadas()
        print("")
        chute = input("Digite uma letra: ")
        indice = 0
        for letra in palavra:
            if chute.upper() == letra:
                letras_acertadas[indice] = letra
            indice = indice + 1
        
        if tentativa == limite_tentativas:
            print("Você perdeu :(\nA palavra era: ", palavra)
            enforcou = True

        if letras_acertadas.count("_") == 0:
            print("Parabéns, você acertou a palavra secreta!")
            mostrar_letras_acertadas()
            acertou = True

        tentativa = tentativa + 1


    #TABELA VERDADE
    #Quero fazer um suco de banana OU maça
    #banana = true
    #maçã = true
    #   E       |       OU
    # v v = v   |     v v = v
    # V F = F   |     V F = V
    # F V = F   |     F V = V
    # F F = F   |     F F = F
if(__name__ == "__main__"):
    jogar()