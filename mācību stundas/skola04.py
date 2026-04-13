# a = input().split()
# K = int(a[0]) # nauda
# N = int(a[1]) # zīmolu skaits

# best_price_per_kg = 10**4
# best_brand = ""
# best_m = 0
# best_c = 0

# for i in range(N):
#     m, c, zimols = input().split()
#     m = int(m)
#     c = int(c)

#     if zimols == "DOGO":
#         continue

#     price_per_kg = c / m

#     if price_per_kg <= best_price_per_kg:
#         best_price_per_kg = price_per_kg
#         best_brand = zimols
#         best_m = m
#         best_c = c

# packs = K // best_c
# kg = packs * best_m

# print(best_brand, packs)