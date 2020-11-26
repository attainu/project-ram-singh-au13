#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import random
delay_time = 1  # Just for effects adding a delay of 1 sec between the actions
max_pos = 100
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

player_turn_text = [
    'Your turn.',
    'Go.',
    'Please proceed.',
    'Are you ready?',
    '',
    ]

snake_bite = ['bummer', 'snake bite', 'oh no']

ladder_jump = ['woohoo', 'woww', 'yaayyy']


def welcome_msg():
    msg = \
        """
    Welcome to Snake and Ladder Game.
    1. Initally both the players are at starting position 0
    2. If you lands at the tail of a ladder,
        you can move up to the head of the ladder.
    3. If you lands on the head of a snake,
        you must slide down to the tail of the snake.
    4. The first player to get to the Final position is the winner.
    5. Hit enter to roll the dice.

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


def got_ladder_jump(old_value, current_value, player_name):
    print('\n' + random.choice(ladder_jump) + '-------->')
    print('\n' + player_name + ' got ladder jump from '
               + str(old_value) + ' to ' + str(current_value))


def got_snake_bite(old_value, current_value, player_name):
    print('\n' + random.choice(snake_bite) + '-------->')
    print('\n' + player_name + ' got snake bite from ' + str(old_value)
               + ' to ' + str(current_value))


def snake_ladder(player_name, current_value, dice_value):
    time.sleep(delay_time)
    old_value = current_value
    current_value = old_value + dice_value
    if current_value > max_pos:
        print('you need ' + str(current_value - max_pos)
                          + ' to win the game')
        return old_value
    print('\n' + player_name + ' move from ' + str(old_value) + ' to '
               + str(current_value))
    if current_value in snakes:
        final_value = snakes[current_value]
        got_snake_bite(current_value, final_value, player_name)
    elif current_value in ladders:
        final_value = ladders[current_value]
        got_ladder_jump(current_value, final_value, player_name)
    else:
        final_value = current_value
    return final_value


def check_win(player_name, position):
    time.sleep(delay_time)
    if max_pos == position:
        print(player_name + ' won the game.')
        print('Congratulations ' + player_name)
        exit()


def start():
    welcome_msg()
    time.sleep(delay_time)
    (player1_name, player2_name) = get_players_name()
    time.sleep(delay_time)
    player1_current_pos = 0
    player2_current_pos = 0

    while True:
        time.sleep(delay_time)
        input('\n' + player1_name + ': '
              + random.choice(player_turn_text)
              + ' Hit the enter to roll dice: ')
        print('\nRolling dice...')
        dice_value = get_dice_value()
        time.sleep(delay_time)
        print(player1_name + ' moving....')
        player1_current_pos = snake_ladder(player1_name,
                                           player1_current_pos, dice_value)

        check_win(player1_name, player1_current_pos)

        input('\n' + player2_name + ': '
              + random.choice(player_turn_text)
              + ' Hit the enter to roll dice: ')
        print('\nRolling dice...')
        dice_value = get_dice_value()
        time.sleep(delay_time)
        print(player2_name + ' moving....')
        player2_current_pos = snake_ladder(player2_name,
                                           player2_current_pos, dice_value)

        check_win(player2_name, player2_current_pos)


if __name__ == '__main__':
    start()
