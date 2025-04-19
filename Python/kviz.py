# Jednoduchý kvíz
spravne = 0  # počítadlo správných odpovědí

otazky = [
    ("Jaké je hlavní město České republiky?", "praha"),
    ("Kolik je 5 + 7?", "12"),
    ("Jakou barvu má tráva?", "zelená"),
    ("Jaké zvíře dělá 'mňau'?", "kočka"),
    ("Kolik měsíců má rok?", "12")
]

for otazka, odpoved in otazky:
    uzivatel = input(otazka + " ").lower()
    if uzivatel == odpoved:
        print("Správně! ✅")
        spravne += 1
    else:
        print(f"Špatně! ❌ Správná odpověď byla: {odpoved}")

print(f"\nKvíz dokončen! Měl(a) jsi {spravne} správných odpovědí z {len(otazky)}.")