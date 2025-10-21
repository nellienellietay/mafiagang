from mafia_member import MafiaMember
from consigliere import Consigliere
from capo import Capo

class Godfather(MafiaMember):
    """Subklass till MafiaMember"""
    def __init__(self, name: str, age: int, loyalty: int = 100) -> None:
        super().__init__(name=name, age=age, loyalty=loyalty, role="Godfather", reports_to=None)
        self.__capos = []            # list of Capo
        self.__consigliere = None    # Consigliere or None
        self.__reports_log = []      # list of str

     def authorize(self, crime) -> None:
        """Approve a crime and log it. Adjust rules here if you need them."""
        entry = (
            f"Authorized {crime.get_type().value} -> "
            f"{crime.get_target()} at {crime.get_location()} amount {crime.get_amount()}"
        )
        self.__reports_log.append(entry)

    def assign(self, crime, to: "MafiaMember") -> None:
        """Delegate the approved crime to a specific member."""
        # Let the assignee decide how to carry it out (Capo will racketeer or delegate)
        to.commit_crime(crime)
        self.__reports_log.append(f"Assigned {crime.get_type().value} to {to.get_name()}")

    def commit_crime(self, crime) -> None:
        """Godfather does not execute crimes directly."""
        print(f"{self.get_name()} does not commit crimes directly.")
        self.__reports_log.append(f"Refused to commit {crime.get_type().value}")

    def describe(self) -> str:
       pass # blev osäker vad som beskrivs

    def __str__(self) -> str:
        return self.describe()
