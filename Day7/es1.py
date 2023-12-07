import functools

hands_map = {}

# Comment to get the solution of the second part
cards = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'T': 11,
        '9': 10,
        '8': 9,
        '7': 8,
        '6': 7,
        '5': 6,
        '4': 5,
        '3': 4,
        '2': 3,
        'J': 2
}

# # Uncomment to get the solution of the first part
# cards = {
#         'A': 14,
#         'K': 13,
#         'Q': 12,
#         'J': 11,
#         'T': 10,
#         '9': 9,
#         '8': 8,
#         '7': 7,
#         '6': 6,
#         '5': 5,
#         '4': 4,
#         '3': 3,
#         '2': 2
# }

score = {
        "FiveOfAKind": 7,
        "FourOfAKind": 6,
        "FullHouse": 5,
        "ThreeOfAKind": 4,
        "TwoPairs": 3,
        "Pair": 2,
        "HighCard": 1
}

def isFiveOfAKind(hand):
    splitHand = [*hand]
    for x in range(1, len(splitHand)):
        if splitHand[x] != splitHand[0]:
            return False
    return True

def isFourOfAKind(hand):
    splitHand = [*hand]
    card = ""
    for x in range(len(splitHand)):
        count = 1
        card = x
        for i in range(x + 1, len(splitHand)):
             if splitHand[x] == splitHand[i]:
                  count += 1
        if count == 4:
             return True
    return False

def isFullHouse(hand):
    splitHand = [*hand]
    splitHand.sort()

    if (
        (splitHand[0] == splitHand[1] == splitHand[2] and splitHand[3] == splitHand[4]) or
        (splitHand[0] == splitHand[1] and splitHand[2] == splitHand[3] == splitHand[4])
    ):
        return True

    return False

def isThreeOfAKind(hand):
    splitHand = [*hand]
    for x in range(len(splitHand)):
        count = 1
        for i in range(x + 1, len(splitHand)):
             if splitHand[x] == splitHand[i]:
                  count += 1
        if count == 3:
             return True
    return False

def hasTwoPairs(hand):
    splitHand = [*hand]
    splitHand.sort()

    if (
        (splitHand[0] == splitHand[1] and splitHand[2] == splitHand[3]) or
        (splitHand[1] == splitHand[2] and splitHand[3] == splitHand[4]) or
        (splitHand[0] == splitHand[1] and splitHand[3] == splitHand[4])
    ):
        return True

    return False

def isPair(hand):
    splitHand = [*hand]
    for x in range(len(splitHand)):
        count = 1
        for i in range(x + 1, len(splitHand)):
             if splitHand[x] == splitHand[i]:
                  count += 1
        if count == 2:
             return True
    return False

def mycmp(a, b):
    handA = a[0]
    handB = b[0]

    scoreA = getHandScore(handA)
    scoreB = getHandScore(handB)
    
    if scoreA == scoreB:
        splitHandA = [*handA]
        splitHandB = [*handB]

        for i in range(len(splitHandA)):
            cardA = cards.get(splitHandA[i], 0)
            cardB = cards.get(splitHandB[i], 0)
            if cardA > cardB:

                return 1
            elif cardA < cardB:

                return -1

    elif scoreA > scoreB:
        return 1
    elif scoreA < scoreB:
        return -1

    return 0

# # Uncomment to get the solution of the first part
# def getHandScore(hand):
#     if isFiveOfAKind(hand):
#         return score["FiveOfAKind"]
#     elif isFourOfAKind(hand):
#         return score["FourOfAKind"]
#     elif isFullHouse(hand):
#         return score["FullHouse"]
#     elif isThreeOfAKind(hand):
#         return score["ThreeOfAKind"]
#     elif hasTwoPairs(hand):
#         return score["TwoPairs"]
#     elif isPair(hand):
#         return score["Pair"]
#     else:
#         return score["HighCard"] 

# Comment to get the solution of the second part
def getHandScore(hand):
    if isFiveOfAKind(hand):
        return score["FiveOfAKind"]
    elif isFourOfAKind(hand) and 'J' in hand:
        return score["FiveOfAKind"]
    elif isFourOfAKind(hand):
        return score["FourOfAKind"]
    elif isFullHouse(hand) and 'J' in hand:
        return score["FiveOfAKind"]
    elif isFullHouse(hand):
        return score["FullHouse"]
    elif isThreeOfAKind(hand) and 'J' in hand:
        return score["FourOfAKind"]
    elif isThreeOfAKind(hand):
        return score["ThreeOfAKind"]
    elif hasTwoPairs(hand) and hand.count('J') == 2:
        return score["FourOfAKind"]
    elif hasTwoPairs(hand) and hand.count('J') == 1:
        return score["FullHouse"]
    elif hasTwoPairs(hand):
        return score["TwoPairs"]
    elif isPair(hand) and 'J' in hand:
        return score["ThreeOfAKind"]
    elif isPair(hand):
        return score["Pair"]
    elif 'J' in hand:
        return score["Pair"]
    else:
        return score["HighCard"] 


with open('input.txt', 'r') as file:

        for line in file:
                line = line.strip()
                hands_map[line.split(" ")[0]] = line.split(" ")[1]


sorted_dict = dict(sorted(hands_map.items(), key=functools.cmp_to_key(mycmp)))


sum = 0
for idx, (k, v) in enumerate(sorted_dict.items()):
    sum += int(v) * (idx + 1)

print(sum)


