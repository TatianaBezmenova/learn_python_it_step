import json
import pickle
from dataclasses import dataclass


@dataclass
class Car:
    _model: str
    _year: int
    _producer: str
    _engine_size: float
    _color: str
    _price: float

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = value

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        self._year = value

    @property
    def producer(self) -> str:
        return self._producer

    @producer.setter
    def producer(self, value: str) -> None:
        self._producer = value

    @property
    def engine_size(self) -> float:
        return self._engine_size

    @engine_size.setter
    def engine_size(self, value: float) -> None:
        self._engine_size = value

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        self._color = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        self._price = value

    def serialize_json(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def deserialize_json(cls, data: str) -> "Car":
        return cls(**json.loads(data))

    def serialize_pickle(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def deserialize_pickle(data: bytes) -> "Car":
        return pickle.loads(data)
