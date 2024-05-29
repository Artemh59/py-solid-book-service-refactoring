import json
import xml.etree.ElementTree as Et
from abc import ABC, abstractmethod

from app.book import Book


class Serialize(ABC):
    @staticmethod
    @abstractmethod
    def serialize(book: Book) -> str:
        pass


class SerializeJson(Serialize):
    @staticmethod
    def serialize(book: Book) -> None:
        return json.dumps({"title": book.title, "content": book.content})


class SerializeXml(Serialize):
    @staticmethod
    def serialize(book: Book) -> None:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = book.title
        content = Et.SubElement(root, "content")
        content.text = book.content
        return Et.tostring(root, encoding="unicode")
