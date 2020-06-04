"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    i = num_rolls
    roll = 0
    sum_of_rolls = 0
    Dice = dice
    while i != 0:
        roll = Dice()
        if roll == 1:
            return 1
        sum_of_rolls += roll
        i -= 1
    return sum_of_rolls

    # END Question 1


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    if num_rolls == 0:
        digits = [int(i) for i in str(opponent_score)]  # https://stackoverflow.com/questions/21270320/turn-a-single-number-into-single-digits-python
        if len(digits) == 1:
            return 1 + digits[0]
        return max(digits[0] + 1, digits[1] + 1)
    return roll_dice(num_rolls, dice)
    # END Question 2

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score + opponent_score) % 7 == 0:
        return four_sided
    return six_sided
    # END Question 3

def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    p_0_digits = [int(i) for i in str(score0)]  # https://stackoverflow.com/questions/21270320/turn-a-single-number-into-single-digits-python
    p_1_digits = [int(i) for i in str(score1)]  # https://stackoverflow.com/questions/21270320/turn-a-single-number-into-single-digits-python
    if len(p_0_digits) == 1:
        p_0_digits.insert(0, 0)
    if len(p_1_digits) == 1:
        p_1_digits.insert(0, 0)
    if p_0_digits[len(p_0_digits) - 1] == p_1_digits[len(p_1_digits) - 2] and p_0_digits[len(p_0_digits) - 2] == p_1_digits[len(p_1_digits) - 1]:
        return True
    return False
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    while score0 < goal and score1 < goal:
        if other(who):
            score_main = score0
            score_opp = score1
            strat = strategy0
        else:
            score_main = score1
            score_opp = score0
            strat = strategy1

        dice = select_dice(score_main, score_opp)
        num_dice = strat(score_main, score_opp)
        score_main += take_turn(num_dice, score_opp, dice)

        temp = 0

        if is_swap(score_main, score_opp):
            temp = score_main
            score_main = score_opp
            score_opp = temp

        if other(who):
            score0 = score_main
            score1 = score_opp
        else:
            score1 = score_main
            score0 = score_opp

        who = other(who)


    # END Question 5
    return score0, score1


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy
