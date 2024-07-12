import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>1234567890qwertyuiopasdfghjklzxcvbnm"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

def srl_game():
    words_0 = ["Бумага","Камень","Ножницы"]
    return random.choice(words_0)
