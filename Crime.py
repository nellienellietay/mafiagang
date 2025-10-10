class Crime:

    def __init__(self, crime_type: str, target: str, profit: float): #
        self._crime_type = crime_type
        self._target = target
        self._profit = profit
        self._assigned_member: Optional['MafiaMember'] = None

    def assign_member(self, member: 'MafiaMember') -> None:
        pass

    def get_type(self) -> str:
        pass

    def set_type(self, crime_type) -> str:
        pass

    def get_target(self) -> str:
        pass

    def set_target(self, target: str) -> None:
        pass

    def set_target(self, target: str) -> None:
        pass

    def set_profit(self, profit: float) -> None:
        pass

    def describe(self) -> str:
        pass