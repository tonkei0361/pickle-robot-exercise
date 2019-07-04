
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

def nums_to_possible_words(num):
    '''
    This function takes a number in the form of
    a string and returns a list with possible
    combinations of letters that are on the
    number pad.
    '''
    letters_list = []
    words_list = []
    for s in num:
        letters_list.append(num2letters(s))
    
    print(letters_list)
    for elem1 in letters_list[0]:
        word1 = elem1
        for elem2 in letters_list[1]:
            word2 = word1 + elem2
            for elem3 in letters_list[2]:
                word3 = word2 + elem3
                words_list.append(word3)
    print(words_list)

def letters_to_possible_words(letters, word='', words=[], position=1):
    if(position == len(letters_list)):
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

    It returns a list of numbers that may be turned into
    words. The length is set to be longer than 2 digits.
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

print('Word database loading......')
with open('popular.txt') as file:
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
print('Database loaded.')

# Do some random tests
while(False):
    user_input = input('type a phone number (x to exit) ')
    if user_input == 'x':
        print('Bye!')
        break
    print(user_input)
    user_input = format_cell(user_input)

    print('possible candidates are ', trim_cell(user_input))
    nums_to_possible_words(trim_cell(user_input)[0])

# Test the recursion function
while True:
    user_input = input('type a phone number (x to exit) ')
    if user_input == 'x':
        print('Bye!')
        break
    print(user_input)
    user_input = format_cell(user_input)

    letters_list = []
    for string in trim_cell(user_input):
        for char in string:
            letters_list.append(num2letters(char))
    words_candidates = letters_to_possible_words(letters_list,'',[])

    words_reference = words_dict[len(words_candidates[0])]
    found = False
    for string in words_candidates:
        if string in words_reference:
            print('found, the word is', string)
            found = True
    if not found:
        print('nothing found...')



