from mafia_member import MafiaMember
from crime import Crime, CrimeType

class Consigliere(MafiaMember):

    def __init__(self, name: str, age: int, expertise: str = "politics", reports_to: "MafiaMember" = None):
        """Initializes a Consigliere as instance
        args:
            name (str): Name of the consigliere
            age (int): Age of the consigliere
            expertise (str): Area of expertise for advice
            reports_to (MafiaMember): The MafiaMember this consigliere reports to
        """
        # calls parent constructor to set shared attr
        super().__init__(name, age, role="Consigliere", reports_to=reports_to)            

        # specific attribute for Consigliere
        self.__expertise: str = expertise

    def commit_crime(self, crime: Crime) -> None:
        """Consigliere involvment in the crime is by commenting on it
        args: 
            crime (Crime): The crime being committed   
        """
        crime_type = crime.get_type()
        name = self.get_name()

        if crime_type == CrimeType.EXTORTION:
            print(f"{name} warns: 'Extortion brings heat from city hall. I'd advise restraint.'")
        elif crime_type == CrimeType.SMUGGLING:
            print(f"{name} notes: 'Smuggling profits are high, but customs are watching closely'")
        elif crime_type == CrimeType.BRIBERY:
            print(f"{name} says: 'Bribes must be subtle. The fewer witnesses, the better.'")
        elif crime_type == CrimeType.RACKETEERING:
            print(f"{name} reminds: 'Keep the front businesses clean. Paperwork wins wars.'")
        elif crime_type == CrimeType.INTIMIDATION:
            print(f"{name} murmurs: 'Fear fade fast. Loyalty lasts longer.'")
        else:
            print(f"{name} calmly says: 'I have no comment on this kind of work'")

    def advise(self, issue: str) -> str:
        """Gives general advice to the Godfather depending on  topic
        returns:
            str: advice string
        """
        issue_lower = issue.lower()

        if "money" in issue_lower or "finance" in issue_lower:
            return "Patience, Godfather. True wealth comes from stability."
        elif "police" in issue_lower or "law" in issue_lower:
            return "Lay low. Influence is stronger than confrontation."
        elif "family" in issue_lower or "conflict" in issue_lower:
            return "Keep the family united at all costs"
        else:
            return "Sometimes, Godfather, doing nothing is the smartest move"

    def __str__(self) -> str:
        """string description of Consigliere"""
        return f"Consigliere {self.get_name()}, expertise in {self.__expertise}"
