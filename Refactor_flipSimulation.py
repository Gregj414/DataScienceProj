# Greg Johnson Data Science Final 2017 Question 3 for Player B
# to use this you can adjust the sim_rounds to run multiple times. There are 500 round per simulation as per instruction

import random


def guess_flip():
    guess = random.random()  # player B randomly guesses since it is never known if the coin is weighted
    if guess < .5:  # 50 % chance of betting head
        guess = 0  # head
    else:
        guess = 1  # tail   # if guess > .5 the guess Tails
    return guess


def flip_the_coin():
    coin_flip = random.random()
    if coin_flip < .55:  # 55% change of flipping head
        coin_flip = 0  # head
    else:
        coin_flip = 1  # tail            # tail
    return coin_flip


def main():
    win_head = 0  # # of time winning
    win_tail = 0  # of time tails winning
    amount_of_bet = 10  # amount of bet
    good_strategy = 0  # # of time strategy worked.
    bad_strategy = 0
    simulator_count = 10000  # number of time to run simulation

    while simulator_count > 0:                           # once countdown reaches 0 stop the simulation
        simulator_count = simulator_count - 1                 # count for simulations

        number_of_rounds = 500  # reset round counter
        sum_wallet = 1000000  # reset wallet amount

        while number_of_rounds > 0:                            # countdown for 500 rounds

            guess = guess_flip()

            coin_flip = flip_the_coin()

            if coin_flip == 0:  # 55% change of flipping head
                win_head = win_head + 1  # count number of wins for Head
            else:
                win_tail = win_tail + 1  # count number of wins for tail

            if coin_flip == guess:
                sum_wallet = sum_wallet + amount_of_bet
                amount_of_bet = 10
            else:
                sum_wallet = sum_wallet - amount_of_bet
                amount_of_bet = amount_of_bet + 10

            number_of_rounds = number_of_rounds - 1

        if sum_wallet > 1000000:
                good_strategy = good_strategy + 1
        else:
                bad_strategy = bad_strategy + 1

    # n = n + 1
    # print(n) #this is to keep track of progress for long runs.
    print('overall this strategy worked this many times:', good_strategy, 'and failed this many times:', bad_strategy)


if __name__ == "__main__":
    main()
