from mafia_member import MafiaMember
from crime import Crime, CrimeType
from soldier import Soldier

class Capo(MafiaMember):
    """subclass of MafiaMember representing the Capo in the mafia hierarchy."""
    def __init__(self, name, age, reports_to=None):
        super().__init__(name=name, age=age, role="Capo", reports_to=reports_to)
        #crew name becomes "the <name> crew" or "the crew" if no name is given
        self.__crew_name = f"the {name.strip().lower()} crew" if name else "the crew"
        self.__soldiers = []  # crew lis

    def get_crew_name(self):
        """ getter for crew name
        """
        return self.__crew_name #getter for crew name

    def add_soldier(self, soldier):
        name = soldier.get_name()
        if any(soldier.get_name().casefold() == name.casefold() for s in self.__soldiers): #casefold to make sure case is okay
            raise ValueError(f"{name} is already in {self.get_name()}'s crew")
        if hasattr(soldier, "set_reports_to"):
            soldier.set_reports_to(self)
        self.__soldiers.append(soldier)
        return self
    
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
        if crime.get_type() == CrimeType.RACKETEERING: #Capo can do racketeering 
            print(f"{self.get_name()} performs Racketeering")
            return
        if self.__soldiers:
            self.__soldiers[0].commit_crime(crime) #assigns to first soldier in crew for now
        else:
            print(f"No soldiers to handle {crime.get_type().value}") 
    
    def __str__(self) -> str:
        return f"Capo {self.get_name()} of crew {self.__crew_name}" 

