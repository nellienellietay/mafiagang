class MafiaMember(ABC): #abstract class


    def __init__(self, name: str, age: int, loyalty: int):
        self._name = name
        self._age = age
        self._loyalty = loyalty
        pass

    def get_name(self) -> str:
        pass

    def set_name(self, name: str) -> None:
        pass

    def get_age(self) -> int:
        pass

    def set_age(self, age: int) -> None:
        pass

    def get_loyalty(self) -> int:
        pass

    def set_loyalty(self, loyalty: int) -> None:
        pass

    @abstractmethod
    def commit_crime(self, crime: Crime) -> None:
        pass
    
    @abstractmethod
    def describe(self) -> str:
        pass