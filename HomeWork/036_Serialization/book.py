import json
import pickle
from dataclasses import dataclass


@dataclass()
class Book:
    _title: str
    _year: int
    _publishing_house: str
    _genre: str
    _author: str
    _price: float

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        self._year = value

    @property
    def publishing_house(self) -> str:
        return self._publishing_house

    @publishing_house.setter
    def publishing_house(self, value: str) -> None:
        self._publishing_house = value

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, value: str) -> None:
        self._genre = value

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        self._author = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        self._price = value

    def serialize_json(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def deserialize_json(cls, data: str) -> "Book":
        return cls(**json.loads(data))

    def serialize_pickle(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def deserialize_pickle(data: bytes) -> "Book":
        return pickle.loads(data)
