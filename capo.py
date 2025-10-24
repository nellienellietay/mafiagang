from mafia_member import MafiaMember
from crime import Crime, CrimeType
from soldier import Soldier

class Capo(MafiaMember):
    """subclass of MafiaMember representing the Capo in the mafia hierarchy."""
    def __init__(self, name, age):
        super().__init__(name=name, age=age, role="Capo")

    def commit_crime(self, crime: Crime) -> None:
        """Capo directly handles only crimes appropriate for a Capo."""
        if crime.get_type() == CrimeType.RACKETEERING: 
            print(f"{self.get_name()} can do some Racketeering")
        else:
            print(f"{self.get_role()} {self.get_name()} does not deal with {crime.get_type().value}")
    
    def __str__(self) -> str:
        return f"Capo {self.get_name()}"
