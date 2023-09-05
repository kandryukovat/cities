import sqlite3
conn = sqlite3.connect('game.db')
cur = conn.cursor()
set = cur.execute('SELECT * FROM cities')
all_city_pairs = cur.fetchall()
conn.close()


def get_new_word(letter, cities_list, already_used_words):
    """gets a new word from the list that starts from the specified letter"""
    next_word = ''
    for word in cities_list:
        #print(word[0])
        if word[0].lower() == letter.lower():
            next_word = word
            break
    if next_word != '':
        update_word_lists(word, cities_list, already_used_words)
    return (next_word, cities_list, already_used_words)

def check_input_word(input_word, cities_list, already_used_words, stop_words):
    """checks if the word is a valid city name and was not used yet"""
    if input_word.lower() in stop_words:
        raise SystemExit
    answer = ''
    for word in already_used_words:
        if word.lower() == input_word.lower():
            answer = 'already'
            break
    if answer == '':
        for word in cities_list:
            if word.lower() == input_word.lower():
                answer = 'valid'
                update_word_lists(word, cities_list, already_used_words)
                break
    return answer

def update_word_lists(word, cities_list, already_used_words):
    cities_list.remove(word)
    already_used_words.append(word)

def get_last_letter(word):
    last_letter = word[-1].lower()
    prohibited = ['ь', 'ъ', 'ы']
    if last_letter in prohibited:
        last_letter = word[-2].lower()
    return last_letter

stop_words = ['стоп', 'сдаюсь']#TODO вынести в настройки
cities_list = []
already_used_words = []
for pair in all_city_pairs:
    cities_list.append(pair[0])
#print(cities_list)
print('Начинай')
stop = 0
while not stop:
    answer = ''
    while not answer == 'valid':
        word = input()
        answer = check_input_word(word, cities_list, already_used_words, stop_words)
        if answer == '':
            print('Такого города не существует в РФ, попробуй еще раз')
        elif answer == 'already':
            print('Этот город уже назывался. Попробуй еще раз')

    last_letter = get_last_letter(word)
    answer = get_new_word(last_letter, cities_list, already_used_words)
    if answer[0] == '':
        print('Города на букву', last_letter, 'закончились\nТвоя победа!')
        stop = 1
    else:
        print(answer[0])



