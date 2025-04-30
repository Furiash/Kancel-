import random
import time

credit = 150

# Seznam symbolů a jejich výhry při 3 shodách
symboly = ["🍒", "🍋", "🔔", "💎", "🍀"]
vyhry = {
    "🍒": 25,
    "🍋": 50,
    "🔔": 75,
    "💎": 100,
    "🍀": 200
}

# Úvod
print("🎰 Vítej u výherního automatu! 🎰")
print("Získáš výhru, když padnou 3 stejné symboly.")
print("Cena jednoho zatočení: 10 kreditů")
print("Za 3 stejné symboly získáš různé výhry podle symbolu!")
while True:
    input("Stiskni Enter pro roztočení...")

    credit -= 10
    if credit < 0:
        print("Nemáš dostatek kreditů! Konec hry.")
        break

    kotouce = [random.choice(symboly) for _ in range(3)]

    # Zobrazení výsledku s efektem
    for symbol in kotouce:
        print(symbol, end=" ", flush=True)
        time.sleep(0.5)
    print()

    # Vyhodnocení
    if kotouce[0] == kotouce[1] == kotouce[2]:
        vyhra = vyhry[kotouce[0]]
        credit += vyhra
        print(f"🎉 Výhra! Máš tři {kotouce[0]} → +{vyhra} kreditů!")
    else:
        print("😢 Nic jsi nevyhrál, zkus to znovu!")

    print(f"Aktuální kredit: {credit}")

    if credit < 10:
        print("Nemáš dostatek kreditů na další hru. Konec.")
        break

    pokracovat = input("Chceš hrát znovu? (ano/ne): ").lower()
    if pokracovat != "ano":
        print("Díky za hru!")
        print(f"Tvůj konečný kredit: {credit}")
        break