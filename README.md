# pickle-robot-exercise

## number2word.py

This file contains multiple functions. The main function that converts a cell number to wordified version is called 'number_to_word'. A cell number is converted by following these steps:
1. Taking a number of type string as input, the function first removes any symbols such as brackets to clean up the format.
2. Only last 7 digits are used for conversion because usually area code is not modified. 0 and 1 do not have corresponding letters.
3. It searches for any combinations of numbers that do not have 0 and 1 and have more than 2 numbers. These combinations can be converted into words.
4. 