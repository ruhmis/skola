    # 1. No teikuma vārdiem izveidot sarakstu.
    # 2. Ar type() funkcijas palīdzību izdrukāt saraksta datu tipu.
    # 3. Aiz saraksta elementa ar indeksu 2 ievietot vārdu “Sveiks”.
    # 4. Sakārtot sarakstu pretēji alfabētiskajai secībai.
    # 5. Izdrukāt kurā vietā tagad atrodas vārds Sveiks.
    # 6. Vai sarakstā ir vārds “abc”? Izdrukāt JA vai NE.
    # 7. Vai teikuma pēdējais vārds atrodas trešajā vietā? Izdrukāt JA vai NE.

teksts=input()
teksts=teksts[:-1]
vardi=teksts.split()

print("1.uzd", *vardi)

print("2.uzd", type(vardi))

vardi.insert(2, "Sveiks") # nestradaa
print("3.uxd", *vardi)

vardi.sort(reverse=True)
print("4.uzd", vardi)

print("5.uzd", vardi.index("Sveiks")+1)

if "abc" in vardi:
    print("6.uzd IR")
else:
    print("6.uzd NAV")
