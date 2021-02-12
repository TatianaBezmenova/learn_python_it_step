import json
import pickle
from dataclasses import dataclass


@dataclass
class Stadium:
    _name: str
    _date_open: str
    _country: str
    _city: str
    _capacity: str

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def date_open(self) -> str:
        return self._date_open

    @date_open.setter
    def date_open(self, value: str) -> None:
        self._date_open = value

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, value: str) -> None:
        self._country = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str) -> None:
        self._city = value

    @property
    def capacity(self) -> str:
        return self._capacity

    @capacity.setter
    def capacity(self, value: str) -> None:
        self._capacity = value

    def serialize_json(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def deserialize_json(cls, data: str) -> "Stadium":
        return cls(**json.loads(data))

    def serialize_pickle(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def deserialize_pickle(data: bytes) -> "Stadium":
        return pickle.loads(data)
