from mafia_member import MafiaMember
from crime import Crime
from crime_type import CrimeType

class Consigliere(MafiaMember):
    """Subclass to MafiaMember"""
    def __init__(self, name: str, age: int) -> None:
        """Initializes a Consigliere as instance
        args:
            name (str): Name of the consigliere
            age (int): Age of the consigliere
        """
        super().__init__(name, age, role="Consigliere")            

    def commit_crime(self, crime: Crime) -> None:
        """Consigliere does not directly commit crimes, but advises on them.
        args: 
            crime (Crime): The crime being committed 
            name (str): Name of the consigliere  
        """
        crime_type = crime.get_type()
        name = self.get_name()

        intro = f"{name} does not directly commit crimes, but is always implicit in his persuasive advice... In this case "

        if crime_type == CrimeType.EXTORTION:
            print(f"{intro}{name} warns: 'Extortion brings heat from city hall... I'd advise restraint.'")
        elif crime_type == CrimeType.SMUGGLING:
            print(f"{intro}{name} notes: 'Smuggling profits are high, but customs are watching closely...'")
        elif crime_type == CrimeType.BRIBERY:
            print(f"{intro}{name} says: 'Bribes must be subtle, my friend... The fewer witnesses, the better.'")
        elif crime_type == CrimeType.RACKETEERING:
            print(f"{intro}{name} reminds: 'Keep the front businesses clean... Paperwork wins wars.'")
        elif crime_type == CrimeType.INTIMIDATION:
            print(f"{intro}{name} murmurs: 'Fear fade fast... Loyalty lasts longer.'")
        else:
            print(f"{intro}{name} calmly says: 'I have no comment on this kind of work...'")

    def __str__(self) -> str:
        """string rep of Consigliere
        returns:
            str representation
        """
        return f"{self.get_role()}, {self.get_name()}, trusted advisor of the Don."
