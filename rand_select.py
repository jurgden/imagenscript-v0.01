import random


def rand_select(list):
    rng = random.randint(0, 1)
    txt = listToString(list[rng])
    return txt


def listToString(arg):
    eStr = " "
    return (eStr.join(arg))
