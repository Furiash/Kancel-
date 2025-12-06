import random

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
print("The rules are simple: buy low, sell high, and try to make a profit!")
print("You buy special items for half, sell for double")
print("Put valid inputs or you will get punished! You will skip the turn if you don't.")
print("And remember, at the end of the day, you have to pay bills!")

def day():

    global money, iron, copper, titanium, gold, current_day, special_item
    
    print("Day", day)
    print("You have", money, "credits. ")
    print("You have", iron, "units of iron.")
    print("You have", copper, "units of copper.")
    print("You have", titanium, "units of titanium.")
    print("You have", gold, "units of gold.")
    
    Iron_exchange_rate = random.uniform(0.75, 1.25) * iron_base_value
    Copper_exchange_rate = random.uniform(0.75, 1.25) * copper_base_value
    Titanium_exchange_rate = random.uniform(0.75, 1.25) * titanium_base_value
    Gold_exchange_rate = random.uniform(0.75, 1.25) * gold_base_value

    print("Today´s iron value is", Iron_exchange_rate)
    print("Today´s copper value is", Copper_exchange_rate)
    print("Today´s titanium value is", Titanium_exchange_rate)
    print("Today´s gold value is", Gold_exchange_rate)
    special_item = random.choice(["iron", "copper", "titanium", "gold"])
    print("Today's special item is", special_item)

    input_a = input("Do you want to buy or sell? (buy/sell) ").lower()

    if input_a == "buy":
        input_b = input("What do you want to buy (iron/copper/titanium/gold) ").lower()
        if input_b == "iron":
            try:
                input_c = int(input("how much "))
            except ValueError:
                print("Please enter a valid number next time")
                return
            
            price = Iron_exchange_rate
            if input_b == special_item:
                price = price / 2
                
            if money < input_c * price:
                print("You don't have enough money to buy that much iron.")
                return
            else:
                money -= input_c * price
                iron += input_c

        elif input_b == "copper":
            try:
                input_c = int(input("how much "))
            except ValueError:
                print("Please enter a valid number next time")
                return
            price = Copper_exchange_rate
            if input_b == special_item:
                price = price / 2
                
            if money < input_c * price:
                print("You don't have enough money to buy that much copper.")
                return
            else:
                money -= input_c * price
                copper += input_c

        elif input_b == "titanium":
            try:
                input_c = int(input("how much "))
            except ValueError:
                print("Please enter a valid number next time")
                return

            price = Titanium_exchange_rate
            if input_b == special_item:
                price = price / 2
            
            if money < input_c * price:
                print("You don't have enough money to buy that much titanium.")
                return
            else:
                money -= input_c * price
                titanium += input_c

        elif input_b == "gold":
            try:
                input_c = int(input("how much "))
            except ValueError:
                print("Please enter a valid number next time")
                return
            
            price = Gold_exchange_rate
            if input_b == special_item:
                price = price / 2
            
            if money < input_c * price:
                print("You don't have enough money to buy that much gold.")
                return
            else:
                money -= input_c * price
                gold += input_c

        else:
            print("Invalid input. Please choose iron, copper, titanium, or gold next time.")
            return
        
    elif input_a == "sell":
        input_b = input("What do you want to sell (iron/copper/titanium/gold) ").lower()

        if input_b == "iron":
            try:
                input_c = int(input("how much "))
            except ValueError:
                print("Please enter a valid number next time")
                return
            
            price = Iron_exchange_rate
            if input_b == special_item:
                price = price * 2

            if input_c > iron:
                print("You don't have enough iron to sell that much.")
                return
            else:
                money += input_c * price
                iron -= input_c

        elif input_b == "copper":
            try:
                input_c = int(input("how much "))
            except ValueError:
                print("Please enter a valid number next time")
                return
            
            price = Copper_exchange_rate
            if input_b == special_item:
                price = price * 2
                
            if input_c > copper:
                print("You don't have enough copper to sell that much.")
                return
            else:
                money += input_c * price
                copper -= input_c

        elif input_b == "titanium":
            try:
                input_c = int(input("how much "))
            except ValueError:
                print("Please enter a valid number next time")
                return
            
            price = Titanium_exchange_rate
            if input_b == special_item:
                price = price * 2
            
            if input_c > titanium:
                print("You don't have enough titanium to sell that much.")
                return
            else:
                money += input_c * price
                titanium -= input_c

        elif input_b == "gold":
            try:
                input_c = int(input("how much "))
            except ValueError:
                print("Please enter a valid number next time")
                return
            
            price = Gold_exchange_rate
            if input_b == special_item:
                price = price * 2
            
            if input_c > gold:
                print("You don't have enough gold to sell that much.")
                return
            else:
                money += input_c * price
                gold -= input_c

        else:
            print("Invalid input. Please choose iron, copper, titanium, or gold next time.")
            return

    else:
        print("Invalid input. Please choose 'buy' or 'sell' next time.")
        return
    
    current_day = current_day + 1
    input_bills = input("Do you want to pay your bills? (yes/no) ").lower()
    if input_bills == "yes":
        money = money - 100

    elif input_bills == "no":
        print("Your problem, you have to pay")
        money = money - 100
    else:
        print("I don´t know what you mean, but you still pay")
        money = money - 100



while True:
    day()