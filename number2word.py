import word2number as w2n


def format_cell(cell: str) -> str:
    """
    This function formats the cell number by
    removing +, (, ), -, and space.
    """
    return ''.join(c for c in cell if c not in '()+- ')


def create_word_database(filename):
    """
    This function creates a database in nested dictionary containing English
    words of length 3 to 7 letters. The first layer uses the length of words
    as the key and the second layer stores a set of words with the same
    number combination on the number pad.
    """
    output = {3: {}, 4: {}, 5: {}, 6: {}, 7: {}}
    with open(filename) as file:
        list_lines = [line.rstrip('\n') for line in file]
    for line in list_lines:
        word_len = len(line)
        if word_len > 2 and word_len < 8:
            number = format_cell(w2n.words_to_number(line))
            if number in output[word_len].keys():
                output[word_len][number].append(line.upper())
            else:
                output[word_len][number] = [line.upper()]
    return output


def number_to_words(cell):

    """
    This function uses sliding window method to search for all possible combinations
    of numbers that can be wordified. It creates an English word database using most
    widely used 25322 words contained in 'popular.txt' The output is a dictionary
    containing all possible wordifications. The key is the wordified part of the cell
    number.

    'popular.txt' file credit: @dolph on Github

    """

    cell = format_cell(cell)
    cell_trimmed = cell[-7:]
    word_database = create_word_database('popular.txt')
    min_word_len = 3
    output = {}
    for start_index in range(0, 5):
        for end_index in range(start_index+min_word_len-1, 7):
            wordify_number = cell_trimmed[start_index:end_index+1]
            len_wordify_number = len(wordify_number)
            if wordify_number in word_database[len_wordify_number].keys():
                if wordify_number not in output.keys():
                    output[wordify_number] = []
                for word in word_database[len_wordify_number][wordify_number]:
                    """
                        Conditions below are for formatting the output cell number considering all
                    possible conditions. The wordifiable number can be at four of the following
                    locations:
                        1) all seven digits can be wordified;
                        3) starting from the first digit with less than seven letters;
                        2) at the end of number and has less than seven letters;
                        4) in the middle of the number with less than seven letters.
                    The four if-elif-else statements accomplish above classifications by
                    utilizing the starting index of wordified number, counted backwards.
                    """
                    if start_index == 0 and end_index == 6:
                        output_cell = cell[:-7] + '-' + word
                        output[wordify_number].append(output_cell)
                    elif start_index != 0 and end_index == 6:
                        output_cell = cell[:-7] + '-' + cell_trimmed[0:start_index] + '-' + word
                        output[wordify_number].append(output_cell)
                    elif start_index == 0 and end_index != 6:
                        output_cell = cell[:-7] + '-' + word + '-' + cell_trimmed[end_index+1:]
                        output[wordify_number].append(output_cell)
                    else:
                        output_cell = cell[:-7] + '-' + cell_trimmed[:start_index] + '-' + \
                                      word + '-' + cell_trimmed[end_index+1:]
                        output[wordify_number].append(output_cell)
    if not output:
        output[cell] = 'No wordification found'
    return output


def main():
    print(number_to_words('2176666666'))
    print(number_to_words('2176666667'))
    print(number_to_words('8006294000'))
    print(number_to_words('2174170499'))


if __name__ == '__main__':
    main()
