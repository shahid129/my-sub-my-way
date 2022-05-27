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


customer = SHEET.worksheet("customer")
# print(customer.get_all_values())

# Rcords all the input by customers in this list
customer_details = []

name = input("Please enter your name: ")
print(f"Welcome to Subway {name}")
customer_details.append(name)


def sandwich_size():
    """
    Describes the size of the sandwich
    """
    while True:
        sub = input("\nWhat would you like to have today: \
            a) Footlong b) 6 Inch\n")
        if sub == "a":
            customer_details.append("Footlong")
            print("\nGreat choice, you chose Footlong\n")
            print("Here are your choices")
            break
        elif sub == "b":
            customer_details.append("6 Inch")
            print("\nGreat choice, you choose a Six Inch")
            print("\nHere are your choices")
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


def sandwich_names():
    """
    A function to fetch all the name of sandwich from
    Google Sheet and print in the console.
    """
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


# Records all the details in customer_details list(created in line 26)
# and this list gets updated in the customer page of google sheet.
customer.append_row(customer_details)


# Obtain the values from the last row of google sheet
cusomter_all_value = customer.get_all_values()
last_row_customer = cusomter_all_value[-1]

# Print the values from the last row of google sheet.
# This can be printed by calling the customer_details list.
# But i wanted to call it from API
print(f"\n{last_row_customer[0].upper()}, You ordered a {last_row_customer[1]}\
 {last_row_customer[2]}")
