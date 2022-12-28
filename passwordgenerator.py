import random
import string
import os
import subprocess

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{colors.BLUE}Welcome to the password generator by Aru#0002{colors.ENDC}")

length = int(input(f"{colors.BOLD}{colors.UNDERLINE}\nEnter the length of password: {colors.ENDC}"))

all = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.sample(all,length))

print(f"\nYour new password is: {colors.UNDERLINE}{colors.GREEN}{password}{colors.ENDC}")

print(f"\nSave to file? ({colors.GREEN}y{colors.ENDC}/{colors.FAIL}n{colors.ENDC})")

ask = input()

if ask == 'y':
    set_name = input(f"\nSet the name of your file:{colors.FAIL} ")
    name = set_name + ".txt"
    path = os.path.join(os.path.expanduser('~'),'Downloads', name)

    f = open(path,"a")

    f.write(password)
    print(f"\n{colors.ENDC}{colors.GREEN}Your new password has been saved!{colors.ENDC}")
    f.close()
    subprocess.Popen(f'explorer /select, "{path}"')
else:
    print(f"\n{colors.FAIL}Your password was not saved.{colors.ENDC}")

print(f"Here's my website = {colors.BLUE}https://vorlie.ga{colors.ENDC} also you can find me at {colors.BLUE}https://discord.gg/ntts{colors.ENDC}")

input(f"\n{colors.WARNING}Press anything to exit{colors.ENDC}")



