import numpy as np
import random
import re
import os


def print_initial_matrix():
    print('This is my Wordle game, prepared as a qualifying test for the ML&Texts Summer School')
    print('------------------------------------------------------------------------------------')
    print('Rules are simple:')
    print('Player is given 6 attempts to guess a word.\nPlayer enters each word separately, and then letters are highlighted for him - \nif the letter highlighted in green, then these letters are not in the word at all. \nRepeating letters not observed - \nif the player is verified word with one letter S and it highlighted green, \nit may be that there is still S in other places. \nAfter six tries game ends, but if the word is guessed before, the game ends immediately. \nWords, whose length is not equal to five is not accepted, \nlike the words that are not in the dictionary')
    print('------------------------------------------------------------------------------------')
    print('To quit the game, type \'quit\'')
    print('\033[91mYou can manipulate vocabulary. \'words-for-guess.txt\' is the original Wordle wordlist that \nis used in random word selection\033[0m')
    print('------------------------------------------------------------------------------------')
    matrix = [['|', '-', '|', '-', '|', '-', '|', '-', '|', '-', '|'],
              ['|', '-', '|', '-', '|', '-', '|', '-', '|', '-', '|'],
              ['|', '-', '|', '-', '|', '-', '|', '-', '|', '-', '|'],
              ['|', '-', '|', '-', '|', '-', '|', '-', '|', '-', '|'],
              ['|', '-', '|', '-', '|', '-', '|', '-', '|', '-', '|'],
              ['|', '-', '|', '-', '|', '-', '|', '-', '|', '-', '|']]

    for i in range(0, 6):
        print(*matrix[i], end=' ')
        print('\n')
    return matrix


def random_word_selector(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.split('\n')
        random_word = random.choice(content)
        return random_word, content


def input_parser(word_by_player: str, all_words: list):
    with open('wordle-Ta.txt', 'r') as file:
        content = file.read()
        all_eng_word = content.split('\n')

    pattern = re.compile(r'^[a-zA-Z]+$')
    all_words = set(all_words)
    latin = 0
    length_five = 0
    is_in_dict = 0
    error = 0

    if all(pattern.fullmatch(lit) for lit in list(word_by_player)):
        latin = 1
    else:
        print("Input error! There must be only latin letters!")

    if len(list(word_by_player)) == 5:
        length_five = 1
    else:
        print("Input error! Length of the word should be five")
    if word_by_player.lower() in all_words or word_by_player.lower() in all_eng_word:
        is_in_dict = 1
    else:
        print("Input error! There is no such word!")

    if not (latin and length_five and is_in_dict):
        error = 1

    return word_by_player, error


def letter_counter(word: str):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict


def input_in_matrix(matrix: list, word_by_player: str,
                    word_for_guessing: str, try_num: int):
    position_codes = [0, 0, 0, 0, 0]
    enum_letters_by_player = {i: char.lower()
                              for i, char in enumerate(word_by_player)}
    enum_letters_for_guessing = {i: char.lower()
                                 for i, char in enumerate(word_for_guessing)}

    cnt_letters_by_player = letter_counter(word_by_player)
    cnt_letters_for_guessing = letter_counter(word_for_guessing)

    x_position = 0

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Try number:{try_num+1}')
    for key_player, value_player in enum_letters_by_player.items():
        used_flag = 0

        if enum_letters_by_player.get(
                key_player) == enum_letters_for_guessing.get(key_player):
            letter = enum_letters_by_player.get(key_player)
            if cnt_letters_by_player.get(letter) > cnt_letters_for_guessing.get(
                    letter) and used_flag == 0:
                matrix[try_num][x_position + x_position +
                                1] = f"\033[32m{letter}\033[0m"
                used_flag = 1
                print(f"\033[32m{letter} is in a right place\033[0m")
                x_position += 1
                position_codes[key_player] = 1
            else:
                matrix[try_num][x_position + x_position +
                                1] = f"\033[32m{letter}\033[0m"
                print(f"\033[32m{letter} is in a right place\033[0m")
                x_position += 1
                position_codes[key_player] = 1

        elif enum_letters_by_player.get(key_player) != enum_letters_for_guessing.get(key_player) and (enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(0) or
                                                                                                      enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(1) or
                                                                                                      enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(2) or
                                                                                                      enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(3) or
                                                                                                      enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(4)):

            letter = enum_letters_by_player.get(key_player)
            if cnt_letters_by_player.get(letter) > cnt_letters_for_guessing.get(letter) and (enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(0) or
                                                                                             enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(1) or
                                                                                             enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(2) or
                                                                                             enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(3) or
                                                                                             enum_letters_by_player.get(key_player) == enum_letters_for_guessing.get(4)):
                matrix[try_num][x_position + x_position +
                                1] = f"\033[90m{letter}\033[0m"
                cnt_letters_by_player[letter] = cnt_letters_by_player.get(
                    letter) - 1
                print(f"\033[90m{letter} is not in the word at all\033[0m")
                x_position += 1
            else:
                if cnt_letters_by_player.get(letter) > cnt_letters_for_guessing.get(
                        letter) and used_flag == 0:
                    matrix[try_num][x_position + x_position +
                                    1] = f"\033[91m\033[93m{letter}\033[0m"
                    used_flag = 1
                    print(
                        f"\033[91m\033[93m{letter} is not in a right place\033[0m")
                    x_position += 1

                elif cnt_letters_by_player.get(letter) > cnt_letters_for_guessing.get(letter) and used_flag == 1:
                    matrix[try_num][x_position + x_position +
                                    1] = f"\033[90m{letter}\033[0m"
                    cnt_letters_by_player[letter] = cnt_letters_by_player.get(
                        letter) - 1
                    print(f"\033[90m{letter} is not in the word at all\033[0m")
                    x_position += 1

                else:
                    matrix[try_num][x_position + x_position +
                                    1] = f"\033[91m\033[93m{letter}\033[0m"
                    print(
                        f"\033[91m\033[93m{letter} is not in a right place\033[0m")
                    x_position += 1

        else:

            letter = enum_letters_by_player.get(key_player)
            matrix[try_num][x_position + x_position +
                            1] = f"\033[90m{letter}\033[0m"
            print(f"\033[90m{letter} is not in the word at all\033[0m")
            x_position += 1

    print('---------------------')
    for i in range(0, 6):
        print(*matrix[i], end=' ')
        print('\n')
    print('---------------------')


def congrats():
    print('-------------------------')
    print('CONGRATULATIONS! YOU WON!')
    print('-------------------------')



def loose(guessed_word: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('----------------------------------------------------------------')
    print(f'UNFORTUNATELY, ATTEMPTS ARE OVER! GUESSED WORD: {guessed_word}')
    print('----------------------------------------------------------------')
