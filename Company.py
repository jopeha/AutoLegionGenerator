from Squad import Squad
from Enums import SQUADTYPES
from configparser import ConfigParser
from random import random,randint

class CompanyHandler:
    presets = ConfigParser()
    presets.read("Settings/CompanyTypes.settings")

    @classmethod
    def load(cls,company_type):
        name=company_type.name
        data = cls.presets[name]
        return CompanyType(name=name,**data)


class CompanyType:
    name= ""
    size = 11
    squadtypes={SQUADTYPES:0}

    def __init__(self,*,name,size,**kw):
        self.name=name
        self.size=size
        self.squadtypes=dict(((SQUADTYPES[key],value) for key,value in kw.items()))







class Company:
    name = "my company"
    squads=[]
    company_type=CompanyType
    company_type_name=""

    def __init__(self,legion):
        self.legion=legion
        self.squads=[]
        self.command_squad=Squad

    def populate(self,company_type_name):
        ct=self.company_type=CompanyHandler.load(company_type_name)
        self.company_type_name=ct.name
        for squadtype,value in ct.squadtypes.items():

            if len(value.split("-"))>1:
                mini,maxi=value.split("-")
                mini,maxi=int(mini),int(maxi)
                amount=randint(mini,maxi)

            elif 0<float(value)<1:
                amount=random()<float(value)
            else:
                amount=int(value)

            for _ in range(amount):

                squad=Squad(self.legion,self)
                squad.populate(squadtype)
                self.squads.append(squad)
                if ct.size==len(self.squads):
                    break
            else:
                continue
            break