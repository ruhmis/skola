a=input()
vardi=a.split()

lielais=False # vai ir vismaz viens drukāts burts
lielo_sk = 0 # drukāto burtu skaits

for apelsins in vardi:
    for bumbieris in apelsins:
        if bumbieris >= 'A' and bumbieris <= 'Z':
            lielais=True
            lielo_sk += 1
if lielais==True:
    print("IR DRUKATS")
else:
    print("NAV DRUKATS")
print(lielo_sk)
