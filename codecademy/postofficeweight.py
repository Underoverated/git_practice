def ground(weight):
    flat_charge = 20.00
    if weight <= 2:
        cost = (weight*1.50) + flat_charge
        return cost
    elif weight > 2 and weight <= 6:
        cost = weight * 3.00 + flat_charge
        return cost
    elif weight > 6 and weight <= 10:
        cost = weight * 4.00 + flat_charge
        return cost
    elif weight > 10:
        cost = weight * 4.75 + flat_charge
        return cost

def drone(weight):
    flat_charge = 0
    if weight <= 2:
        cost = (weight*4.50) + flat_charge
        return cost
    elif weight > 2 and weight <= 6:
        cost = weight * 9.00 + flat_charge
        return cost
    elif weight > 6 and weight <= 10:
        cost = weight * 12.00 + flat_charge
        return cost
    elif weight > 10:
        cost = weight * 14.25 + flat_charge
        return cost
def best_price(prem_ground,ground_price,drone_price):
    if prem_ground < ground_price and prem_ground < drone_price:
        print("Your best price is Premium Ground")
        return("Your price is:", prem_ground)
    elif ground_price < drone_price and ground_price < prem_ground:
        print("Your best price is Standard Ground")
        return("Your price is:", ground_price)
    elif drone_price < prem_ground and drone_price < ground_price:
        print("Your best price is Drone Shipping")
        return("Your price is:", drone_price)
    else:
        return("You have two that are equal")

weight = input("What is the weight of your package: ")
weight = float(weight)
prem_ground = 125.00
ground_price = (ground(weight))
drone_price = (drone(weight))
print ("Premium Ground:", prem_ground)
print("Standard Ground:", ground_price)
print("Drone Shipping:", drone_price)
print("")
print(best_price(prem_ground,ground_price,drone_price))
