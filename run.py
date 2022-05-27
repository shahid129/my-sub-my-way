"""
Import gspread so that we can work with google API
"""
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
sandwich_list = sandwich.col_values(2)[1:]  # List of Sandwiches in spreadsheet

customer = SHEET.worksheet("customer")
# print(customer.get_all_values())

customer_details = []

name = input("Please enter your name: ")
print(f"Welcome to Subway {name}")
customer_details.append(name)


def sandwich_size():
    """
    Describes the size of the sandwich
    """
    while True:
        sub = input("\nwhat would you like to have today: a) Footlong\
            b) 6 Inch\n")
        if sub == "a":
            customer_details.append("Footlong")
            print("great choice, you chose Footlong\n")
            print("here are your choices")
            break
        elif sub == "b":
            customer_details.append("6 Inch")
            print("you choose a six Inch")
            print("here are your choices")
            break
        else:
            print("Please type a or b")
            continue
    return sub


sandwich_size()
