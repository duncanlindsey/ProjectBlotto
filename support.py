import random
from scipy.special import comb
from scipy.stats import binom

def gen_random(towers, troops):
    army = [0 for x in range(towers)]
    for x in range(troops):
        army[random.randint(0,towers-1)] += 1
    return army

def fight(army1, army2):
    if len(army1) == len (army2):
        points1 = 0
        points2 = 0
        for battle in range(len(army1)):
            if army1[battle] > army2[battle]:
                points1 += battle + 1
            elif army1[battle] < army2[battle]:
                points2 += battle + 1
        return (points1, points2)

def gen_enemies(players, towers, troops, method):
    methods = {'random': gen_random}
    npcs = [0 for x in range(players)]
    for x in range(players):
        npcs[x] = methods[method](towers, troops)
    return npcs

def brawl(player_army, enemies, method):

    #Extract brawl parameters from player army
    towers = len(player_army)
    troops = sum(player_army)

    #Build enemy armies and combine with player army
    npcs = gen_enemies(enemies, towers, troops, method)
    brawl = [player_army, *npcs]

    #Run a "everyone players everyone once" battle
    scores = [0 for x in range(len(brawl))]
    for player in range(len(scores)):
        for opponent in range(player + 1, len(scores)):
            #print ("Player %s versus Player %s" % (player, opponent))
            results = fight(brawl[player],brawl[opponent])
            #print ("The score is %s!" % (str(results)))
            scores[player] += results[0]
            scores[opponent] += results[1]
    return rank_score(scores[0], scores)

def rank_score(my_score, all_scores):
    sorted_scores = sorted(all_scores, reverse = True)
    return sorted_scores.index(my_score) + 1

def simulation(army, enemies, method, iterations):
    rank_distribution = [0 for x in range(enemies+1)]
    for x in range(iterations):
        rank_distribution[brawl(army, enemies, method)-1] += 1
    return rank_distribution

#def binom(towers, k, troops):
    #return comb(troops, k) * ((1/towers)**k) * ((1-(1/towers))**(troops - k))

def binom_dist(towers, troops):
    rv = binom(troops, 1/towers)
    return [rv.pmf(k) for k in range(0, troops + 1)]
