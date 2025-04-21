import pytest
from conftest import collector
from main import (BooksCollector)

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_add_new_book_add_three_books(self, collector):
        collector.add_new_book('Азазель')
        collector.add_new_book('Укрытие')
        collector.add_new_book('Сияние')
        assert len(collector.get_books_genre()) == 3

    def test_add_new_book_add_duplicate(self, collector):
        collector.add_new_book('Дракула')
        collector.add_new_book('Дракула')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_incorrect_length(self, collector):
        collector.add_new_book('')
        collector.add_new_book('ЖизньиудивительныеприключенияРобинзонаКру')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_correct(self, collector):
        collector.books_genre['Чемодан'] = ''
        collector.set_book_genre('Чемодан', 'Комедии')
        assert collector.books_genre['Чемодан'] == 'Комедии'

    def test_set_book_genre_incorrect(self, collector):
        collector.books_genre['Три товарища'] = ''
        collector.set_book_genre('Три товарища', 'Роман')
        assert collector.get_book_genre('Три товарища') == ''

    def test_get_book_genre_book_without_genre(self, collector):
        collector.books_genre['Три товарища'] = ''
        assert collector.get_book_genre('Три товарища') == ''

    def test_get_book_genre_with_existing_genre(self, collector):
        collector.books_genre['Три товарища'] = 'Роман'
        assert collector.get_book_genre('Три товарища') == 'Роман'

    def test_get_books_genre(self, collector):
        collector.books_genre['Дракула'] = 'Ужасы'
        assert collector.get_books_genre() == {'Дракула': 'Ужасы'}

    def test_get_books_genre_one_book_add_without_genre(self, collector):
        collector.books_genre['Три товарища'] = ''
        assert collector.get_book_genre('Три товарища') == ''

    def test_get_books_genre_not_book(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_with_specific_genre_invalid_genre(self, collector):
        collector.books_genre['Чемодан'] = 'Комедии'
        assert collector.get_books_with_specific_genre('Драмма') == []

    def test_get_books_with_specific_genre(self, collector):
        collector.books_genre['Азазель'] = 'Детективы'
        collector.books_genre['Шерлок Холмс'] = 'Детективы'
        assert collector.get_books_with_specific_genre('Детективы') == ['Азазель', 'Шерлок Холмс']

    def test_get_books_with_specific_genre_empty(self, collector):
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_for_children_list_is_empty(self, collector):
        collector.books_genre['Туман'] = 'Ужасы'
        assert 'Туман' not in collector.get_books_for_children()

    def test_get_books_for_children_list_is_not_empty(self, collector):
        collector.books_genre['Приключения Незнайки'] = 'Мультфильмы'
        assert 'Приключения Незнайки' in collector.get_books_for_children()

    def test_add_book_in_favorites(self, collector):
        collector.books_genre['Капитан Немо'] = ''
        collector.add_book_in_favorites('Капитан Немо')
        assert 'Капитан Немо' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self, collector):
        collector.books_genre['Сто лет тому вперёд'] = ''
        collector.add_book_in_favorites('Сто лет тому вперёд')
        collector.add_book_in_favorites('Сто лет тому вперёд')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collector):
        collector.books_genre['Шерлок Холмс'] = ''
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.delete_book_from_favorites('Шерлок Холмс')
        assert 'Шерлок Холмс' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self, collector):
        collector.books_genre['Туман'] = ''
        collector.add_book_in_favorites('Туман')
        assert collector.get_list_of_favorites_books() == ['Туман']

    @pytest.mark.parametrize('name, genre', [
        ('Туман', 'Ужасы'),
        ('Азазель', 'Детективы'), ('Чемодан', 'Комедии')])
    def test_get_list_of_favorites_books_added_corretly(self, collector, name, genre):
        collector.books_genre[name] = genre
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()
