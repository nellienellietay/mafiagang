
from member_factory import MemberFactory

class Family_Inventory:
    def _init_(self):
        self.__factory = MemberFactory() #instance of MemberFactory
        self.__members = [] #list to hold members

    def add_member(self, role: str, **kwargs) -> None: 
        member = self.__factory.create_member(role, **kwargs) 
        self.__members.append(member) 
        return member

    def remove_member(self, name: str) -> None: #if names are the same, remove the first one found
        for member in self.__members: #iterate through list of members in inventory
            if member.get_name().lower() == name.lower(): # case insensitive comparison
                self.__members.remove(m)
                print("Member removed")
                return
        print("Not found")
        print("---------")

    def update_member(self, old_name: str, new_name: str, new_age: int, new_loyalty: int) -> None:
        for member in self.__members: #iterate through list of members     
            if member.get_name().lower() == old_name.lower(): 
                if new_name is not None: # check if new_name is provided
                    member.set_name(new_name)
                if new_age is not None:
                    member.set_age(new_age)
                if new_loyalty is not None: 
                    member.set_loyalty(new_loyalty)
                print("Member updated")
                print("--------------")
                return
        print("Member not found")
        print("----------------")

    def search_member(self, keyword: str) -> None:
        found = False
        for member in self.__members:
            if keyword.lower() in member.get_name().lower():
                role = m.__class__.__name__
                print(f"Role: {role} Name: {member.get_name()} Age: ({member.get_age()}) Loyalty: ({member.get_loyalty()})")
                found = True
        if not found:
            print("No matching member found")

    def list_members(self):
        pass

    def display_member_hierarchy(self):
        pass
