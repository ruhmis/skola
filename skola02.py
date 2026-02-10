# Malkas Iepirkšana

print("grib malku (kg): ",end="")
n=int(input())

print("ievadiet piegādātāju piedāvajumus: ")
for i in range(n):
    a=input()
    b=a.split()
    p=int(b[0])
    c=int(b[1])

    saini=h//p
    atlukums=h%p

    if atlukums>0:
        saini+=1
    nauda=saini*c
    if i==0:
        min_nauda=nauda1
    if nauda1<min_nauda:
        min_nauda=nauda1
    
    print(min_nauda)