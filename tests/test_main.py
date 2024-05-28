from io import StringIO
import sys

import pytest

from app.main import Book


def get_stdout(func, *args, **kwargs) -> str:
    new_stdout = StringIO()
    old_stdout = sys.stdout
    sys.stdout = new_stdout

    func(*args, **kwargs)

    sys.stdout = old_stdout
    return new_stdout.getvalue()


@pytest.fixture()
def book() -> Book:
    return Book("Sample Book", "This is some sample content.")


def test_display_console(book) -> None:
    output = get_stdout(book.display)
    assert "This is some sample content." in output


def test_display_reverse(book) -> None:
    output = get_stdout(book.reverse_display)
    assert "tnetnoc elpmas emos si sihT" in output


def test_print_console(book) -> None:
    output = get_stdout(book.print_book)
    assert book.title in output
    assert "This is some sample content." in output


def test_print_reverse(book) -> None:
    output = get_stdout(book.print_reverse_book)
    assert book.title in output
    assert "tnetnoc elpmas emos si sihT" in output


def test_serialize_json(book) -> None:
    serialized_book = book.serialize_json()
    assert (
        serialized_book
        == '{"title": "Sample Book", "content": "This is some sample content."}'
    )


def test_serialize_xml(book) -> None:
    serialized_book = book.serialize_xml()
    assert "<title>Sample Book</title>" in serialized_book
    assert "<content>This is some sample content.</content>" in serialized_book
