import unittest
import main as game

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.cities_list = []


    def test_get_new_word_ru_1(self):
        """if an appropriate city name exists"""
        cities_list = ['Анапа', 'Агрыз', 'Брянск', 'Новосибирск', 'Москва']
        already_used_words = []
        letter = 'а'
        res = game.get_new_word(letter, cities_list, already_used_words)
        self.assertEqual(res, ('Анапа', ['Агрыз', 'Брянск', 'Новосибирск', 'Москва'], ['Анапа']))


    def test_get_new_word_ru_2(self):
        """if an appropriate city name doesn't exist"""
        cities_list = ['Анапа', 'Брянск', 'Новосибирск', 'Москва']
        already_used_words = ['Омск']
        letter = 'в'
        res = game.get_new_word(letter, cities_list, already_used_words)
        self.assertEqual(res, ('', ['Анапа', 'Брянск', 'Новосибирск', 'Москва'], ['Омск']))

    def test_check_input_word_ru_1(self):#check_input_word(last_letter, input_word, cities_list, already_used_words, stop_words)
        """if the first letter of an input word is wrong"""
        last_letter = 'б'
        input_word = 'анапа'
        cities_list = ['Брянск', 'Москва']
        already_used_words = []
        stop_words = []
        answer = game.check_input_word(last_letter, input_word, cities_list, already_used_words, stop_words)
        self.assertEqual(answer,'letter')

    def test_check_input_word_ru_2(self):
        """if the input word was already used"""
        last_letter = 'б'
        input_word = 'бийск'
        cities_list = ['Брянск', 'Москва']
        already_used_words = ['Бийск']
        stop_words = []
        answer = game.check_input_word(last_letter, input_word, cities_list, already_used_words, stop_words)
        self.assertEqual(answer,'already')


    def test_check_input_word_ru_3(self):
        """if the input word is not in the list"""
        last_letter = 'б'
        input_word = 'бийск'
        cities_list = ['Брянск', 'Москва']
        already_used_words = []
        stop_words = []
        answer = game.check_input_word(last_letter, input_word, cities_list, already_used_words, stop_words)
        self.assertEqual(answer,'')


    def test_check_input_word_ru_4(self):
        """if the input word is in the list"""
        last_letter = 'б'
        input_word = 'брянск'
        cities_list = ['Брянск', 'Москва']
        already_used_words = []
        stop_words = []
        answer = game.check_input_word(last_letter, input_word, cities_list, already_used_words, stop_words)
        self.assertEqual(answer,'valid')


    def test_check_input_word_ru_5(self):
        """if the input word starts with a big letter """
        last_letter = 'б'
        input_word = 'БрЯнСК'
        cities_list = ['Брянск', 'Москва']
        already_used_words = []
        stop_words = []
        answer = game.check_input_word(last_letter, input_word, cities_list, already_used_words, stop_words)
        self.assertEqual(answer,'valid')


    def test_check_input_word_ru_6(self):
        """if the input word is a stop word """
        last_letter = 'б'
        input_word = 'стоп'
        cities_list = ['Брянск', 'Москва']
        already_used_words = []
        stop_words = ['0', 'стоп', 'хватит']
        answer = game.check_input_word(last_letter, input_word, cities_list, already_used_words, stop_words)
        self.assertEqual(answer,'stop')


    def test_get_last_letter_ru_1(self):
        """if the last letter is big"""
        word = 'омсК'
        letter = game.get_last_letter(word)
        self.assertEqual(letter, 'к')


    def test_get_last_letter_ru_2(self):
        """if the last letter is weird"""
        word = 'грязь'
        letter = game.get_last_letter(word)
        self.assertEqual(letter, 'з')


    def test_get_last_letter_ru_3(self):
        """if the last letter is usual"""
        word = 'москва'
        letter = game.get_last_letter(word)
        self.assertEqual(letter, 'а')


    def test_check_arguable_ru_1(self):
        """if the word is not in arguable list"""
        word = 'Омск'
        arguable = ['Анапа', 'Москва']
        res = game.check_arguable(word, arguable)
        self.assertEqual(res, False)


    def test_check_arguable_ru_2(self):
        """if the word is in arguable list, small case"""
        word = 'анапа'
        arguable = ['Анапа', 'Москва']
        res = game.check_arguable(word, arguable)
        self.assertEqual(res, True)

    def test_check_arguable_ru_3(self):
        """if the word is in arguable list, big case"""
        word = 'Анапа'
        arguable = ['Анапа', 'Москва']
        res = game.check_arguable(word, arguable)
        self.assertEqual(res, True)
