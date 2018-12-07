import support as sup
import matplotlib.pyplot as plt

def hill_climb(towers, troops):
    dist = sup.binom_dist(towers, troops)
    print (dist)
    strategy = [0 for x in range(towers)]
    for x in range(troops):
        deltas = [(i+1)*dist[strategy[i]] for i in range(towers)] #Evaluate adding a troop to each tower
        strategy[deltas.index(max(deltas))] += 1
        #print (deltas)
        print (strategy)
    return strategy

my_army = hill_climb(7,19)
#my_army = [0,3,7]
print(sup.simulation(my_army, 9, 'random', 10000))

##npcs = sup.gen_enemies(10000, 5, 15, 'random')
#plt.hist([i[0] for i in npcs])
#plt.show()

#print (hill_climb(5, 15))
#print (sup.binom_dist(5,15))


