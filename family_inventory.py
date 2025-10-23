from mafia_member import MafiaMember
from godfather import Godfather
from consigliere import Consigliere
from capo import Capo
from soldier import Soldier

"""This is the family invetory."""

class FamilyInventory:

    def __init__(self): 
        """Initialize the family inventory"""

        self.__members = [] # list to hold mafia members

    def add_member(self, role: str, name: str, age: int, reports_to=None, skills=None):
        """ Add a new member"""

        # Check if we have a Godfather already
        if role == "godfather":
            for member in self.__members:
                if isinstance(member, Godfather):
                    raise ValueError("Who are you trying to fool. There can only be one Godfather.")

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
        return member

    def remove_member(self, name: str): 
        """ Remove a member by name and return a message.
        Error handling is done in family_system, not here"""
        
        name = name.strip().lower()

        # Loops through all members 
        for member in self.__members:

            #  Compares the names, not taking into consideration small/big letters
            if member.get_name().lower() == name: 

                # Removes member from the list 
                self.__members.remove(member)
                return f"Member '{member.get_name()}' removed."
            
        # If the loops does not find a match 
        return f"No member named '{name}' found."

    def update_member(self, old_name, new_name=None, new_age=None): 
        """ Update member name and/or age:
            old_name (str): current name of the member to update
            new_name (str, optional): new name to set
            new_age (int, optional): new age to set
        """
        
        old_name = (old_name or "").strip().lower()

        # Loops through all members in a list
        for member in self.__members:
            if member.get_name().lower() == old_name:
                updated = False

                if new_name:
                    member.set_name(new_name.strip())
                    updated = True

                if new_age is not None:
                    member.set_age(int(new_age))

                return ("Member updated") if updated else "No changes provided."
        
        return f"No member named '{old_name}' found"

    def search_member(self, keyword):

        """ Search for members by keyword in their name"""

        keyword = (keyword or "").strip().lower()
        found_members = [] 

        # Loop through all the members.
        for member in self.__members:
            if keyword in member.get_name().lower(): 
                found_members.append(member)

        if found_members:
            for member in found_members:
                role = member.__class__.__name__
                print(f"Role: {role} | Name: {member.get_name()} | Age: {member.get_age()}") 
        else:
            print("No matching member found")

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
            return("No members.")

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
                "godfather": [godfather] if godfather else [],
                "consigliere": [consigliere] if consigliere else [],
                "capos": capos,
                "soldiers": soldiers,
            }
