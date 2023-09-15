import unittest
import main as game

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.cities_list = []


    def test_get_new_word(self):
        cities_list = ['Анапа', 'Брянск', 'Новосибирск', 'Москва', 'Омск']
        already_used_words = []
        letter = 'а'
        res = game.get_new_word(letter, cities_list, already_used_words)
        self.assertEqual(res[0], 'Анапа')


