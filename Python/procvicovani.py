import random

print("Vyber si operaci")
print("1 = sčítání")
print("2 = odčítání")
print("3 = násobení")
print("4 = dělení")

operace = input("Zadej číslo operace (1-4): ")

for i in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    if operace == "4":
        b = random.randint(1, 10)  # aby dělitel nebyl moc velký

    if operace == "1":
        vysledek = a + b
        priklad = f"{a} + {b} = "

    elif operace == "2":
        vysledek = a - b
        priklad = f"{a} - {b} = "

    elif operace == "3":
        vysledek = a * b
        priklad = f"{a} * {b} = "

    elif operace == "4":
        vysledek = round(a / b)  # ZAOKROUHLUJEME NA CELÁ ČÍSLA
        priklad = f"{a} ÷ {b} = (zaokrouhli na celé číslo) "

    else:
        print("Neplatná volba")
        break  # ukončí program

    # NAČÍTÁNÍ ODPOVĚDI
    odpoved = input(priklad)
    odpoved = odpoved.replace(",", ".")  # nahradíme čárku za tečku

    try:
        uzivatel = float(odpoved)
    except ValueError:
        print("Chyba! Zadal(a) jsi neplatné číslo. ❌")
        continue

    # POROVNÁNÍ ODPOVĚDI
    if uzivatel == vysledek:
        print("Správně! ✅")
    else:
        print(f"Špatně! ❌ Správná odpověď je: {vysledek}")

print("Konec procvičování! 👏")