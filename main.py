from settings import Settings


def get_new_word(letter, cities_list, already_used_words, arguable):
    """gets a new word from the list that starts from the specified letter"""
    next_word = ''
    for word in cities_list:
        if word[0].lower() == letter.lower() and word.lower() not in arguable:
            next_word = word
            break
    if next_word != '':
        update_word_lists(word, cities_list, already_used_words)
    return (next_word, cities_list, already_used_words)

def check_input_word(last_letter, input_word, cities_list, already_used_words, stop_words, arguable):#TODO: check the lose conditions
    """checks if the word is a valid city name and was not used yet"""
    answer = ''
    input_word = input_word.lower()
    if input_word in stop_words:
        return 'stop'
    if last_letter.lower() != input_word[0]:
        if last_letter != '':
            return 'letter'
    for word in already_used_words:
        if word.lower() == input_word:
            answer = 'already'
            break
    if answer == '':
        for word in cities_list:
            if word.lower() == input_word:
                answer = 'valid'
                update_word_lists(word, cities_list, already_used_words)
                break
        for a in arguable:
            if a == input_word:
                answer = 'arguable'
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
    word_lower = word.lower()
    for a in arguable:
        if a.lower() == word_lower:
            return True
    return False


if __name__ == "__main__":
    s = Settings()

    stop_words = s.get_stop_words()
    all_city_pairs = s.get_cities()
    sayings = s.get_sayings()
    arguable_msg = s.get_arguable_saying()
    use_arguable = s.get_use_arguable()
    if use_arguable == True:
        arguable = []
    else:
        arguable_initial = s.get_arguables()
        arguable = []
        for word in arguable_initial:
            arguable.append(word.lower())


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
            answer = check_input_word(last_letter, word, cities_list, already_used_words, stop_words, arguable)
            if answer == 'stop':
                raise SystemExit
            elif answer == '':
                print(sayings['no_such_city_message'])
            elif answer == 'already':
                print(sayings['already_was_message'])
            elif answer == 'letter':
                print(sayings['wrong_letter_message'], last_letter)
            elif answer == 'arguable':
                print(arguable_msg)
            elif answer == 'valid':
                pass

        last_letter = get_last_letter(word)

        answer = get_new_word(last_letter, cities_list, already_used_words, arguable)
        computers_word = answer[0]
        if computers_word == '':
            print(s.get_win_sayng(last_letter))
            stop = 1
        else:
            print(computers_word)
            last_letter = get_last_letter(computers_word)



