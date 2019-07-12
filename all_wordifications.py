import number2word as n2w
import word2number as w2n


def all_wordifications(cell: str):
    cell_trimmed = n2w.format_cell(cell)[-7:]
    word_database = n2w.create_word_database('popular.txt')
    single_wordified_cell = n2w.number_to_words(cell)
    min_len = 3
    output = []
    for index_first_start in range(0, 2):
        for index_first_end in range(index_first_start + min_len, 5):
            first_number = cell_trimmed[index_first_start:index_first_end]
            if first_number in single_wordified_cell.keys():
                first_word_list = word_database[len(first_number)][first_number]
                for index_second_start in range(index_first_end, 5):
                    for index_second_end in range(index_second_start+min_len-1, 7):
                        second_number = cell_trimmed[index_second_start:index_second_end+1]
                        if second_number in single_wordified_cell.keys():
                            second_word_list = word_database[len(second_number)][second_number]
                            for word_f in first_word_list:
                                for word_s in second_word_list:
                                    begin_elem = '' if index_first_start == 0 \
                                        else cell_trimmed[0:index_first_start] + '-'
                                    middle_elem = '-' if index_first_end == index_second_start \
                                        else '-' + cell_trimmed[index_first_end:index_second_start] + '-'
                                    end_elem = '' if index_second_end == 6 \
                                        else '-' + cell_trimmed[index_second_end+1:]
                                    cell_wordified_formatted = n2w.format_cell(cell)[:-7] + '-' + \
                                                               begin_elem + word_f + middle_elem + word_s + end_elem
                                    output.append(cell_wordified_formatted)
    if not output:
        output.append['No other combinations']
    return output


def main():
    cell_test = ['800QUALITY', '617-HARVARD', '800RECTIFY', '800RIGIDLY',
                 '2175683968', '8007825439', '8001397328', '8001ROOKIE',
                 '8002222345', '8006666666']
    selection = -3
    print(w2n.words_to_number(cell_test[selection]))
    print('Single wordification:')
    for key, value in n2w.number_to_words(w2n.words_to_number(cell_test[selection])).items():
        print(key, ':', value)
    print('Multiple wordifications:')
    print(all_wordifications(w2n.words_to_number(cell_test[selection])))
    print(len(all_wordifications(w2n.words_to_number(cell_test[selection]))))


if __name__ == '__main__':
    main()