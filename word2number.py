
def words_to_number(cell):

    cell = cell.upper()

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
    return cell

while True:
    user_input = input('tyep a number with letters (x to exit):')
    if user_input == 'x':
        print('Bye!')
        break
    print(words_to_number(user_input))


