import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()

    def test_get_books_genre_after_adding_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        books_genre = collector.get_books_genre()
        assert books_genre == {'Гордость и предубеждение и зомби': ''}

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert len(collector.get_books_genre()) == 1

    def test_get_books_genre_after_adding_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_new_book('1984')
        assert collector.get_books_genre() == ['1984']

    def test_add_new_book_too_long_name(self):
        collector = BooksCollector()
        long_name = 'a' * 41
        collector.add_new_book(long_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Моби Дик')
        collector.set_book_genre('Моби Дик', 'Фантастика')
        assert collector.get_book_genre('Моби Дик') == 'Фантастика'

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Неизвестная книга', 'Фантастика')
        assert len(collector.get_books_genre()) == 0

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('451 градус по Фаренгейту')
        collector.set_book_genre('451 градус по Фаренгейту', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['451 градус по Фаренгейту']

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Приключения Тома Сойера')
        collector.set_book_genre('Приключения Тома Сойера', 'Комедии')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        assert collector.get_books_for_children() == ['Приключения Тома Сойера']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_book_in_favorites('Гарри Поттер')
        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_add_book_in_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Гарри Поттер')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_with_items(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_book_in_favorites('Гарри Поттер')

        assert len(collector.get_list_of_favorites_books()) == 1

    @pytest.mark.parametrize("book_name, genre", [
        ('Книга 1', 'Фантастика'),
        ('Книга 2', 'Комедии'),
        ('Книга 3', 'Детективы'),
    ])
    def test_add_multiple_books_with_genres(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre
