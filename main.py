from settings import Settings


def get_new_word(letter, cities_list, already_used_words):
    """gets a new word from the list that starts from the specified letter"""
    next_word = ''
    for word in cities_list:
        if word[0].lower() == letter.lower():
            next_word = word
            break
    if next_word != '':
        update_word_lists(word, cities_list, already_used_words)
    return (next_word, cities_list, already_used_words)

def check_input_word(last_letter, input_word, cities_list, already_used_words, stop_words):
    """checks if the word is a valid city name and was not used yet"""
    if input_word.lower() in stop_words:
        raise SystemExit
    answer = ''

    if last_letter.lower() != input_word[0].lower():
        if last_letter != '':
            print(sayings['wrong_letter_message'], last_letter)
            return 'letter'
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

def check_arguable(word, arguable):
    for a in arguable:
        if a.lower() == word.lower():
            return True
    return False

s = Settings()

stop_words = s.get_stop_words()
all_city_pairs = s.get_cities()
arguable = s.get_arguables()
sayings = s.get_sayings()
arguable_msg = s.get_arguable_saying()
use_arguable = s.get_use_arguable()

cities_list = []
already_used_words = []

for pair in all_city_pairs:
    cities_list.append(pair[0])

print(sayings['greeting'])
stop = 0
last_letter = ''
while not stop:
    answer = ''
    while not answer == 'valid':
        word = input()
        answer = check_input_word(last_letter, word, cities_list, already_used_words, stop_words)
        if answer == '':
            print(sayings['no_such_city_message'])
        elif answer == 'already':
            print(sayings['already_was_message'])
        elif answer == 'valid':
            if use_arguable == False:
                if check_arguable(word, arguable):
                    answer = 'arguable'
                    print(arguable_msg)

    last_letter = get_last_letter(word)
    answer = get_new_word(last_letter, cities_list, already_used_words)
    computers_word = answer[0]
    if computers_word == '':
        print(s.get_win_sayng(last_letter))
        stop = 1
    else:
        print(computers_word)
        last_letter = get_last_letter(computers_word)



