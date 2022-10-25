import sys

inp = ""
out = ""
INPUT = []
OUTPUT = []
RW = ['import',
      'from',
      'printf',
      'var',
      '//',
      'func',
      '{',
      '}',
      'retu',
      'getchar',
      'char',
      'int',
      'float',
      'double',
      'in',
      'scanf',
      'if',
      'else',
      'elif',
      'for',
      'calc',
      'continue',
      'break',
      'switch',
      'case',
      'default',
      'loop',
      'return',
      'call'
      ]

PY = [
    ['#include <', 1, '>'],
    ['#include ', 1],
    ['printf (', 1, ')', ';'],
    [1, ' ', 2, ' = ', 4, 5, 6, 7, 8, 9, 10, 11,
        12, 13, 14, 15, 16, 17, 18, 19, 20, ';'],
    ['// ', 1],
    [1, ' ', 2, ' (', 3, ' ', 4, ' ', 5, ' ', 6, ' ', 7, ' ', 8, ' ', 9, ' ', 10, ' ',  11, ' ',
     12, ' ', 13, ' ', 14, ' ', 15, ' ', 16, ' ', 17, ' ', 18, ' ', 19, ' ', 20, ') ', "{"],
    ['{'],
    ['}'],
    ['return ', 1, ';', '\n', '}'],
    ['getchar', 1, ';'],
    ['char ', 1, ';'],
    ['int ', 1, ';'],
    ['float ', 1, ';'],
    ['double ', 1, ';'],
    [1, ' = ', 3, ';'],
    ['scanf (', 1, ', ', 2, ')', ';'],
    ['if (', 1, ')'],
    ['else'],
    ['else if (', 1, ')'],
    ['for (', 1, ')'],
    [1, ';'],
    ['continue;'],
    ['break;'],
    ['switch (', 1, ')'],
    ['case ', 1, ':'],
    ['default:'],
    ['while (', 1, ')'],
    ['return', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ';'],
    [1]
]

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


for i in OUTPUT:
    for j in i:
        file = open(makeFile, mode='a')
        file.write(j + "\n")
