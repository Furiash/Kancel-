import random

vyhry = 0

def hraj_hru():
    global vyhry
    uhodnuta_pismena = []
    neuhodnuta_pismena = []
    slova = ["program", "python", "kolo", "auto", "stroj", "kniha", "zahrada",
             "pocitac", "slunce", "strom", "kvetina", "zvire", "jidlo", "kava",
             "postel", "pivo", "vino", "skrin", "zvuk", "film", "hudba", "sport", "pohadka", "pohyb",
            "zabava", "prace", "uceni", "cestovani", "priroda", "zazitek", "zaznam"]
    tajne_slovo = random.choice(slova)

    print("Hra: Hádej slovo po písmenkách!")

    try:
        obtiznost = int(input("Obtížnost: 1 = lehká, 2 = střední, 3 = těžká: "))
        if obtiznost == 1:
            max_pokusu = 10
        elif obtiznost == 2:
            max_pokusu = 7
        elif obtiznost == 3:
            max_pokusu = 5
        else:
            print("Neplatná obtížnost, nastavím 5 pokusů.")
            max_pokusu = 5
    except ValueError:
        print("Zadání nebylo platné, nastavím 5 pokusů.")
        max_pokusu = 5

    print(f"Máš {max_pokusu} pokusů na uhodnutí slova.")

    while True:
        hadani = input("Zadej písmeno nebo celé slovo: ").lower()

        # Zpracování celého slova
        if len(hadani) > 1:
            if hadani.isalpha():
                if hadani == tajne_slovo:
                    print("Gratuluji, uhodl jsi celé slovo! 🎉")
                    vyhry += 1
                    print(f"Počet výher: {vyhry}")
                    break
                else:
                    print("To není správné slovo.")
                    max_pokusu -= 1
                    print(f"Zbývá pokusů: {max_pokusu}")
                    if max_pokusu == 0:
                        print("Došly ti pokusy. Slovo bylo:", tajne_slovo)
                        break
                    continue
            else:
                print("Zadej jen písmena (bez čísel nebo znaků).")
                continue

        # Zpracování jednoho písmene
        if len(hadani) == 1 and hadani.isalpha():
            if hadani in uhodnuta_pismena or hadani in neuhodnuta_pismena:
                print("Toto písmeno jsi už zkusil.")
                continue

            if hadani in tajne_slovo:
                print("Správně!")
                uhodnuta_pismena.append(hadani)
            else:
                print("Špatně!")
                neuhodnuta_pismena.append(hadani)
                max_pokusu -= 1
        else:
            print("Zadej jedno písmeno nebo celé slovo (jen písmena).")
            continue

        # Výpis aktuálního stavu slova
        vystup = ""
        for pismeno in tajne_slovo:
            vystup += pismeno if pismeno in uhodnuta_pismena else "_"

        print("Slovo:", vystup)
        print(f"Zbývá pokusů: {max_pokusu}")
        print(f"Špatná písmena: {', '.join(neuhodnuta_pismena)}")

        if max_pokusu == 0:
            print("Došly ti pokusy. Slovo bylo:", tajne_slovo)
            break

        if vystup == tajne_slovo:
            print("Gratuluji, uhodl jsi celé slovo! 🎉")
            vyhry += 1
            print(f"Počet výher: {vyhry}")
            break

# Hlavní smyčka hry
while True:
    hraj_hru()
    znova = input("Chceš hrát znovu? (ano/ne): ").lower()
    if znova != "ano":
        print(f"Díky za hru! 👋 Celkový počet výher: {vyhry}")
        break