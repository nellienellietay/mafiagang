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
            print("3. Do crime") 
            print("4. Remove member")
            print("5. Update member")
            print("6. Search member")
            print("0. Exit")

            choice: str = input("Select: ").strip()    #get user input and remove whitespace

            if choice == "0":
                print("Goodbye.")
                break
            
            # Name 
            elif choice == "1":
                name: str = input("Enter name: ").strip() 
               
                if not name:
                    print("Invalid name. You must enter something.")
                    continue
                if not name.replace(" ", "").isalpha():
                    print("Invalid name. Letters only.")
                    continue

                # Age
                age_input: str = input("Enter age: ").strip()
                if not age_input.isdigit():
                    print("Invalid age. Please enter a number.")
                    continue

                age: int = int(age_input)
  
                # Member role 
                role: str = input("Enter role (Godfather, Capo, Soldier, Consigliere): ").strip().capitalize()
                
                try:
                    member = self.__inv.add_member(role, name=name, age=age)
                    print(f"{member.get_name()} added as {member.__class__.__name__}.")
                
                except ValueError as e:
                    print(e)

            elif choice == "2":
                members: list[MafiaMember] = self.__inv.list_members()
                if not members:
                    print("No members found.")
                    continue 
                for m in members:
                    print(f"{m.__class__.__name__}: {m.get_name()}, {m.get_age()} years old")


            elif choice == "3":
                print(" Do crime")
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
                    print("Invalid number.")
                    continue

                member: MafiaMember = members[index]

                crime: Crime = Crime(crime_type, [member.get_name()])
                self.__crimes.append(crime) #store the crime in the list

                member.commit_crime(crime)

            elif choice == "4":
                name: str = input("Enter name to remove: ").strip()

                # Error handling
                if not name:
                    print("You must enter a name.")
                    continue

                # This line calls logic from inventory file
                result: str = self.__inv.remove_member(name) 

                print(result)

            elif choice == "5":
                old_name: str = input("Enter current name of the member: ").strip()

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

                # Calls inventory logic 
                result: str = self.__inv.update_member(old_name, new_name or None, new_age)
                print(result)

            elif choice == "6":
                keyword: str = input("Enter name or part of name to search for: ").strip()
                if not keyword:
                    print("You much enter something to search for.")
                    continue

                # Calls inventory-method
                self.__inv.search_member(keyword)

            else:
                print("Invalid choice. Try again.")

    def run(self) -> None: 
        """Start the family system application"""
        self.menu() #starts the menu loop

if __name__ == "__main__": #run ONLY if executed as the main script
    app = FamilySystem() #create instance of Familysystem
    app.run()  
