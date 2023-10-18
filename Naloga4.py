'''
Poiščite vsa praštevila med 1 in 50.
'''

n = 2

while n <= 50:
    prastevilo = True
    delitelj = 2
    
    while delitelj < n:
        if n % delitelj == 0:
            prastevilo = False
            break
        delitelj += 1

    if prastevilo:
        print(n)

    n += 1