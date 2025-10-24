from enum import Enum 

class CrimeType(Enum):
    RACKETEERING = "Racketeering"
    EXTORTION = "Extortion"
    BRIBERY = "Bribery"
    SMUGGLING = "Smuggling"
    INTIMIDATION = "Intimidation"

class Crime:
    def __init__(self, crime_type: CrimeType, participants: list[str]): 
        """Initializes a Crime instance"""
        self.__type =  crime_type
        self.__participants = participants

    def get_type(self) -> CrimeType:
        """returns the type of crime
        returns:
            CrimeType: the type of crime committed
        """
        return self.__type
    
    def get_participants(self) -> list[str]:
        """returns the participants involved in the crime
        Returns:
            list[str]: list of participants involved in the crime
        """
        return self.__participants

    def __str__(self) -> str:
        """string description of Crime
        Returns:
            str: string description of the crime
        """
        return f"a string"
