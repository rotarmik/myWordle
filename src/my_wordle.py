import realisation

current_matrix = realisation.print_initial_matrix()
word_for_guessing, all_words = realisation.random_word_selector(
    'words-for-guess.txt')
try_num = 0
word_by_palayer = ''

win_flag = 0

while (word_by_palayer != ('quit') and try_num < 6 and win_flag == 0):

    if word_by_palayer.lower() == word_for_guessing:
        win_flag = 1
        break
    else:
        word_by_palayer, error = realisation.input_parser(input(), all_words)

    if error == 0:
        realisation.input_in_matrix(
            current_matrix,
            word_by_palayer,
            word_for_guessing,
            try_num)
        try_num += 1

if win_flag == 1:
    realisation.congrats()
else:
    realisation.loose(word_for_guessing)
