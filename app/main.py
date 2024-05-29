from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serialize import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                DisplayConsole.display(book)
            else:
                DisplayReverse.display(book)
        elif cmd == "print":
            if method_type == "console":
                PrintConsole.print(book)
            else:
                PrintReverse.print(book)
        elif cmd == "serialize":
            if method_type == "json":
                return SerializeJson.serialize(book)
            else:
                return SerializeXml.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
