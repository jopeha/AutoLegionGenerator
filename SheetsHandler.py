import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import ctime
import string
from Legion import Legion
from Enums import LEGIONS
class SheetsHandler:

    def __init__(self):
        scope = ["http://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name("sheets/servicekey.json",scope)

        self.gc = gspread.authorize(credentials)
        self.file=None

    def make_new(self,legion):#,sharemail):
        #f=self.file=self.gc.create(f"LegionSheet_{legion.name}_{ctime().replace(' ','-')}")
        f=self.file=self.gc.open("ArttuRopeOutputSheet")

        #self.file.share("teemu.o.harju@gmail.com",perm_type="user",role="writer")

        ws=f.get_worksheet(0)
        h=6
        w=14
        startrow=10
        startcol=0
        headerrow=[["NAME","RANK","ROLE","SQUAD","COMPANY","LEGION","AGE","HOMEWORLD","PERSONALITY","LOYALTY","TEMPERAMENT","DEVOTION","EQUIPMENT"]]
        for company in legion.companies:

#            ws = f.add_worksheet(title = company.name,rows = 200, cols = 26)
            ws.update(self.toRange(startcol,startrow-1,startcol+w,startrow-1),headerrow)
            for pos,squad in enumerate(company.squads):

                ws.update(self.toRange(startcol,startrow+pos,startcol+w,startrow+pos+len(squad.members)),[x.output_for_sheet() for x in squad.members])





    @staticmethod
    def toRange(c1,r1,c2,r2):
        return SheetsHandler.toA1(c1,r1)+":"+SheetsHandler.toA1(c2,r2)
    @staticmethod
    def toA1(col,row):
        if col>len(string.ascii_uppercase):
            raise ValueError("can only handle small numbers as cols")
        letter=string.ascii_uppercase[col]
        return f"{letter}{row}"




if __name__=="__main__":
    a=SheetsHandler()
    l=Legion()
    l.populate(LEGIONS.Luna_wolves)
    a.make_new(l)


