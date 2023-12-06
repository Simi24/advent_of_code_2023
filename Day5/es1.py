
import threading

def elabora_seeds(seed, realSeeds):
    for x in range(seeds[seeds.index(seed) + 1]):
        realSeeds.append(seed + x)

class Map:
    def __init__(self, destinationRangeStart, sourceRangeStart, rangeLenght):
        self.destinationRangeStart = destinationRangeStart
        self.sourceRangeStart = sourceRangeStart
        self.rangeLenght = rangeLenght

with open('input.txt', 'r') as file:

    seeds = []
    realSeeds = []
    map = {}
    mapp = []


    for line in file:

        line = line.strip()

        if not line:
            newSeeds = []
            if mapp != []:
                inRange = False
                for k in seeds:
                    for c in mapp:

                        if k >= c.sourceRangeStart and k <= c.sourceRangeStart + c.rangeLenght - 1:

                            newSeeds.append(c.destinationRangeStart + (k - c.sourceRangeStart))
                            inRange = True
                    if inRange == False:
                        newSeeds.append(k)
                    inRange = False
                seeds = sorted(newSeeds)
                newSeeds = []

            mapp = []
        else:
            if ":" in line:
                lineSplit = line.split(":")

                if lineSplit[0] == "seeds":
                    seeds = [int(value) for value in lineSplit[1].split()]
                    for seed in seeds:
                        if seeds.index(seed) % 2 == 0:
                            nuovo_thread = threading.Thread(target=elabora_seeds, args=(seed, realSeeds))

# Avvio del thread
                            nuovo_thread.start()

# Attendi che il thread termini (se necessario)
                            nuovo_thread.join()
                    seeds = sorted(seeds)
                    seeds = sorted(realSeeds)
            else:
                lineSplit = line.strip().split(" ")

                destinationRangeStart = int(lineSplit[0])
                sourceRangeStart = int(lineSplit[1])
                rangeLenth = (int(lineSplit[2]))
                mapp.append(Map(destinationRangeStart, sourceRangeStart, rangeLenth))
    
    print(seeds[0])

