from enum import Enum

class LEGIONS(Enum):
    Luna_wolves=1
    Death_Guard=2
    World_Eaters=3
    Imperial_Fists=4
    Emperors_Children=5

class SQUADTYPES(Enum):
    command = 1
    veteran = 2
    terminator = 3
    legion_command = 4
    reaver = 5
    devastator = 6
    tactical = 7
    assault = 8

class COMPANYTYPES(Enum):
    veteran = 1
    battle = 2
    reserve = 3

print(SQUADTYPES["assault"])