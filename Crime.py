from enum import Enum #Enum enables the creation of certain chosen values something can have. A list of approved constants

#A helpclass that defines and stores our crime-types
class CrimeTye(Enum):
    RACKETEERING = "Racketeering"
    EXTORTION = "Extortion"
    BRIBERY = "Bribery"
    SMUGGLING = "Smuggling"
    INTIMIDATION = "Intimidation"

class Crime:
    def __init__(self, crime_type: Crimetype, str, target: str, amount: float, location: str, participants: list[str]): 
        self.__type =  crime_type
        self.__target = target
        self.__amount = amount 
        self.__location = location
        self.__participants = participants

    def get_type(self) -> CrimeType:
        return self.__type

    def set_type(self, crime_type) -> str:
        pass

    def get_target(self) -> str:
        pass

    def set_target(self, target: str) -> None:
        pass

    def set_target(self, target: str) -> None:
        pass

    def set_profit(self, profit: float) -> None:
        pass

    def describe(self) -> str:
        pass