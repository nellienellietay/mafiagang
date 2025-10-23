from crime import Crime, CrimeType
from family_inventory import FamilyInventory
from mafia_member import MafiaMember

class FamilySystem():
    """Handles user interaction and connects UI to the mafia family data layer."""

    def __init__(self) -> None:
        """Initialize the family system application"""
        self.__inv: FamilyInventory = FamilyInventory()
        self.__crimes: list[Crime] = []  #type hint + create empty list

# The looping menu that starts the whole application
    def menu(self) -> None:
        """Display menu and handle user input"""
        while True:
            print("\n- - -The Family- - -")
            print("1. Add member")
            print("2. List members")
            print("3. Show hierarchy")
            print("4. Do crime") 
            print("5. Remove member")
            print("0. Exit")

            choice: str = input("Select: ").strip()    #get user input and remove whitespace

            if choice == "0":
                print("Goodbye.")
                break
            
            elif choice == "1":
                name: str = input("Enter name: ").strip() 
                if not name.isalpha(): #check if name contains letters *only letters
                    print("Invalid name.")
                    continue

                age_input: str = input("Enter age: ").strip()
                if not age_input.isdigit():
                    print("Invalid age.")
                    continue
                age: int = int(age_input)
  
                role: str = input("Enter role (Godfather, Capo, Soldier, Consigliere): ").strip().capitalize()
                member: MafiaMember | None = self.__inv.add_member(role, name=name, age=age)
                
                if member:
                    print(f"{member.get_name()} added as {member.__class__.__name__}.")
                else:
                    print("Invalid role or creation failed.")

            elif choice == "2":
                members: list[MafiaMember] = self.__inv.list_members()
                if not members:
                    print("No members found.")
                    continue 
                for m in members:
                    print(f"{m.__class__.__name__}: {m.get_name()}, {m.get_age()} years old")

            elif choice == "3":
                hierarchy = self.__inv.display_member_hierarchy()
                if not any(hierarchy.values()):
                    print("No members yet")
                    continue
                for role, members in hierarchy.items(): #loop through the hierarchy dictionary
                    for m in members:
                        print(f"{role}: {m.get_name()}")

            elif choice == "4":
                print("Register a crime")
                print("Available crimes: Racketeering, Extortion, Bribery, Smuggling, Intimidation")

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
                if not member_choice.isdigit(): #check if input is a number
                    print("Invalid choice.")
                    continue

                index = int(member_choice) - 1 #adjust for 0-based index
                if index < 0 or index >= len(members): #check valid index
                    print("Invalid member number.")
                    continue

                member: MafiaMember = members[index]

                crime: Crime = Crime(crime_type, [member.get_name()])
                self.__crimes.append(crime) #store the crime in the list

                member.commit_crime(crime)
                print(f"{member.get_name()} committed {crime_type.value}.")

            elif choice == "5":
                name: str = input("Enter name to remove: ").strip()
                result: str = self.__inv.remove_member(name) #remove member by name
                print(result)

            else:
                print("Invalid choice. Try again.")

            #except Exception as error:  #avoid runtime errors
                #print(f"Error: {error}") 

    def run(self) -> None: 
        """Start the family system application"""
        self.menu() #starts the menu loop

if __name__ == "__main__": #run ONLY if executed as the main script
    app = FamilySystem() #create instance of Familysystem
    app.run()  
