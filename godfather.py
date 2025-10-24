from mafia_member import MafiaMember
from consigliere import Consigliere
from capo import Capo

class Godfather(MafiaMember):
    """Subclass to MafiaMember"""
    def __init__(self, name: str, age: int) -> None:
        """Initializes Godfather with name, age, role, capos and the consigliere"""
        super().__init__(name=name, age=age, role="Godfather")
        self.__capos = []            # list of Capo
        self.__consigliere = None    # Consigliere or None

    def commit_crime(self, crime) -> None:
        """Godfather does not execute crimes directly."""
        raise PermissionError(f"Godfather {self.get_name()} does not commit crime directly")

    def __str__(self) -> str:
        return f"Godfather {self.get_name()}, head of the family"
