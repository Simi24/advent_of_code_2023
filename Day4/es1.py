
def getAnswer(validNumbers, myHand):
    myValidNumbers = []
    for n in validNumbers:
        for x in myHand:
            if n == x:
                myValidNumbers.append(x)
    return myValidNumbers

# Open file
with open('input.txt', 'r') as file:
    map = {}
    sum = 0
    sum2 = 0
    i = 1
    # One line
    for line in file:
        noCard = line.split(":")[1].strip()
        part = noCard.split('|')
        if map.get(i):
            map.update({i : map[i] + 1}) 
        else:
             map.update({i : 1})

        validNumbers = [int(number) for number in part[0].split()]
        myHand = [int(number) for number in part[1].split()]
        lenValidNumbers = len(getAnswer(validNumbers, myHand))
        sum += 2 ** (lenValidNumbers - 1) if lenValidNumbers > 0 else 0

        if lenValidNumbers > 0:
            for j in range(lenValidNumbers):
                cardToUpdate = i + j+1
                if map.get(cardToUpdate):
                    map.update({cardToUpdate : map.get(cardToUpdate) + (1 * map.get(i))})
                else:
                    map.update({cardToUpdate : (1 * map.get(i))})
        i += 1
    
    for k, v in map.items():
        sum2 += v
    
    print("First part answer: ", sum)
    print("Second part answer: ",sum2)