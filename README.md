# pickle-robot-exercise

## number2word.py

This file contains multiple functions. The main function that converts a cell number to wordified version is called <code>number_to_word</code>. A cell number is converted by following these steps:
1. Taking a number of type string as input, the function first removes any symbols such as brackets to clean up the format.
2. Only last 7 digits are used for conversion because usually area code is not modified. 0 and 1 do not have corresponding letters.
3. It searches for any combinations of numbers that do not have 0 and 1 and have more than 2 numbers. These combinations can be converted into words.
4. Using all combinations of numbers found from above step, it lists all possible combinations of letters that correspond to each digit on the number pad for each combination of numbers.
5. This file creates a dictionary used for looking up a match between a word and any combinations of letters. After obtaining all combinations of letters, it starts searching for any matching cases. It is possible to find multiple words that match with the same number.
6. The function returns the same, wordified cell number. If no words are found, it returns the original number.

## word2number.py

This file converts any alphabets inside a cell number into corresponding number on the number pad. Different from above function, this function is much simpler. Each alphabet has only one matching number, so there is no need to find any possible combinations.