import re


def num2letters(num: str):
    """
    This function takes a single integer as the input and returns
    the corresponding letters on the number pad.
    """
    num = int(num)

    if num == 2:
        letters = ['a', 'b', 'c']
    elif num == 3:
        letters = ['d', 'e', 'f']
    elif num == 4:
        letters = ['g', 'h', 'i']
    elif num == 5:
        letters = ['j', 'k', 'l']
    elif num == 6:
        letters = ['m', 'n', 'o']
    elif num == 7:
        letters = ['p', 'q', 'r', 's']
    elif num == 8:
        letters = ['t', 'u', 'v']
    elif num == 9:
        letters = ['w', 'x', 'y', 'z']
    else:
        letters = [str(num)]
    return letters


def letters_to_possible_words(letters, word='', words=[], position=1):
    """
    This function is a recursive function that finds all possible
    combinations of words corresponding to a series of numbers on
    the number pad.

    Parameters
    ----------
    letters: list[list[str]]
        A list containing lists that stores corresponding letters of a number
        on the number pad.
    word: str
        A temporary parameter for recursion storing one combination of all
        possible words.
    words: list[str]
        A list storing all possible combinations of number-to-word for a specific
        number.
    position: int
        A variable to keep track of which digit current recursive function is
        at.

    Returns
    -------
    words: list[str]
        A list storing all possible combinations of number-to-word for a specific
        number.
    """

    if position == len(letters):
        for elem in letters[-1]:
            words.append(word + elem)
        return words

    for elem in letters[position - 1]:
        letters_to_possible_words(letters, word + elem, words, position + 1)
    if position == 1:
        return words


def format_cell(cell: str) -> str:
    """
    This function formats the cell number by
    removing +, (, ), -, and space.
    """
    return ''.join(c for c in cell if c not in '()+- ')


def find_single_wordification(cell):
    """
    This function identifies all possible ways that a cell number
    can be rewritten in terms of a single word with a minimum length.
    It can be part or all of the cell number.

    For example, 79374 with minimum of 3 letters, the function returns
    [793, 7937, 79374, 937, 9374, 374].
    """
    cell = format_cell(cell)
    number_candidates = [elem for elem in re.split('0|1', cell[-7:]) if len(elem) > 2]
    number_candidates_all_combinations = {}
    minimum_letters = 3

    for string in number_candidates:
        for start_index in range(0, len(string)-minimum_letters+1):
            end_index = start_index + minimum_letters
            while end_index <= len(string):
                word_len = end_index - start_index
                if word_len in number_candidates_all_combinations:
                    number_candidates_all_combinations[word_len].append(string[start_index:end_index])
                else:
                    number_candidates_all_combinations[word_len] = [(string[start_index:end_index])]
                end_index += 1
            number_candidates_all_combinations[word_len] = list(set(number_candidates_all_combinations[word_len]))
    return number_candidates_all_combinations


def special_case(cell, repeated_num, count):
    cell = format_cell(cell)
    cell_trimmed = cell[-7:]
    if count == 4:
        pass
    elif count == 5:
        pass
    elif count == 6:
        pass
    elif count == 7:
        pass
    else:
        pass


def word_database(filename):
    """
    This function creates a word database used for searching a match
    between a cell number and a word. This database is the most popular
    25322 words. Since words shorter than 3 or longer than 7 letters
    are not used, only useful part of the entire database is selected
    and stored in a dictionary.

    'popular.txt' file credit: @dolph on Github

    """

    with open(filename) as file:
        list_lines = [line.rstrip('\n') for line in file]
        words_3char = [s for s in list_lines if len(s) == 3]
        words_4char = [s for s in list_lines if len(s) == 4]
        words_5char = [s for s in list_lines if len(s) == 5]
        words_6char = [s for s in list_lines if len(s) == 6]
        words_7char = [s for s in list_lines if len(s) == 7]
    words_dict = {
        3: words_3char,
        4: words_4char,
        5: words_5char,
        6: words_6char,
        7: words_7char
    }
    return words_dict


def number_to_words(cell):
    """
    This is the main function that converts part or all of
    a cell number into words.

    Output is a list of cell numbers with part or all of them
    converted to words.
    """

    cell = format_cell(cell)
    cell_trimmed = cell[-7:]
    output = {}
    repeated_segment = 'None'
    for char in '23456789':
        num_occurrence = cell[-7:].count(char)
        if num_occurrence > 3:
            repeated_segment = char * num_occurrence

    for combinations in find_single_wordification(cell).values():
        for string in combinations:
            letters_list = []
            for char in string:
                letters_list.append(num2letters(char))
            words_candidates = letters_to_possible_words(letters_list, '', [])
            words_reference = word_database('popular.txt')[len(string)]
            for word in words_candidates:
                if word in words_reference and string not in repeated_segment:
                    """
                        Conditions below are for formatting the output cell number considering all
                    possible conditions. The wordifiable number can be at four of the following
                    locations:
                        1) starting from the first digit with less than seven letters;
                        2) at the end of number and has less than seven letters;
                        3) all seven digits can be wordified;
                        4) in the middle of the number with less than seven letters.
                    The four if-elif-else statements accomplish above classifications by
                    utilizing the starting index of wordified number, counted backwards.
                    """
                    index = cell.find(string) - len(cell)
                    if index == -7 and len(word) < 7:
                        output_cell = cell[:index] + \
                                      '-' + word.upper() + \
                                      '-' + cell[index+len(word):]
                    elif -index == len(word) and len(word) < 7:
                        output_cell = cell[:-7] + \
                                      '-' + cell[-7:index] + \
                                      '-' + word.upper()
                    elif index == -7 and len(word) == 7:
                        output_cell = cell[:index] + \
                                      '-' + word.upper()
                    else:
                        output_cell = cell[:-7] + \
                                      '-' + cell[-7:index] + \
                                      '-' + word.upper() + \
                                      '-' + cell[index+len(word):]
                    if string not in output:
                        output[string] = [output_cell]
                    else:
                        output[string].append(output_cell)
                elif word in words_reference and string in repeated_segment:
                    """
                        This portion follows the same logic above for repeated elements. All possible
                        location of a word inside repeated portion of a cell number is list out. To
                        test the function, use inputs like 800-233-3333 and 800-666-6666
                    """
                    for start_index in range(cell_trimmed.find(repeated_segment),len(repeated_segment)+1-len(string)):
                        end_index = start_index + len(string)
                        if start_index == 0 and end_index != 7:
                            output_cell = cell[:-7] + '-' + word.upper() + '-' + cell_trimmed[end_index:]
                        elif start_index != 0 and end_index == 7:
                            output_cell = cell[:-7] + cell_trimmed[:start_index] + '-' + word.upper()
                        elif start_index == 0 and end_index == 7:
                            output_cell = cell[:-7] + '-' + word.upper()
                        else:
                            output_cell = cell[:-7] + '-' + cell_trimmed[:start_index] + '-' + word.upper() + '-' + cell_trimmed[end_index:]
                        if string not in output:
                            output[string] = [output_cell]
                        else:
                            output[string].append(output_cell)
    if not output:
        output['None'] = [cell]
    return output


def main():
    while True:
        print(number_to_words('2176666666'))
        print(number_to_words('2176666667'))
        print(number_to_words('8006294000'))
        # user_input = input('type a phone number (x to exit) ')
        # if user_input == 'x':
        #     print('Bye!')
        #     break
        # for key, value in number_to_words(user_input).items():
        #     print(key, '->', value)
        # print(find_single_wordification(user_input))
        break


if __name__ == '__main__':
    exit(main())
