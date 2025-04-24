import random

uhodnuta_pismena = []
slova = ["program", "python", "kolo", "auto", "stroj", "kniha", "zahrada", "pocitac", "slunce", "strom", "kvetina", "zvire", "jidlo"]
tajne_slovo = random.choice(slova)
max_pokusu = 5  # Maximální počet pokusů

print("Hra: Hádej slovo po písmenkách!")
print(f"Máš {max_pokusu} pokusů na uhodnutí slova.")

while True:
    hadani = input("Zadej písmeno nebo celé slovo: ").lower()

    # Pokud uživatel zadal celé slovo
    if hadani == tajne_slovo:
        print("Gratuluji, uhodl jsi celé slovo! 🎉")
        break

    # Pokud zadal neplatný vstup
    if len(hadani) != 1 or not hadani.isalpha():
        print("Zadej prosím pouze jedno písmeno nebo celé slovo.")
        continue

    # Pokud už bylo písmeno hádáno
    if hadani in uhodnuta_pismena:
        print("Toto písmeno jsi už uhodl, zkus jiné.")
        continue

    # Správné nebo špatné písmeno
    if hadani in tajne_slovo:
        print("Správně!")
        uhodnuta_pismena.append(hadani)
    else:
        print("Špatně!")
        max_pokusu -= 1

    # Vygenerování zobrazeného slova
    vystup = ""
    for pismeno in tajne_slovo:
        if pismeno in uhodnuta_pismena:
            vystup += pismeno
        else:
            vystup += "_"

    print("Slovo:", vystup)
    print(f"Zbývá pokusů: {max_pokusu}")

    # Konec hry kvůli vyčerpání pokusů
    if max_pokusu == 0:
        print("Bohužel, došly ti pokusy. Slovo bylo:", tajne_slovo)
        break

    # Konec hry, pokud je slovo uhodnuté
    if vystup == tajne_slovo:
        print("Gratuluji, uhodl jsi celé slovo! 🎉")
        break