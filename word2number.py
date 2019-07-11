
def words_to_number(cell):
    """
    This function takes a number containing words and other characters and convert
    all alphabets to numbers.
    """

    cell = cell.upper()
    cell = ''.join(c for c in cell if c not in '()+- ')

    for char in cell:
        if char in 'ABC':
            cell = cell.replace(char, '2')
        elif char in 'DEF':
            cell = cell.replace(char, '3')
        elif char in 'GHI':
            cell = cell.replace(char, '4')
        elif char in 'JKL':
            cell = cell.replace(char, '5')
        elif char in 'MNO':
            cell = cell.replace(char, '6')
        elif char in 'PQRS':
            cell = cell.replace(char, '7')
        elif char in 'TUV':
            cell = cell.replace(char, '8')
        elif char in 'WXYZ':
            cell = cell.replace(char, '9')
        else:
            pass
        output = cell[:-7] + '-' + cell[-7:-4] + '-' + cell[-4:]
    return output


def main():
    test_cases = ['800REST479', '617HARVARD', '800QUALITY', '800RECTIFY', '800RIGIDLY', '8001ROOKIE']
    for test in test_cases:
        print('Convert', test, ':', words_to_number(test))
    while True:
        user_input = input('tyep a number with letters (x to exit):')
        if user_input == 'x':
            print('Bye!')
            break
        print(words_to_number(user_input))


if __name__ == '__main__':
    main()

