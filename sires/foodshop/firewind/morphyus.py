import re
from bs4 import BeautifulSoup
import pymorphy3


class Morphyus:
    def __init__(self):
        self.regexp_word = re.compile(r'([a-zа-я0-9]+)', re.IGNORECASE | re.UNICODE)
        self.regexp_entity = re.compile(r'&([a-zA-Z0-9]+);')
        self.pymorphy = pymorphy3.MorphAnalyzer()

    def get_words(self, content, filter=True):
        """
        Разбивает текст на массив слов

        :param content: Исходный текст для выделения слов
        :param filter: Активирует фильтрацию HTML-тегов и сущностей
        :return: Результирующий массив
        """
        # Фильтрация HTML-тегов и HTML-сущностей
        if filter:
            content = self.strip_tags(content)
            content = self.regexp_entity.sub(' ', content)

        # Перевод строки в верхний регистр
        content = content.upper()

        # Замена "Ё" на "Е"
        content = content.replace('Ё', 'Е')

        # Выделение слов из контекста
        words_src = self.regexp_word.findall(content)
        return words_src


    def strip_tags(self, html):
        """
        Удаляет HTML теги из строки

        :param html: Строка с HTML контентом
        :return: Строка без HTML тегов
        """
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()

    def lemmatize(self, word):
        """
        Находит леммы слова

        :param word: Исходное слово
        :return: Массив возможных лемм слова, либо пустой список
        """
        lemmas = [p.normal_form for p in self.pymorphy.parse(word)]
        return lemmas

    def weigh(self, word, profile=False):
        parts_of_speech = self.get_part_of_speech(word)

        if not profile:
            profile = {
                # Служебные части речи
                'PREP': 0,
                'CONJ': 0,
                'INTJ': 0,
                'PRCL': 0,
                'NPRO': 0,

                # Наиболее значимые части речи
                'NOUN': 5,
                'VERB': 5,
                'INFN': 5,
                'PRTF': 3,
                'PRTS': 3,
                'ADVB': 3,

                # Остальные части речи
                'DEFAULT': 1
            }

        # Если не удалось определить возможные части речи
        if not parts_of_speech:
            return profile['DEFAULT']

        # Определение ранга
        range_values = []
        for pos in parts_of_speech:
            range_values.append(profile.get(pos, profile['DEFAULT']))

        return max(range_values)

    def get_part_of_speech(self, word):
        """
        Получает возможные части речи слова

        :param word: Исходное слово
        :return: Список частей речи
        """
        parsed_word = self.pymorphy.parse(word)
        parts_of_speech = []
        for p in parsed_word:
            pos = p.tag.POS
            if pos:
                parts_of_speech.append(pos)
        return parts_of_speech


