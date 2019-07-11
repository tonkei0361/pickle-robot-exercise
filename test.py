import all_wordifications as aw
import number2word as n2w
import word2number as w2n

# Test number_to_word function
test_n2w = ['800-747-9300', '8006294000', '6174797052']
print(test_n2w)

for case in test_n2w:
    wordified = n2w.number_to_words(case)
    print(wordified)
    for wordified_numbers_list in wordified.values():
        for wordified_number in wordified_numbers_list:
            if n2w.format_cell(w2n.words_to_number(wordified_number)) != n2w.format_cell(case):
                print('Mismatch detected!')

# Test word_to_number function
test_w2n = ['880JACKSON', '9811HEYDOG', '800BLABLA1', '217LD13KSX']
print(test_w2n)
numeric_list = []
for case in test_w2n:
    numeric = w2n.words_to_number(case)
    numeric_list.append(numeric)
print(numeric_list)