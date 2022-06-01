"""
Import gspread so that we can work with google API
"""
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("MySubMyWay")

sandwich = SHEET.worksheet("Sheet1")
sandwich_list = sandwich.col_values(3)[1:]  # List of Sandwiches in spreadsheet
bread_list = sandwich.col_values(2)[1:]  # List of Breads in spreadsheet
cheese_list = sandwich.col_values(4)[1:]  # List of Cheese in spreadsheet
salad_list = sandwich.col_values(5)[1:]  # List of Salads in spreadsheet
sauce_list = sandwich.col_values(6)[1:]  # List of Sauces in spreadsheet


customer = SHEET.worksheet("customer")
# print(customer.get_all_values())

# Rcords all the input by customers in this list
customer_details = []

while True:
    name = input("\nPlease enter your last name: ").capitalize()
    if not name.isalpha():
        print(f"{name} is not a valid name. Please enter a valid name")
        continue
    else:
        print(f"\nWelcome to My-Sub My-Way {name}")
        customer_details.append(name)
    break

prices = []


def food_price():
    """
    Calculates the food of the price depending on footlong
    or six inch
    """
    for price in prices:
        return int(price)


def sandwich_size():
    """
    Describes the size of the sandwich
    """
    while True:
        sub = input("\nWhat would you like to have today? \
a) Footlong b) 6 Inch\n")
        if sub == "a":
            customer_details.append("Footlong")
            print("\nGreat choice, you chose Footlong\n")
            prices.append(9)
            # print("Here are your choices")
            break
        elif sub == "b":
            customer_details.append("6 Inch")
            print("\nGreat choice, you choose a Six Inch")
            prices.append(6)
            # print("\nHere are your choices")
            break
        else:
            print("Please type a or b")
            continue
    return sub


sandwich_size()


def bread_names():
    """
    Prints a list of bread list from the spreadsheet.
    """
    print("\nWhat bread would you like to have?")
    print("\nYour options are")
    time.sleep(1)  # sleep for 1 second
    bread_name = []
    for brd_name in bread_list:
        bread_name.append(brd_name)
    num = []
    for i in range(1, 5):
        num.append(i)

    names = dict(zip(num, bread_name))
    for number, bread in names.items():
        print(number, bread)
    return bread_name


bread_names()


def choose_bread():
    """
    User can choose a bread using the number from 1 to 4

    """
    print("\nPlease enter a number between 1 to 4")
    while True:
        brd = input("\nPlease Choose your Bread: ")
        if brd == "1":
            print(f"\nYou Chose {sandwich.col_values(2)[1]}, awesome!!")
            customer_details.append(sandwich.col_values(2)[1])
            break
        elif brd == "2":
            print(f"\nYou Chose {sandwich.col_values(2)[2]}, awesome!!")
            customer_details.append(sandwich.col_values(2)[2])
            break
        elif brd == "3":
            print(f"\nYou Chose {sandwich.col_values(2)[3]}, awesome!!")
            customer_details.append(sandwich.col_values(2)[3])
            break
        elif brd == "4":
            print(f"\nYou Chose {sandwich.col_values(2)[4]}, awesome!!")
            customer_details.append(sandwich.col_values(2)[4])
            break
        else:
            print("\nPlease type a number between 1 to 4.")
            continue
    return brd


choose_bread()


def sandwich_names():
    """
    A function to fetch all the name of sandwich from
    Google Sheet and print in the console.
    """
    print("\nWhat would you like in your sandwich?")
    sandwich_name = []
    for sand_name in sandwich_list:
        sandwich_name.append(sand_name)
    num = []
    for i in range(1, 7):
        num.append(i)
    time.sleep(1)

    names = dict(zip(num, sandwich_name))
    for key, value in names.items():
        print(key, value)
    return sandwich_name


sandwich_names()


def choose_sandwich():
    """
    A function where users can choose their sandwich,
    and the name of the sandwich is saved in google sheet
    in customer page.
    """
    print("\nPlease enter a number between 1 to 6 to select your sandwich")
    while True:
        choose = input("\nPlease choose your sandwich: ")
        if choose == "1":
            print(f"\nYou chose {sandwich.col_values(3)[1]}, awesome!!")
            customer_details.append(sandwich.col_values(3)[1])
            break
        elif choose == "2":
            print(f"\nYou chose {sandwich.col_values(3)[2]}, awesome!!")
            customer_details.append(sandwich.col_values(3)[2])
            break
        elif choose == "3":
            print(f"\nYou chose {sandwich.col_values(3)[3]}, awesome!!")
            customer_details.append(sandwich.col_values(3)[3])
            break
        elif choose == "4":
            print(f"\nYou chose {sandwich.col_values(3)[4]}, awesome!!")
            customer_details.append(sandwich.col_values(3)[4])
            break
        elif choose == "5":
            print(f"\nYou chose {sandwich.col_values(3)[5]}, awesome!!")
            customer_details.append(sandwich.col_values(3)[5])
            break
        elif choose == "6":
            print(f"\nYou chose {sandwich.col_values(3)[6]}, awesome!!")
            customer_details.append(sandwich.col_values(3)[6])
            break
        else:
            print("Please type a number between 1 to 6.")
            continue
    return choose


choose_sandwich()


def cheese_names():
    """
    Prints a list of cheese list from the spreadsheet.
    """
    print("\nWhat cheese would you like to have?")
    print("\nYour options are")
    time.sleep(1)  # sleep for 1 second
    cheese_name = []
    for chse_name in cheese_list:
        cheese_name.append(chse_name)
    num = []
    for i in range(1, 4):
        num.append(i)

    names = dict(zip(num, cheese_name))
    for numb, cheese in names.items():
        print(numb, cheese)
    return cheese_name


def select_cheese():
    """
    A function where user can select their cheese
    """
    while True:
        which_cheese = input("\nWhich cheese would you like to have? ")
        if which_cheese == "1":
            print(f"\nYou chose {sandwich.col_values(4)[1]} cheese,\
 great choice!!")
            customer_details.append(sandwich.col_values(4)[1])
            break
        elif which_cheese == "2":
            print(f"\nYou chose {sandwich.col_values(4)[2]} cheese,\
 great choice!!")
            customer_details.append(sandwich.col_values(4)[2])
            break
        elif which_cheese == "3":
            print(f"\nYou chose {sandwich.col_values(4)[3]} cheese,\
 great choice!!")
            customer_details.append(sandwich.col_values(4)[3])
            break
        else:
            print("\nPlease type between 1, 2 or 3")


def choose_cheese():
    """
    Returns list of cheese from spreadsheet
    if the user choses y
    """
    while True:
        cheese = input("\nWould you like to have cheese? y/n ")
        if cheese == "y":
            # Returns theese two function if users wants cheese
            return cheese_names(), select_cheese()
        elif cheese == "n":
            print("\nThank you")
            break
        else:
            print("\nPlease type 'y' or 'n' ")


choose_cheese()


def salad_names():
    """
    A function to fetch all the name of salads from
    Google Sheet and print in the console.
    """
    print("\nSalad selections are - ")
    salad_name = []
    for sld_name in salad_list:
        salad_name.append(sld_name)
    num = []
    for i in range(1, 7):
        num.append(i)
    time.sleep(1)
    # the variable names at bottim is assigned to the
    # function salad_names  so that it can be
    # accessed from other functions
    salad_names.names = dict(zip(num, salad_name))
    for num, salad in salad_names.names.items():
        print(num, salad)

    return salad_name


salad_names()


def get_salad_from_user():
    """
    Checks for the user input with the default salad list
    and returns the salad list.
    """
    while True:
        try:
            # accept input from user as list of items
            print("\nPlease type in the following format 123456,\
 without space between numbers")
            choose_salad = list(input("\nwhat salad would you like to have? "))

            # Sort out the list from low to high
            choose_salad.sort()

            # convert the list of items to integer
            selected_salad = [int(i) for i in choose_salad]

            # Restricts user from unlimited selction of salads
            if len(choose_salad) > 6:
                print("\nMaximum 6 Salads allowed")
                continue

            for get_salad_from_user.salads in selected_salad:
                if get_salad_from_user.salads in salad_names.names:
                    print(f"\nYou selected\
 {salad_names.names[get_salad_from_user.salads]}")
                else:
                    print(f"\nPlease Check your selection {choose_salad}\
 not all are on my list.")
                    # salad_names()
                    break

            if get_salad_from_user.salads in salad_names.names:
                break
            else:
                continue

        except ValueError:
            print(f"\nPlease type a number between 1 to 6\
to choose your salad.{choose_salad} is not valid.")


get_salad_from_user()


def sauce_names():
    """
    A function to fetch all the name of sauces from
    Google Sheet and print in the console.
    """
    print("\nSauce selections are - ")
    sauce_name = []
    for sce_name in sauce_list:
        sauce_name.append(sce_name)
    num = []
    for i in range(1, 7):
        num.append(i)
    time.sleep(1)
    # the variable "names" at bottom is assigned to the
    # function sauce_names  so that it can be
    # accessed from other functions
    sauce_names.names = dict(zip(num, sauce_name))
    for num, sauce in sauce_names.names.items():
        print(num, sauce)

    return sauce_name


sauce_names()


def get_sauce_from_user():
    """
    Checks for the user input with the default sauce list
    and returns the sauce list.
    """
    while True:
        print("\nPlease type in the following format 123456,\
without space between numbers")
        # accept input from user as list of items
        choose_sauce = list(input("\nwhat sauce would you like to have? "))
        # Sort out the list from low to high
        choose_sauce.sort()
        # convert the list of items to integer
        selected_sauce = [int(i) for i in choose_sauce]

        # the variable "sauce" is assigned to the
        # function get_sauce_from_user so that it can be
        # accessed from the while loop at the bottom

        for get_sauce_from_user.sauces in selected_sauce:
            if get_sauce_from_user.sauces in sauce_names.names:
                print(f"\nYou selected\
 {sauce_names.names[get_sauce_from_user.sauces]}")
            else:
                print("\nPlease type a number between 1 to 6\
 to choose your salad.")
                # salad_names()
        if get_sauce_from_user.sauces in sauce_names.names:
            break
        else:
            continue


get_sauce_from_user()


# Obtain the values from the last row of google sheet
cusomter_all_value = customer.get_all_values()
last_row_customer = cusomter_all_value[-1]

# Print the values from the last row of google sheet.
# This can be printed by calling the customer_details list.
# But i wanted to call it from API
print(f"\n{last_row_customer[0].upper()}, You ordered a {last_row_customer[1]}\
 {last_row_customer[2]} bread with {last_row_customer[3]}")

print("\nCalculating price...")
time.sleep(2)

print(f"\nPrice of Sub is €{food_price()}")


def discount_price():
    """
    Calculates 15% off to the price of either footlong
    or six inch if the customer wish to take the offer
    """
    while True:
        discount = input("\nI can see on my system, that you are eligible of '15%' discount.\
 Would you like to take that discount? \nType 'y' or 'n: ")
        if discount == "y":
            print("\nCalulating discounted price...")
            time.sleep(2)
            new_price = round(food_price() * 0.85, 2)
            print(f"€{new_price}")
            customer_details.append(new_price)
            break
        elif discount == "n":
            print(f"\nPrice of Sub is €{food_price()}")
            customer_details.append(food_price())
            break
        else:
            print("\nPlease type 'y" or 'n')


discount_price()


# Records all the details in customer_details list(created in line 26)
# and this list gets updated in the customer page of google sheet.
customer.append_row(customer_details)


print(f"\nThank you for visiting My-Sub My-Way {name}. Have a great day!!\n")
