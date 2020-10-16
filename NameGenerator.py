from Enums import LEGIONS
from random import choice,random,choices


class NameGenerator:
    _first_names={
        LEGIONS.Luna_wolves:"Odoban, Akkar, Tanis, Vaddon, Orrin, Karis, Madras, Sulla, Volc, Tarik, Luc, Kalus, Tybarr, Grael, Gorus, Malo, Argo, Aran, Janos, Lidon, Litus, Berro, Morros, Uras, Garen, Agos, Obar, Andor, Soric, Orro, Varx".split(",")
    }

    _rare_last_names = {
        LEGIONS.Luna_wolves:"Loken, Moy, Vargas, Valus, Noctua, Marr, Ouros, Qruze, Baar".split(",")

    }#make seperate lists for captain names and officer names

    _rare_first_names = {
        LEGIONS.Luna_wolves: "Maloghurst,Horus,Ezekyle,Serghar,Tybalt,Verulam,Falkus,Xavyer,Garviel".split(",")

    }

    _last_name_prefixes={
        LEGIONS.Luna_wolves:"Mola, Uru, Moria, Kiro, Aba, Axi, Tar, Bolo, Sedi, Ekka, Ju, Fala, Dera, Kara, Syra, Kora, Gola, Bera, Vi, Loga".split(","),

    }
    _last_name_suffixes = {
        LEGIONS.Luna_wolves: "pus, ddon, mand, rae, rgo, r, bre, bal, den, kul, s, tur, nus".split(","),

    }
    @classmethod
    def get_normal(cls,legion_instance):

        legion=legion_instance.enum

        first_name = choice(cls._first_names[legion])
        last_name_pre = choice(cls._last_name_prefixes[legion])
        if last_name_pre[-1] in "sxnzc":
            last_name_suf=""
        else:
            last_name_suf = choice(cls._last_name_suffixes[legion])
        last_name=last_name_pre.strip(" ")+last_name_suf.strip(" ")
        return first_name,last_name


    @classmethod
    def get_random(cls,legion_instance):
        return cls.get_normal(legion_instance)

    @classmethod
    def get_captain(cls,legion_instance):
        return cls.get_normal(legion_instance)

    @classmethod
    def get_officer(cls, legion_instance):
        return cls.get_normal(legion_instance)


if __name__=="__main__":
    class a:
        enum=LEGIONS.Luna_wolves

    while input(NameGenerator.get_normal(a))!="e":
        pass
