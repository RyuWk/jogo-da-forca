import random
palavras = ['abacate', 'banana', 'pera', 'uva', 'jabuticaba', 'goiaba', 'manga', 'abacaxi', 'acerola', 'pitanga', 'amora', 'cerejeira', 'figo', 'framboesa', 'groselha', 'kiwi', 'laranja', 'melancia', 'morango', 'pitaia', 'siriguela', 'tangerina']
p = random.choice(palavras)
linhas = ["_"] * len(p)
tentativas = 6

while tentativas > 0 and "_" in linhas:
    print(" ".join(linhas))
    print(f"Tentativas restantes: {tentativas}\n")
    letra = input("Digite uma letra: ").lower()
    if letra in linhas:
        print("Você já escolheu essa letra antes. Tente novamente.\n")
        continue

    if letra in p:
        print("Letra correta!\n")

        for i, char in enumerate(p):
            if char == letra:
                linhas[i] = letra
    else:
        print("Letra incorreta. Tente novamente.\n")
        tentativas -= 1


if "_" not in linhas:
    print("Parabéns, você ganhou!")
else:
    print(f"Você perdeu! A palavra secreta era '{p}'.")
