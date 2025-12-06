import random
import time

current_day = 0
money = 1000
iron = 5
iron_base_value = 70
copper = 8
copper_base_value = 50
titanium = 10
titanium_base_value = 40
gold = 3
gold_base_value = 100
special_item = None

print("Welcome to Space Trader!")
time.sleep(2)
print("The rules are simple: buy low, sell high, and try to make a profit!")
time.sleep(2)
print("You buy special items for half, sell for double")
time.sleep(2)
print("Put valid inputs or you will get punished! You will skip the turn if you don't.")
time.sleep(2)
print("And remember, at the end of the day, you have to pay bills!")
time.sleep(2)

def day():

    

    global money, iron, copper, titanium, gold, current_day, special_item

    if money <= 0:
        print("You have run out of money! Game over.")
        exit()
    
    print("Day", current_day)
    time.sleep(2)
    print("You have", money, "credits. ")
    time.sleep(2)
    print("You have", iron, "units of iron.")
    time.sleep(2)
    print("You have", copper, "units of copper.")
    time.sleep(2)
    print("You have", titanium, "units of titanium.")
    time.sleep(2)
    print("You have", gold, "units of gold.")
    time.sleep(2)
    
    Iron_exchange_rate = round(random.uniform(0.75, 1.25) * iron_base_value)
    Copper_exchange_rate = round(random.uniform(0.75, 1.25) * copper_base_value)
    Titanium_exchange_rate = round(random.uniform(0.75, 1.25) * titanium_base_value)
    Gold_exchange_rate = round(random.uniform(0.75, 1.25) * gold_base_value)

    print("Today´s iron value is", Iron_exchange_rate)
    time.sleep(2)
    print("Today´s copper value is", Copper_exchange_rate)
    time.sleep(2)
    print("Today´s titanium value is", Titanium_exchange_rate)
    time.sleep(2)
    print("Today´s gold value is", Gold_exchange_rate)
    time.sleep(2)
    special_item = random.choice(["iron", "copper", "titanium", "gold"])
    print("Today's special item is", special_item)
    time.sleep(2)

    input_a = input("Do you want to buy or sell? (buy/sell) ").lower()
    time.sleep(2)

    if input_a == "buy":
        input_b = input("What do you want to buy (iron/copper/titanium/gold) ").lower()
        time.sleep(2)
        if input_b == "iron":
            try:
                input_c = int(input("how much "))
                time.sleep(2)
            except ValueError:
                print("Please enter a valid number next time")
                return
            
            price = Iron_exchange_rate
            if input_b == special_item:
                price = price / 2
                
            if money < input_c * price:
                print("You don't have enough money to buy that much iron.")
                time.sleep(2)
                return
            else:
                money -= input_c * price
                iron += input_c

        elif input_b == "copper":
            try:
                input_c = int(input("how much "))
                time.sleep(2)
            except ValueError:
                print("Please enter a valid number next time")
                time.sleep(2)
                return
            price = Copper_exchange_rate
            if input_b == special_item:
                price = price / 2
                
            if money < input_c * price:
                print("You don't have enough money to buy that much copper.")
                time.sleep(2)
                return
            else:
                money -= input_c * price
                copper += input_c

        elif input_b == "titanium":
            try:
                input_c = int(input("how much "))
                time.sleep(2)
            except ValueError:
                print("Please enter a valid number next time")
                time.sleep(2)
                return

            price = Titanium_exchange_rate
            if input_b == special_item:
                price = price / 2
            
            if money < input_c * price:
                print("You don't have enough money to buy that much titanium.")
                time.sleep(2)
                return
            else:
                money -= input_c * price
                titanium += input_c

        elif input_b == "gold":
            try:
                input_c = int(input("how much "))
                time.sleep(2)
            except ValueError:
                print("Please enter a valid number next time")
                time.sleep(2)
                return
            
            price = Gold_exchange_rate
            if input_b == special_item:
                price = price / 2
            
            if money < input_c * price:
                print("You don't have enough money to buy that much gold.")
                time.sleep(2)
                return
            else:
                money -= input_c * price
                gold += input_c

        else:
            print("Invalid input. Please choose iron, copper, titanium, or gold next time.")
            time.sleep(2)
            return
        
    elif input_a == "sell":
        input_b = input("What do you want to sell (iron/copper/titanium/gold) ").lower()
        time.sleep(2)

        if input_b == "iron":
            try:
                input_c = int(input("how much "))
                time.sleep(2)
            except ValueError:
                print("Please enter a valid number next time")
                time.sleep(2)
                return
            
            price = Iron_exchange_rate
            if input_b == special_item:
                price = price * 2

            if input_c > iron:
                print("You don't have enough iron to sell that much.")
                time.sleep(2)
                return
            else:
                money += input_c * price
                iron -= input_c

        elif input_b == "copper":
            try:
                input_c = int(input("how much "))
                time.sleep(2)
            except ValueError:
                print("Please enter a valid number next time")
                time.sleep(2)
                return
            
            price = Copper_exchange_rate
            if input_b == special_item:
                price = price * 2
                
            if input_c > copper:
                print("You don't have enough copper to sell that much.")
                time.sleep(2)
                return
            else:
                money += input_c * price
                copper -= input_c

        elif input_b == "titanium":
            try:
                input_c = int(input("how much "))
                time.sleep(2)
            except ValueError:
                print("Please enter a valid number next time")
                time.sleep(2)
                return
            
            price = Titanium_exchange_rate
            if input_b == special_item:
                price = price * 2
            
            if input_c > titanium:
                print("You don't have enough titanium to sell that much.")
                time.sleep(2)
                return
            else:
                money += input_c * price
                titanium -= input_c

        elif input_b == "gold":
            try:
                input_c = int(input("how much "))
                time.sleep(2)
            except ValueError:
                print("Please enter a valid number next time")
                time.sleep(2)
                return
            
            price = Gold_exchange_rate
            if input_b == special_item:
                price = price * 2
            
            if input_c > gold:
                print("You don't have enough gold to sell that much.")
                time.sleep(2)
                return
            else:
                money += input_c * price
                gold -= input_c

        else:
            print("Invalid input. Please choose iron, copper, titanium, or gold next time.")
            time.sleep(2)
            return

    else:
        print("Invalid input. Please choose 'buy' or 'sell' next time.")
        time.sleep(2)
        return
    
    current_day = current_day + 1



while True:
    day()
        input_bills = input("Do you want to pay your bills? (yes/no) ").lower()
    if input_bills == "yes":
        money = money - 100

    elif input_bills == "no":
        print("Your problem, you have to pay")
        money = money - 100
    else:
        print("I don´t know what you mean, but you still pay")
        money = money - 100