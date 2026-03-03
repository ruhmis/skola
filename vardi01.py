vards1 = input() # test: aleksandrs un sandra
garums1 = len(vards1)
vards2 = input()
garums2 = len(vards2)
sakrit=0
for p in range(garums1):
    for o in range(garums2):
        if vards1[p]==vards2[o]:
            sakrit+=1
            vards2=vards2[:o]+'#'+vards2[o+1:]
            break
if sakrit==garums2:
    print("VAR")
else:
    print("NEVAR")