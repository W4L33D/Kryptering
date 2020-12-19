import math

def encode(tekst):
    arr = list(tekst)
    lengde = len(arr)
    tabell = []
    for i in range(0, math.ceil(lengde/2)):
        tabell.append(arr[2*i])
    for i in range(0, math.floor(lengde/2)):
        tabell.append(arr[2*i+1])
    noe = ''.join(map(str, tabell))
    return noe

def decode(tekst):
    arr = list(tekst)
    lengde = len(arr)
    tabell = []
    pivot = math.ceil(lengde/2)
    for i in range(0, pivot):
        if pivot+i < len(arr):
            tabell.append(arr[i])
            tabell.append(arr[pivot + i])
        else: tabell.append(arr[i])
    noe = ''.join(map(str, tabell))
    return noe

melding = open("test.txt", "r")
Kryptert = encode(melding.read())
print(Kryptert)
Dekryptert = decode(Kryptert)
print(Dekryptert)