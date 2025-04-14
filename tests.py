import pytest
from conftest import collector, add_book, add_genre, add_to_favorites, delete_from_favorites
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


    def test_add_new_book_add_three_books(self, collector, add_book):
        add_book('Азазель')
        add_book('Укрытие')
        add_book('Сияние')
        assert len(collector.get_books_genre()) == 3

    def test_add_new_book_add_duplicate(self, collector, add_book):
        add_book('Дракула')
        add_book('Дракула')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_incorrect_length(self, collector, add_book):
        add_book('')
        add_book('ЖизньиудивительныеприключенияРобинзонаКру')
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_correct(self, collector, add_book, add_genre):
        add_book('Чемодан')
        add_genre('Чемодан', 'Комедии')
        assert collector.get_book_genre('Чемодан') == 'Комедии'

    def test_set_book_genre_incorrect(self, collector, add_book, add_genre):
        add_book('Три товарища')
        add_genre('Три товарища', 'Роман')
        assert collector.get_book_genre('Три товарища') == ''

    @pytest.mark.parametrize('book_name, genre', [('Азазель', 'Детективы'), ('Дракула', 'Ужасы')])
    def test_get_books_with_specific_genre(self, collector, add_book, add_genre, book_name, genre):
        add_book(book_name)
        add_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    def test_get_books_with_specific_genre_empty(self, collector):
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_for_children_list_is_empty(self, collector, add_book, add_genre):
        add_book('Туман')
        add_genre('Туман', 'Ужасы')
        assert 'Туман' not in collector.get_books_for_children()

    def test_get_books_for_children_list_is_not_empty(self, collector, add_book, add_genre):
        add_book('Приключения Незнайки')
        add_genre('Приключения Незнайки', 'Мультфильмы')
        assert 'Приключения Незнайки' in collector.get_books_for_children()

    def test_add_book_in_favorites(self, collector, add_book, add_to_favorites):
        add_book('Капитан Немо')
        add_to_favorites('Капитан Немо')
        assert 'Капитан Немо' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self, collector, add_book, add_to_favorites):
        add_book('Сто лет тому вперёд')
        add_to_favorites('Сто лет тому вперёд')
        add_to_favorites('Сто лет тому вперёд')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, collector, add_book, add_to_favorites, delete_from_favorites):
        add_book('Шерлок Холмс')
        add_to_favorites('Шерлок Холмс')
        delete_from_favorites('Шерлок Холмс')
        assert 'Шерлок Холмс' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []
lector()