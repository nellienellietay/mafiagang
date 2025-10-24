from mafia_member import MafiaMember
from consigliere import Consigliere
from capo import Capo

class Godfather(MafiaMember):
    """Subclass to MafiaMember"""
    def __init__(self, name: str, age: int) -> None:
        """Initializes Godfather with name, age, role, capos and the consigliere"""
        super().__init__(name=name, age=age, role="Godfather")
        self.__capos = []
        self.__consigliere = None

    def commit_crime(self, crime) -> None:
        """Godfather does not execute crimes directly.
        args:
            crime (Crime): The crime not being committed"""
        raise PermissionError(f"Godfather {self.get_name()} does not commit crime directly")

    def __str__(self) -> str:
        """string rep of Godfather
        returns:
            str representation
        """
        return f"Godfather {self.get_name()}, head of the family"
