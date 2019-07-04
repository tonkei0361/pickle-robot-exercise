
def num2letters(num):
    '''
    This function takes a single integer as
    the input and returns the corresponding
    letters on the number pad, organized in
    a list
    '''
    try:
        num = int(num)
    except ValueError:
        print('Input should be an integer!!')
        return 'null'
    
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
    '''
    This function is a recursive function that finds all possible
    conbinations of words corresponding to a series of numbers on
    the number pad. 
    '''

    if(position == len(letters)):
        for elem in letters[-1]:
            words.append(word + elem)
        return words

    for elem in letters[position-1]:
        letters_to_possible_words(letters, word+elem, words, position+1)
    if position == 1:
        return words

def format_cell(cell):
    '''
    This function formats the cell number by
    removing +, (, ), -, and space.
    '''
    return ''.join( c for c in cell if c not in '()+- ' )

def trim_cell(cell):
    '''
    This function trims the input, which is a cell number
    with special characters removed. It removes the area
    code and only leaves the last 7 digits.

    It returns a list of numbers inside the cell number 
    that may be turned into words. The length is set to
    be longer than 2 digits.
    '''
    cell_trimmed = cell[-7:]
    temp = ''
    count = 0
    word_candidates = []
    for c in cell_trimmed:
        count += 1
        if(c == '0' or c == '1'):
            word_candidates.append(temp)
            temp = ''
        else:
            temp += c
        if count == len(cell_trimmed):
            word_candidates.append(temp)
    word_candidates = [s for s in word_candidates if len(s) > 2]
    return word_candidates

def word_database(filename):
    '''
    This function creates a word database used for searching a match
    between a cell number and a word. This database is the most popular
    25322 words. Since words shorter than 3 or longer than 7 letters
    are not used, only useful part of the entire database is selected
    and stored in a dictionary.

    'popular.txt' file credit: @dolph on Github
    '''

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
    '''
    This is the main function that converts part or all of
    a cell number into words.

    Output is a list of cell nubmers with part or all of them
    converted to words.
    '''

    cell = format_cell(cell)
    for string in trim_cell(cell):
        letters_list = []
        for char in string:
            letters_list.append(num2letters(char))
        words_candidates = letters_to_possible_words(letters_list,'',[])
    words_reference = word_database('popular.txt')[len(words_candidates[0])]
    output = []
    for word in words_candidates:
        if word in words_reference:
            output.append(cell.replace(string, word.upper()))
    if not output:
        output.append(cell)
    return output

# Loop to test the function
while True:
    user_input = input('type a phone number (x to exit) ')
    if user_input == 'x':
        print('Bye!')
        break
    print(number_to_words(user_input))



