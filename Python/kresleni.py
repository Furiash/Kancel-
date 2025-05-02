import turtle

# Vytvoření kreslícího plátna
okno = turtle.Screen()
okno.bgcolor("black")

# Vytvoření želvy
zelva = turtle.Turtle()
zelva.pensize(10)
zelva.color("white")

def ctverec():
    for _ in range(4):
        zelva.forward(100)
        zelva.right(90)
def trojuhelnik():
    for _ in range(3):
        zelva.forward(100)
        zelva.right(120)
def kruh():
    zelva.circle(50)

try:
    tvar = int(input("Zadej tvar (1 = čtverec, 2 = trojúhelník, 3 = kruh): "))
except ValueError:
    print("Neplatný vstup, nastavím čtverec.")
    exit()

if tvar not in [1, 2, 3]:
    print("Neplatný tvar.")
    exit()

if tvar == 1:
    ctverec()
elif tvar == 2:
    trojuhelnik()
else:
    kruh()
    
okno.mainloop()  # Udržuje okno otevřené