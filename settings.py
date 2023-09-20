import sqlite3

class Settings():

    def __init__(self):
        self.conn = sqlite3.connect('game.db')
        self.cur = self.conn.cursor()
        set = self.cur.execute('SELECT * FROM cities')
        self.all_city_pairs = self.cur.fetchall()
        self.lang = 'ru'#TODO: add other languages
        self.stop_words = {'ru': ['стоп', '0', 'сдаюсь'], 'en': ['stop', '0']}
        self.arguable_ru = ['Алупка', 'Алушта', 'Армянск', 'Бахчисарай', 'Белогорск', 'Джанкой',
            'Евпатория', 'Керчь', 'Красноперекопск', 'Саки', 'Севастополь', 'Симферополь',
            'Старый Крым', 'Судак', 'Феодосия', 'Щёлкино', 'Ялта']
        self.use_arguable = False


    def get_lang(self):
        return self.lang


    def get_cities(self):
        return self.all_city_pairs


    def get_stop_words(self):
        if self.lang == 'ru':
            return self.stop_words['ru']
        elif self.lang == 'en':
            return self.stop_words['en']
        else:
            return ['0']


    def get_arguables(self):
        if self.lang == 'ru':
            return self.arguable_ru
        else:
            return []


    def close_connection(self):
        self.conn.close()


    def get_sayings(self):
        if self.lang == 'ru':
            greeting = 'Привет, начинай!'
            no_such_city_message = 'Такого города не существует в РФ, попробуй еще раз'
            already_was_message = 'Этот город уже назывался. Попробуй еще раз'
            wrong_letter_message = 'Нужно назвать город на букву'
        else:
            greeting = 'Hi, shoot!'
            no_such_city_message = 'There is no such city in USA. Try again'
            already_was_message = 'This one has already been named. Try again'
            wrong_letter_message = 'You have to enter a city that starts with the letter'
        return {'greeting': greeting,
                'no_such_city_message': no_such_city_message,
                'already_was_message': already_was_message,
                'wrong_letter_message': wrong_letter_message}


    def get_win_sayng(self, letter):
        if self.lang == 'ru':
            you_win_message = 'Города на букву ' + letter + ' закончились\nТвоя победа!'
        else:
            you_win_message = 'There is no more cities that end on ' + letter + '\nYou win!'
        return you_win_message


    def get_arguable_saying(self):
        return 'Этот город не признан за РФ. При текущих настройках такие города не участвуют в игре'


    def get_use_arguable(self):
        return self.use_arguable

"""
    def change_lang(self, value):
        try:
            self.cur.execute('UPDATE Main SET lang = ?', (value,))
        except:
            return False
        else:
            self.conn.commit()
            self.lang = value
            return True
"""


