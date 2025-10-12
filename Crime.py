class Crime:

    def __init__(self, crime_type: str, target: str, profit: float): #
        self.__crime_type = crime_type # "Racketeering","Extortion","Bribery","Smuggling","Intimidation"
        self.__target = target
        self.__amount = amount
        self.__assigned_to = []

    def get_type(self) -> str:
        return self.__crime_type # strings of crime type

    def set_type(self, crime_type) -> str:
        self.__type = crime_type # set new type by user input

    def get_target(self) -> str:
        return self.__target # 

    def set_target(self, target: str) -> None:
        self.__target = target 

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        if amount < 0: # 
            print("Amount cannot be negative")
        else:
            self.__amount = amount # change amount if valid

    def get_assigned_to(self):
        return self.__assigned_to

    def assign_to(self, member):
        if member not in self.__assigned_to: #control if member is already assigne
            self.__assigned_to.append(member) 
            print(member.get_name(), "has been assigned to crime")
        else: 
            print(member.get_name(), "is already assigned")
# !!!!add error handling

    def remove_assignee(self, member):
        if member in self.__assigned_to: #check if member is in the list
            self.__assigned_to.remove(member) #remove member from the list
            print(member.get_name(), "removed from this crime.")
    

    def describe(self) -> str:
        pass
