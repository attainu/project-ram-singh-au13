#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import random
delay_time = 1  # Just for effects adding a delay of 1 sec between the actions
final_pos = 100
dice_face = 6  # max value of dice face

# snake takes you down from key to value

snakes = {
    18: 4,
    26: 10,
    39: 5,
    50: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    92: 25,
    99: 53,
    }

# ladder takes you up from key to value

ladders = {
    3: 20,
    11: 28,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    73: 86,
    }


def welcome_msg():
    msg = \
        """
    Welcome to Snake and Ladder Game.
    1. The first player to get to the Final position is the winner.
    2. Hit enter to roll the dice.
    3. If anyone of the player want to quit game just type 0 and press enter.
    4. The player who quit in between will loose the game
    """
    print(msg)


def get_players_name():
    player1_name = None
    while not player1_name:
        player1_name = input('enter the name for player1: ')
    player2_name = None
    while not player2_name:
        player2_name = input('enter the name for player2: ')
    return (player1_name, player2_name)


def get_dice_value():
    time.sleep(delay_time)
    dice_value = random.randint(1, dice_face)
    print('its a ' + str(dice_value))
    return dice_value


def got_ladder_jump(old_value, curr_value, player_name):
    print('\n' + 'ladder jump' + '-------->')
    print('\n' + player_name + ' got ladder jump from '
               + str(old_value) + ' to ' + str(curr_value))


def got_snake_bite(old_value, curr_value, player_name):
    print('\n' + 'snake bite' + '-------->')
    print('\n' + player_name + ' got snake bite from ' + str(old_value)
               + ' to ' + str(curr_value))


def snake_ladder(player_name, curr_value, dice_value):
    time.sleep(delay_time)
    old_value = curr_value
    curr_value = old_value + dice_value
    if curr_value > final_pos:
        print('you need ' + str(curr_value - final_pos)
                          + ' to win the game')
        return old_value
    print('\n' + player_name + ' move from ' + str(old_value) + ' to '
               + str(curr_value))
    if curr_value in snakes:
        final_value = snakes[curr_value]
        got_snake_bite(curr_value, final_value, player_name)
    elif curr_value in ladders:
        final_value = ladders[curr_value]
        got_ladder_jump(curr_value, final_value, player_name)
    else:
        final_value = curr_value
    return final_value


def check_win(player_name, position):
    time.sleep(delay_time)
    if final_pos == position:
        print(player_name + ' won the game.')
        print('Congratulations ' + player_name)
        exit()


def play_game():
    welcome_msg()
    time.sleep(delay_time)
    (player1_name, player2_name) = get_players_name()
    time.sleep(delay_time)
    player1_curr_pos = 0
    player2_curr_pos = 0

    while True:
        time.sleep(delay_time)
        player1 = input('\n' + player1_name + ': '
                             + 'Your turn'
                             + ' Hit the enter to roll dice: ')
        if player1 == '0':
            print('\n' + player2_name + ' won the game')
            exit()
        print('\nRolling dice...')
        dice_value = get_dice_value()
        time.sleep(delay_time)
        print(player1_name + ' moving....')
        player1_curr_pos = snake_ladder(player1_name,
                                        player1_curr_pos, dice_value)

        check_win(player1_name, player1_curr_pos)

        player2 = input('\n' + player2_name + ': '
                             + 'Your turn'
                             + ' Hit the enter to roll dice: ')
        if player2 == '0':
            print('\n' + player1_name + ' won the game')
            exit()
        print('\nRolling dice...')
        dice_value = get_dice_value()
        time.sleep(delay_time)
        print(player2_name + ' moving....')
        player2_curr_pos = snake_ladder(player2_name,
                                        player2_curr_pos, dice_value)

        check_win(player2_name, player2_curr_pos)


if __name__ == '__main__':
    play_game()
