from mafia_member import MafiaMember
from crime import Crime, CrimeType

class Soldier(MafiaMember):
    """Subklass till MafiaMember"""
    def __init__(
            self,
            name: str,
            age: int,
            skills: list[CrimeType],
            reports_to: MafiaMember 
        ):

        """calls the constructor of the parent class (MafiaMember) so all shared attributes
        like name, age, role, and reports_to are created there."""
        super().__init__(name, age, role="Soldier", reports_to=reports_to)

        """creates a list for e soldiers skills (type CrimeType)
        #: list[CrimeType] is a type hint
        #this list should only contain CrimEtype values and if no list is provided the soldier gets an empty list"""

        self.__skills: list[CrimeType] = skills if skills is not None else [] 
    
    def commit_crime(self, crime: Crime) -> None:
        """commits the crime though comparing the crimetype to a chosen soldiers skill,
        if crimetype = a crimetype = print a matching line of text.
        not sure where a chosen soldier comes in 
        """
        match_found = False 

        #get info from crime-object and save it in variables
        crime_type = crime.get_type()

        for skill in self.__skills:
            if skill == crime_type:
                match_found = True
                print(f"{self.get_name()} executes {crime_type.value}")
                break

        if not match_found: 
            print(f"{self.get_name()} fails to handle {crime_type.value}")

    # Ny funktion kl.23.47 
    def get_assigned_capo(self):
        """Return the capo this soldier reports to"""
        return self.get_reports_to()

    def __str__(self):
        return f"Soldier {self.get_name()}"
        
