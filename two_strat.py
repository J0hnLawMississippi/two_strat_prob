#!/usr/bin/env python3

import random

#First puzzle of 2025. Don't trade if you cannot code this to get an answer. You have 2 strats you think are
#profitable, but every week, one makes 1% or losses 2% and the other makes 2% or losses 1%, both with win rate 50%.
#What is the probability to make 10% after 52 weeks?

def flip_coin():
    return random.randint(0, 1)


def strat_one(alloc):
    coinflip = flip_coin()
    if coinflip == 0:
        new_alloc = alloc * 1.01
    elif coinflip == 1:
        new_alloc = alloc * 0.98
        
    return new_alloc
        
def strat_two(alloc):
    coinflip = flip_coin()
    if coinflip == 0:
        new_alloc = alloc * 1.02
    elif coinflip == 1:
        new_alloc = alloc * 0.99

    return new_alloc


def weekly_one(cap):
    last = cap[-1]
    week_perf = strat_one(last) 
    return week_perf

def weekly_two(cap):
    last = cap[-1]
    week_perf = strat_two(last)
    return week_perf

def history():

    strat1_capital = [5000]
    strat2_capital = [5000]

    for _ in range(52):
        
        strat1_capital.append(weekly_one(strat1_capital))
        strat2_capital.append(weekly_two(strat2_capital))

    return strat1_capital[-1] + strat2_capital[-1]


simulations = [history() for _ in range(10000)]

count = sum(1 for _ in simulations if _ >= 11000)

prob = count / len(simulations)

print(prob)
    
