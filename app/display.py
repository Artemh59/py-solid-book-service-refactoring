from app.book import Book
from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def display(self):
        pass


class DisplayConsole(Display, Book):
    def display(self) -> None:
        print(self.content)


class DisplayReverse(Display, Book):
    def display(self) -> None:
        print(self.content[::-1])
