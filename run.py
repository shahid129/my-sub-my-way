"""
Import gspread so that we can work with google API
"""
# import to exit or restart the program
import os
import sys

import time
import random
from datetime import date, datetime
import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from art import tprint

from colorama import Fore, Style

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

# Prints logo
tprint("\n\nMy-Sub My-Way\n\n", font="cybermedum")


def last_receipt():
    """
    A Fuuntion that seraches for customer details by their name in
    the customer spread sheet and fetches all the details
    about their last order.
    """
    table = PrettyTable()

    # finds the user name in the list. if there is multiple of
    # same name it fetches the last one from the list
    cell = customer.findall(name)[-1]
    values_list = customer.row_values(cell.row)

    while True:
        if name in values_list:
            latest_recipt = input(Fore.GREEN + "\n" + name + ", We found your details, \
would you like to view your last recept? Type 'y' or 'n': " + Style.RESET_ALL)
            if latest_recipt == "y":
                print("\nFetching your latest receipt...\n")
                time.sleep(2)
                table.field_names = (["My-Sub My-Way"])
                # getting all these details from spreadsheet.
                table.add_row([f"\nReciept Number: {values_list[8]}"])
                table.add_row([f"\nDate: {values_list[6]}"])
                table.add_row([f"\nTime: {values_list[7]}"])
                table.add_row(["\n------- ORDER DETAILS --------"])
                table.add_row([f"\nName: {values_list[0]}"])
                table.add_row([f"\nSize: {values_list[1].upper()}"])
                table.add_row([f"\nBread name: {values_list[2].upper()}"])
                table.add_row([f"\nSandwich Name: {values_list[3].upper()}"])
                table.add_row([f"\nPrice: €{values_list[5]}"])
                table.add_row([f"\n\nThank you for visiting My-Sub My-Way {values_list[0]}.\
        \nHave a great day!!"])
                print(table)
                time.sleep(1.5)
                print("\nWell, lets' take your order.")
                break
            elif latest_recipt == "n":
                time.sleep(1.5)
                print("\nPerfact, lets take your order")
                break
            else:
                print("\nPlease type 'y' or 'n'")
                continue
        else:
            break

# last_receipt()


# Rcords all the input by customers in this list
customer_details = []

while True:
    try:
        name = input(Fore.GREEN + "\nPlease enter your \
last name: " + Style.RESET_ALL).capitalize()
        if not name.isalpha():
            print(Fore.RED + f"{name} is not a valid name. Please enter \
a valid name" + Style.RESET_ALL)
            continue
        elif len(name) <= 2 or len(name) > 9:
            print(Fore.RED + f"Your name '{name}' should be more than 2 character or \
less than 9 character. Try again." + Style.RESET_ALL)
            continue
        else:
            customer_details.append(name)
            last_receipt()
            break
    except IndexError:
        print(f"\nWelcome to My-Sub My-Way {name}")
        break

prices = []


def food_price():
    """
    Calculates the food of the price depending on footlong
    or six inch
    """
    for price in prices:
        return float(round(price, 2))


def sandwich_size():
    """
    Describes the size of the sandwich
    """
    while True:
        sub = input(Fore.GREEN + "\nWhat would you like to have today? \
a) Footlong b) 6 Inch\n" + Style.RESET_ALL).lower()
        if sub == "a":
            customer_details.append("Footlong")
            print("\nGreat choice, you chose Footlong\n")
            prices.append(9.50)
            break
        elif sub == "b":
            customer_details.append("6 Inch")
            print("\nGreat choice, you choose a Six Inch")
            prices.append(6.50)
            break
        else:
            print(Fore.RED + "Please type a or b" + Style.RESET_ALL)
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

    # convert bread name and num to dict
    bread_names.names = dict(zip(num, bread_name))

    bread_table = PrettyTable()
    bread_table.field_names = num
    bread_table.add_row(bread_name)
    print(bread_table)
    return bread_name


bread_names()


def choose_bread():
    """
    User can choose a bread using the number from 1 to 4
    """
    while True:
        try:
            # accept input from user as list of items
            brd = list(input(Fore.GREEN + "\nWhat bread would \
you like to have? " + Style.RESET_ALL))

            # Sort out the list from low to high
            brd.sort()

            # convert the list of items to integer
            selected_bread = [int(i) for i in brd]

            # Restricts user from multiple inputs
            if len(brd) > 1:
                print("\nMaximum 1 bread is allowed")
                continue

            # the variable "brd" is assigned to the
            # function choose_bread so that it can be
            # accessed from the while loop at the bottom
            for choose_bread.brd in selected_bread:
                if choose_bread.brd in bread_names.names:
                    print(f"\nYou selected\
 {bread_names.names[choose_bread.brd]}")
                else:
                    print(f"\nPlease Check your selection {brd}\
 not all are on my list.")
                    break

            if choose_bread.brd in bread_names.names:
                customer_details.append(bread_names.names[choose_bread.brd])
                break
            else:
                continue

        except ValueError:
            print(Fore.RED + f"\nPlease type a number between 1 to 4\
to choose your bread. {brd} is not valid choice." + Style.RESET_ALL)
        except AttributeError:
            print(Fore.RED + "\nPlease type a number between \
                1 to 4" + Style.RESET_ALL)


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

    # convert sandwich name and num to dict
    sandwich_names.names = dict(zip(num, sandwich_name))

    sandwich_table = PrettyTable()
    sandwich_table.field_names = num
    sandwich_table.add_row(sandwich_name)
    print(sandwich_table)
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
        try:
            # accept input from user as list of items
            choose = list(input(Fore.GREEN + "\nWhat sandwich \
would you like to have? " + Style.RESET_ALL))

            # convert the list of items to integer
            selected_sandwich = [int(i) for i in choose]

            # Restricts user from multiple inputs
            if len(choose) > 1:
                print("\nOnly 1 type of sandwich is allowed")
                continue

            # the variable "choose" is assigned to the
            # function choose_sandwich so that it can be
            # accessed from the while loop at the bottom
            for choose_sandwich.choose in selected_sandwich:
                if choose_sandwich.choose in sandwich_names.names:
                    print(f"\nYou selected\
 {sandwich_names.names[choose_sandwich.choose]}")
                else:
                    print(f"\nPlease Check your selection. {choose}\
 not all are on my list.")
                    break

            if choose_sandwich.choose in sandwich_names.names:
                customer_details.\
                    append(sandwich_names.names[choose_sandwich.choose])
                break
            else:
                continue

        except ValueError:
            print(Fore.RED + f"\nPlease type a number between 1 to 6\
to choose your bread. {choose} is not valid choice." + Style.RESET_ALL)
        except AttributeError:
            print(Fore.RED + "\nPlease type a number \
between 1 to 6" + Style.RESET_ALL)

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

    # Convert num and cheese name to dict
    cheese_names.names = dict(zip(num, cheese_name))

    cheese_table = PrettyTable()
    cheese_table.field_names = num
    cheese_table.add_row(cheese_name)
    print(cheese_table)
    return cheese_name


def select_cheese():
    """
    A function where user can select their cheese
    """
    while True:
        try:
            # accept input from user as list of items
            which_cheese =\
                list(input(Fore.GREEN + "\nWhich cheese would \
you like to have? " + Style.RESET_ALL))

            # convert the list of items to integer
            selected_cheese = [int(i) for i in which_cheese]

            # Restricts user from multiple inputs
            if len(which_cheese) > 1:
                print("\nOnly one type of cheese is allowed")
                continue

            # the variable "which_cheeae" is assigned to the
            # function choose_cheese so that it can be
            # accessed from the while loop at the bottom
            for choose_cheese.which_cheese in selected_cheese:
                if choose_cheese.which_cheese in cheese_names.names:
                    print(f"\nYou selected\
 {cheese_names.names[choose_cheese.which_cheese]}")
                else:
                    print(f"\nPlease Check your selection {which_cheese}\
 not all are on my list.")
                    break

            if choose_cheese.which_cheese in cheese_names.names:
                customer_details.\
                    append(cheese_names.names[choose_cheese.which_cheese])
                break
            else:
                continue

        except ValueError:
            print(Fore.RED + f"\nPlease type a number between 1, 2 or 3 \
to choose cheese. {which_cheese} is not valid choice." + Style.RESET_ALL)
        except AttributeError:
            print(Fore.RED + "\nPlease type a number between\
1, 2 or 3" + Style.RESET_ALL)


def choose_cheese():
    """
    Returns list of cheese from spreadsheet
    if the user choses y
    """
    while True:
        cheese = input(Fore.GREEN + "\nWould you like \
to have cheese? y/n " + Style.RESET_ALL)
        if cheese == "y":

            # Returns theese two function if users wants cheese
            return cheese_names(), select_cheese()
        elif cheese == "n":
            print("\nThank you")
            customer_details.\
                append("No Cheese")
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

    # Convert num and salad name to dict
    salad_names.names = dict(zip(num, salad_name))

    salad_table = PrettyTable()
    salad_table.field_names = num
    salad_table.add_row(salad_name)
    print(salad_table)

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
            choose_salad = list(input(Fore.GREEN + "\nWhat salad would \
you like to have? " + Style.RESET_ALL))

            # Sort out the list from low to high
            choose_salad.sort()

            # convert the list of items to integer
            selected_salad = [int(i) for i in choose_salad]

            # Restricts user from unlimited selction of salads
            if len(choose_salad) > 6:
                print("\nMaximum 6 Salads allowed")
                continue

            # the variable salad is attached to the
            # function get_salad from user so that it can be
            # accessed from the while loop at the bottom
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
            print(Fore.RED + f"\nPlease type a number between 1 to 6 \
to choose your salad.{choose_salad} is not valid." + Style.RESET_ALL)
        except AttributeError:
            print(Fore.RED + "\nPlease type a number \
between 1 to 6" + Style.RESET_ALL)


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

    # Convert num and sauce name to dict
    sauce_names.names = dict(zip(num, sauce_name))
    sauce_table = PrettyTable()
    sauce_table.field_names = num
    sauce_table.add_row(sauce_name)
    print(sauce_table)

    return sauce_name


sauce_names()


def get_sauce_from_user():
    """
    Checks for the user input with the default sauce list
    and returns the sauce list.
    """
    while True:
        try:
            print("\nPlease type in the following format 123456, \
without space between numbers")

            # accept input from user as list of items
            choose_sauce = list(input(Fore.GREEN + "\nwhat sauce \
would you like to have? " + Style.RESET_ALL))

            # Sort out the list from low to high
            choose_sauce.sort()

            # convert the list of items to integer
            selected_sauce = [int(i) for i in choose_sauce]

            # Restricts user from unlimited selction of salads
            if len(choose_sauce) > 3:
                print("\nMaximum 3 Sauces allowed")
                continue

            # the variable "sauce" is assigned to the
            # function get_sauce_from_user so that it can be
            # accessed from the while loop at the bottom

            for get_sauce_from_user.sauces in selected_sauce:
                if get_sauce_from_user.sauces in sauce_names.names:
                    print(f"\nYou selected\
 {sauce_names.names[get_sauce_from_user.sauces]}")
                else:
                    print(f"\nPlease Check your selection {choose_sauce}\
 not all are on my list.")
                    break

            if get_sauce_from_user.sauces in sauce_names.names:
                break
            else:
                continue

        except ValueError:
            print(Fore.RED + f"\nPlease type a number between 1 to 6 \
to choose your salad.{choose_sauce} is not valid." + Style.RESET_ALL)
        except AttributeError:
            print(Fore.RED + "\nPlease type a number between \
1 to 6" + Style.RESET_ALL)


get_sauce_from_user()

time.sleep(1.5)

print("\nCalculating price...")
time.sleep(2)

print(f"\nPrice of Sub is €{food_price()}")


def discount_price():
    """
    Calculates 15% off to the price of either footlong
    or six inch if the customer wish to take the offer
    """
    while True:
        discount = input(Fore.GREEN + "\nI can see on my system, \
that you are eligible of '15%' discount. \
Would you like to take that discount? \nType 'y' or 'n: " + Style.RESET_ALL)
        if discount == "y":
            print("\nCalulating discounted price...")
            time.sleep(2)
            new_price = round(food_price() * 0.85, 2)
            print(f"\nDiscounted New Price is €{new_price}")
            customer_details.append(new_price)
            break
        elif discount == "n":
            print(f"\nPrice of Sub is €{food_price()}")
            customer_details.append(food_price())
            break
        else:
            print("\nPlease type 'y" or 'n')


discount_price()


# Date and time generated for reciept function
today = date.today()
customer_details.append(str(today))

now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
customer_details.append(dt_string)

random_num = random.randint(11, 99)
customer_details.append(random_num)

# Records all the details in customer_details list(created in line 26)
# and this list gets updated in the customer page of google sheet.
customer.append_row(customer_details)


# Obtain the values from the last row of google sheet
cusomter_all_value = customer.get_all_values()
last_row_customer = cusomter_all_value[-1]


def print_reciept():
    """
    Print the receipt from the user data that is saved
    in google sheet.
    """
    receipt_table = PrettyTable()
    print("\nPrinting Receipt\n")
    time.sleep(2)
    receipt_table.field_names = (["My-Sub My-Way"])

    # generate random reciipt number
    receipt_table.add_row([f"\nReciept Number: {random_num}"])

    # Add date and time
    receipt_table.add_row([f"\nDate: {today}"])
    receipt_table.add_row([f"\nTime: {dt_string}"])
    receipt_table.add_row(["\n------- ORDER DETAILS --------"])

    # Print the values from the last row of google sheet.
    # This can be printed by calling the customer_details list
    # (created in line 26).
    # But i wanted to call it from API
    receipt_table.add_row([f"\nName: {last_row_customer[0].upper()}"])
    receipt_table.add_row([f"\nSize: {last_row_customer[1].upper()}"])
    receipt_table.add_row([f"\nBread name: {last_row_customer[2].upper()}"])
    receipt_table.add_row([f"\nSandwich Name: {last_row_customer[3].upper()}"])
    receipt_table.add_row([f"\nPrice: €{last_row_customer[5]}"])
    receipt_table.add_row([f"\n\nThank you for visiting My-Sub My-Way {name}.\
 \nHave a great day!!"])

    print(receipt_table)


print_reciept()


# this block of code is taken from stackoverflow
# Restart the whole program if the user selects y

def restart():
    """
    Restart the whole program if the user selects y
    or ends the code if anthing else is pressed
    """
    while True:
        order_again = input(Fore.GREEN + "\nWould you like to order another \
sandwich? 'y' or 'n': " + Style.RESET_ALL)

        if order_again == "y":
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        elif order_again == "n":
            print(f"\n\nThank you {name}, have a lovely day! Bye...\n\n")
            sys.exit(0)
        else:
            print("\nPlease type 'y' or 'n' ")


restart()
