import unittest
import re

from src.util.Utils import Utils

from src.model.WordList import WordList

class Unit_tests(unittest.TestCase):

    def test_remove_invalid_character(self):
        resp = Utils.remove_special_characters("pronto.")
        self.assertTrue(resp == "pronto")
        resp = Utils.remove_special_characters("fácil.")
        self.assertTrue(resp == "fácil")
        resp = Utils.remove_special_characters("código.")
        self.assertTrue(resp == "código")

    def test_is_valid_word(self):
        self.assertTrue(re.match(r'[a-zA-ZÀ-ú]', "Falar"))
        self.assertTrue(re.match(r'[a-zA-ZÀ-ú]', "é"))
        self.assertTrue(re.match(r'[a-zA-ZÀ-ú]', "fácil."))
        self.assertTrue(re.match(r'[a-zA-ZÀ-ú]', "Mostre-me"))
        self.assertTrue(re.match(r'[a-zA-ZÀ-ú]', "o"))
        self.assertTrue(re.match(r'[a-zA-ZÀ-ú]', "código."))
        self.assertTrue(re.match(r'[a-zA-ZÀ-ú]',  "c3po."))
        self.assertFalse(re.match(r'[a-zA-ZÀ-ú]',  "3po."))

    def test_add_word(self):
        word_list = WordList()
        word_list.add("Falar é fácil. Mostre-me o código. Falar")
        resp = ['falar', 'é', 'fácil', 'mostre', 'me', 'o', 'código']
        self.assertTrue(resp == list(word_list.dict_words.keys()))

    def test_add_list(self):
        phase1 = "Falar é fácil. Mostre-me o código."
        phase2 = "É fácil escrever código. Difícil é escrever código que funcione."
        word_list = WordList()
        word_list.add_list([phase1,phase2])
        self.assertTrue(list(word_list.dict_words.keys()) == ['falar', 'é', 'fácil', 'mostre', 'me', 'o', 'código', 'escrever', 'difícil', 'que', 'funcione'])

    def test_print_dictionary(self):
        phase1 = "Falar é fácil. Mostre-me o código."
        phase2 = "É fácil escrever código. Difícil é escrever código que funcione."
        word_list = WordList()
        word_list.add_list([phase1, phase2])
        mock = ['falar', 'é', 'fácil', 'mostre', 'me', 'o', 'código', 'escrever', 'difícil', 'que', 'funcione']
        self.assertTrue(mock == list(word_list.dict_words.keys()))

    def test_evaluate_word(self):
        phrase1 = "Falar é fácil. Mostre-me o código."
        phrase2 = "É fácil escrever código. Difícil é escrever código que funcione."
        mock = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
        word_list = WordList()
        word_list.add_list([phrase1, phrase2])
        match = word_list.value_of_phrase(phrase1)
        self.assertTrue(mock ==list(match.values()))

    def test_valuate_phrases(self):
        phrase1 = "Falar é fácil. Mostre-me o código."
        phrase2 = "É fácil escrever código. Difícil é escrever código que funcione."
        mock = "texto1:[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]"
        word_list = WordList()
        word_list.add_list([phrase1, phrase2])
        match = word_list.valuate_all_phrases()
        self.assertTrue(mock == match[0])

    def test_test_valuate_phrases_without_stop_wors(self):
        arquivo1 = "Falar é fácil. Mostre-me o código."
        arquivo2 = "É fácil escrever código. Difícil é escrever código que funcione."
        word_list2 = WordList()
        word_list2.add_list(list=[arquivo1, arquivo2], remove_stop_words=True)
        mock1 = "texto1:[1, 1, 1, 1, 1, 0, 0, 0]"
        mock2 = "texto2:[0, 2, 1, 0, 2, 2, 1, 1]"
        resp = word_list2.valuate_all_phrases()
        self.assertTrue(mock1 == resp[0])
        self.assertTrue(mock2 == resp[1])

    def test_populate_dict_2(self):
        arquivo1 = "Falar é fácil. Mostre-me o código."
        arquivo2 = "É fácil escrever código. Difícil é escrever código que funcione."
        word_list = WordList()
        word_list.add_list(list=[arquivo1, arquivo2], remove_stop_words=False)
        mock1 = "texto1:[1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]"
        mock2 = "texto2:[0, 1, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1]"
        resp = word_list.valuate_all_phrases(vocabulary=2)
        self.assertTrue(mock1 == resp[0])
        self.assertTrue(mock2 == resp[1])

