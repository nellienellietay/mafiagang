from mafia_member import MafiaMember
from consigliere import Consigliere
from capo import Capo
from crime import Crime
from crime_type import CrimeType


class Godfather(MafiaMember):
    """Subclass to MafiaMember"""
    def __init__(self, name: str, age: int) -> None:
        """Initializes Godfather with name, age, role"""
        super().__init__(name=name, age=age, role="Godfather")
        self.__capos = []
        self.__consigliere = None

    def commit_crime(self, crime: Crime) -> None:
        """Godfather may handle racketeering and bribery. Others are refused."""
        if crime.get_type() == CrimeType.RACKETEERING:
            print(f"{self.get_name()} can do some racketeering and will start planning right away...")
        elif crime.get_type() == CrimeType.BRIBERY:
            print(f"{self.get_name()} can do some bribery and will begin right away...")
        else:
            print(f"{self.get_role()} {self.get_name()} does not deal with petty {crime.get_type().value}")

    def __str__(self) -> str:
        """string rep of Godfather
        returns:
            str representation
        """
        return f"Godfather {self.get_name()}, head of the family"
