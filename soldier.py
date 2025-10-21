from mafia_member import MafiaMember
from crime import Crime, CrimeType


class Soldier(MafiaMember):
    """Subklass till MafiaMember"""
    def __init__(
            self,
            name: str,
            age: int,
            skills: list[CrimeType] | None = None,
            loyalty: int = 100,
            reports_to: 'MafiaMember' | None = None
        ):
        #calls the constructor of the parent class (MafiaMember) so all shared attributes
        #like name, age, role, loyalty, and reports_to are created there.
        super().__init__(name, age, role="Soldier", loyalty=loyalty, reports_to=reports_to)
        #creates a list for e soldiers skills (type CrimeType)
        #: list[CrimeType] is a type hint
        #this list should only contain CrimEtype values and if no list is provided the soldier gets an empty list
        self.__skills: list[CrimeType] = skills if skills is not None else [] 
    
    def commit_crime(self, crime: Crime) -> None:
        """commits the crime though comparing the crimetype to a chosen soldiers skill,
        if crimetype = a crimetype = print a matching line of text.
        not sure where a chosen soldier comes in 
        """
        match_found = False 

        #get info from crime-object and save it in variables
        crime_type = crime.get_type()
        location = crime.get_location()
        amount = crime.get_amount()
        target = crime.get_target()

        for skill in self.__skills:
            if skill == crime_type:
                match_found = True
                print(f"{self.get_name()} executes {crime_type.value} in {location}, earns {amount}")
                break
            
        # här kan vi lägga in roligare prints som är kopplade till olika crimetype
        # och som skriver ut olika meddelanden beroende på vilket crime 

        if not match_found: 
            print(f"{self.get_name} fails to handle {crime_type.value} in {location}.")

    def __str__(self):
        pass
        
