n, h = map(int, input().split()) # Malkas Iepirkšana
min_nauda = None

for i in range(n):
    p, c = map(int, input().split())
    
    saini = (h + p - 1) // p
    nauda = saini * c
    
    if min_nauda is None or nauda < min_nauda:
        min_nauda = nauda

print(min_nauda)

# Ievaddati
# Ievada pirmajā rindā divi naturāli skaitļi
# N (1 ≤ N ≤ 100) un H (1 ≤ H ≤ 50000)
# – piegādātāju skaits un apkures sezonai nepieciešamā malkas masa.
# Nākamajās N rindiņās sniegta informācija par piegādātājiem:
# divi skaitļi P un C (1 ≤ i ≤ N) – malkas masa sainī un saiņa cena.
# Izvaddati
# Izvadā sniegt vienu skaiti – minimālo naudas daudzumu centos,
# kāds būs nepieciešams Jurim,
# lai iegādātos vismaz H kilogramus malkas.