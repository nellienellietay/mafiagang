from abc import ABC, abstractmethod
from crime import Crime

class MafiaMember(ABC): #abstract class

        #tagit bort alla "optional" eftersom det inte behövs när man gör type-hinting tydligen
        #'MafiaMember' | None  betyder att det kan vara antingen ett instance of a class eller None

    def __init__(self, name: str, age: int, role: str, reports_to = None): 
        """Initializes a MafiaMember as instance"""
        self.__name = name
        self.__age = age
        self.__role = role
        self.__reports_to = reports_to

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

    def get_reports_to(self):  # returns MafiaMember or None
        """Gets who this member reports to
        returns:
            MafiaMember: None
        """
        return self.__reports_to
        # returnerar den här medlemmens chef (MafiaMember-objekt) eller None om den inte har någon chef
    
    def set_reports_to(self, new_reports_to) -> None:
        """ Sets who this member reports to"""
        self.__reports_to = new_reports_to

    #abstractmethod är tomma med pass eftersom de kommer override:as i varje subclass
    #man skapar aldrig instance of an object av abstract methods
    @abstractmethod
    def commit_crime(self, crime: Crime) -> None:
        """Abstract method for committing a crime"""
        pass
    
    @abstractmethod
    #ändrat från describe till str, bättre praxis, osäker om den fortfarande behöver vara abstract 
    def __str__(self) -> str:
        """Returns string representation, is overwritten when used in a subclass"""
        return f"{self.get_role()}: {self.get_name()}, {self.get_age()} years old"
