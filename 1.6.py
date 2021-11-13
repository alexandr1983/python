while True:
    a = float(input("Chislo km: "))
    b = float(input("Rezultat ne menee km: "))
    d = 1
    if (a <= 0) or (b < 0):
        print("!=0 and >0")
    else:
        while a < b:
            a = a + a * 0.1
            d += 1
        print(f"Rezultat za {d} dnei {b:.0f} km")
        break
