from mafia_member import MafiaMember
from godfather import Godfather
from consigliere import Consigliere
from capo import Capo
from soldier import Soldier

class FamilyInventory:
    """Handles storage and management of all MafiaMember objects in the family."""
    def __init__(self): 
        """Initialize empty inventory with the mafia family members
        returns: 
            members list[MafiaMember]"""
        self.__members = []

    def add_member(self, role: str, name: str, age: int): 
        """Adds a new member through the inputted variable role.
        
        Args: 
            role (str): role of the member
            name (str): name of new member
            age (int): age of new member

        Returns:
            MafiaMember: the created member instance
        """
        role = (role or "").strip().lower()

        if role == "godfather":
            for member in self.__members:
                if isinstance(member, Godfather):
                    raise ValueError("Who are you trying to fool? There can only be one Godfather in this family.")
            member = Godfather(name=name, age=age)

        elif role == "consigliere":
            member = Consigliere(name=name, age=age)
        elif role == "capo":
            member = Capo(name=name, age=age)
        elif role == "soldier":
            member = Soldier(name=name, age=age)
        else:
            raise ValueError(f"This '{role}' that you are talking about is unbeknown to us.")
        self.__members.append(member)
        return member

    def remove_member(self, name: str): 
        """ Remove a member from the inventory through name
        returns: 
        flag (bool): True if member was removed, False if person not found"""
        
        for member in self.__members:
            if member.get_name().lower == name.lower():
                self.__members.remove(member)
                return True
        return False

    def update_member(self, old_name, new_name=None, new_age=None): 
        """ Update member name and/or age
        args:
            old_name (str): current name of the member to update
            new_name (str, optional): new name to set
            new_age (int, optional): new age to set

        returns: 
            update status (str)
            not found message (str)
        """
        old_name = (old_name or "").strip().lower()

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
        """ Search for members by keyword in their name
        args: 
            str keyword: keyword to search for
        """

        keyword = (keyword or "").strip().lower()
        found = False

        for member in self.__members:
            if keyword in member.get_name().lower(): 
                print(member)
                found = True
        if not found:
            print("No matching member found")

    def list_members(self): 
        """Return all members in the family inventory
        returns:
            list[MafiaMember]: list of all members
        """
        return list(self.__members)
