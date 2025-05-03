import turtle
import random
import time

# Nastavení obrazovky
okno = turtle.Screen()
okno.bgcolor("white")

# Seznam symbolů a výher
symboly = ["🍒", "🍋", "🔔", "💎", "🍀"]
vyhry = {
    "🍒": 25,
    "🍋": 50,
    "🔔": 75,
    "💎": 100,
    "🍀": 200
}

# Vytvoření želvy pro kreslení rámečků
zelva = turtle.Turtle()
zelva.hideturtle()
zelva.pensize(10)
zelva.color("black")
zelva.speed(0)

def ctverec():
    for _ in range(4):
        zelva.forward(50)
        zelva.right(90)

# Vytvoření želvy pro psaní textu (symbolů)
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.pensize(5)
text.color("black")
text.speed(0)  # Nastavíme maximální rychlost

# Startovní pozice pro sloty
start_x = -60
start_y = 0

# Funkce pro zobrazení výsledku (výhra/prohra)
def zobraz_vysledek(vyhra):
    text.goto(0, -100)
    time.sleep(1)  # Pauza před zobrazením výsledku
    text.clear()  # Smaže předchozí výsledek
    if vyhra:
        text.write("Výhra! 🎉", align="center", font=("Arial", 24, "bold"))
    else:
        text.write("Prohra! 😔", align="center", font=("Arial", 24, "bold"))

# Funkce pro točení slotů
def tocení():
    symboly_na_slotu = []
    
    # Skryjeme želvy před kreslením
    zelva.hideturtle()
    text.hideturtle()
    
    for i in range(3):
        zelva.penup()
        zelva.goto(start_x + i * 60, start_y)
        zelva.setheading(0)
        zelva.pendown()
        ctverec()  # Kreslíme čtverce pro sloty

        # Výběr a zobrazení náhodného symbolu
        symbol = random.choice(symboly)
        symboly_na_slotu.append(symbol)
        text.penup()
        text.goto(start_x + i * 60 + 10, start_y - 35)  # Pozice do středu čtverce
        text.write(symbol, font=("Arial", 20, "normal"))
        
    # Zobrazíme výsledek (s výhrami/prohrami) po chvíli
    text.showturtle()  # Zobrazíme textovou želvu
    # Kontrola výhry
    if symboly_na_slotu[0] == symboly_na_slotu[1] == symboly_na_slotu[2]:
        zobraz_vysledek(True)
        return vyhry[symboly_na_slotu[0]]  # Vrátí hodnotu výhry podle symbolu
    else:
        zobraz_vysledek(False)
        return 0  # Pokud není výhra, vracíme 0

# Funkce pro zahájení hry s kredity
def hrat():
    text.hideturtle()  # Skryje textovou želvu
    zelva.hideturtle()  # Skryje kreslící želvu
    okno.reset()
    kredity = 150  # Začáteční kredity
    print(f"Počet kreditů: {kredity}")
    
    while kredity > 0:
        # Uživatelský vstup pro zahájení točení
        print(f"\nPočet kreditů: {kredity}")
        volba = input("Chceš točit? (ano/ne): ").lower()
        
        if volba in ["ano", "a", "jj", "jo"]:
            kredity -= 10  # Každé točení stojí 10 kreditů
            print(f"Točíme... Zbývá kreditů: {kredity}")
            
            vyhra = tocení()  # Zavolání funkce pro točení
            
            if vyhra > 0:
                kredity += vyhra  # Pokud vyhraje, přičteme výhru
            else:
                print(f"Zbývá kreditů: {kredity}")
            
        elif volba in ["ne", "n", "nn"]:
            print("Díky za hru! 👋")
            break
            time.sleep(2)
            okno.bye()  # Ukončí okno hry
        else:
            print("Neplatná volba. Zadej 'ano' nebo 'ne'.")

# Spuštění hry
hrat()