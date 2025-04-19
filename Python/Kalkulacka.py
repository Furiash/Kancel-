print("Zadej typ operace")
print("1 = sčítání")
print("2 = odčítání")
print("3 = násobení")
print("4 = dělení")
print("5 = mocnina")
print("6 = odmocnina")

ans = input("Vyber si operaci (1–6): ")

try:
    a = float(input("Zadej první číslo: "))
    b = float(input("Zadej druhé číslo: "))

except ValueError:
    print("Chyba: zadaný vstup není číslo.")
    exit()

if ans == "1":
    print("Výsledek:", round(a + b, 5))

elif ans == "2":
    print("Výsledek:", round(a - b, 5))

elif ans == "3":
    print("Výsledek:", round(a * b, 5))

elif ans == "4":
    s = input("Dělení beze zbytku (1), nebo se zbytkem (2): ")

    if s == "1":
        if b == 0:
            print("Chyba: nelze dělit nulou.")
        else:
            print("Výsledek:", round(a / b, 5))

    elif s == "2":
        if b == 0:
            print("Chyba: nelze dělit nulou.")
        else:
            print("Výsledek:", round(a // b, 5), "(Zb.:", round(a % b, 5), ")")
    else:
        print("Neplatná volba pro dělení.")

elif ans == "5":
    print("Výsledek:", round(a ** b, 5))

elif ans == "6":
    if b == 0:
        print("Chyba: nelze odmocnit nulovým exponentem.")
    else:
        print("Výsledek:", round(a ** (1 / b), 5))

else:
    print("Neplatná volba")