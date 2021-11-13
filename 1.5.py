v = float(input("Viruchka: "))
i = float(input("Izderjki: "))
n = int(input("Vvedite kolichestvo sotrudnikov: "))
if v > i:
    print(f"Viruchka > Izderjek {v - i}")
    print(f"Rentabelnost: {100 * (v - i) / v:.1f}%")
    print(f"Na kajdogo sotrudnika po {(v - i) / n:.2f}")
elif i > v:
    print(f"Viruchka < Izderjek {v - i}")
else:
    print(f"Rabota v - {v - i} !!!")
