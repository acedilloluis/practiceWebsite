from __future__ import print_function
import random
import sys

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']*4

playerhand1 = [random.choice(deck), random.choice(deck)]
dealerhand1 = [random.choice(deck), random.choice(deck)]

def blackjack():
    print("After your hand has been dealt, type hit to add an additional card or stand to keep your hand. When typing your action type it like this: 'hit'")
    print(playerhand1)
    print("The dealer's hand has a face up ", random.choice(dealerhand1))
    conditional()
    playeraction()
     
def playeraction():
    action = input('What would you like to do: ')
    if 'h' in action:
        hit()
    elif 'sta' in action:
        stand()

def dconditional():
    global dtotal
    dtotal = 0
    for card in dealerhand1:
        if card == 'J':
            dtotal += 10
        elif card == 'Q':
            dtotal += 10
        elif card == 'K':
            dtotal += 10
        elif card == 'A':
            dtotal += 1
        else:
            dtotal += card
    print(dtotal)
    
    if dtotal > 21:
        print('You Win')
        sys.exit()
    elif dtotal <= 15:
        dhit()
    elif dtotal == 21:
        print('House Wins.')
        sys.exit()
   
def conditional():
    total = 0
    for card in playerhand1:
        if card == 'J':
            total += 10
        elif card == 'Q':
            total += 10
        elif card == 'K':
            total += 10
        elif card == 'A':
            total += 1
        else:
            total += card
    print(total)
    
    if total > 21:
        print('You lose')
        sys.exit()
    elif total == 21:
        print('You Win')
        sys.exit()
    elif total < 21:
        playeraction()

def finalConditional():
    total = 0
    for card in playerhand1:
        if card == 'J':
            total += 10
        elif card == 'Q':
            total += 10
        elif card == 'K':
            total += 10
        elif card == 'A':
            total += 1
        else:
            total += card
    
    if total > 21:
        print('You lose')
        sys.exit()
    elif total == 21:
        print('You Win')
        sys.exit()
    elif total < dtotal:
        print(dealerhand1)
        print('House Wins')
        sys.exit()
    elif total > dtotal:
        print(dealerhand1)
        print('You Win')
        sys.exit()
    elif total == dtotal:
        print(dealerhand1)
        print('Tie')
        sys.exit()

def stand():
    print('You have chosen to stand.')
    dconditional()
    finalConditional()
    
def hit():   
    playerhand1.append(random.choice(deck))
    print(playerhand1)
    conditional()
    
def dhit():        
    dealerhand1.append(random.choice(deck))
    print(dealerhand1)
    dconditional()
    finalConditional()

blackjack()