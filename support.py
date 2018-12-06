import random

def gen_random(towers, troops):
    army = [0 for x in range(towers)]
    for x in range(troops):
        army[random.randint(0,towers-1)] += 1
    return army