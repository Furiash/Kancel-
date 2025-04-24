import random

uhodnuta_pismena = []
slova = ["program", "python", "kolo", "auto", "stroj"]
tajne_slovo = random.choice(slova)
max_pokusu = 5  # Maximální počet pokusů

print("Hra: Hádej slovo po písmenkách!")
print(f"Máš {max_pokusu} pokusů na uhodnutí slova.")

while True:
    hadani = input("Zadej písmeno: ").lower()

    # Kontrola, zda je zadáno pouze jedno písmeno
    if len(hadani) != 1 or not hadani.isalpha():
        print("Zadej prosím pouze jedno písmeno.")
        continue

    # Kontrola, zda písmeno již bylo uhodnuto
    if hadani in uhodnuta_pismena:
        print("Toto písmeno jsi už uhodl, zkus jiné.")
        continue

    if hadani in tajne_slovo:
        print("Správně!")
        uhodnuta_pismena.append(hadani)
    else:
        print("Špatně!")
        max_pokusu -= 1  # Snížíme počet pokusů

    # Vytvoříme řetězec s uhodnutými písmeny a _ místo neuhodnutých
    vystup = ""
    for pismeno in tajne_slovo:
        if pismeno in uhodnuta_pismena:
            vystup += pismeno
        else:
            vystup += "_"

    print("Slovo:", vystup)
    print(f"Zbývá pokusů: {max_pokusu}")

    # Konec hry, pokud byly pokusy vyčerpány
    if max_pokusu == 0:
        print("Bohužel, došly ti pokusy. Slovo bylo:", tajne_slovo)
        break

    # Kontrola, zda bylo celé slovo uhodnuto
    if vystup == tajne_slovo:
        print("Gratuluji, uhodl jsi celé slovo! 🎉")
        break