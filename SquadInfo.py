import configparser
from Enums import SQUADTYPES
from random import choice
from configparser import ConfigParser

class SquadTypeHandler:
    presets = ConfigParser()
    presets.read("Settings/SquadTypes.settings")


    @classmethod
    def load(cls, squad_type):
        name=squad_type.name
        data = cls.presets[name]
        if data["Automate"]=="True":
            cls.generateautosquad(data,name)
        return SquadType(name=name,**data)

    @classmethod
    def generateautosquad(cls,data,name):
        auto=cls.presets["AUTO"]
        for item in auto:
            if "AUTO" in item:
                data[item.replace("AUTO",name)]=auto[item]


class SquadRole:

    presets=configparser.ConfigParser()
    presets.read("Settings/SquadRoles.settings")

    def __init__(self,role,equipment,rank,type="marine"):
        self.name=self.role = role
        self.equipment = equipment
        self.rank = rank
        self.type = type


    @classmethod
    def load(cls,name):
        data=cls.presets[name]
        return cls(**data)


class SquadType:
    name= ""
    size = 10
    def __init__(self,*,name,size,leader_rank,automate,choice,**kw):
        self.name=name
        self.size=size
        self.leader_rank=leader_rank
        self.squadroles=dict(kw)
        self.choice=choice





