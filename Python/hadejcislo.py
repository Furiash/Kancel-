import random

# Výběr obtížnosti
try:
    obtiznost = int(input("Vyber si obtížnost, 1 = Lehká, 2 = Střední, 3 = Těžká: "))
except ValueError:
    print("Chyba: zadaný vstup není číslo.")
    exit()  # ukončí program

# Nastavení počtu pokusů podle obtížnosti
if obtiznost == 1:
    pokusy = 9
elif obtiznost == 2:
    pokusy = 7
elif obtiznost == 3:
    pokusy = 5
else:
    print("Chybná volba obtížnosti.")
    exit()

# Generování tajného čísla
tajne_cislo = random.randint(1, 50)

# Herní smyčka
for pokus in range(pokusy):
    try:
        x = int(input(f"Hádej číslo (pokus {pokus + 1}/{pokusy}): "))
    except ValueError:
        print("Chyba: zadaný vstup není číslo.")
        continue  # vrátí tě zpět na začátek cyklu, neskončí hru

    if x == tajne_cislo:
        print("Uhodnuto! ✅")
        break
    else:
        if x < tajne_cislo:
            print("Více ➡️")
        else:
            print("Méně ⬅️")
else:
    print(f"Nepovedlo se! ❌ Tajné číslo bylo {tajne_cislo}.")