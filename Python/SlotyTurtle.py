import turtle
import random
import time

# Nastavení obrazovky
okno = turtle.Screen()
okno.bgcolor("white")
okno.title("Výherní Automat 🎰")

# Seznam symbolů a výher
symboly = ["🍒", "🍋", "🔔", "💎", "🍀"]
vyhry = {
    "🍒": 25,
    "🍋": 50,
    "🔔": 75,
    "💎": 100,
    "🍀": 200
}

# Počáteční počet kreditů
kredity = 150

# Želvy
zelva = turtle.Turtle()
zelva.hideturtle()
zelva.pensize(10)
zelva.color("black")
zelva.speed(0)

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("black")
text.speed(0)

info = turtle.Turtle()
info.hideturtle()
info.penup()
info.color("blue")
info.speed(0)

# Startovní pozice pro sloty
start_x = -60
start_y = 0

# Funkce pro kreslení jednoho čtverce
def ctverec():
    for _ in range(4):
        zelva.forward(50)
        zelva.right(90)

# Aktualizace zobrazení kreditů
def zobraz_kredity():
    info.clear()
    info.goto(0, 120)
    info.write(f"Kredity: {kredity}", align="center", font=("Arial", 16, "bold"))

# Zobrazení výhry/prohry
def zobraz_vysledek(vyhra):
    text.goto(0, -100)
    time.sleep(1)
    text.clear()
    if vyhra > 0:
        text.write(f"Výhra! Vyhrál jsi {vyhra} kreditů 🎉", align="center", font=("Arial", 24, "bold"))
    else:
        text.write("Prohra! 😔", align="center", font=("Arial", 24, "bold"))

# Točení
def tocení():
    symboly_na_slotu = []
    text.clear()

    for i in range(3):
        zelva.penup()
        zelva.goto(start_x + i * 60, start_y)
        zelva.setheading(0)
        zelva.pendown()
        ctverec()

        symbol = random.choice(symboly)
        symboly_na_slotu.append(symbol)

        text.penup()
        text.goto(start_x + i * 60 + 10, start_y - 35)
        text.write(symbol, font=("Arial", 20, "normal"))

    if symboly_na_slotu[0] == symboly_na_slotu[1] == symboly_na_slotu[2]:
        vyhra = vyhry[symboly_na_slotu[0]]
        zobraz_vysledek(vyhra)
        return vyhra
    else:
        zobraz_vysledek(0)
        return 0

# Spustí točení
def spustit_toceni():
    global kredity
    if kredity < 10:
        text.goto(0, -160)
        text.write("Nemáš dost kreditů.", align="center", font=("Arial", 16, "bold"))
        time.sleep(2)
        text.clear()
        return

    kredity -= 10
    vyhra = tocení()
    kredity += vyhra
    zobraz_kredity()

# Ukončí hru a zobrazí kredit
def konec_hry():
    info.clear()
    text.clear()
    zelva.clear()
    text.goto(0, -30)
    text.write(f"Konec hry!\nMáš {kredity} kreditů 💰", align="center", font=("Arial", 20, "bold"))
    time.sleep(3)
    okno.bye()

# Nakreslí tlačítko TOČIT
def nakresli_tlacitko_tocit():
    tlac = turtle.Turtle()
    tlac.hideturtle()
    tlac.penup()
    tlac.goto(-70, -150)
    tlac.pendown()
    tlac.fillcolor("lightgreen")
    tlac.begin_fill()
    for _ in range(2):
        tlac.forward(140)
        tlac.left(90)
        tlac.forward(40)
        tlac.left(90)
    tlac.end_fill()
    tlac.penup()
    tlac.goto(0, -145)
    tlac.color("black")
    tlac.write("🎰 TOČIT 🎰", align="center", font=("Arial", 16, "bold"))

# Nakreslí tlačítko NECHCI TOČIT
def nakresli_tlacitko_konec():
    tlac = turtle.Turtle()
    tlac.hideturtle()
    tlac.penup()
    tlac.goto(-70, -210)
    tlac.pendown()
    tlac.fillcolor("salmon")
    tlac.begin_fill()
    for _ in range(2):
        tlac.forward(140)
        tlac.left(90)
        tlac.forward(40)
        tlac.left(90)
    tlac.end_fill()
    tlac.penup()
    tlac.goto(0, -205)
    tlac.color("black")
    tlac.write("NECHCI TOČIT", align="center", font=("Arial", 14, "bold"))

# Kliknutí myší
def klik(x, y):
    if -70 <= x <= 70 and -150 <= y <= -110:
        spustit_toceni()
    elif -70 <= x <= 70 and -210 <= y <= -170:
        konec_hry()

# Spuštění hry
nakresli_tlacitko_tocit()
nakresli_tlacitko_konec()
zobraz_kredity()
okno.onclick(klik)
okno.listen()
okno.mainloop()