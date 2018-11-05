# -*- coding: utf-8 -*-
from src.model.WordList import WordList
from src.util.Utils import Utils


def start():
    arq1 = Utils.read_archive("../texto1.txt")
    arq2 = Utils.read_archive("../texto2.txt")

    word_list = WordList()
    word_list.add_list([arq1, arq2])
    print("Resposta para o primeiro problema:")
    [print(resp) for resp in word_list.valuate_all_phrases(vocabulary=1)]

    print("\nResposta para o segundo problema:")
    [print(resp) for resp in word_list.valuate_all_phrases(vocabulary=2)]

    word_list2 = WordList()
    word_list2.add_list(list=[arq1, arq2], remove_stop_words=True)
    print("\nResposta para o primeiro problema sem stop-words:")
    [print(resp) for resp in word_list2.valuate_all_phrases(vocabulary=1)]

    print("\nResposta para o segundo problema sem stop-words:")
    [print(resp) for resp in word_list2.valuate_all_phrases(vocabulary=2)]


if __name__ == '__main__':
    start()
