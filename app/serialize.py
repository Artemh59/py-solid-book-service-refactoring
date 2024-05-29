import json
import xml.etree.ElementTree as Et
from app.book import Book
from abc import ABC, abstractmethod


class Serialize(ABC):
    @abstractmethod
    def serialize(self):
        pass


class SerializeJson(Serialize, Book):
    def serialize(self) -> None:
        return json.dumps({"title": self.title, "content": self.content})


class SerializeXml(Serialize, Book):
    def serialize(self) -> None:
        root = Et.Element("book")
        title = Et.SubElement(root, "title")
        title.text = self.title
        content = Et.SubElement(root, "content")
        content.text = self.content
        return Et.tostring(root, encoding="unicode")
