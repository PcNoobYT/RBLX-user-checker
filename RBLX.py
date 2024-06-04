from colorama import Fore, Style
import random
import string
import os
import requests
import concurrent.futures


def main():
    os.system("cls")
    print(f"{Fore.MAGENTA}[{Fore.RESET}1{Fore.MAGENTA}]{Fore.RESET} Generate usernames")
    print(f"{Fore.MAGENTA}[{Fore.RESET}2{Fore.MAGENTA}]{Fore.RESET} Check names.txt")
    print(f"{Fore.RED}[{Fore.RESET}3{Fore.RED}]{Fore.RED} Erase 'valid.txt'")
    print(f"{Fore.RED}[{Fore.RESET}4{Fore.RED}]{Fore.RED} Erase 'names.txt'")
    option = int(input(f"{Fore.LIGHTGREEN_EX}[{Fore.RESET}>{Fore.LIGHTGREEN_EX}]{Fore.RESET}"))

    if option == 1:
        os.system("cls")

        def generate_random_strings(num_strings, length):
            return [''.join(random.choices(string.ascii_lowercase, k=length)) for _ in range(num_strings)]

        amount = int(input("How many usernames would you like to generate: "))
        length = int(input("How many letters would you like the username to be: "))
        random_strings = generate_random_strings(amount, length)

        os.system("cls")

        with open('../names.txt', 'w') as f:
            f.write('\n'.join(random_strings) + '\n')

    elif option == 2:
        os.system("cls")

        def validate_username(username):
            url = f"https://auth.roblox.com/v1/usernames/validate?birthday=2010-02-18T07:00:00.000Z&context=Signup&username={username}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data['code'] == 0:
                    print(f"{Fore.GREEN}The username '{username}' is valid and available{Style.RESET_ALL}\n")
                    return ('valid', username)
                elif data['code'] == 1:
                    print(f"{Fore.RED}The username '{username}' is already in use{Style.RESET_ALL}\n")
                elif data['code'] == 2:
                    print(f"{Fore.RED}The username '{username}' is not appropriate for Roblox{Style.RESET_ALL}\n")
                    return ('inappropriate', username)
                elif data['code'] == 10:
                    print(
                        f"{Fore.YELLOW}The username '{username}' might contain private information{Style.RESET_ALL}\n")
            else:
                print(f"{Fore.RED}Unable to access Roblox API{Style.RESET_ALL}\n")
            return (None, None)

        def validate_usernames_from_file(filename):
            with open(filename, "r") as file:
                usernames = file.read().splitlines()

            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {executor.submit(validate_username, username): username for username in usernames}

                valid_usernames = []
                inappropriate_usernames = []

                for future in concurrent.futures.as_completed(futures):
                    result, username = future.result()
                    if result == 'valid':
                        valid_usernames.append(username)
                    elif result == 'inappropriate':
                        inappropriate_usernames.append(username)

                with open('../valid.txt', 'a') as file:
                    file.write('\n'.join(valid_usernames) + '\n')

                with open('../inappropriate.txt', 'a') as file:
                    file.write('\n'.join(inappropriate_usernames) + '\n')

        filename = input(f"{Fore.MAGENTA}[{Fore.RED}!{Fore.MAGENTA}] Press enter to check usernames")
        validate_usernames_from_file('../names.txt')
        print("Valid usernames saved in 'valid.txt'")

    elif option == 3:
        os.system("cls")
        open('../valid.txt', 'w').close()
        input(f"{Fore.RED}'Valid.txt' successfully erased!")

    elif option == 4:
        os.system("cls")
        open('../names.txt', 'w').close()
        input(f"{Fore.RED}'names.txt' successfully erased!")


if __name__ == "__main__":
    main()
