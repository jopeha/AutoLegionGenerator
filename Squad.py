from Character import Character
from SquadInfo import SquadType,SquadTypeHandler,SquadRole
from CharInfo import CharInfo
from Enums import SQUADTYPES

from random import choice

class Squad:
    leader= Character
    squad_type = SquadType
    squad_type_name= ""
    leader_rank=""
    name= "my squad"
    devotion = ""
    loyalty = ""

    def __init__(self,legion,company):
        self.legion=legion
        self.company=company
        self.members=[]
        self.leader=Character

    def populate(self,squadtype):
        st=self.squad_type=SquadTypeHandler.load(squadtype)
        self.squad_type_name=st.name
        self.leader_rank=st.leader_rank
        self.devotion= choice(CharInfo.devotions)
        self.loyalty= choice(CharInfo.loyalties)

        if st.choice!="False":
            options= st.choice.split("/")
            winner=choice(options)
            for group in options:
                for key in group.split("&"):
                    if key not in winner:
                        st.squadroles[key]=0

        for role,amount in st.squadroles.items():
            for _ in range(int(amount)):
                context={
                    "legion":self.legion,
                    "company":self.company,
                    "role":SquadRole.load(role.title()),
                    "squad":self
                }
                char=Character(**context)
                char.generate_fill()
                self.members.append(char)
                if len(self.members)==st.size:
                    break

