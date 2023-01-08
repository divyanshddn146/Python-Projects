# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
print("We have following Pizzas in our Veg Section listed below:")
print("1)FARMHOUSE PIZZA:A pizza that goes ballistic on veggies! Check out this mouth watering overload of crunchy, crisp capsicum, succulent mushrooms and fresh tomatoes \n2)PEPPY PANEER PIZZA:Chunky paneer with crisp capsicum and spicy red pepper - quite a mouthful!\n3)DELUX VEGGIE:For a vegetarian looking for a BIG treat that goes easy on the spices, this one's got it all.. The onions, the capsicum, those delectable mushrooms - with paneer and golden corn to top it all.\n4)VEGGIE PARADISE:Goldern Corn, Black Olives, Capsicum & Red Paprika\n5)CHEESE N CORN:Cheese I Golden Corn | Cheese n Corn Pizza")
piz=input("What pizza you have to order:")
piz=piz.lower()
size = input("What size pizza do you want? S, M, or L ")
size=size.upper()
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_pepperoni=add_pepperoni.upper()
extra_cheese = input("Do you want extra cheese? Y or N ")
extra_cheese=extra_cheese.upper()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if(piz=="farmhouse" or "peppy paneer" or "veggie paradise"):
    spizza=259
    lpizza=459
    mpizza=689
    if(size=="S"):
        if(add_pepperoni=="Y"):
            spizza+=60
        if(extra_cheese=="Y"):
            spizza+=75
        print(f"Your final bill is: ${spizza}.")
    elif(size=="L"):
        if(add_pepperoni=="Y"):
            lpizza+=60
        if(extra_cheese=="Y"):
            lpizza+=75
        print(f"Your final bill is: ${lpizza}.")
    elif(size=="M"):
        if(add_pepperoni=="Y"):
            mpizza+=60
        if(extra_cheese=="Y"):
            mpizza+=75
    if(piz=="delux veggie"):
        spizza=299
        lpizza=549
        mpizza=799
        if(size=="S"):
            if(add_pepperoni=="Y"):
                spizza+=60
            if(extra_cheese=="Y"):
                spizza+=75
            print(f"Your final bill is: ${spizza}.")
        elif(size=="L"):
            if(add_pepperoni=="Y"):
                lpizza+=60
            if(extra_cheese=="Y"):
                lpizza+=75
            print(f"Your final bill is: ${lpizza}.")
        elif(size=="M"):
            if(add_pepperoni=="Y"):
                mpizza+=60
            if(extra_cheese=="Y"):
                mpizza+=75
    if(piz=="cheese n corn"):
        spizza=209
        lpizza=379
        mpizza=609
        if(size=="S"):
            if(add_pepperoni=="Y"):
                spizza+=60
            if(extra_cheese=="Y"):
                spizza+=75
            print(f"Your final bill is: ${spizza}.")
        elif(size=="L"):
            if(add_pepperoni=="Y"):
                lpizza+=60
            if(extra_cheese=="Y"):
                lpizza+=75
            print(f"Your final bill is: ${lpizza}.")
        elif(size=="M"):
            if(add_pepperoni=="Y"):
                mpizza+=60
            if(extra_cheese=="Y"):
                mpizza+=75
    
        print(f"Your final bill is: ${mpizza}.")
