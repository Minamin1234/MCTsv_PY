from typing import NoReturn as void
from typing import List

class MCsv(object):
    ENCODING:str = "UTF-8"

    def __init__(self) -> void:
        return

    def ToCSVFromList(self,words:List[List[str]]) -> str:
        result:str = ""
        for cword in words:
            for rword in cword:
                result += rword + ","
            result = result.rstrip(",")
            result += "\n"
        return result

    def ToListFromCSV(self,words:str) -> List[List[str]]:
        clevel:int = 0
        rlevel:int = 0
        result:List[List[str]] = [[""]]
        for w in words:
            if w == ",":
                result[clevel].append("")
                rlevel += 1
                continue
            if w == "\n":
                result.append([""])
                clevel += 1
                rlevel = 0
                continue
            result[clevel][rlevel] += w
        return result

    def RemakeCSV(self,words:str,textalign="right") -> str:
        Counts:List[int] = []
        Cnt:int = 0
        result:str = ""

        for w in words:
            if w == "," or w == "\n":
                Counts.append(Cnt)
                Cnt = 0
                continue
            Cnt += 1
        Counts.append(Cnt)
        MAX:int = max(Counts)

        Idx:int = 0
        Frag:bool = False
        if textalign == "left":
            for w in words:
                if w == "," or w == "\n":
                    result += " " * (MAX - Counts[Idx])
                    result += w
                    Idx += 1
                    continue 
                result += w
            return result

        for w in words:
            if w == "," or w == "\n":
                Frag = False
                Idx += 1
                result += w
                continue

            if Frag == False:
                Frag = True
                result += " " * (MAX - Counts[Idx])

            result += w
        return result

    def GetTextFromCSVFile(self,path:str) -> str:
        return

    def ToTSV(self,CSVtext:str) -> str:
        return
