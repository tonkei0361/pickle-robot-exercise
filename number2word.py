
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

def nums2words(num):
    '''
    This function takes a number in the form of
    a string and returns a list with possible
    combinations of letters that are on the
    number pad.
    '''
    letters_list = []
    for s in num:
        letters_list.append(num2letters(s))
    print(letters_list)
        
    
        
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
print('Database loaded.')


while(True):
    user_input = input('type a phone number (x to exit) ')
    print((user_input))
    if user_input == 'x':
        print('Bye!')
        break
    user_input = format_cell(user_input)
    print('possible candidates are ', trim_cell(user_input))
    nums2words(trim_cell(user_input)[0])


