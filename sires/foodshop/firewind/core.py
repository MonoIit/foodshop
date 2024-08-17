from firewind.morphyus import Morphyus
import json

class IndexNode:
    def __init__(self, source, count, weight, basic):
        self.source = source
        self.count = count
        self.range = None  # Range will be calculated later
        self.weight = weight
        self.basic = basic


    def to_dict(self):
        return {
            'source': self.source,
            'count': self.count,
            'range': self.range,
            'weight': self.weight,
            'basic': self.basic,
        }

    @classmethod
    def from_dict(cls, data):
        instance = cls(
            source=data['source'],
            count=data['count'],
            weight=data['weight'],
            basic=data['basic']
        )
        instance.range = data.get('range')  # Восстанавливаем range, если он есть в JSON
        return instance

class firewind:
    version = "1.0.0"

    def __init__(self):
        self.morphyus = Morphyus()


    def make_index(self, content, range_value=1):
        """
        Создает индекс значимых слов из текста

        :param content: Исходный текст
        :param range_value: Значение диапазона для весов слов
        :return: Объект с индексом слов
        """


        index = {'range': range_value, 'words': []}

        # Выделение слов из текста
        words = self.morphyus.get_words(content)

        for word in words:
            # Оценка значимости слова
            weight = self.morphyus.weigh(word)

            if weight > 0:
                # Количество слов в индексе
                length = len(index['words'])

                # Проверка существования исходного слова в индексе
                for i in range(length):
                    if index['words'][i].source == word:
                        # Исходное слово уже есть в индексе
                        index['words'][i].count += 1
                        index['words'][i].range = (
                                range_value * index['words'][i].count * index['words'][i].weight
                        )

                        # Обработка следующего слова
                        break
                else:
                    # Если исходного слова еще нет в индексе
                    lemma = self.morphyus.lemmatize(word)

                    if lemma:
                        # Проверка наличия лемм в индексе
                        for i in range(length):
                            # Если у сравниваемого слова есть леммы
                            if index['words'][i].basic:
                                difference = len(
                                    set(lemma) - set(index['words'][i].basic)
                                )

                                # Если сравниваемое слово имеет менее двух отличных лемм
                                if difference == 0:
                                    index['words'][i].count += 1
                                    index['words'][i].range = (
                                            range_value * index['words'][i].count * index['words'][i].weight
                                    )

                                    # Обработка следующего слова
                                    break
                        else:
                            # Если в индексе нет ни лемм, ни исходного слова, значит пора добавить его
                            node = IndexNode(source=word, count=1, weight=weight, basic=lemma)
                            node.range = range_value * weight
                            index['words'].append(node)

        return index

    def search(self, target, index):
        """
        Выполняет поиск по индексу слов, сравнивая целевые слова с индексированными словами
        и вычисляя общую значимость совпадений.

        :param target: Целевой индекс, содержащий слова для поиска
        :param index: Индекс для поиска
        :return: Общая значимость совпадений
        """
        total_range = 0

        # Перебор слов запроса
        for target_word in target['words']:
            # Перебор слов индекса
            for index_word in index['words']:
                if index_word.source == target_word.source:
                    total_range += index_word.range
                elif index_word.basic and target_word.basic:
                    # Если у искомого и индексированного слов есть леммы
                    index_count = len(index_word.basic)
                    target_count = len(target_word.basic)

                    for i in range(target_count):
                        for j in range(index_count):
                            if index_word.basic[j] == target_word.basic[i]:
                                total_range += index_word.range
                                break

        return total_range

