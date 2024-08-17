import json

from firewind.core import firewind, IndexNode
from menu.models import product


def search_products(query):
    analyzer = firewind()

    query_index = analyzer.make_index(content=query)

    results = []
    for product_index in product.objects.filter(in_stock=True):
        # Декодируем из json в объект IndexNode
        product_description_index = product_index.productdescription.index
        product_description_index['words'] = [IndexNode.from_dict(index) for index in product_description_index['words']]

        # Считаем ранг
        score = analyzer.search(query_index, product_description_index)
        if score > 0:
            results.append((product_index.pk, score))

    results.sort(reverse=True, key=lambda x: x[1])

    return [product_id for product_id, _ in results]


