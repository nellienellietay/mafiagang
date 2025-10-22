from member_factory import MemberFactory
from crime import Crime, CrimeType
from family_inventory import FamilyInventory

"""
FamilySystem class: Handles the user interface and input logic for the Mafia Family program.
Responsible for menu control, input validation and delegating tasks to other classes.
"""

class Familysystem():

    def __init__(self) -> None:
        """Initialize the family system application"""
        self.__inv = FamilyInventory()
        self.__factory = MemberFactory()
        self.__crimes = []  #list to hold crimes
        self.__next_crime_id = 1   # unique id for crimes


# The looping menu that starts the whole application
    def show_menu(self) -> None:
        """Display menu and handle user input"""
        while True:
            print("\n- - -The Family- - -")
            print("1. Add member")
            print("2. List members")
            print("3. Show hierarchy")
            print("4. Register crime") 
            print("0. Exit")

    def run(self) -> None:
        """Start familysystem"""
        while True:
            self.show_menu()
            choice: str = input("Select: ").strip()

            if choice not in ["0","1","2","3","4"]:
                print("Invalid option. Please enter a number between 0-4.")
                continue 

            try:
                if choice == "1":
                    self.__add_member()   

                elif choice == "2":
                    self.list_members() 

                elif choice == "3":
                    self._inv.display_member_hierarchy() 

                elif choice == "4": 
                    crime_type_input = input("Enter crime type: Racketeering, Extortion, Bribery, Smuggling or Intimidation: ").strip().upper() 
                    
                    if crime_type_input not in CrimeType._member_names_: # validate crime type in CrimeType class
                        print("Invalid crime type. Try again ")
                        continue
                    
                    print(f"Crime confirmed and ready to take place")
                    #here we will ask for target, amount, member

                elif choice == "0": 
                    print("Bye.")
                    break
                    
                else:
                    print("Invalid option")

            except Exception as error:  #avoid runtime errors
                print(f"Error: {error}") 

    def run(self) -> None:
        """Start the family system application"""
        self.menu() #starts the menu loop

if __name__ == "__main__": #run ONLY if executed as the main script
    app = Familysystem() #create instance of Familysystem
    app.run()  
