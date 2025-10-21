from mafia_member import MafiaMember
from member_factory import MemberFactory

class FamilyInventory:
    def __init__(self):  # constructor
        """ Initialize the family inventory"""
        self.__factory = MemberFactory()
        self.__members = [] # list to hold mafia members

    def add_member(self, role, **kwargs):
        member = self.__factory.create_member(role, **kwargs) # create member using factory
        self.__members.append(member)
        print("Member added")
        return member

    def remove_member(self, name): 
        for member in self.__members: 
            if member.get_name().lower() == name.lower(): 
                self.__members.remove(member)
                print("Member removed")
                return
        print("Not found")

    def update_member(self, old_name, new_name=None, new_age=None, new_loyalty=None): 
        """ Update member details
        args:
            old_name (str): current name of the member to update
            new_name (str, optional): new name to set
            new_age (int, optional): new age to set
            new_loyalty (int, optional): new loyalty to set
        """
        for member in self.__members:
            if member.get_name().lower() == old_name.lower():
                if new_name is not None: # update name if provided
                    member.set_name(new_name)
                if new_age is not None:
                    member.set_age(new_age)
                if new_loyalty is not None:
                    member.set_loyalty(new_loyalty)
                print("Member updated")
                return
        print("Member not found")

    def search_member(self, keyword):
        """ Search for members by keyword in their name"""
        keyword = (keyword or "").strip().lower()
        found = False # search for members matching keyword
        for member in self.__members:
            if keyword in member.get_name().lower(): 
                role = member.__class__.__name__ # get role from class name
                print(f"Role: {role} | Name: {member.get_name()} | Age: {member.get_age()} | Loyalty: {member.get_loyalty()}") 
                found = True #set found to true if match found 
        if not found:
            print("No matching member found.")

    def list_members(self): # return list of all members
        """ List all members in the family inventory
            returns: 
                List[MafiaMember] - list of all members
        """
        return list(self.__members)

    def display_member_hierarchy(self):
        """ Display the hierarchy of members in order:
        1. Godfather, 2. Consigliere, 3. Capos, 4. Soldiers
        """
        if not self.__members:
            print("No members.")
            return

        godfather = None # find and categorize members by role
        consigliere = None # 
        capos = []
        soldiers = []

        for member in self.__members: # 
            role = member.__class__.__name__ 
            if role == "Godfather" and godfather is None:
                godfather = member
            elif role == "Consigliere" and consigliere is None:
                consigliere = member
            elif role == "Capo":
                capos.append(member) #append to capos list
            elif role == "Soldier":
                soldiers.append(member) # append to soldiers list
                
        if godfather: 
            print(f"Godfather - {godfather.get_name()}")
            
        if consigliere:
            print(f"Consigliere - {consigliere.get_name()}") 
            
        for capo in capos:
            print(f"Capo - {capo.get_name()}, {capo.get_crew_name()}") 

        for soldier in soldiers:
            assigned = soldier.get_assigned_capo()
            assigned_name = assigned.get_name() if hasattr(assigned, "get_name") else str(assigned) #hasattr to avoid errors
            print(f"soldier - {soldier.get_name()}, {assigned_name}")

