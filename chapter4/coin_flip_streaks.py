import random

def generateCoins(num=100):
    coins=''
    for i in range(num):
        if (random.randint(0,1) == 0):
            coins += 'H'
        else:
            coins += 'T'

    return coins

def findStreak(coins):
    matchH = 'H' * 6
    matchT = 'T' * 6
    return (matchH in coins or matchT in coins)

numberOfStreaks = 0
for experimentNumber in range(10000):
    coins = generateCoins()
    if (findStreak(coins)):
        numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
