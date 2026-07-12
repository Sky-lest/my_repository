meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            'VDD': 'abreviação da palavra "verdade"',
            'BISCOITAR': 'postar algo apenas para chamar a atenção',
            'HATER': 'pessoa que está constantemente criticando os outros',
            'MOGAR': 'superar alguém em relação à beleza, porte físico ou estilo',
            'BETA': 'alguém que é "inferior"',
            'AURA': 'carisma ou o quão legal alguém é'
            }


while True:
    word = input("Digite uma palavra moderna que você não entende (em letras maiúsculas)")

    
    if word in meme_dict.keys():
        print(meme_dict[word])
        print(' ')
    else:
        print('Essa palavra não está no dicionário')
        print('tente outra')
        print(' ')
        # O que devemos fazer se a palavra não for encontrada?
