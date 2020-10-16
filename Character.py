from CharInfo import charinfos
from NameGenerator import NameGenerator



from random import choices,gauss,choice,random

class Character:
    firstname,lastname="",""
    rank=""
    homeworld=""
    temper=""
    loyalty=""
    devotion=""
    personality=""
    legion_name= ""
    age=""
    equipment=[]
    squad_name= ""
    company_name= ""
    warrior_lodge=False

    def __init__(self,*,name=",",legion,squad,role,**info):
        self.legion=legion
        self.squad=squad
        self.role=role
        self.legion_name = legion.name
        self.squad_name = squad.name
        self.rank=role.rank
        self.name=name.split(",")
        self.equipment=[]
        self.updated=info.keys()
        self.background=[]

    @property
    def name(self):
        return " ".join((self.firstname,self.lastname))

    @name.setter
    def name(self,value):
        self.firstname,self.lastname=value

    def generate_fill(self):
        CI=charinfos[self.legion.enum]


        if "homeworld" not in self.updated:
            W=CI.homeworld_weights
            worlds= list(W.keys())
            weights=list(W.values())
            self.homeworld = choices(worlds,weights,k=1)[0]
        if "age" not in self.updated:
            A= CI.ages_by_homeworld[self.homeworld]
            ages=[i[1] for i in  A]
            weights =[ i[0] for i in A]
            a=choices(ages,weights)[0]
            average,spread = choices(ages,weights)[0]
            self.age = int(gauss(average,spread))
        if "temper" not in self.updated:
            self.temper=choice(CI.tempers)
        if "personality" not in self.updated:
            personalities=choices((CI.uncommon_personalities,CI.common_personalities),[1,10])[0]
            self.personality = choice(personalities)
        if self.name == " ":
            if self.rank == "captain":
                if self.squad.squadtype!="reserve":
                    self.name = NameGenerator.get_captain(self.legion)
                else:
                    self.name = NameGenerator.get_random(self.legion)
            elif self.rank in ["lieutenant","Company Ancient","Legion Apotechary","Legion Techmarine"]:
                self.name = NameGenerator.get_officer(self.legion)
            else:
                self.name = NameGenerator.get_normal(self.legion)
        if self.squad.squad_type_name=="command":
            if "devotion" not in self.updated:
                self.devotion = choice(CI.devotions)
            if "loyalty" not in self.updated:
                if self.rank =="captain":
                    self.loyalty = choice(CI.captainloyalties)
                else:
                    self.loyalty = choice(CI.captainloyalties)
        else:
            self.devotion=self.squad.devotion
            self.loyalty=self.squad.loyalty
        if "equipment" not in self.updated:
            for items in self.role.equipment.split(","):
                self.equipment+= choice(items.split("/")).split("&")

        if "warrior lodge" not in self.updated:
            if random()>=.4:
                self.warrior_lodge=True

    @property
    def rolename(self):
        if self.role.name in ["Sergeant","Marine"]:
            return self.squad.squad_type_name+" "+self.role.name
    @property
    def stats(self):
        return {
            "name":self.name,
            "rank":self.rank,
            "role":self.rolename,
            "squad":self.squad_name,
            "company":self.company_name,
            "legion": self.legion_name,
            "homeworld":self.homeworld,
            "temper":self.temper,
            "loyalty":self.loyalty,
            "devotion":self.devotion,
            "personality":self.personality,
            "age":self.age,
            "equipment":self.equipment,
            "warrior_lodge":self.warrior_lodge,
        }

    def minicard(self):

        out=f"*{'-'*80}\n"\
            f"|   Name: {self.name.strip(' '):<20}Rank: {self.rank:16}   role: {self.rolename}\n"\
            f"|  Squad: {self.squad_name:<17}Company: {self.company_name:13}    Legion: {self.legion_name}\n"\
            f"|    Age: {self.age:<15}Homeworld: {self.homeworld:12}Personality: {self.personality}\n"\
            f"|Loyalty: {self.loyalty:<13}Temperament: {self.temper:12}   Devotion: {self.devotion}\n"\
            f"|Equipment: {', '.join(self.equipment)}\n"\
            f"|{'Member of the warrior lodge' if self.warrior_lodge else ''}"


        return out

    def output_for_sheet(self):
        l = [
            ["Name:",self.name.strip(" "),"Rank:",self.rank,"Role:",self.rolename],
            ["Squad:",self.squad_name,"Homeworld:", self.homeworld, "Personality:" ,self.personality],
            ["Loyalty:", self.loyalty,"Temperament:", self.temper, "Devotion:",self.devotion],
            ["Equipment:",*self.equipment]
        ]
        l = [ self.name.strip(" "),
              self.rank,
              self.rolename,
              self.squad_name,
              self.company_name,
              self.legion_name,
              self.age,
              self.homeworld,
              self.personality,
              self.loyalty,
              self.temper,
              self.devotion,
              *self.equipment
              ]


        return [s.title() if s else s for s in l]

