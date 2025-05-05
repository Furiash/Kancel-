import turtle
import random
import time
import pygame  # ← zvuková knihovna
je_toceni = False

# --- Inicializace pygame pro zvuky ---
pygame.mixer.init()

# --- Načti zvuky ---
pygame.mixer.music.load("background_music.mp3")  # Hudba na pozadí
vyhra_zvuk = pygame.mixer.Sound("vyhra.mp3")
prohra_zvuk = pygame.mixer.Sound("prohra.mp3")

# Spusť hudbu na pozadí v nekonečné smyčce
pygame.mixer.music.play(-1)  # -1 = stále dokola

# Nastav hlasitost hudby
pygame.mixer.music.set_volume(0.3)  # Hlasitost 30%
vyhra_zvuk.set_volume(0.9)  # Hlasitost 90%
prohra_zvuk.set_volume(0.4)  # Hlasitost 40%

# --- Nastavení obrazovky ---
okno = turtle.Screen()
okno.bgcolor("white")
okno.title("Výherní Automat 🎰")

symboly = ["🍒", "🍋", "🔔", "💎", "🍀"]
vyhry = {
    "🍒": 25,
    "🍋": 50,
    "🔔": 75,
    "💎": 100,
    "🍀": 200
}

kredity = 150

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

start_x = -160
start_y = 0

def ctverec():
    for _ in range(4):
        zelva.forward(100)
        zelva.right(90)

def zobraz_kredity():
    info.clear()
    info.goto(0, 80)
    info.write(f"Kredity: {kredity}", align="center", font=("Arial", 32, "bold"))

def zobraz_vysledek(vyhra):
    text.goto(35, 0)
    time.sleep(0.7)  # ← pauza před zobrazením výsledku
    text.clear()
    if vyhra:
        text.write(f"Výhra! Vyhrál jsi {vyhra} kreditů 🎉", align="center", font=("Arial", 48, "bold"))
        vyhra_zvuk.play()  # ← zvuk výhry
    else:
        text.write("Prohra! 😔", align="center", font=("Arial", 48, "bold"))
        prohra_zvuk.play()  # ← zvuk prohry
def tocení():
    symboly_na_slotu = []
    text.clear()

    for i in range(3):
        zelva.penup()
        zelva.goto(start_x + i * 120, start_y)
        zelva.setheading(0)
        zelva.pendown()
        ctverec()

        symbol = random.choice(symboly)
        symboly_na_slotu.append(symbol)

        text.penup()
        text.goto(start_x + i * 120 + 20, start_y - 60)
        text.write(symbol, font=("Arial", 40, "normal"))

    if symboly_na_slotu[0] == symboly_na_slotu[1] == symboly_na_slotu[2]:
        zobraz_vysledek(vyhry[symboly_na_slotu[0]])
        return vyhry[symboly_na_slotu[0]]
    else:
        zobraz_vysledek(False)
        return 0

def spustit_toceni():
    global kredity, je_toceni
    if je_toceni:
        return
    if kredity < 10:
        text.goto(0, -320)
        text.write("Nemáš dost kreditů.", align="center", font=("Arial", 32, "bold"))
        return
    je_toceni = True
    kredity -= 10
    vyhra = tocení()
    kredity += vyhra
    zobraz_kredity()
    je_toceni = False

def konec_hry():
    info.clear()
    text.clear()
    zelva.clear()
    text.goto(0, -60)
    text.write(f"Konec hry!\nMáš {kredity} kreditů 💰", align="center", font=("Arial", 40, "bold"))
    time.sleep(3)
    pygame.mixer.music.stop()  # ← vypne hudbu
    okno.bye()

def nakresli_tlacitko_tocit():
    tlac = turtle.Turtle()
    tlac.hideturtle()
    tlac.penup()
    tlac.goto(-140, -240)
    tlac.pendown()
    tlac.fillcolor("lightgreen")
    tlac.begin_fill()
    for _ in range(2):
        tlac.forward(280)
        tlac.left(90)
        tlac.forward(80)
        tlac.left(90)
    tlac.end_fill()
    tlac.penup()
    tlac.goto(0, -220)
    tlac.color("black")
    tlac.write("🎰 TOČIT 🎰", align="center", font=("Arial", 32, "bold"))

def nakresli_tlacitko_konec():
    tlac = turtle.Turtle()
    tlac.hideturtle()
    tlac.penup()
    tlac.goto(-140, -350)
    tlac.pendown()
    tlac.fillcolor("salmon")
    tlac.begin_fill()
    for _ in range(2):
        tlac.forward(280)
        tlac.left(90)
        tlac.forward(80)
        tlac.left(90)
    tlac.end_fill()
    tlac.penup()
    tlac.goto(0, -340)
    tlac.color("black")
    tlac.write("NECHCI TOČIT", align="center", font=("Arial", 28, "bold"))

def klik(x, y):
    if -140 <= x <= 140 and -225 <= y <= -145:
        spustit_toceni()
    elif -140 <= x <= 140 and -350 <= y <= -270:
        konec_hry()

# Spuštění hry
nakresli_tlacitko_tocit()
nakresli_tlacitko_konec()
zobraz_kredity()
okno.onclick(klik)
okno.listen()
okno.mainloop()