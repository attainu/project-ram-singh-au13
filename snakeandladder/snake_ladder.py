#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import random
delay_time = 1  # Just for effects adding a delay of 1 sec between the actions
max_val = 100
dice_face = 6  # max value of dice face

# snake takes you down from key to value

snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63,
    }

# ladder takes you up from key to value

ladders = {
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91,
    }

player_turn_text = [
    'Your turn.',
    'Go.',
    'Please proceed.',
    'Lets win this.',
    'Are you ready?',
    '',
    ]

snake_bite = ['boohoo', 'bummer', 'snake bite', 'oh no', 'dang']

ladder_jump = ['woohoo', 'woww', 'nailed it', 'oh my God...', 'yaayyy']


def welcome_msg():
    msg = \
        """
    Welcome to Snake and Ladder Game.
    Developed by: Ram Punia
    1. Initally both the players are at starting position 0
    2. If you lands at the bottom of a ladder,
        you can move up to the top of the ladder.
    3. If you lands on the head of a snake,
        you must slide down to the bottom of the snake.
    4. The first player to get to the FINAL position is the winner.
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
    if current_value > max_val:
        print('you need ' + str(current_value - max_val)
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
    if max_val == position:
        print('''


Thats it.

''' + player_name + ' won the game.')
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
