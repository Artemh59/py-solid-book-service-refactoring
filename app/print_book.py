from app.book import Book
from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print(self):
        pass


class PrintConsole(Print, Book):
    def print(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class PrintReverse(Print, Book):
    def print(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
