from colorama import Fore
import random
import string
import os

os.system("cls")
print(f"{Fore.MAGENTA}[{Fore.RESET}1{Fore.MAGENTA}]{Fore.RESET} Generate usernames")
print(f"{Fore.MAGENTA}[{Fore.RESET}2{Fore.MAGENTA}]{Fore.RESET} Check names.txt")
print(f"{Fore.RED}[{Fore.RESET}3{Fore.RED}]{Fore.RED} Erase 'valid.txt'")
print(f"{Fore.RED}[{Fore.RESET}4{Fore.RED}]{Fore.RED} Erase 'names.txt'")
option = int(input(f"{Fore.LIGHTGREEN_EX}[{Fore.RESET}>{Fore.LIGHTGREEN_EX}]{Fore.RESET}"))

if option == 1:
    os.system("cls")
    def generate_random_strings(num_strings, length):
        result = []
        for _ in range(num_strings):
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
            result.append(random_string)
        return result


    amount = int(input("How many usernames would you like to generate: "))
    length = int(input("How many letter would you like the username to be: "))
    random_strings = generate_random_strings(amount, length)

    os.system("cls")

    with open('names.txt', 'w') as f:
        for i, s in enumerate(random_strings):
            f.write(f"{s}\n")
if option == 2:
    os.system("cls")
    import requests
    from colorama import Fore, Style
    import os


    def validate_username(username):
        url = f"https://auth.roblox.com/v1/usernames/validate?birthday=2006-09-21T07:00:00.000Z&context=Signup&username={username}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['code'] == 0:
                print(f"{Fore.GREEN}The username '{username}' is valid and available{Style.RESET_ALL}")
                with open('valid.txt', 'a') as file:
                    file.write(username + '\n')
            elif data['code'] == 1:
                print(f"{Fore.RED}The username '{username}' is already in use{Style.RESET_ALL}")
            elif data['code'] == 2:
                print(f"{Fore.RED}The username '{username}' is not appropriate for Roblox{Style.RESET_ALL}")
                with open('innappropriate.txt', 'a') as file:
                    file.write(username + '\n')
            elif data['code'] == 10:
                print(f"{Fore.YELLOW}The username '{username}' might contain private information{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Unable to access Roblox API{Style.RESET_ALL}")


    def validate_usernames_from_file(filename):
        with open("names.txt", "r") as file:
            usernames = file.read().splitlines()
        for username in usernames:
            validate_username(username)

    while True:
        filename = input(f"{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}] Press enter to check usernames")
        validate_usernames_from_file(filename)
        print("Valid usernames saved in 'valid.txt'")
if option == 3:
    os.system("cls")
    open('valid.txt', 'w').close()
    input(f"{Fore.RED}'Valid.txt' successfully erased!")
if option == 4:
    os.system("cls")
    open('names.txt', 'w').close()
    input(f"{Fore.RED}'names.txt' successfully erased!")