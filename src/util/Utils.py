import os
import re

import sys
from nltk.corpus import stopwords


class Utils(object):

    @staticmethod
    def remove_stop_words(new_words):
        return [word for word in new_words if word not in stopwords.words('portuguese')]

    @staticmethod
    def remove_special_characters(word):
        return ''.join(e for e in word if e.isalnum() or e == "-")

    @staticmethod
    def to_lower_list(words):
        return [x.lower() for x in words]

    @staticmethod
    def is_key(word, my_dict):
        for key in list(my_dict.keys()):
            if key == word:
                return True
        return False

    @staticmethod
    def read_archive(path):
        if not os.path.exists(path):
            print("arquivo {} nao existe".format(path))
            sys.exit(-1)
        else:
            _file = open(path, "r", encoding='utf-8')
            data = _file.readlines()
            _file.close()
        return data[0]