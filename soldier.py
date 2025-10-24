from mafia_member import MafiaMember
from crime import Crime
from crime_type import CrimeType


class Soldier(MafiaMember):
    """Subclass to MafiaMember"""
    
    def __init__(self, name: str, age: int) -> None:
        """Initializes Soldier with name, age and role"""
        super().__init__(name, age, "Soldier")

    def commit_crime(self, crime: Crime) -> None:
        """confirms the crime """
        print(f"{self.get_name()} will do {crime.get_type().value}.")

    def __str__(self) -> str:
        """Returns string representation of Soldier
        returns:
            str representation
        """
        return f"Soldier {self.get_name()}"
