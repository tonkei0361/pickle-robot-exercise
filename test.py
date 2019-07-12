import all_wordifications as aw
import number2word as n2w
import word2number as w2n

cell_test = ['8001EMPIRE', '800QUALITY', '617-HARVARD', '800RECTIFY',
             '2175683968', '8007825439', '8001397328', '8001ROOKIE',
             '8002222345', '8006666666', '2174170499', '8006294000',
             '800-747-9300', '6174797052', '880JACKSON', '9811HEYDOG',
             '217LD13KSX', '800RIGIDLY']

for cell in cell_test:
    print('Original input:', cell)
    print('Convert to numerical only:', w2n.words_to_number(cell))
    print('Single wordification:')
    for key, value in n2w.number_to_words(w2n.words_to_number(cell)).items():
        print(key, ':', value)
    print('Now, find all other combinations.')
    print(aw.all_wordifications(w2n.words_to_number(cell)))
    print(len(aw.all_wordifications(w2n.words_to_number(cell))))
    input('To go to next case, hit enter...')
