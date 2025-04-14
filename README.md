# qa_python

# Список тестов для BooksCollector

# Реализованные тесты
1. test_add_new_book_add_three_books - Добавление трех книг в словарь.

2. test_add_new_book_add_duplicate_book - Проверка попытки добавить книгу с одинаковым названием. Книга не должна добавляться дважды.

3. test_add_new_book_incorrect_length - Проверка добавления книги с некорректной длиной названия (меньше 1 или больше 40 символов).

4. test_set_book_genre_correct - Проверка корректной установки жанра книги.

5. test_set_book_genre_incorrect - Проверка попытки установить некорректный жанр для книги.

6. test_get_books_with_specific_genre - Проверяет, что метод возвращает книги с указанным жанром.

7. test_get_books_with_specific_genre_empty - Проверка получения пустого списка книг для несуществующего жанра.

8. test_get_books_for_children_list_is_empty - Проверяет, что метод правильно не возвращает книги, неподходящие для детей.

9. test_get_books_for_children_list_is_not_empty - Проверяет, что метод правильно возвращает книги, подходящие для детей.

10. test_add_book_in_favorites - Проверка добавления книги в избранное.

11. test_add_book_in_favorites_duplicate - Проверка добавления книги в избранное при попытке добавить уже существующую книгу.

12. test_delete_book_from_favorites - Проверка удаления книги из избранного.

13. test_get_list_of_favorites_books_empty - Проверка получения пустого списка избранных книг.