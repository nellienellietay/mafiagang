from abc import ABC, abstractmethod
from crime import Crime

class MafiaMember(ABC): #abstract class


    def __init__(self, name: str, age: int, loyalty: int, role: str, reports_to: Optional['MafiaMember'] = None):
        self.__name = name
        self.__age = age
        self.__loyalty = loyalty
        self.__role = role
        self.__reports_to = reports_to

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        self.__name = new_name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, new_age: int) -> None:
        self.__age = new_age

    def get_loyalty(self) -> int:
        return self.__loyalty

    def set_loyalty(self, new_loyalty: int) -> None:
        self.__loyalty = new_loyalty

    def get_role(self) -> str:
        return self.__role
    
    def set_role(self, new_role: str) -> None:
        self.__role = new_role

    def get_reports_to(self) -> Optional['MafiaMember']:
        return self.__reports_to
    
    def set_reports_to(self, new_reports_to: 'MafiaMember') -> None:
        self.__reports_to = new_reports_to

    @abstractmethod
    def commit_crime(self, crime: Crime) -> None:
        
    
    @abstractmethod
    def describe(self) -> str:
        pass