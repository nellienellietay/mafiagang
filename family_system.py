from member_factory import MemberFactory
from Crime import Crime
from Family_inventory import Family_Inventory

class Familysystem():
    def __init__(self):
        self._inv = Family_Inventory()
        self._factory = MemberFactory()
        self._crimes = []          #mple in-memory list
        self._next_crime_id = 1    #incrementing id


# creating looping menu
    def menu(self):
        while True:
            print("\n- - -The Family- - -")
            print("1. Add member")
            print("2. List members")
            print("3. Show hierarchy")
            print("0. Exit")
            choice = input("Select: ").strip() #get user input and remove whitespace
            try:
                if choice == "1":
                    self.add_member() 
                elif choice == "2":
                    self.list_members() 
                elif choice == "3":
                    self._inv.display_member_hierarchy() # display hierarchy
                elif choice == "0":
                    print("Bye.")
                    break
                else:
                    print("Invalid option")
            except Exception as error:  #catch runtime errors
                print(f"Error: {error}") 

    def run(self):
        self.menu() #start menu loop

if __name__ == "__main__": #run ONLY if executed as the main script
    app = Familysystem() #create instance of Familysystem
    app.run() 
