from mafia_member import MafiaMember
from Crime import Crime
from soldier import Soldier


class Capo():
    def __init__(self, id: str, type: str, target: str, amount: float, assigned_to: list, location: str):
        self.__id = id
        self.__type = type 
        self.__target = target
        self.__amount = amount
        self.__assigned_to = assigned_to
        self.__location = location 
    
    def assign(self, crime: Crime, soldier: Soldier) -> None:
        if soldier not in self._Capo__soldiers:
            raise ValueError(f"{to.get_name()} is not in {self.get_name()}'s crew")
        to.commit_crime(crime)

    def commit_crime(self, crime: Crime) -> None:
        pass # should capo directly commit crime?
    
    def __str__(self) -> str:
        return f"Crime(name={self.name})"
