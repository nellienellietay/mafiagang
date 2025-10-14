
from abc import ABC, abstractmethod


class MafiaMember(ABC): #abstract class


    def __init__(self, name: str, age: int, loyalty: int):
        self._name = name
        self._age = age
        self._loyalty = loyalty


    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = str(name)

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        age = int(age)
        if age < 0:
            raise ValueError("unvalid age")
        self._age = age

    def get_loyalty(self) -> int:
        pass

    def set_loyalty(self, loyalty: int) -> None:
        pass

    @abstractmethod
    def commit_crime(self, crime: "Crime") -> None:
        pass
    
    @abstractmethod
    def describe(self) -> str:
        pass
