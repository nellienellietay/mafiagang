from enum import Enum #Enum enables the creation of certain chosen values something can have. A list of approved constants

#A helpclass that defines and stores our crime-types
class CrimeType(Enum):
    RACKETEERING = "Racketeering"
    EXTORTION = "Extortion"
    BRIBERY = "Bribery"
    SMUGGLING = "Smuggling"
    INTIMIDATION = "Intimidation"

class Crime:
    def __init__(self, crime_type: CrimeType, str, target: str, amount: float, location: str, participants: list[str]): 
        self.__type =  crime_type
        self.__participants = participants

    def get_type(self) -> CrimeType:
        return self.__type

    def get_participants(self) -> list[str]:
        return self.__participants

    def __str__(self) -> str:
        names = ", ".join(self.__participants)
        return f"{self.__type.value} by {names}"
