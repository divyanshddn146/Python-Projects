print("Welcome to Python Pizza Deliveries!")
k=input("What will be your pizza choice veg(v) or non-veg(n):")
l=k.lower()
print()
if(l=="veg"or l=="v"):
    print("We have following Pizzas in our Veg Section listed below:")
    print("1)FARMHOUSE PIZZA:A pizza that goes ballistic on veggies! Check out this mouth watering overload of crunchy, crisp capsicum, succulent mushrooms and fresh tomatoes \n2)PEPPY PANEER PIZZA:Chunky paneer with crisp capsicum and spicy red pepper - quite a mouthful!\n3)DELUX VEGGIE:For a vegetarian looking for a BIG treat that goes easy on the spices, this one's got it all.. The onions, the capsicum, those delectable mushrooms - with paneer and golden corn to top it all.\n4)VEGGIE PARADISE:Goldern Corn, Black Olives, Capsicum & Red Paprika\n5)CHEESE N CORN:Cheese I Golden Corn | Cheese n Corn Pizza(enter the number)")
if(l=="non-veg" or l=="n"):
    print("We have following Pizzas in our Non-veg Section listed below:")
    print("1)NON VEG SUPREME:Bite into supreme delight of Black Olives, Onions, Grilled Mushrooms, Pepper BBQ Chicken, Peri-Peri Chicken, Grilled Chicken Rashers\n2)CHICKEN GOLDEN DELIGHT:Barbeque chicken with a topping of golden corn loaded with extra cheese. Worth its weight in gold!\n3)CHICKEN DOMINATOR:Treat your taste buds with Double Pepper Barbecue Chicken, Peri-Peri Chicken, Chicken Tikka & Grilled Chicken Rashers(enter the number)")
    
piz=input("What pizza you have to order:")
piz=piz.lower()
size = input("What size pizza do you want? S, M, or L ")
size=size.upper()
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_pepperoni=add_pepperoni.upper()
extra_cheese = input("Do you want extra cheese? Y or N ")
extra_cheese=extra_cheese.upper()
if(l=="v"):
    if((piz=="1" or piz=="3" or piz=="4")):
        spizza=259
        lpizza=689
        mpizza=459
        if(size=="S"):
            if(add_pepperoni=="Y"):
                spizza+=60
            if(extra_cheese=="Y"):
                spizza+=75
            print(f"Your final bill is: Rs{spizza}.")
        elif(size=="L"):
            if(add_pepperoni=="Y"):
                lpizza+=60
            if(extra_cheese=="Y"):
                lpizza+=75
            print(f"Your final bill is: Rs{lpizza}.")
        elif(size=="M"):
            if(add_pepperoni=="Y"):
                mpizza+=60
            if(extra_cheese=="Y"):
                mpizza+=75
            print(f"Your final bill is: Rs{mpizza}.")
    elif(piz=="5" or "2"):
        spizza=209
        lpizza=609
        mpizza=379
        if(size=="S"):
            if(add_pepperoni=="Y"):
                spizza+=60
            if(extra_cheese=="Y"):
                spizza+=75
            print(f"Your final bill is: Rs{spizza}.")
        elif(size=="L"):
            if(add_pepperoni=="Y"):
                lpizza+=60
            if(extra_cheese=="Y"):
                lpizza+=75
            print(f"Your final bill is: Rs{lpizza}.")
        elif(size=="M"):
            if(add_pepperoni=="Y"):
                mpizza+=60
            if(extra_cheese=="Y"):
                mpizza+=75
            print(f"Your final bill is: Rs{mpizza}.")
if(l=="n"):
    if(piz=="3" or piz=="1"):
        spizza=359
        lpizza=919
        mpizza=599
        if(size=="S"):
            if(add_pepperoni=="Y"):
                spizza+=60
            if(extra_cheese=="Y"):
                spizza+=75
            print(f"Your final bill is: Rs{spizza}.")
        elif(size=="L"):
            if(add_pepperoni=="Y"):
                lpizza+=60
            if(extra_cheese=="Y"):
                lpizza+=75
            print(f"Your final bill is: Rs{lpizza}.")
        elif(size=="M"):
            if(add_pepperoni=="Y"):
                mpizza+=60
            if(extra_cheese=="Y"):
                mpizza+=75
            print(f"Your final bill is: Rs{mpizza}.")
    elif(piz=="2"):
        spizza=309
        lpizza=829
        mpizza=559
        if(size=="S"):
            if(add_pepperoni=="Y"):
                spizza+=60
            if(extra_cheese=="Y"):
                spizza+=75
            print(f"Your final bill is: Rs{spizza}.")
        elif(size=="L"):
            if(add_pepperoni=="Y"):
                lpizza+=60
            if(extra_cheese=="Y"):
                lpizza+=75
            print(f"Your final bill is: Rs{lpizza}.")
        elif(size=="M"):
            if(add_pepperoni=="Y"):
                mpizza+=60
            if(extra_cheese=="Y"):
                mpizza+=75
            print(f"Your final bill is: Rs{mpizza}.")
    