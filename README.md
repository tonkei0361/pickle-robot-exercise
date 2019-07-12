# pickle-robot-exercise

## number2word.py

In this file, a cell number is converted into wordified version with a single word. The procedure is as below:
1. The function first creates a database in the form of a nested dictionary containing words of length 3 to 7 letters.
Inside the database, words are organized based on their corresponding numbers on the number pad.
2. Sliding window algorithm is used to find any matches between the cell number and the word database.
3. If there is a match, that portion of the cell number is replaced with corresponding word/s.
4. Steps 2 and 3 are repeated to find all possible words that fit inside the cell number.

One simplification made in this problem is that the minimum length of a word is limited to 3 letters. This is to make
wordified cell number more meaningful and does not contain words like as, if, or. However, if desired, the function
can be easily changed to fit different needs.

## word2number.py

This file converts any alphabets inside a cell number into corresponding number on the number pad. 
Each alphabet has only one matching number, so there is no need to find any possible combinations.

## all_wordifications.py

This file utilizes functions inside above two files to find all possible combinations of wordifications. With the
minimum length of a word being 3 letters, at most 2 words can fit inside a cell number. The function 
<code>all_wordification</code> uses sliding window algorithm as well to find all possible combinations.