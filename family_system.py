from crime import Crime
from crime_type import CrimeType
from family_inventory import FamilyInventory
from mafia_member import MafiaMember

class FamilySystem():
    """Handles user interaction and connects UI to the mafia family data layer."""

    def __init__(self) -> None:
        """Initialize the family system application"""
        self.__inv: FamilyInventory = FamilyInventory()
        self.__crimes: list[Crime] = []

    def menu(self) -> None:
        """Display menu and handle user input"""
        while True:
            print("\n- - -The Family- - -")
            print("1. Add new member")
            print("2. List members")
            print("3. Do crime") 
            print("4. Get rid of member")
            print("5. Update member")
            print("6. Search member")
            print("0. Exit")

            choice: str = input("Select: ").strip()
            if choice == "0":
                print("Goodbye.")
                break
# 1. 
            elif choice == "1":
                name: str = input("Enter name: ").strip() 
                if not name:
                    print("Invalid name. You must enter something.")
                    continue
                
                if not name.replace(" ", "").isalpha():
                    print("Invalid name. Letters only.")
                    continue
                
                age_input: str = input("Enter age: ").strip()
                if not age_input.isdigit():
                    print("Invalid age. Please enter a number.")
                    continue

                age: int = int(age_input)
  
                role: str = input("Enter role (Godfather, Capo, Soldier, Consigliere): ").strip().capitalize()
                try:
                    member = self.__inv.add_member(role, name=name, age=age)
                    print(f"{member.get_name()} added as {member.__class__.__name__}.")
                except ValueError as e:
                    print(e)
# 2.
            elif choice == "2":
                members = self.__inv.list_members()
                if not members:
                    print("No members found.")
                else: 
                    for member in members:
                        print(member)
#3.
            elif choice == "3":
                print(" Do crime")
                print("Choose crime: Racketeering, Extortion, Bribery, Smuggling, Intimidation")
                crime_input: str = input("Enter crime type: ").strip().upper()
                if crime_input not in CrimeType._member_names_:
                    print("Invalid crime type")
                    continue
                crime_type: CrimeType = CrimeType[crime_input]

                members: list[MafiaMember] = self.__inv.list_members()
                if not members:
                    print("No members available")
                    continue

                print("Family members")
                for i in range(len(members)):
                    print(f"{i + 1}. {members[i].get_name()}")
                member_choice: str = input("Select member number: ").strip()
                if not member_choice.isdigit(): 
                    print("Invalid choice.")
                    continue
                
                index = int(member_choice) - 1 
                if index < 0 or index >= len(members):
                    print("Invalid number.")
                    continue
                
                member: MafiaMember = members[index]
                crime: Crime = Crime(crime_type, [member.get_name()])
                self.__crimes.append(crime) 
                member.commit_crime(crime)
# 4.
            elif choice == "4":
                name: str = input("Enter name to remove: ").strip()
                if not name:
                    print("You must enter a name.")
                    continue
                removed: bool = self.__inv.remove_member(name) 
                if removed:
                    print(f"Member has been {name} removed.")
                else:
                    print(f"No member named {name} found.")
# 5.
            elif choice == "5":
                old_name: str = input("Enter current name: ").strip()

                if not old_name:
                    print("You must enter a name.")
                    continue

                new_name: str = input("Enter new name: ").strip()
                new_age_input: str = input("Enter new age: ").strip()

                if new_age_input:
                    if not new_age_input.isdigit():
                        print("Invalid age. Please enter a number.")
                        continue
                    new_age = int(new_age_input)
                else:
                    new_age = None
                result: str = self.__inv.update_member(old_name, new_name or None, new_age)
                print(result)
# 6.
            elif choice == "6":
                keyword: str = input("Enter name or part of name to search for: ").strip()
                if not keyword:
                    print("You must enter something to search for.")
                    continue

                self.__inv.search_member(keyword)

            else:
                print("Invalid choice. Try again.")

    def run(self) -> None: 
        """Start the family system application"""
        self.menu() 

if __name__ == "__main__":
    app = FamilySystem()
    app.run()  
