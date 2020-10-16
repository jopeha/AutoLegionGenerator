from Enums import LEGIONS,COMPANYTYPES
from Company import Company
from Squad import Squad
from random import sample,choice

from configparser import ConfigParser

class LegionHandler:
    preset=ConfigParser()
    preset.read("Settings/LegionTypes.settings")

    @classmethod
    def load(cls,legion_type):
        return LegionType(name=legion_type.name,**cls.preset[legion_type.name])

class LegionType:
    size=0
    name="legion type"
    companies={COMPANYTYPES:0}
    def __init__(self,*,name,size,**companies):
        self.name=name
        self.size=size

        self.companies = dict(((COMPANYTYPES[key],int(value)) for key,value in companies.items()))

class Legion:
    name="legion name"
    enum=LEGIONS
    legion_type=LegionType

    def __init__(self):
        self.companies=[]
        self.command_squad_members=[]

    def populate(self,legion_type):
        self.name=legion_type.name
        self.enum=legion_type
        lt=self.legion_type=LegionHandler.load(legion_type)
        for company_type,amount in lt.companies.items():
            for i in range(amount):
                comp=Company(self)
                comp.populate(company_type)
                self.companies.append(comp)

    @property
    def main_title(self):
        return self.name.title()



leg=Legion()
leg.populate(LEGIONS.Luna_wolves)

for i in leg.companies[0].squads[0].members:
    print(i.minicard())