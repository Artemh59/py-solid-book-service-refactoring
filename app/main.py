import json
import xml.etree.ElementTree as Et


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content

    def display(self) -> None:
        print(self.content)

    def reverse_display(self) -> None:
        print(self.content[::-1])

    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)

    def print_reverse_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])

    def serialize_json(self) -> str:
        return json.dumps({"title": self.title, "content": self.content})

    def serialize_xml(self) -> str:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.title
        content = Et.SubElement(root, "content")
        content.text = self.content
        return Et.tostring(root, encoding="unicode")


# def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
#     for cmd, method_type in commands:
#         if cmd == "display":
#             if method_type == "reverse":
#                 book.reverse_display()
#             else:
#                 book.display()
#
#         elif cmd == "print":
#             if method_type == "reverse":
#                 book.print_reverse_book()
#             else:
#                 book.print_book()
#
#         elif cmd == "serialize":
#             if method_type == "xml":
#                 return book.serialize_xml()
#             else:
#                 return book.serialize_json()
#
#
# if __name__ == "__main__":
#     sample_book = Book("Sample Book", "This is some sample content.")
#     print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
