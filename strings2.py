"""
data = "from jeiel.lima@uam.imp.ma Sat Apr  5 09:14:06 2023"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ",atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
"""
## Exercício

str = "X-DSPAM-Confidence: 0.8475 "

findstr = str.find(":")
print(findstr)

piece = str[findstr+2:]
print(class.piece)

value = float(piece)
print(class.value)

