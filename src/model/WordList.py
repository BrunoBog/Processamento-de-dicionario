import re

from src.util.Utils import Utils


class WordList(object):
    def __init__(self):
        self.regular_definition = r'[a-zA-ZÀ-ú]+'
        self.words = []
        self.phrases = []
        self.dict_words = {}
        self.dict_2words = {}

    def add_list(self, list, remove_stop_words=False):
        for item in list:
            self.add(item, remove_stop_words)

    def add(self, phrase, remove_stop_words=False):
        self.phrases.append(phrase)
        self.format_words(re.findall(self.regular_definition, phrase), remove_stop_words)
        self.populate_simple_dict()
        self.populate_dict_2_words()

    def format_words(self, words, remove_stop_words):
        self.words = self.remove_invalid_words(words)
        if remove_stop_words:
            self.remove_stop_words()
        self.words = self.remove_invalid_character()
        self.words = Utils.to_lower_list(self.words)

    def populate_simple_dict(self):
        for word in self.words:
            if word not in self.dict_words:
                self.dict_words[word] = 0

    def populate_dict_2_words(self):
        for i in range(0, len(self.words) - 1):
            new_therm = self.words[i] + " " + self.words[i+1]
            if new_therm not in self.dict_words:
                self.dict_2words[new_therm] = 0

    def remove_invalid_words(self, words):
        return [word for word in words if re.match(self.regular_definition, word)]

    def remove_stop_words(self):
        self.words = Utils.remove_stop_words(self.words)

    def remove_invalid_character(self):
        return [Utils.remove_special_characters(word) for word in self.words]

    def valuate_all_phrases(self, vocabulary=1):
        resp = []
        for i in range(0, len(self.phrases)):
            if vocabulary == 1:
                resp.append("texto{}:{}".format(str(i + 1), str(list(self.value_of_phrase(self.phrases[i]).values()))))
            else:
                resp.append("texto{}:{}".format(str(i + 1), str(list(self.value_of_phrase_double_word(self.phrases[i]).values()))))
        return resp

    def value_of_phrase(self, phrase):
        words = self.dict_words.copy()
        phrase = self.format_phase(phrase)
        for word in phrase:
            if Utils.is_key(word, words):
                words[word] += 1
        return words

    def value_of_phrase_double_word(self, phrase):
        words = self.dict_2words.copy()
        phrase = self.format_phase(phrase)
        for i in range(0, len(phrase) - 1):
            new_therm = phrase[i] + " " + phrase[i+1]
            if Utils.is_key(new_therm, words):
                words[new_therm] += 1
        return words

    def format_phase(self, phrase):
        phrase = re.findall(self.regular_definition, phrase)
        return Utils.to_lower_list(phrase)






