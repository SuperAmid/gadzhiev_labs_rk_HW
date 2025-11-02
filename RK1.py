# используется для сортировки
from operator import itemgetter

class Section:
    """Раздел"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Document:
    """Документ"""
    def __init__(self, id, title, author, section_id):
        self.id = id
        self.title = title
        self.author = author
        self.section_id = section_id

class DocumentSection:
    """Документы раздела для реализации связи многие-ко-многим"""
    def __init__(self, section_id, document_id):
        self.section_id = section_id
        self.document_id = document_id

# Разделы
sections = [
    Section(1, 'Административные документы'),
    Section(2, 'Аналитические материалы'),
    Section(3, 'Научные работы'),
    Section(4, 'Техническая документация'),
    Section(5, 'Отчетные документы'),
]

# Документы
documents = [
    Document(1, 'Приказ №1', 'Иванов', 1),
    Document(2, 'Анализ рынка', 'Петров', 2),
    Document(3, 'Исследование AI', 'Сидоров', 3),
    Document(4, 'Техническое задание', 'Кузнецов', 4),
    Document(5, 'Годовой отчет', 'Смирнов', 5),
    Document(6, 'Акт выполненных работ', 'Николаев', 1),
    Document(7, 'Статья по математике', 'Васильев', 3),
    Document(8, 'Анализ производительности', 'Федоров', 2),
]

# Связи многие-ко-многим
documents_sections = [
    DocumentSection(1, 1),
    DocumentSection(1, 6),
    DocumentSection(2, 2),
    DocumentSection(2, 8),
    DocumentSection(3, 3),
    DocumentSection(3, 7),
    DocumentSection(4, 4),
    DocumentSection(5, 5),
    # Дополнительные связи для демонстрации многие-ко-многим
    DocumentSection(1, 2),
    DocumentSection(3, 5),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(d.title, d.author, s.name)
                   for s in sections
                   for d in documents
                   if d.section_id == s.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(s.name, ds.section_id, ds.document_id)
                         for s in sections
                         for ds in documents_sections
                         if s.id == ds.section_id]

    many_to_many = [(d.title, d.author, section_name)
                    for section_name, section_id, document_id in many_to_many_temp
                    for d in documents if d.id == document_id]

    print('Задание Д1')
    # Список всех документов, у которых автор заканчивается на "ов", и названия их разделов
    res_1 = list(filter(lambda i: i[1].endswith('ов'), one_to_many))
    print(res_1)

    print('\nЗадание Д2')
    # Список разделов со средней длиной названия документов в каждом разделе,
    # отсортированный по средней длине
    res_2_unsorted = []
    # Перебираем все разделы
    for s in sections:
        # Список документов раздела
        s_docs = list(filter(lambda i: i[2] == s.name, one_to_many))
        # Если раздел не пустой
        if len(s_docs) > 0:
            # Длины названий документов раздела
            doc_title_lengths = [len(title) for title, _, _ in s_docs]
            # Средняя длина названия документов (сумма длин / количество)
            avg_title_length = sum(doc_title_lengths) / len(doc_title_lengths)
            res_2_unsorted.append((s.name, round(avg_title_length, 2)))

    # Сортировка по средней длине названия
    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    print(res_2)

    print('\nЗадание Д3')
    # Список всех разделов, у которых название начинается с буквы «А», 
    # и список документов в них
    res_3 = {}
    # Перебираем все разделы
    for s in sections:
        if s.name.startswith('А'):
            # Список документов раздела
            s_docs = list(filter(lambda i: i[2] == s.name, many_to_many))
            # Только названия документов
            s_docs_titles = [title for title, _, _ in s_docs]
            # Добавляем результат в словарь
            # ключ - раздел, значение - список названий документов
            res_3[s.name] = s_docs_titles

    print(res_3)

if __name__ == '__main__':
    main()