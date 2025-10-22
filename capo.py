from mafia_member import MafiaMember
from Crime import Crime, CrimeType
from soldier import Soldier

class Capo(MafiaMember):
    """subclass of MafiaMember representing a Capo in the mafia hierarchy."""
    def __init__(self, name, age, loyalty=95, reports_to=None):
        super().__init__(name=name, age=age, loyalty=loyalty, role="Capo", reports_to=reports_to)
        self.__crew_name = (name.split()[-1] if name else "Crew")  # a safety feature, if no name given default to "Crew"
        # crew name is basically just last name
        self.__soldiers = []  # crew list

    def get_crew_name(self):
        """ getter for crew name
        """
        return self.__crew_name #getter for crew name
    
    def assign_by_name(self, crime, soldier_name): #explicit assignment (order from Godfather routed by Capo)
        """assigns a crime to a soldier by name within the Capo's crew
            args: 
                crime (Crime): the crime to be assigned
                soldier_name (str): the name of the soldier to assign the crime to
        """
        for crew_soldier in self.soldiers: #iterates through soldiers in crew
            if crew_soldier.get_name().lower() == soldier_name.lower(): 
                crew_soldier.commit_crime(crime) #findd soldier by name and assigns crime
                return
            raise ValueError(f"{soldier_name} is not in {self.get_name()}'s crew") #
    
    def commit_crime(self, crime: Crime) -> None:
        """ Capo delegates crimes to soldiers in his crew
        args:
            crime (Crime): the crime to be committed
        """
        #får orders från godfather och fördelar till rätt soldat.
        #tror han borde kunna utföra brott också i nödfall... / i think he should only be able to do racketeering
        
        if crime.get_type() == CrimeType.RACKETEERING: #Capo can do racketeering 
            print(f"{self.get_name()} performs Racketeering in {crime.get_location()}, amount {crime.get_amount()}")
            return
        if self.__soldiers:
            self.__soldiers[0].commit_crime(crime) #assigns to first soldier in crew for now
        else:
            print(f"No soldiers to handle {crime.get_type().value}") 
    
    def __str__(self) -> str:
        return f"Capo {self.get_name()} of crew {self.__crew_name}" 

