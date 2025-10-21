class MemberFactory:
    """ Factory class to create mafia family members based on their roles
        returns instances of Godfather, Consigliere, Capo, or Soldier
    """
    def create_member(self, role: str, name: str, **kwargs): # create member based on role
        role = (role or "").strip().lower()
        if "age" not in kwargs:
            raise ValueError("age is required when creating a member")

        age = kwargs["age"] # kwargs must contain age
        reports_to = kwargs.get("reports_to") 
        skills = kwargs.get("skills") # for soldier role

        if role == "godfather":
            from godfather import Godfather
            return Godfather(name=name, age=age) # create Godfather instance

        if role == "consigliere":
            from consigliere import Consigliere
            return Consigliere(name=name, age=age, reports_to=reports_to) 

        if role == "capo":
            from capo import Capo
            return Capo(name=name, age=age, reports_to=reports_to)

        if role == "soldier":
            from soldier import Soldier
            return Soldier(name=name, age=age, assigned_capo=reports_to, skills=skills) 

        raise ValueError(f"Unknown role: {role}") # raise error for unknown role
