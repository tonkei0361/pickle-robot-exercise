

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
        
def format_cell(cell):
    '''
    This function formats the cell number by
    removing +, (, ), -, and space.
    '''
    
    return ''.join( c for c in cell if c not in '()+- ' )


while(True):
    user_input = input('type a phone number (x to exit) ')
    if user_input == 'x':
        print('Bye!')
        break
    user_input = format_cell(user_input)
    for c in user_input:
        print(c, 'corresponds to ', num2letters(c))


