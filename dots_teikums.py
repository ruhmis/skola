a=input()

if a[-1] == '.':
    print("stāstījuma")
elif a[-1] == '!':
    print("rosinājuma")
elif a[-1] == '?':
    print("jautājuma")

print(a.count(" ") + 1) # vārdu skaits teikumā

for i in range(0, len(a)-1): # katra vārda pēdējais burts
    if a[i] == " ":
        print(a[i-1], end=" ")
print(a[-2], end=" ")