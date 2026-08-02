import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "cara"
    else:
        return "coroa"

def gen_emoji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)

def yes_no():
    choice = random.randint(0, 1)
    if choice == 0:
        return 'Sim'
    else:
        return 'Não'

def guess_number():
    n = random.randint(1, 10)
    return n
