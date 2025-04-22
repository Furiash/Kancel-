# Kamen, Nuzky, Papir
import random

volby = {1: "kámen", 2: "nůžky", 3: "papír"}
pocitac = random.randint(1, 3)

try:
    hrac = int(input("Kámen = 1, nůžky = 2, papír = 3: "))
except ValueError:
    print("Chyba: neplatná volba.")
    exit()

if hrac not in [1, 2, 3]:
    print("Chyba: musíš zadat číslo 1, 2 nebo 3!")
    exit()

print(f"Počítač vybral {volby[pocitac]}.")

if hrac == pocitac:
    print("Remíza! 🤝")
elif (hrac == 1 and pocitac == 2) or (hrac == 2 and pocitac == 3) or (hrac == 3 and pocitac == 1):
    print("Vyhrál jsi! 🏆")
else:
    print("Prohrál jsi! ❌")