from member_factory import MemberFactory
from crime import Crime, CrimeType
from family_inventory import FamilyInventory

class Familysystem():
    def __init__(self) -> None:
        """Initialize the family system application"""
        self._inv = FamilyInventory()
        self._factory = MemberFactory()
        self._crimes = []  #list to hold crimes
        self._next_crime_id = 1   # unique id for crimes


# The looping menu that starts the whole application
    def menu(self) -> None:
        """Display menu and handle user input"""
        while True:
            print("\n- - -The Family- - -")
            print("1. Add member")
            print("2. List members")
            print("3. Show hierarchy")
            print("4. Register crime") 
            print("0. Exit")
            choice: str = input("Select: ").strip() #get user input and remove whitespace
            try:
                if choice == "1":
                    self.add_member() 
                elif choice == "2":
                    self.list_members() 
                elif choice == "3":
                    self._inv.display_member_hierarchy() # display hierarchy
                    
                # register crime lacks functionality in other class so creating a very basic version here    
                elif choice == "4": 
                    crime_type_input = input("Enter crime type: ").strip().lower() 
                    if crime_type_input not in CrimeType._member_names_: # validate crime type in CrimeType class
                        print("Invalid crime type.")
                        continue
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
