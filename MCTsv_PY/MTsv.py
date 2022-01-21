from typing import NoReturn as void
from typing import List

class MTsv(object):
    ENCODING:str = "UTF-8"

    def __init__(self):
        return

    def ToTSVFromList(self,words:List[List[str]]) -> str:
        result:str = ""
        for cword in words:
            for rword in cword:
                result += rword + "\t"
            result = result.rstrip("\t")
            result += "\n"
        return result

    def ToListFromTSV(self,words:str) -> List[List[str]]:
        return

    def RemakeTSV(self,words:str) -> str:
        return

    def GetTextFromTSVFile(self,path:str) -> str:
        return

    def ToCSV(self,TSVtext:str) -> str:
        return