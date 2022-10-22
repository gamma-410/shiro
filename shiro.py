import sys
import os

inp = ""
out = ""
INPUT = []
OUTPUT = []
RW = ['import', 'printf', 'var', '//', 'func', '{', '}', 'retu']
PY = [['#include <', 1, '>'], ['printf (', 1, ')', ';'], [1, ' ', 2, ' = ', 4, ';'], ['// ', 1], [1, ' ', 2, ' ', 3, ' ', 4, "{"], ['{'], ['}'], ['return ', 1, ';', '\n', '}']]
args = sys.argv

openName = args[1]
openFile = openName + ".sr"
makeFile = openName + ".c"

open(makeFile, mode='w')

while inp != "END":
    i = open(openFile)
    for inp in i:
        INPUT.append(list(map(str, inp.split())))


for i in INPUT:
    if i[0] in RW:
        indexRW = RW.index(i[0])

        for n in PY[indexRW]:
            if type(n) is int:
                if n <= len(i) - 1:
                    out += i[n]
            else:
                out += n

        OUTPUT.append([out])
        out = ""


# トランスパイルした結果を出力
for i in OUTPUT:
    for j in i:
        file = open(makeFile, mode='a')
        file.write(j + "\n")
