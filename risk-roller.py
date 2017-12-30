'''
By Vegar Andreas Bergum, 31/12/2017

A simple application that eliminates the need for dice in the board-game Risk.
This application asks for troop-numbers and prints out the result of the
fighting.
'''
#TODO: 
    # Loop risk_roller until cancelled by user
    # Print result of each roll and prompt to continue attacking...

from random import randrange

def risk_roller():
    '''Main flow of the application. Asks for input, makes the rolls and prints
    out the result'''
    attacker = int(input("Attacker's troops: "))
    defender = int(input("Defender's troops: "))
    #randrange(5)

    while(attacker > 1 and defender > 0):
        a_rolls = get_rolls(get_amount_of_dice(True, attacker))
        d_rolls = get_rolls(get_amount_of_dice(False, defender))

        lost_attackers = 0
        lost_defenders = 0
        for i in range(min(len(a_rolls), len(d_rolls))):
            a_roll = max(a_rolls)
            d_roll = max(d_rolls)
            a_rolls.remove(a_roll)
            d_rolls.remove(d_roll)

            if (d_roll >= a_roll):
                lost_attackers += 1
            else:
                lost_defenders += 1

            attacker -= lost_attackers
            defender -= lost_defenders

            lost_attackers = 0
            lost_defenders = 0

    if (defender < 1):
        print('Attacker won, and has {0} troops left'.format(str(attacker)))
    elif (attacker == 1 and defender > 0):
        print('Defender won, and has {0} remaining. Attacker has {1} remaining'.format(str(defender), str(attacker)))


def get_amount_of_dice(attacker, troops):
    '''Returns the amount of dice the player can use. Attacker boolean, false =
    defender'''
    if (attacker):
        if (troops == 2): return 1
        elif (troops == 3): return 2
        elif (troops == 4): return 3
        elif (troops > 4): return 3
    else:
        if (troops < 2 and troops > 0):
            return 1 
        elif (troops < 1):
            return 2
        else: 
            return 2

def get_rolls(amount):
    '''Returns a list of dice-rolls, for amount of dice'''
    rolls = []
    for i in range(amount):
        rolls.append(randrange(5))

    return rolls
        
risk_roller()
