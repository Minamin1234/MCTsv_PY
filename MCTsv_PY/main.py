from MCsv import MCsv

Csvdev = MCsv()

data = [
    ["aa","ab","ac"],
    ["ba","bb","bc"]
    ]

f = open("LIST.csv","r")
csvdata = f.read()

newdata = Csvdev.ToCSVFromList(data)
print(newdata)

newdata = Csvdev.ToListFromCSV(csvdata)
print(newdata)

newdata = Csvdev.RemakeCSV(csvdata)
print(newdata)