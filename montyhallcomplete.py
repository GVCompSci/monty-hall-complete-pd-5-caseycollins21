'''
Created on Jan 30, 2019

@author: casey
'''
import random
wincount=0
rounds=int(input('How many rounds would you like to play (must be beyweem 10 and 10,000) ?: '))
while rounds<10 or rounds>10000:
    rounds=int(input('You must enter a number between 10 and 10000: '))
decision=input('Are you going to swap or stay?: ')
car=random.randint(1,3)
guess=random.randint(1,3)
if decision.lower()=='stay':
    for rounds in range(1,rounds+1,1):
        if guess==car:
            wincount+=1
if decision.lower()=='swap':
    newguess=random.randint(1,3)
    while newguess==guess:
        newguess=random.randint(1,3)
    for rounds in range(1,rounds+1,1):
        if newguess==car:
            wincount+=1
winpercent=(wincount/rounds)*100
print('You won',wincount,'/',rounds,'games, which is',format(winpercent,'2.2f'),'%')