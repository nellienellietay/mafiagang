from mafia_member import MafiaMember
from crime import Crime, CrimeType

class Soldier(MafiaMember):
    """Subclass to MafiaMember"""
    
    def __init__(self, name: str, age: int):
        """Initializes Soldier with name, age and role"""
        super().__init__(name, age, "Soldier")

    def commit_crime(self, crime: Crime) -> None:
        """commits the crime """
        print(f"{self.get_name()} commits {crime.get_type().value}.")

    def __str__(self):
        """Returns string representation of Soldier
        returns:
            str representation
        """
        return f"Soldier {self.get_name()}"
