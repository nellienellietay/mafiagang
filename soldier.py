from mafia_member import MafiaMember
from crime import Crime, CrimeType

"""This is a subklass to MafiaMember"""

class Soldier(MafiaMember):
    
    def __init__(self, name: str, age: int):
            super().__init__(name, age, "Soldier")

    
    def commit_crime(self, crime: Crime) -> None:
        """commits the crime """
        print(f"{self.get_name()} commits {crime.get_type().value}.")


    def __str__(self):
        return f"Soldier {self.get_name()}"
        
