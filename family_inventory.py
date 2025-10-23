from mafia_member import MafiaMember
from godfather import Godfather
from consigliere import Consigliere
from capo import Capo
from soldier import Soldier

class FamilyInventory:
    def __init__(self):  # constructor
        """Initialize the family inventory"""
        self.__members = [] # list to hold mafia members

    def add_member(self, role: str, **kwargs):
        """ Add a new member to the family inventory
        args:
            role: Role of the member 
            kwargs: Additional attributes depending on role
        returns: 
            mafiaMember
        """
        role = (role or "").strip().lower()
        name = kwargs["name"]
        age = kwargs["age"]
        reports_to = kwargs.get("reports_to")
        skills = kwargs.get("skills")

        if role == "godfather":
            member = Godfather(name=name, age=age)
        elif role == "consigliere":
            member = Consigliere(name=name, age=age, reports_to=reports_to)
        elif role == "capo":
            member = Capo(name=name, age=age, reports_to=reports_to)
        elif role == "soldier":
            member = Soldier(name=name, age=age, skills=skills, reports_to=reports_to)
        else:
            raise ValueError(f"Unknown role: {role}")

        self.__members.append(member)
        print("Member added")
        return member

    def remove_member(self, name): 
        """ Remove a member by name"""
        for member in self.__members: 
            if member.get_name().lower() == name.lower(): 
                self.__members.remove(member)
                print("Member removed")
                return
        print("Not found")

    def update_member(self, old_name, new_name=None, new_age=None): 
        """ Update member details
        args:
            old_name (str): current name of the member to update
            new_name (str, optional): new name to set
            new_age (int, optional): new age to set
        """
        for member in self.__members:
            if member.get_name().lower() == old_name.lower():
                if new_name is not None: # update name if provided
                    member.set_name(new_name)
                if new_age is not None:
                    member.set_age(new_age)
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
                print(f"Role: {role} | Name: {member.get_name()} | Age: {member.get_age()}") 
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
                assigned = member.get_assigned_capo() if hasattr(member, "get_assigned_capo") else None #### review get assign capo
                assigned_member = assigned if isinstance(assigned, MafiaMember) else None
                soldiers.append({"soldier": member, "assigned_capo": assigned_member})
                
        return {
                "godfather": godfather,
                "consigliere": consigliere,
                "capos": capos,
                "soldiers": soldiers,
            }
