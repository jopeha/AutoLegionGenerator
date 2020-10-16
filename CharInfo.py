from Enums import LEGIONS

class CharInfo:
    common_personalities = [
        "merciless",
        "heroic",
        "malicious",
        "callous",
        "daring",
        "vengeful",
        "just",
        "righteous",
        "defiant",
        "energetic",
        "bold",
        "alert",
        "eager",
        "calm",
        "youthful",
        "archaic",
        "lone wolf",
        "dignified",
        "serious",
        "hateful",
        "impulsive",
        "humble",
        "braggart",
        "sadistic"
    ]

    uncommon_personalities=[
        "romantic",
        "warm",
        "empathic",
        "friendly"
    ]

    tempers = [
        "Choleric", "Flegmatic", "Sanquine", "Melancholic"
    ]

    devotions = [
        "Nonexistent", "Mild", "Strong", "Fierce", "Unbreaking"
    ]

    loyalties = [
        "Emperor", "Primarch", "Captain", "Squad leader",
    ]

    captainloyalties = [
        "Emperor", "Primarch", "Captain", "Chaos"
    ]

class LunaInfo(CharInfo):
    homeworld_weights={
        "Terra":25,
        "Luna":5,
        "Cthonia":70
    }
    ages_by_homeworld={
        "Terra":[(1,(240,25))],
        "Luna":[(1,(240,25))],
        "Cthonia": [(5, (50, 15)),
                    (90, (110, 20)),
                    (5, (200, 15))]
    }





charinfos = {
    LEGIONS.Luna_wolves: LunaInfo
}
