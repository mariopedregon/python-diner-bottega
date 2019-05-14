def main():
    totalCost = 0
    print('''
    "Welcome to the Bottega Diner , What can we get you started today!"
    ''')
    name = input("What is your name?")
    print("Hello " + name + "!")
    print('''
     You get one entree and two side choices at regular cost.
    ''')

    print('''
    Here is our menu!
    ''')

    mainMenu(totalCost)

def mainMenu(totalCost):
    print("1.Steak $13.99")
    print("2.Chicken $11.99")
    print("3.Ribs $15.99")
    selection = int(input("Enter Choice:"))
    print("\n")
    if selection  == 1:
        totalCost += Steak(totalCost)
        totalCost += sideMenu(totalCost)
        receipt = "your total is $" + str(totalCost)
        print(receipt)
    elif selection  == 2:
        totalCost += Chicken(totalCost)
        totalCost += sideMenu(totalCost)
        receipt = "your total is $" + str(totalCost)
        print(receipt)
    elif selection  == 3:
        totalCost += Ribs(totalCost)
        totalCost += sideMenu(totalCost)
        receipt = "your total is $" + str(totalCost)
        print(receipt)
    else:
        print("Invalid choice. enter 1-3")
        mainMenu()


def Steak(totalCost):
    print("Great choice!")
    totalCost += 8
 
    return totalCost


def Chicken(totalCost):
    print("Great choice!")
    totalCost += 7.5

    return totalCost


def Ribs(totalCost):
    print("Great Choice")
    totalCost += 6

    return totalCost


def sideMenu(totalCost):
    print("1.corn on the cob $10.50")
    print("2.house salad $7.50")
    print("3.Fries $3")
    selection = int(input("Enter Choice:"))
    if selection == 1:
        totalCost += corn(totalCost)
        return totalCost
    elif selection == 2:
        totalCost += house(totalCost)
        return totalCost
    elif selection == 3:
        totalCost += Drink(totalCost)
        return totalCost
    else:
        print("Invalid choice. enter 1-3")
        sideMenu()


def corn(totalCost):
    print("That'll be $10.50.")
    totalCost += 10.5
    
    return totalCost


def house(totalCost):
    print("That'll be $7.50")
    totalCost += 7.5

    return totalCost


def Drink(totalCost):
    print("Sweet!")
    totalCost += 3

    return totalCost
    receipt = "your total is $" + str(totalCost)

main()