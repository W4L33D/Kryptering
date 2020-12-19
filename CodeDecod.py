import math

def encode(tekst):
    arr = list(tekst)
    x = len(arr)
    mid = []
    for i in range(0, math.ceil(x/2)):
        mid.append(arr[2*i])
    for i in range(0, math.floor(x/2)):
        mid.append(arr[2*i+1])
    noe = ''.join(map(str, mid))
    return noe

def decode(tekst):
    arr = list(tekst)
    x = len(arr)
    mid = []
    y = math.ceil(x/2)
    for i in range(0, y):
        if y+i < len(arr):
            mid.append(arr[i])
            mid.append(arr[y + i])
        else: mid.append(arr[i])
    noe = ''.join(map(str, mid))
    return noe

f = open("test.txt", "r")
random = encode(f.read())
print(random)
ras = decode(random)
print(ras)