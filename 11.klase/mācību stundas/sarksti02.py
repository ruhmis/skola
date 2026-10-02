    # 1. No teikuma vārdiem (ar visām pieturzīmēm pie tiem) izveidot sarakstu.
    # 2. Vai sarakstā ir vārds, kurš satur tieši 3 burtus a? Izdrukāt JA vai NE.
    # 3. Izdrukāt visas pieturzīmes pretējā secībā, nekā tās dotas teikumā (izdrukāt vienā rindā).
    # 4. No saraksta izdzēst visus vārdus “abc”.
    # 5. Visiem saraksta vārdiem aizvākt visas pieturzīmes.

teksts=input()
vardi=teksts.split()

print("1.uzd", *vardi)

if "aaa" in vardi:
    print("2.uzd IR")
else:
    print("2.uzd NAV")

pieturzimes = []
for vards in vardi:
    if (vards[-1]>='A' and vards[-1]<='Z') or (vards[-1]>='a' and vards[-1]<='z'):
        pass
    else:
        pieturzimes.append(vards[-1])
print(pieturzimes)