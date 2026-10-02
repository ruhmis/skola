a=input() # Sporta Inventārs
b=a.split()

nauda=int(b[0])
apavu_cena=int(b[1])
kreklu_cena=int(b[2])

print(nauda//apavu_cena,end=" ") # cik apavus var nopirkt
print(nauda//kreklu_cena) # cik kreklus var nopirkt

if nauda//apavu_cena>nauda//kreklu_cena: # vai apavu var nopirkt vairāk
    print("Apavi")
elif nauda//apavu_cena<nauda//kreklu_cena: # vai kreklu var nopirkt vairāk
    print("Krekli")
else:
    print("Apavi Krekls") 