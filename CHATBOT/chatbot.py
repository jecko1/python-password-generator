import datetime
from random import *
from termcolor import colored
import string
import sys
import time
import csv


def print_created_passwords(filename):
    fields = []
    rows = []
    with open(filename + ".csv", 'r') as csv_file:
        csvReader = csv.reader(csv_file)
        fields = next(csvReader)
        for row in csvReader:
            rows.append(row)
    print("Field Names:    %30s" % ("   |   ".join(field for field in fields)), "\n")
    for row in rows[:]:
        for col in row:
            print("%18s | " % col, end='')
        print("\n")


def create_user_pass():
    pas_gen = string.digits + string.punctuation + string.ascii_letters
    date_created = datetime.date
    pass_create = "".join(choice(pas_gen) for pass_gen in range(randint(8, 13)))
    return pass_create


def re_trail_pass_length():
    time.sleep(3)
    print("Wrong input format. Retrying...")
    time.sleep(6)
    question = input("Want to retry (y/n): ")
    time.sleep(3)
    if question == "y".lower():
        passwordT = int(input("Enter password length (8 - 13): "))
        username = input("Enter username: ")
        creation = datetime.date.today()
        account = input("Enter the account name(email, yahoo etc): ")
        password_length_verifier(passwordT, username, creation, account)
    elif question == "n".lower():
        time.sleep(2)
        view_recorded = input("VIEW RECORDED PASSWORDS?: ")
        if view_recorded == 'y':
            file_name = input("Enter file name: ")
            print_created_passwords(file_name)
        print(colored("SYSTEM GOING TO SLEEP...", 'blue'))
        time.sleep(3)
        sys.exit(0)
    else:
        time.sleep(2)
        print("[-]", end='')
        print(colored(" YOU ENTERED THE WRONG FORMAT!!! ", 'red'), end='')
        print("[-]")
        time.sleep(2)
        re_trail_pass_length()


def password_length_verifier(length, user, creation_date, acc):
    if 8 >= length <= 13:
        print(colored("[-] PASSWORD LENGTH BETWEEN 8 & 13!!! [-]", 'red'))
        re_trail_pass_length()
    else:
        time.sleep(3)
        print(colored("[+] GENERATED PASSWORD: ", 'green'), end='')
        print(colored(create_letters(), 'white'))

        def create_more():
            save_more = input("[+]" + colored(" GENERATE MORE PASSWORDS (y/n) ", 'green') + "[+]")
            if save_more == "y".lower():
                take_details()
            elif save_more == 'n'.lower():
                time.sleep(3)
                sys.exit(0)
            else:
                time.sleep(2)
                print("[-]" + colored("IMPROPER ENTRY. ABORTING THE SYSTEM", 'red') + "[-]")
            time.sleep(2)

        def save_record():
            save_detail = input("[+]" + colored(" SAVE DETAILS? ", 'blue') + "[+]: ")
            if save_detail == 'y'.lower():
                fields = ["USERNAME", "PASSWORD", "CREATION_DATE", "ACCOUNT"]
                rows = [
                    [user, create_letters(), creation_date, acc]
                ]
                with open('account_registry.csv', 'a') as csv_file:
                    fileWriter = csv.writer(csv_file)
                    fileWriter.writerow(fields)
                    fileWriter.writerows(rows)
                    time.sleep(2)
                print(colored("[+] DETAILED SUCCESSFULLY RECODED [+].", 'blue'))
                time.sleep(3)
                create_more()
            elif save_detail == 'n'.lower():
                print(colored("SYSTEM GOING TO SLEEP...", 'blue'))
                time.sleep(3)
                sys.exit(0)
            else:
                save_record()

        save_record()
        create_more()


def take_details():
    password = int(input("Enter password length (8 - 13): "))
    userName = input("Enter username: ")
    CREATION = datetime.date.today()
    Account = input("Enter the account name(email, yahoo etc): ")
    return password_length_verifier(password, userName, CREATION, Account)


take_details()
print(take_details())
