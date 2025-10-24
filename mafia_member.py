from abc import ABC, abstractmethod
from crime import Crime

class MafiaMember(ABC): 
    def __init__(self, name: str, age: int, role: str): 
        """Initializes a MafiaMember as instance"""
        self.__name = name
        self.__age = age
        self.__role = role

    def get_name(self) -> str:
        """Gets name of mafia member
        returns: 
            str name
        """
        return self.__name

    def set_name(self, new_name: str) -> None:
        """Sets name for mafia member"""
        self.__name = new_name

    def get_age(self) -> int:
        """Gets age of mafia member
        returns: 
            int age
        """
        return self.__age

    def set_age(self, new_age: int) -> None:
        self.__age = new_age

    def get_role(self) -> str:
        """Gets role of mafia member
        returns: 
            str role
        """
        return self.__role
    
    def set_role(self, new_role: str) -> None:
        """Sets role for  mafia member"""
        self.__role = new_role

    @abstractmethod
    def commit_crime(self, crime: Crime) -> None:
        """Abstract method for committing a crime"""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Returns string representation, is overwritten when used in a subclass"""
        return f"{self.get_role()}: {self.get_name()}, {self.get_age()} years old"
